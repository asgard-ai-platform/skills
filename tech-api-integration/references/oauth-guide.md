# OAuth 2.0 Flow Details

## Grant Type Decision Table

Pick the grant type based on who runs the code and whether a user is involved.

| Scenario | Grant Type | Reason |
|----------|-----------|--------|
| Web app, user logs in | Authorization Code | Most secure; token never exposed to browser |
| Web app + public client (SPA, mobile) | Authorization Code + PKCE | No client secret possible; PKCE replaces it |
| Server-to-server, no user | Client Credentials | Machine identity, no user consent needed |
| User trusts you with their password | Resource Owner Password | Legacy only; avoid unless forced |
| Short-lived token needs renewal | Refresh Token | Paired with Authorization Code flow |

**Never use Implicit flow.** It was deprecated in RFC 8252 (2017) and replaced by Authorization Code + PKCE.

---

## Authorization Code Flow (Web Apps)

This is the standard flow for server-side applications that can keep a `client_secret` confidential.

### Actors

- **Resource Owner** — the user who owns the data
- **Client** — your application
- **Authorization Server** — issues tokens (e.g., Google's `accounts.google.com`)
- **Resource Server** — the API you're calling (e.g., `api.google.com`)

### Step-by-Step

```
Step 1: Your server builds and sends the authorization URL

  GET https://auth.provider.com/oauth/authorize?
    response_type=code
    &client_id=YOUR_CLIENT_ID
    &redirect_uri=https%3A%2F%2Fyourapp.com%2Fcallback
    &scope=read%3Auser%20read%3Aemail
    &state=RANDOM_UNGUESSABLE_STRING

  → Browser redirects the user to this URL.

Step 2: User authenticates and approves scopes on the provider's UI.

Step 3: Provider redirects back to your redirect_uri

  GET https://yourapp.com/callback?
    code=AUTH_CODE_abc123
    &state=RANDOM_UNGUESSABLE_STRING

  → Verify `state` matches what you generated in Step 1.
    If it doesn't match, ABORT — this is a CSRF attack.

Step 4: Your server exchanges the code for tokens (server-to-server, never from browser)

  POST https://auth.provider.com/oauth/token
  Content-Type: application/x-www-form-urlencoded

  grant_type=authorization_code
  &code=AUTH_CODE_abc123
  &redirect_uri=https%3A%2F%2Fyourapp.com%2Fcallback
  &client_id=YOUR_CLIENT_ID
  &client_secret=YOUR_CLIENT_SECRET

Step 5: Provider returns tokens

  {
    "access_token": "eyJhbGci...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "refresh_token": "def50200...",
    "scope": "read:user read:email"
  }

Step 6: Call the API

  GET https://api.provider.com/user
  Authorization: Bearer eyJhbGci...
```

### State Parameter (CSRF Protection)

Generate a cryptographically random value. Store it in your session. Compare on callback.

```python
import secrets

# Before redirect
state = secrets.token_urlsafe(32)
session['oauth_state'] = state

# On callback
if request.args['state'] != session.pop('oauth_state', None):
    raise SecurityError("State mismatch — possible CSRF")
```

---

## Authorization Code + PKCE (SPAs and Mobile Apps)

PKCE (Proof Key for Code Exchange, RFC 7636) solves the problem of clients that cannot keep a `client_secret` safe (SPAs, mobile apps, desktop apps).

### PKCE Parameters

```
code_verifier  — random string, 43–128 chars, URL-safe
code_challenge — BASE64URL(SHA256(code_verifier))
code_challenge_method — "S256" (always use S256, not plain)
```

### Step-by-Step (differences from Authorization Code)

```python
import hashlib, base64, secrets

# Step 1: Generate PKCE pair
code_verifier = secrets.token_urlsafe(64)          # ~86 chars, URL-safe
digest = hashlib.sha256(code_verifier.encode()).digest()
code_challenge = base64.urlsafe_b64encode(digest).rstrip(b'=').decode()

# Step 2: Authorization URL — add PKCE params, omit client_secret
auth_url = (
    "https://auth.provider.com/oauth/authorize"
    f"?response_type=code"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&scope=read:user"
    f"&state={state}"
    f"&code_challenge={code_challenge}"
    f"&code_challenge_method=S256"
)

# Step 3-4: Token exchange — send code_verifier instead of client_secret
payload = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "code_verifier": code_verifier,   # ← no client_secret
}
```

The authorization server hashes the `code_verifier` and compares it to the stored `code_challenge`. An attacker who intercepts the `code` cannot use it without the `code_verifier`.

---

## Client Credentials Flow (Machine-to-Machine)

No user is involved. Your service authenticates as itself.

```
POST https://auth.provider.com/oauth/token
Content-Type: application/x-www-form-urlencoded
Authorization: Basic BASE64(client_id:client_secret)

grant_type=client_credentials
&scope=reports:read

Response:
{
  "access_token": "eyJhbGci...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

No refresh token is issued — just re-request when the token expires.

```python
import base64, requests, time

class MachineTokenClient:
    def __init__(self, token_url, client_id, client_secret, scope):
        self.token_url = token_url
        self.credentials = base64.b64encode(
            f"{client_id}:{client_secret}".encode()
        ).decode()
        self.scope = scope
        self._token = None
        self._expires_at = 0

    def get_token(self):
        if time.time() < self._expires_at - 60:   # 60s buffer
            return self._token
        resp = requests.post(self.token_url, headers={
            "Authorization": f"Basic {self.credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }, data={"grant_type": "client_credentials", "scope": self.scope})
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._expires_at = time.time() + data["expires_in"]
        return self._token
```

---

## Refresh Token Flow

Access tokens expire (typically 1 hour). Refresh tokens let you get a new access token without re-prompting the user.

```
POST https://auth.provider.com/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token=def50200...
&client_id=YOUR_CLIENT_ID
&client_secret=YOUR_CLIENT_SECRET

Response:
{
  "access_token": "NEW_eyJhbGci...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "NEW_def50200..."   ← may be rotated
}
```

**Refresh token rotation**: Many providers issue a new refresh token each time you use the old one. If you use a refresh token twice (e.g., race condition), the second use will fail and both tokens are revoked. Store the latest refresh token atomically.

```python
def call_api_with_refresh(client_id, client_secret, token_store, request_fn):
    """Makes an API call, refreshing the token if needed."""
    access_token = token_store.get_access_token()

    response = request_fn(access_token)

    if response.status_code == 401:
        # Token expired — try refresh
        refresh_token = token_store.get_refresh_token()
        new_tokens = exchange_refresh_token(client_id, client_secret, refresh_token)
        token_store.save(new_tokens)   # atomic write — both tokens together
        response = request_fn(new_tokens["access_token"])

    return response
```

---

## Token Storage Rules

| Environment | Access Token | Refresh Token |
|------------|-------------|--------------|
| Server-side web app | In-memory or encrypted server session | Encrypted DB row, per user |
| SPA (browser) | In-memory (JS variable) | Do NOT store in browser — use Backend For Frontend |
| Mobile app | Secure enclave / Keychain | Secure enclave / Keychain |
| CLI tool | File with `chmod 600` | Same file, `chmod 600` |
| Server daemon | Environment variable or secrets manager | Secrets manager (AWS SM, Vault) |

**Never** store tokens in:
- `localStorage` or `sessionStorage` (XSS steals them)
- URLs or query parameters (logged by servers, proxies, browsers)
- Source code or config files committed to git

---

## Scopes

Scopes limit what the token can do. Request the minimum needed.

```
read:user         → read user profile
write:user        → update user profile
repo              → full repo access (GitHub — very broad)
repo:read         → read-only repo access (prefer this)
openid profile email  → OIDC standard identity scopes
```

**Principle of Least Privilege**: if your integration only reads data, request only read scopes. Users and security reviewers will reject apps requesting unnecessary scopes.

---

## Common Errors and What They Mean

| Error | Cause | Fix |
|-------|-------|-----|
| `invalid_client` | Wrong `client_id` or `client_secret` | Double-check credentials; check encoding |
| `invalid_grant` | Code already used, expired, or wrong `redirect_uri` | Codes are one-time-use; `redirect_uri` must match exactly |
| `invalid_scope` | Scope not allowed for this client | Check app registration on provider dashboard |
| `access_denied` | User rejected the consent screen | Handle gracefully; do not retry |
| `unsupported_grant_type` | Provider doesn't support this flow | Check provider docs |
| `401` on API call | Access token expired or revoked | Refresh the token; if refresh fails, re-authorize |
| `invalid_token` (in body) | Token malformed or revoked | Re-authorize; do not retry with same token |

---

## Worked Example: GitHub OAuth App

```python
import secrets, hashlib, base64, os
import requests
from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET"]

CLIENT_ID     = os.environ["GITHUB_CLIENT_ID"]
CLIENT_SECRET = os.environ["GITHUB_CLIENT_SECRET"]
REDIRECT_URI  = "https://yourapp.com/callback"

@app.route("/login")
def login():
    state = secrets.token_urlsafe(32)
    session["oauth_state"] = state
    return redirect(
        f"https://github.com/login/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=read:user+user:email"
        f"&state={state}"
    )

@app.route("/callback")
def callback():
    # CSRF check
    if request.args.get("state") != session.pop("oauth_state", None):
        return "State mismatch", 400

    code = request.args.get("code")
    if not code:
        return "No code returned", 400

    # Exchange code for token
    resp = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "redirect_uri": REDIRECT_URI,
        },
    )
    resp.raise_for_status()
    tokens = resp.json()

    if "error" in tokens:
        return f"OAuth error: {tokens['error_description']}", 400

    access_token = tokens["access_token"]

    # Use the token
    user_resp = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user = user_resp.json()

    # Store token encrypted in session (server-side session only)
    session["access_token"] = access_token
    session["user_login"] = user["login"]

    return f"Logged in as {user['login']}"
```

GitHub uses short-lived tokens for some apps and long-lived tokens for others — check your app settings. GitHub's tokens do not expire by default for classic OAuth Apps, but do for fine-grained tokens.

---

## PKCE Worked Example: CLI Tool

```python
#!/usr/bin/env python3
"""
OAuth 2.0 Authorization Code + PKCE for a CLI tool.
Opens the browser, starts a local HTTP server to receive the callback.
"""
import hashlib, base64, secrets, webbrowser, urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

CLIENT_ID    = os.environ["APP_CLIENT_ID"]
AUTH_URL     = "https://auth.example.com/oauth/authorize"
TOKEN_URL    = "https://auth.example.com/oauth/token"
REDIRECT_URI = "http://localhost:8080/callback"

# Generate PKCE
code_verifier  = secrets.token_urlsafe(64)
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).rstrip(b"=").decode()
state = secrets.token_urlsafe(16)

received_code = None

class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global received_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if params.get("state", [None])[0] != state:
            self.send_response(400); self.end_headers()
            return
        received_code = params["code"][0]
        self.send_response(200); self.end_headers()
        self.wfile.write(b"Login complete. Return to terminal.")

# Open browser
auth_params = urllib.parse.urlencode({
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": "read:user",
    "state": state,
    "code_challenge": code_challenge,
    "code_challenge_method": "S256",
})
webbrowser.open(f"{AUTH_URL}?{auth_params}")

# Wait for callback (single request, then stop)
server = HTTPServer(("localhost", 8080), CallbackHandler)
server.handle_request()

# Exchange code
resp = requests.post(TOKEN_URL, data={
    "grant_type": "authorization_code",
    "code": received_code,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "code_verifier": code_verifier,   # no client_secret needed
})
tokens = resp.json()
print(f"Access token: {tokens['access_token'][:20]}...")
```

---

## OpenID Connect (OIDC) — OAuth 2.0 for Identity

OIDC adds an `id_token` (a JWT) to the Authorization Code flow. Use it when you need to know **who** the user is, not just what they can access.

```
scope=openid profile email

Additional response field:
{
  "access_token": "...",
  "id_token": "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMjM0NTY...",
  "expires_in": 3600
}
```

The `id_token` is a JWT. Decode the payload (middle segment, base64url):

```json
{
  "sub": "1234567890",        ← stable user identifier; use this as your user ID
  "name": "Jane Doe",
  "email": "jane@example.com",
  "email_verified": true,
  "iss": "https://accounts.google.com",
  "aud": "YOUR_CLIENT_ID",    ← MUST match your client_id
  "exp": 1712345678,
  "iat": 1712342078
}
```

**Validate the `id_token` before trusting it:**

1. Verify signature using the provider's public keys (`/.well-known/jwks.json`)
2. Check `iss` matches the expected issuer
3. Check `aud` matches your `client_id`
4. Check `exp` is in the future
5. Check `iat` is not too far in the past (clock skew allowance: 5 minutes)

Use a library — do not write JWT validation from scratch:

```python
# PyJWT + cryptography
import jwt
from jwt import PyJWKClient

jwks_client = PyJWKClient("https://accounts.google.com/.well-known/jwks.json")
signing_key = jwks_client.get_signing_key_from_jwt(id_token)

claims = jwt.decode(
    id_token,
    signing_key.key,
    algorithms=["RS256"],
    audience=CLIENT_ID,
    issuer="https://accounts.google.com",
)
user_id = claims["sub"]   # use sub as the stable identifier, not email
```

**Use `sub` as the user's stable ID**, not `email`. Users can change their email; `sub` is permanent.

---

## Provider Discovery (OIDC)

OIDC providers publish their configuration at `/.well-known/openid-configuration`. Fetch this instead of hardcoding URLs.

```python
import requests

discovery = requests.get(
    "https://accounts.google.com/.well-known/openid-configuration"
).json()

AUTH_URL  = discovery["authorization_endpoint"]
TOKEN_URL = discovery["token_endpoint"]
JWKS_URI  = discovery["jwks_uri"]
```

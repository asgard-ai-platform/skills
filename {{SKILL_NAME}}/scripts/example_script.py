#!/usr/bin/env python3
"""
{{Script description}}

Part of: {{PLUGIN_NAME}}
Usage:  python {{script_name}}.py --help
"""
import argparse
import json
import sys
from pathlib import Path


def analyze(data: list[dict]) -> dict:
    """
    Core analysis logic.

    Args:
        data: List of records from input file.

    Returns:
        Analysis result as dict.
    """
    # TODO: Implement analysis
    result = {
        "summary": {},
        "details": [],
        "metadata": {
            "input_records": len(data),
            "skill": "{{SKILL_NAME}}",
        },
    }
    return result


def load_input(file_path: str) -> list[dict]:
    """Load input data from CSV or JSON."""
    path = Path(file_path)
    if path.suffix == ".json":
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif path.suffix == ".csv":
        import csv
        with open(path, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    else:
        print(
            json.dumps({"error": f"Unsupported file format: {path.suffix}", "code": "UNSUPPORTED_FORMAT"}),
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="{{Script description}}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python %(prog)s -i data.csv
  python %(prog)s -i data.json -o result.json
        """,
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Input file path (CSV or JSON)",
    )
    parser.add_argument(
        "--output", "-o", default="-",
        help="Output file path (default: stdout)",
    )
    args = parser.parse_args()

    data = load_input(args.input)
    result = analyze(data)

    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output == "-":
        print(output)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)


if __name__ == "__main__":
    main()

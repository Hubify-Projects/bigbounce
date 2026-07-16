"""Command-line receipt verification for NaMaster Proof."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence

from .receipts import validate_json_receipt, verify_json_receipt


def _expectation(value: str) -> tuple[str, Any]:
    key, separator, raw = value.partition("=")
    if not separator or not key:
        raise argparse.ArgumentTypeError("expectations must use KEY=VALUE")
    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError:
        decoded = raw
    return key, decoded


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="namaster-proof")
    commands = parser.add_subparsers(dest="command", required=True)
    verify = commands.add_parser("verify", help="verify a result/receipt binding")
    verify.add_argument("result", type=Path)
    validate = commands.add_parser(
        "validate", help="verify a binding and expected receipt metadata"
    )
    validate.add_argument("result", type=Path)
    validate.add_argument(
        "--expect",
        action="append",
        default=[],
        type=_expectation,
        metavar="KEY=VALUE",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "verify":
        _, receipt = verify_json_receipt(args.result)
    else:
        expectations = dict(args.expect)
        if len(expectations) != len(args.expect):
            raise ValueError("duplicate --expect keys are not allowed")
        _, receipt = validate_json_receipt(args.result, expected=expectations)
    print(
        json.dumps(
            {
                "result": str(args.result),
                "result_sha256": receipt["result_sha256"],
                "status": "PASS",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

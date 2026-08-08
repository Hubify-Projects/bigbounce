#!/usr/bin/env python3
"""Retired API-backed meta-review launcher.

Run meta-review through an authenticated Codex CLI worker so the OpenAI
perspective is covered by the ChatGPT subscription, not separate API billing.
"""
from __future__ import annotations

import sys


POLICY_MESSAGE = (
    "API-backed OpenAI meta-review is disabled: use an authenticated Codex CLI "
    "worker with API-key environment variables unset so the ChatGPT subscription is used."
)


def main() -> int:
    print(POLICY_MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

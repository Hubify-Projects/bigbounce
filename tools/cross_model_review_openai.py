#!/usr/bin/env python3
"""Retired OpenAI-API review launcher.

Historical R42 outputs are preserved under ``project-context/peer-reviews``.
New OpenAI reviews must use the authenticated Codex CLI/ChatGPT subscription.
"""
from __future__ import annotations

import sys


POLICY_MESSAGE = (
    "OpenAI API review dispatch is disabled: use the authenticated Codex CLI "
    "with API-key environment variables unset so the ChatGPT subscription is used."
)


def main() -> int:
    print(POLICY_MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

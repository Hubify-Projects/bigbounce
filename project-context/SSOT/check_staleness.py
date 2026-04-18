#!/usr/bin/env python3
"""SSOT staleness check.

Scans every `Last authoritative update:` line in `project-context/SSOT/*.md`
and `project-context/SSOT/paper-*/status.md`. Flags any file whose update
date is older than STALE_DAYS (default 7). Exits non-zero if any stale.

Run manually:
    python3 project-context/SSOT/check_staleness.py
    python3 project-context/SSOT/check_staleness.py --days 14

Run via the weekly cron scheduled by `P-SSOT-CRON` (queue.md).
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys

SSOT_DIR = pathlib.Path(__file__).resolve().parent
# Accept either "Last authoritative update: YYYY-MM-DD" (prose) or
# "last_updated: YYYY-MM-DD" (YAML frontmatter).
DATE_RE = re.compile(
    r"(?:Last authoritative update:|last_updated:)\s*(\d{4}-\d{2}-\d{2})", re.I
)
# Status-bearing files only — README.md and drive-to-100.md are not status docs.
TARGET_NAMES = {"index.md", "queue.md"}


def scan(days: int) -> list[tuple[pathlib.Path, dt.date]]:
    """Return list of (path, last_update_date) for files older than `days`."""
    today = dt.date.today()
    threshold = today - dt.timedelta(days=days)
    stale: list[tuple[pathlib.Path, dt.date]] = []
    targets = [p for p in SSOT_DIR.glob("*.md") if p.name in TARGET_NAMES]
    targets += list(SSOT_DIR.glob("paper-*/status.md"))
    for path in sorted(targets):
        text = path.read_text(encoding="utf-8", errors="replace")
        match = DATE_RE.search(text)
        if not match:
            stale.append((path, dt.date(1970, 1, 1)))
            continue
        try:
            update = dt.date.fromisoformat(match.group(1))
        except ValueError:
            stale.append((path, dt.date(1970, 1, 1)))
            continue
        if update < threshold:
            stale.append((path, update))
    return stale


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag stale SSOT files.")
    parser.add_argument("--days", type=int, default=7, help="Stale threshold (days)")
    args = parser.parse_args()

    stale = scan(args.days)
    today = dt.date.today()

    if not stale:
        print(f"[ok] all SSOT files fresh within {args.days} days (today={today})")
        return 0

    print(f"[stale] {len(stale)} SSOT file(s) older than {args.days} days (today={today}):")
    for path, last in stale:
        rel = path.relative_to(SSOT_DIR.parent.parent)
        age = (today - last).days if last != dt.date(1970, 1, 1) else "no-date"
        print(f"  {rel}  last={last}  age_days={age}")
    return 1


if __name__ == "__main__":
    sys.exit(main())

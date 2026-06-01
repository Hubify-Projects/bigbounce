"""
Parse R-round markdown outputs and bulk-seed Convex findings.

For each reviewer file project-context/peer-reviews/<round-label>_<paper>_R-round_direct_<reviewer>.md:
  - Create one r_rounds row (or reuse if it already exists)
  - For each finding header (## PAPER-XXX-Y# OR **PAPER-XXX-Y#**),
    extract the classification (BLOCKER / MAJOR / MINOR / NIT) from the
    ID letter, parse the body text, push as a findings row.

Usage:
  CONVEX_URL=... python3 tools/seed_findings_from_round.py <round_label> <paper_slug>

Example:
  CONVEX_URL=https://brilliant-panther-471.convex.cloud \\
    python3 tools/seed_findings_from_round.py 2026-06-01_R-direct-P1B paper-1b
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
import urllib.error
import ssl
from pathlib import Path

try:
    import certifi
    _CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _CTX = ssl.create_default_context()

CONVEX_URL = os.environ.get("CONVEX_URL", "https://brilliant-panther-471.convex.cloud")
REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
PR_DIR = REPO / "project-context" / "peer-reviews"


def convex_call(action: str, args: dict) -> dict:
    """Call a Convex query or mutation via HTTP."""
    url = f"{CONVEX_URL}/api/{action}"
    body = json.dumps({"path": args["path"], "args": args.get("args", {}), "format": "json"}).encode("utf-8")
    req = urllib.request.Request(
        url, data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode("utf-8", errors="replace")}


def query(path: str, args: dict | None = None) -> dict:
    return convex_call("query", {"path": path, "args": args or {}})


def mutation(path: str, args: dict | None = None) -> dict:
    return convex_call("mutation", {"path": path, "args": args or {}})


def classification_for(finding_id: str) -> str:
    """Determine classification from finding ID letter. Examples:
    PAPER-GPT-B1 -> BLOCKER
    PAPER-GRO-M2 -> MAJOR
    PAPER-PER-m1 -> MINOR
    PAPER-GEM-nit -> NIT
    """
    # Last segment after last hyphen
    m = re.search(r"([A-Za-z]+)(\d*)$", finding_id)
    if not m:
        return "MINOR"
    letter = m.group(1).upper()
    if letter.startswith("B"):
        return "BLOCKER"
    if letter.startswith("MAJ") or letter == "M":
        return "MAJOR"
    if letter.startswith("MIN") or letter == "M_" or letter == "Mi":
        return "MINOR"
    if letter.startswith("NIT") or letter.startswith("N"):
        return "NIT"
    return "MINOR"


def parse_findings(md_path: Path) -> list[dict]:
    """Extract findings from a reviewer's markdown output. Returns list of
    {findingId, classification, location, claim, proposedFix}."""
    text = md_path.read_text()
    findings = []

    # Match either ## PAPER-XXX-Y or **PAPER-XXX-Y** (Grok format)
    # The trailing portion after :/—/-/space may carry an override classification
    # (e.g. Perplexity: "## PAPER-PER-B1 — **BLOCKER**" or "## PAPER-PER-B5 — **minor**")
    patterns = [
        re.compile(
            r"^##\s+(PAPER-[A-Z]+-[A-Za-z]+\d*)(?:\s*[—:\-]\s*\*?\*?(BLOCKER|MAJOR|MINOR|NIT|minor|nit)\*?\*?)?(?::\s*(.*))?",
            re.MULTILINE | re.IGNORECASE,
        ),
        re.compile(r"^\*\*(PAPER-[A-Z]+-[A-Za-z]+\d*)\*\*\s*$", re.MULTILINE),
    ]
    matches = []
    seen_ids: set[str] = set()
    for pat in patterns:
        for m in pat.finditer(text):
            fid = m.group(1)
            if fid in seen_ids:
                continue
            seen_ids.add(fid)
            override = m.group(2) if pat.groups >= 2 else None
            matches.append((m.start(), fid, override))
    matches.sort()
    if not matches:
        return findings

    # Extract body between successive matches
    for i, (pos, fid, override_cls) in enumerate(matches):
        body_start = pos + len(matches[i][1]) + 5  # skip header
        body_end = matches[i + 1][0] if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        # Try to split body into location | claim | fix
        # Heuristic: first non-empty line is location, second-half is the rest
        lines = [ln.strip() for ln in body.split("\n") if ln.strip()]
        if not lines:
            continue
        location = ""
        claim = ""
        fix = ""
        # Look for "Fix:" or "Proposed fix:" delimiter
        fix_idx = None
        for j, ln in enumerate(lines):
            if re.match(r"^(\*\*)?[Ff]ix:?", ln) or "Fix:" in ln:
                fix_idx = j
                break
        if fix_idx is None:
            # No explicit fix delimiter; treat first line as location, rest as claim
            if len(lines) >= 2:
                location = lines[0][:200]
                claim = " ".join(lines[1:])[:1000]
            else:
                claim = lines[0][:1000]
        else:
            # location = pre-fix, claim = pre-fix middle, fix = post-fix
            if fix_idx > 0:
                location = lines[0][:200]
                claim = " ".join(lines[1:fix_idx])[:1000]
            else:
                claim = ""
            fix = " ".join(lines[fix_idx:])[:1000]
            fix = re.sub(r"^\*\*?[Ff]ix:?\s*\*?\*?\s*", "", fix).strip()

        cls = override_cls.upper() if override_cls else classification_for(fid)
        if cls == "MINOR" and override_cls and override_cls.lower() == "nit":
            cls = "NIT"
        findings.append({
            "findingId": fid,
            "classification": cls,
            "location": location or "(unspecified)",
            "claim": claim or "(empty)",
            "proposedFix": fix or "(none provided)",
        })
    return findings


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <round_label> <paper_slug>")
        return 1
    round_label = sys.argv[1]
    paper_slug = sys.argv[2]

    paper = query("papers:getBySlug", {"slug": paper_slug})
    if not paper or paper.get("status") == "error":
        print(f"FAIL: paper not found: {paper_slug}", file=sys.stderr)
        return 2

    # Determine paper version from getPaperState
    state = query("papers:getPaperState", {"slug": paper_slug})
    paper_version = (state.get("value") or state).get("currentVersion", {}) if isinstance((state.get("value") or state).get("currentVersion"), dict) else None
    version_str = (paper_version or {}).get("version") if paper_version else "unknown"

    # Find all reviewer files for this round
    pattern = f"{round_label}_*_R-round_direct_*.md"
    files = sorted(PR_DIR.glob(pattern))
    print(f"Found {len(files)} reviewer files for round {round_label}")

    vendors = []
    all_findings = []
    for f in files:
        reviewer_name = f.stem.split("_R-round_direct_")[-1]
        findings = parse_findings(f)
        vendors.append(reviewer_name)
        for fd in findings:
            fd["reviewerName"] = reviewer_name
            all_findings.append(fd)
        print(f"  {reviewer_name}: {len(findings)} findings (B={sum(1 for x in findings if x['classification']=='BLOCKER')} M={sum(1 for x in findings if x['classification']=='MAJOR')} m={sum(1 for x in findings if x['classification']=='MINOR')} N={sum(1 for x in findings if x['classification']=='NIT')})")

    if not all_findings:
        print("No findings parsed; nothing to seed.")
        return 0

    # Create r_rounds row
    round_res = mutation("rRounds:create", {
        "paperSlug": paper_slug,
        "paperVersionReviewed": version_str or "unknown",
        "roundLabel": round_label,
        "source": "direct",
        "vendors": vendors,
    })
    if isinstance(round_res, dict) and "error" in round_res:
        print(f"FAIL creating r_round: {round_res['error'][:500]}", file=sys.stderr)
        return 3
    round_id = round_res.get("value") or round_res
    print(f"\nCreated r_round {round_id}")

    # Bulk-insert findings
    created = 0
    for fd in all_findings:
        res = mutation("findings:create", {
            "roundId": round_id,
            "paperSlug": paper_slug,
            "reviewerName": fd["reviewerName"],
            "findingId": fd["findingId"],
            "classification": fd["classification"],
            "location": fd["location"],
            "claim": fd["claim"],
            "proposedFix": fd["proposedFix"],
        })
        if isinstance(res, dict) and "error" in res:
            print(f"  FAIL on {fd['findingId']}: {res['error'][:200]}", file=sys.stderr)
        else:
            created += 1
    print(f"\nSeeded {created}/{len(all_findings)} findings to Convex.")

    # Re-fetch paper state for verification
    state = query("papers:getPaperState", {"slug": paper_slug})
    v = state.get("value") or state
    print(f"\nNew paper state for {paper_slug}:")
    print(f"  readinessComputed = {v.get('readinessComputed')}")
    fb = v.get('findingsByClassification', {}).get('open', {})
    print(f"  open findings: {fb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

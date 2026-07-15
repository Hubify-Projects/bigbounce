#!/bin/bash
# Run mechanical detection for patterns 037, 038, 039 on every bigbounce paper.
# 037: future-dated \date{} block
# 038: σ-mixing without per-juxtaposition qualifier
# 039: hardcoded Roman-numeral table reference

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
PAPERS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

declare_papers() {
  python3 - "$PAPERS_ROOT/project-context/paper_registry.json" <<'PY'
import json, sys
papers = json.load(open(sys.argv[1], encoding="utf-8"))["papers"]
for paper_id, record in papers.items():
    print(f'{paper_id}:{record["tex_path"]}')
PY
}

CUR_YEAR=$(date +%Y)
NEXT_YEAR=$((CUR_YEAR + 1))

declare_papers | while IFS=: read -r tag rel; do
  tex="$PAPERS_ROOT/$rel"
  if [ ! -f "$tex" ]; then
    echo "[$tag] .tex not found at $rel — skip"
    continue
  fi
  echo ""
  echo "=== $tag ($rel) ==="

  # Pattern 037: future date
  future_dates=$(grep -nE '\\date\{[^}]*20(2[7-9]|[3-9][0-9])\b' "$tex" || true)
  if [ -n "$future_dates" ]; then
    echo "  ⚠ p037 future-year date:"
    echo "$future_dates" | sed 's/^/    /'
  fi
  # Also check \newcommand{\paperTimestamp}
  ts=$(grep -E "newcommand\{\\\\paperTimestamp\}" "$tex" | head -1 || true)
  if [ -n "$ts" ]; then
    if echo "$ts" | grep -qE "20(2[7-9]|[3-9][0-9])"; then
      echo "  ⚠ p037 future paperTimestamp: $ts"
    fi
  fi

  # Pattern 038: only flag an individual caption that juxtaposes at least two
  # sigma values without a local null-procedure/non-comparability qualifier.
  python3 - "$tex" <<'PY'
import pathlib, re, sys
text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
for start in (m.end() for m in re.finditer(r"\\caption\{", text)):
    depth, end = 1, start
    while end < len(text) and depth:
        if text[end] == "{" and (end == 0 or text[end - 1] != "\\"):
            depth += 1
        elif text[end] == "}" and (end == 0 or text[end - 1] != "\\"):
            depth -= 1
        end += 1
    caption = text[start:end - 1]
    sigma_values = re.findall(
        r"(?:[+\-−]?\d+(?:\.\d+)?\s*(?:\\,)?\s*(?:\\sigma|σ)|"
        r"(?:\\sigma|σ)\s*[=<>~]?\s*\d+(?:\.\d+)?)",
        caption,
    )
    if len(sigma_values) < 2:
        continue
    if re.search(r"not directly comparable|distinct null|different null", caption, re.I):
        continue
    line = text.count("\n", 0, start) + 1
    excerpt = " ".join(caption.split())[:220]
    print(f"  ⚠ p038 caption line {line}: {len(sigma_values)} sigma values without local qualifier: {excerpt}")
PY

  # Pattern 039: hardcoded Roman-numeral table reference in prose
  prose_ref=$(grep -nE "Table[[:space:]~]+I+V?I*\b" "$tex" \
    | grep -v "\\\\ref" | grep -vE '^[0-9]+:[[:space:]]*%' | head -5 || true)
  if [ -n "$prose_ref" ]; then
    echo "  ⚠ p039 hardcoded prose 'Table II/IV' reference(s):"
    echo "$prose_ref" | sed 's/^/    /'
  fi

  # Pattern 040 (P4-E12 type): same percentage paired with two different integer counts.
  # Find "<INT>,?<INT>" patterns followed by "<float>%" within 200 chars; bucket by percentage.
  python3 -c "
import re, sys
text = open('$tex').read()
text = '\n'.join(line.split('%', 1)[0] for line in text.splitlines())
# Match N{,}NNN followed within 200 chars by P.PP%
buckets = {}
for m in re.finditer(r'(\d{1,3}(?:[,]\s?\d{3})+)\b[^\n]{0,200}?(\d+\.\d{2}%)', text):
    n, pct = m.group(1).replace(',','').replace(' ',''), m.group(2)
    buckets.setdefault(pct, set()).add(n)
flagged = {pct: ns for pct, ns in buckets.items() if len(ns) > 1}
for pct, ns in flagged.items():
    print(f'  ⚠ p040 candidate: same percentage \"{pct}\" paired with different counts: {sorted(ns)}')
" 2>/dev/null
done

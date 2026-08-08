---
pattern_id: ppattern-figure-only-in-build-dir
status: seeded
first_seen: P1-2026-06-19
papers_observed: []
proposed_by: paper-packaging-round 2026-06-19
---

# ppattern-figure-only-in-build-dir — Figure exists in local build dir but missing from tarball

## Defect

A figure file referenced by `\includegraphics` exists in the local LaTeX build
directory (e.g. from a previous pdflatex run's aux cache, or generated locally
by a script) but is not committed to the repo or explicitly included in the
tarball assembly step. The paper compiles locally but the arXiv tarball
STANDALONE-compile fails with "File not found."

## How to detect

During the P-round STANDALONE-compile-verify step:
```bash
# Extract tarball to a clean temp dir
mkdir /tmp/test_compile && cd /tmp/test_compile
tar -xzf paper.tar.gz
pdflatex paper.tex 2>&1 | grep -i 'not found\|missing\|cannot find'
```
Any "not found" on a `.png`/`.pdf`/`.eps` file is this pattern.

Also:
```bash
# Check which figures are referenced vs which are in the tarball
grep -oh 'includegraphics[^{]*{[^}]*}' paper.tex | sed 's/.*{//;s/}//' > referenced.txt
tar -tzf paper.tar.gz | grep -E '\.(png|pdf|eps)' > in_tarball.txt
diff referenced.txt in_tarball.txt
```

## Fix

In the tarball assembly script:
1. Parse all `\includegraphics{<path>}` calls in the `.tex` (including `\input`
   children).
2. For each referenced figure path, resolve relative to the `.tex` directory and
   include the file in the tarball.
3. Re-run STANDALONE-compile-verify after every tarball rebuild.

Never rely on the local pdflatex cache (`paper.aux`, `paper.pdf`, build dir
PNG cache) as a proxy for what the tarball contains.

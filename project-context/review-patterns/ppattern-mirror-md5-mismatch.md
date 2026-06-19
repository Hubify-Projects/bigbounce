---
pattern_id: ppattern-mirror-md5-mismatch
status: seeded
first_seen: P1-2026-06-19
papers_observed: []
proposed_by: paper-packaging-round 2026-06-19
---

# ppattern-mirror-md5-mismatch — PDF mirror does not byte-match the canonical source PDF

## Defect

After a P-round PDF mirror operation, one or more of the destination copies
(site `public/papers/`, legacy static path, versioned filename) differs byte-for-
byte from the canonical source PDF. Readers downloading from a stale mirror get a
different (older) version of the paper than what was reviewed and signed off. This
can be caused by a failed copy, a partial upload, a git-lfs pointer mismatch, or a
cached CDN serving stale content.

## How to detect

```bash
# Compute canonical MD5
canonical_md5=$(md5sum source/paper.pdf | awk '{print $1}')

# Check every mirror path
for path in \
    site/public/papers/paper.pdf \
    site/public/papers/paper_v1.0.NNN.pdf \
    old/papers/paper.pdf; do
    mirror_md5=$(md5sum "$path" 2>/dev/null | awk '{print $1}')
    if [ "$mirror_md5" != "$canonical_md5" ]; then
        echo "MISMATCH: $path ($mirror_md5 vs $canonical_md5)"
    fi
done
```

Run `/bigbounce-paper-pdf-mirror` which includes this check as a hard gate.

## Fix

Re-copy the canonical PDF to every mirror path:
```bash
cp source/paper.pdf site/public/papers/paper.pdf
cp source/paper.pdf site/public/papers/paper_v1.0.NNN.pdf
```
Re-verify MD5s. If a CDN is serving stale content, trigger a cache purge or
promote the new deploy via `vercel promote <deploy-id>`. The P-round does not
close until all mirror MD5s match.

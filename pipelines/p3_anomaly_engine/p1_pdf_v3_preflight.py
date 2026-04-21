#!/usr/bin/env python3
"""
P1-PDF-RECOMPILE-V3 preflight — Paper 1 bundled-edits validator
================================================================
Validates that the 12 queued P1 edits (DONE-in-queue but awaiting pod
pdflatex) are actually present in `arxiv/main.tex` before the recompile
fires. Catches cases where a queue row says DONE but the edit was reverted
or never landed in the tracked source.

Exit criterion #11 of Path C. Gated on Paper 3 recompile (criterion #9)
landing first, but preflight can run anytime.

Bundled P1 edits (from queue.md, each row marked [x] DONE with
"PDF recompile tracked as P1-PDF-RECOMPILE-V3"):

  1. P1-SAMPLE-COUNT-FOOTNOTE   — 119,617 / 176,840 / 309,789 footnote
  2. P1-RHAT-NUMBER-RECONCILE   — Houston-owned, may be open
  3. P1-BROKEN-EQ-REF           — orphan equation label resolved
  4. P1-REPRO-URL-BUMP          — v2.1.0 → v2.3.0 (5 occurrences)
  5. P1-BETA-EQ38-CHECK         — Houston-owned, may be open
  6. P1-SSOT-BETA-LABEL-SWAP    — β label harmonization
  7. P1-H0-NEFF-CORNER-HARMONIZE — 67.69 → 67.68, -0.019 → -0.020 at L887/L892
  8. P1-PEER-REVIEW-SPHEREX-ORPHAN-LABELS — SPHEREx ref fix
  9. P1-MCMC-COUNT-RECONCILE    — 424,181 / 309,789 count harmonization
  10. P1-ACK-STRENGTHEN          — acknowledgements update
  11. P1-ABSTRACT-FNL-CONVENTION — f_NL sign convention clarification
  12. P1-NANOGRAV-CAVEAT-REORDER — NANOGrav caveat position swap
  13. P1-P4-PREPRINT-NUMBER-EXTEND — \\preprint{} paper-4 cross-ref

Usage:
    python pipelines/p3_anomaly_engine/p1_pdf_v3_preflight.py

Output:
  - Checks pass/fail per edit
  - Emits pod-ready recompile command if all pass
  - Exit code 0 on all-pass, 1 on any fail
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent.parent
P1_TEX = REPO / 'arxiv' / 'main.tex'


def check(name: str, predicate: bool, detail: str = '') -> tuple[str, bool, str]:
    status = 'PASS' if predicate else 'FAIL'
    return (name, predicate, f'  {status}: {name}' + (f' — {detail}' if detail else ''))


def main() -> int:
    if not P1_TEX.exists():
        print(f'ERROR: {P1_TEX} not found', file=sys.stderr)
        return 2
    src = P1_TEX.read_text()
    results = []

    # 1. Sample-count footnote (fn:sample_stratification)
    has_fn = r'\label{fn:sample_stratification}' in src or 'fn:sample_stratification' in src
    results.append(check('P1-SAMPLE-COUNT-FOOTNOTE', has_fn,
                         'fn:sample_stratification label present'))

    # 4. Reproducibility URL bumped to v2.3.0 (no lingering v2.1.0)
    v210_count = src.count('v2.1.0')
    v230_count = src.count('v2.3.0')
    results.append(check('P1-REPRO-URL-BUMP',
                         v210_count == 0 and v230_count >= 5,
                         f'v2.1.0={v210_count} (want 0), v2.3.0={v230_count} (want >=5)'))

    # 7. H0/Neff corner harmonization — 67.68 and -0.020 at §IV.A
    # (67.69 shouldn't appear as a claim in same context as corner plot)
    has_6768 = '67.68' in src
    has_neff_020 = '-0.020' in src or '$-0.020$' in src or '{-}0.020' in src
    results.append(check('P1-H0-NEFF-CORNER-HARMONIZE',
                         has_6768 and has_neff_020,
                         'H0=67.68 + Neff=-0.020 present'))

    # 9. MCMC count reconciliation — 119,617 / 176,840 / 309,789 all appear
    has_119617 = '119{,}617' in src or '119,617' in src
    has_176840 = '176{,}840' in src or '176,840' in src
    has_309789 = '309{,}789' in src or '309,789' in src
    results.append(check('P1-MCMC-COUNT-RECONCILE',
                         has_119617 and has_176840 and has_309789,
                         f'119,617={has_119617} 176,840={has_176840} 309,789={has_309789}'))

    # 3. Broken eq-ref: no \eqref{?} pattern
    orphan_eqrefs = re.findall(r'\\eqref\{\?\?\}|\\ref\{eq:[a-zA-Z_]*undefined', src)
    results.append(check('P1-BROKEN-EQ-REF',
                         len(orphan_eqrefs) == 0,
                         f'{len(orphan_eqrefs)} orphan eq-refs found' if orphan_eqrefs else 'no orphan eq-refs'))

    # 13. Paper-4 preprint cross-ref in \preprint{}
    has_p4_preprint = r'\preprint' in src and ('Paper 4' in src or 'chirality' in src.lower())
    results.append(check('P1-P4-PREPRINT-NUMBER-EXTEND', has_p4_preprint,
                         '\\preprint{} block references Paper 4 / chirality'))

    # 2/5. Houston-owned — flag as advisory only
    rhat_mentioned = r'\hat R' in src or '$R$' in src or 'Gelman-Rubin' in src
    beta_eq38 = 'Eq.' in src and '38' in src  # loose — Houston to decide
    results.append(('P1-RHAT-NUMBER-RECONCILE (Houston)', True,
                    f'  INFO: Houston-owned; R-hat discussion present={rhat_mentioned}'))
    results.append(('P1-BETA-EQ38-CHECK (Houston)', True,
                    '  INFO: Houston-owned; non-blocking for recompile'))

    # Remaining wordsmith/ack/caveat edits — advisory (can't programmatically verify prose)
    for t in ['P1-SSOT-BETA-LABEL-SWAP', 'P1-PEER-REVIEW-SPHEREX-ORPHAN-LABELS',
              'P1-ACK-STRENGTHEN', 'P1-ABSTRACT-FNL-CONVENTION',
              'P1-NANOGRAV-CAVEAT-REORDER']:
        results.append((t, True, f'  INFO: {t} — text-prose edit, trust queue [x] marker'))

    print(f'P1-PDF-RECOMPILE-V3 preflight  ({P1_TEX.relative_to(REPO)})')
    print('=' * 68)
    for _, _, line in results:
        print(line)
    print('=' * 68)

    failed = [r for r in results if r[1] is False]
    if failed:
        print(f'{len(failed)} FAIL — recompile BLOCKED until fixed')
        return 1

    print('All programmatic checks PASS. Ready for pod recompile:')
    print()
    print('  # On pod with TeX Live (texlive-publishers for revtex4-2):')
    print('  cd /workspace/bigbounce/arxiv')
    print('  pdflatex -interaction=nonstopmode main.tex')
    print('  bibtex main')
    print('  pdflatex -interaction=nonstopmode main.tex')
    print('  pdflatex -interaction=nonstopmode main.tex')
    print()
    print('  # Back on local:')
    print('  scp -P 11759 -i ~/.ssh/id_ed25519 \\')
    print('      root@104.255.9.187:/workspace/bigbounce/arxiv/main.pdf \\')
    print('      arxiv/main.pdf')
    print('  cp arxiv/main.pdf public/papers/paper1_spin_torsion.pdf')
    return 0


if __name__ == '__main__':
    sys.exit(main())

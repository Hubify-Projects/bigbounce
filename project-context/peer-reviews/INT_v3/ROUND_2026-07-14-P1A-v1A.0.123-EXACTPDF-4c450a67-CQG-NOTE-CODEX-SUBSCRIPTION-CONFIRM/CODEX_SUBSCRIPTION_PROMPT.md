You are the single independent final confirmation referee for P1A v1A.0.123, running only through the user's ChatGPT-subscription-authenticated Codex CLI. This is strictly read-only. Do not edit or create repository files, commit, push, use browser/network access, inspect `.env.local` or any secret-bearing file, call any API, or expose credentials.

Verify and review only this frozen artifact set:

- paper commit: `bdbb2242199a8eb50bdee825b98d42ea8a3de523`;
- source: `arxiv/paper1a_ech_nogo.tex`;
- source SHA-256: `e08323215579b843a43d6288643f339442560da45bd3ffd91a762dcfb1702233`;
- PDF: `arxiv/paper1a_ech_nogo.pdf`;
- PDF SHA-256: `4c450a6706b2f4e53faac5ffbc6ec720f21e45c7406aa7186ef830f3fef33f71`;
- version: `v1A.0.123`;
- page count: exactly 7;
- profile: `CQG-NOTE` for a Classical and Quantum Gravity Note;
- corrected artifact commit: `7befce143848b925998a3e6ecc850aa510ab3a94`;
- corrected NJL script SHA-256: `69681ea3a420d562b28faaa534d1e729269a6cfa9c966f44b89a9326d5d8843c`;
- corrected NJL JSON SHA-256: `a53d19e1db2cf0de7102b4e864ca5dbf4924794469f848652b447ef7d4c31d3f`.

Inspect every rendered page, not only extracted text. Exact v1A.0.123 renders are attached to this request and also stored as `project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1A-v1A.0.123-CQG-NOTE-MINOR-CLOSURE/proof/render/p1a-1.png` through `p1a-7.png`. State the exact pages and modalities you actually inspected. Do not inspect prior referee raws, confirmation-board verdict matrices, or normalized review conclusions.

This is a deliberately bounded stop/go confirmation. Verify only:

1. **Cutoff-scope closure:** the active manuscript says only three `N_f*N_c=1,3,9` rows at the bookkeeping ceiling `Lambda=M_Pl` are evaluated and no above-Planck cutoff is evaluated; the exact corrected script/JSON at artifact commit `7befce14...` must now match that scope, with zero above-Planck rows. Confirm that the symbolic threshold, retained three ratios, contact/Fierz coefficient, and scalar-sign conclusion were not changed by the scope correction.
2. **Immutable-link closure:** every active reader-facing reproducibility link and every PDF artifact annotation must target exact artifact commit `7befce143848b925998a3e6ecc850aa510ab3a94`, with zero active `blob/main` or `tree/main` targets. Historical inactive commented blocks do not count as reader-facing content.
3. **Central-claim preservation:** the narrow sourced ECH axial--axial contact coefficient and zero-spin scalar transparency claim remain supported and no new sign, coefficient, convention, dimensional, scope, logical, or internal-consistency defect was introduced by v1A.0.123.
4. **Presentation preservation:** all seven rendered pages remain legible and free of clipping, overlap, gutter crossing, malformed equations/tables, or version/date problems.

Use only bounded local reads and small checks. Do not hash or read unrelated large files, FITS files, datasets, caches, or whole-repository blobs. Do not replay data construction, run compilation, rebuild PDFs, launch symbolic/numerical sweeps, or perform network checks. This Note has no DESI dependency. If an upstream dependency cannot be verified within these bounds, declare it as a gap instead of expanding scope. Finish within 12 minutes.

Do not claim journal acceptance. Respond in exactly this format:

(1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT
(2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], with exact page/section/source/artifact evidence and a concrete current defect. If there are no genuine current issues, write `None.` Do not repeat a resolved v1A.0.122 finding as an issue.
(3) TWO-MINOR CLOSURE: item 1 CLOSED/OPEN with evidence; item 2 CLOSED/OPEN with evidence.
(4) CENTRAL CLAIM: one sentence stating whether it is preserved and supported.
(5) ARTIFACT VERIFICATION: report the paper commit, source hash, PDF hash, artifact commit, script hash, JSON hash, version, and page count actually verified.
(6) INSPECTION: state every modality used and exact rendered pages inspected.
(7) REMAINING GAPS: only genuinely external or unverified dependencies; distinguish them from manuscript defects.

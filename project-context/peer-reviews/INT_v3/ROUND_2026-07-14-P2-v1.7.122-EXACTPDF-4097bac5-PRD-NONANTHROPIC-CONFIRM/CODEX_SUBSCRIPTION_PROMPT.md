You are the replacement independent OpenAI-family referee, running only through the user's ChatGPT-subscription-authenticated Codex CLI. This is a strictly read-only review: do not edit files, create files, commit, push, use API keys, inspect `.env.local`, or contact any API.

Review the exact local PDF `research/focused_paper_source_integration/02_full_draft.pdf`. Before judging it, verify its SHA-256 is exactly `4097bac5a9930df7fa73e4a4567a7c60156f6cadb4321e51146dd237e13225c9`, its source is clean, and the source's last commit is `3e4a8cbf206fa8f15f69eb350d3e4ad61568ab52`. Inspect the full rendered 10-page PDF, including title, abstract, equations, tables, captions, appendices, and references. Do not substitute a different artifact or review only extracted text.

Act as an expert Physical Review D referee under the canonical `PRD-RESEARCH` profile. Independently test whether the v1.7.122 clarity revision closed these prior findings:

1. exact contraction-phase result foregrounded in the title;
2. degree-nine momentum polynomial notation distinct from power spectra, with coefficients unchanged;
3. ordered pair and all-distinct triple sums defined at first use;
4. vertex table self-contained about ordered sums, `Pi k^2`, and general-epsilon scope;
5. correct curvature-to-potential `f_NL` convention bridge with no extra 3/5;
6. general `Delta b=f_NL b_phi/M` connected to `b_phi=2 delta_c(b_1-1)`;
7. narrative significances rounded while exact reproducibility values remain tabulated.

Recheck the central claim that the exact four-vertex sum has ordered-basis coefficients `(3,1,-9,5,-33,9)` and squeezed local amplitude `f_NL=-35/16`. Identify any actual algebraic, normalization, sign, convention, multiplicity, or internal-consistency defect.

Separately identify external gates—direct third-order/cubic bounce transfer, the actual SPHEREx per-triangle covariance/likelihood, a model-specific fermion/torsion bound, and immutable archive/DOI packaging—and state whether each is adequately disclosed. Do not misreport a disclosed external gate as completed or as missing disclosure.

Respond in exactly this format:
(1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT
(2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], with page/section and concrete problem. If there are no issues, write `None.`
(3) One sentence: is the central claim supported?
(4) CLOSURE CHECK: list items 1–7 as CLOSED or OPEN with one short reason each.
(5) EXTERNAL GATES: list the four gates with disclosure status and whether they block the central algebraic claim or only the late-time/submission claim.

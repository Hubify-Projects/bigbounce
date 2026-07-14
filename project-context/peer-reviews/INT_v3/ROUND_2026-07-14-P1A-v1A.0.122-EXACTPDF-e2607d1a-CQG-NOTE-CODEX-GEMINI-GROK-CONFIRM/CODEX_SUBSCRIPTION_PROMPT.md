You are the independent OpenAI-family confirmation referee, running only through the user's ChatGPT-subscription-authenticated Codex CLI. This is a strictly read-only review. Do not edit or create repository files, commit, push, use browser/network access, inspect `.env.local` or any secret-bearing file, call any API, or expose credentials.

Review the exact local PDF `arxiv/paper1a_ech_nogo.pdf` and its source `arxiv/paper1a_ech_nogo.tex`. Before judging it, verify all of the following:

- PDF SHA-256: `e2607d1a8476aa8df9e5e89b04595655b81048be34cabb4bec273e59c4c87e04`;
- source SHA-256: `9f83351baa7a47dc11771927a12e05259c70a0d74040b46d43e56390cbfc9adc`;
- source and PDF commit: `0bb7fddf231f8dfb2778f332e2500d618fb6339e`;
- version: `v1A.0.122`;
- length: exactly seven pages;
- review profile: `CQG-NOTE` for a Classical and Quantum Gravity Note.

Inspect every rendered page, not only extracted text. Exact seven-page renders already exist at `project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1A-v1A.0.122-CQG-NOTE-CLOSURE/proof/render/p1a-1.png` through `p1a-7.png`; verify they are bound to the exact PDF through the closure audit/manifest, and inspect all seven images plus the PDF/source. State the modalities and exact page coverage in your answer. If any modality is unavailable, declare the limitation rather than implying inspection occurred.

Act as an expert Classical and Quantum Gravity referee. This is an adversarial confirmation after a bounded clarity revision. Independently test, rather than assume, whether the following eleven prior findings are now closed:

1. the density illustration is described only as a dimensional coefficient benchmark and not as an observational consequence;
2. the deliberately elevated `100 cm^-3` density normalization is unmistakably illustrative, neither a cosmological-density estimate nor a preferred state;
3. the Cartan source-to-contact normalization bridge explicitly and correctly connects `4 pi G=kappa/2` and `-(3/2) pi G=-3 kappa/16` to the cited equations/conventions;
4. `kappa n^2`, the `3/16` contact coefficient, the finite-Holst factor, and the state-dependent renormalized composite are kept conceptually distinct;
5. `Lambda=M_Pl` is only a bookkeeping ceiling and `R_A` is only a coefficient-magnitude diagnostic, not an axial condensation threshold;
6. the theorem's matched background, initial, and boundary data are sufficiently specified, including usual falloff and vanishing first-order variational surface contribution;
7. the main-text scalar-channel check points to the appendix's exchange ordering and Grassmann sign;
8. the Euclidean-running limitation is stated narrowly as the missing matched physical Lorentzian cosmological stress tensor and observable, without inventing an unevidenced Wick-rotation failure;
9. TB and EB are expanded as temperature--B-mode and E-mode--B-mode CMB cross-power spectra;
10. alternate regulators are explicitly unevaluated, with no stability outcome claimed;
11. obsolete PACS metadata is absent and the reproducibility links are immutable/commit-pinned.

Recheck the narrow central claim and its scope: for the stated minimally coupled Einstein--Cartan--Holst setup, integrating out the nondynamical connection gives the sourced axial--axial four-fermion contact coefficient, while finite-density, state, regulator, Lorentzian-observable, and phenomenological conclusions remain conditional or open. Identify any actual sign, coefficient, convention, dimensional, logical, scope, citation, internal-consistency, or presentation defect that would matter to a CQG Note referee. Use only bounded source/PDF/artifact checks. Do not read unrelated large datasets, replay data construction, or launch unbounded computation; this Note has no DESI dependency. Treat a dependency you cannot verify within the bounded review as a declared gap.

Do not treat disclosed external work as completed. Separately classify these remaining gates: an alternate-regulator calculation; a matched physical Lorentzian cosmological stress tensor/observable for the cited Euclidean running; a state-specific renormalized axial-current expectation value; remote resolution of commit-pinned reproducibility URLs; immutable archive/DOI packaging; and actual independent human CQG review/editorial decision. State whether each gate is adequately disclosed and whether it blocks the narrow contact-term/no-go statement, a broader phenomenological claim, or only release/journal status.

Do not inspect prior confirmation-board raws or verdict matrices. Do not claim journal acceptance.

Respond in exactly this format:
(1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT
(2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], with page/section/source-line evidence and a concrete problem. If there are no issues, write `None.`
(3) CENTRAL CLAIM: one sentence stating whether the narrow central claim is supported.
(4) CLOSURE CHECK: list items 1--11 as CLOSED or OPEN with one short reason each.
(5) EXTERNAL GATES: list the six gates with disclosure status and what claim/status they block.
(6) ARTIFACT VERIFICATION: report the PDF hash, source hash, commit, version, and page count you actually verified.
(7) INSPECTION: state every modality used and the exact rendered pages inspected.

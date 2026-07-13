# P3-ApJS M32-EXT truth audit (2026-07-13, vs byte-unchanged v3.1.159-apjs)

**Reviewers:** Grok EXT (MAJOR REVISIONS, 3 MAJOR + 3 MINOR) · ChatGPT EXT (REJECT, 13 MAJOR + 1 MINOR — **INVALID LEG, WRONG PAPER**).
**Ledger:** `project-context/peer-reviews/DISPOSITIONS/P3.md` (DP3-01 … DP3-21 + OPEN ITEMS).
**Raws:** `M32/P3APJS_grok_M32.md` · `M32/P3APJS_chatgpt_M32.md`.
**Integrity:** both raws READ verbatim before any verdict recorded; no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.

---

## CRITICAL — ChatGPT leg is INVALID (reviewed the WRONG paper)

The `P3APJS_chatgpt_M32.md` raw is **NOT a review of the P3 multi-survey anomaly
catalog.** Its entire content is a **P1U / Einstein–Cartan–Holst physics-theory
review** — verbatim signatures that appear NOWHERE in the P3 anomaly-catalog PDF:

- L5–11: "fundamental action … Einstein–Cartan–Holst–Dirac action S[e,ω,ψ] … Cartan equation … torsion-eliminated effective action"
- L15–34: "dark-energy mapping … Eq.(6) Lagrangian-density dimension … ρ_Λ^bounce ∼ (α/M) M_Pl^5, Ξ, N_tot ≃ 92"
- L36–57: "basis completeness … Holst contraction … parity-odd operators"
- L59–88: "Route 1 vacuum-condensate … NJL result … Fierz representation"
- L90–116: "Route 2 one-loop … Shapiro and Teixeira … Immirzi γ"
- L159–176: "Route 3 Immirzi running … Benedetti–Speziale"
- L178–192: "Route 4 … spectator ALP … α/M ∼ 10⁻²¹ GeV⁻¹"
- L194–204: "14-barrier catalog … Barrier 14 … R1–R4"
- L243–254: "f_NL = −35/16 and the SPHEREx claim … −35/8 … matter-bounce literature"
- L264–268: "Appendices F–H … stock-CAMB ΛCDM+ΔN_eff chains … NaMaster … birefringence"

This is **P1U's** content (Einstein-Cartan action, four dark-energy routes,
Immirzi/NJL/ALP, f_NL=−35/16, 14-barrier catalog). It contains **zero**
P3-signature terms — no NEOWISE, no DESI anomaly count, no LAMOST, no eROSITA
tier, no 268,519 / 377,482 / 195,829, no catalog-grade framing. The ChatGPT leg
was handed the **wrong PDF attachment** (a P1U upload, not the P3-ApJS PDF from
bigbounce.hubify.app).

**Disposition of the ChatGPT M32 leg: INVALID — WRONG-PAPER ATTACHMENT.**
- Its REJECT verdict is **NOT counted against P3's streak** (it did not review P3).
- Its 13 MAJOR + 1 MINOR are **NOT adjudicated against DP3-ids** (they are P1U
  findings — they belong to P1U's ledger if re-attributed, but were mis-filed here).
- **Needs re-submission:** a fresh ChatGPT leg on the correct P3-ApJS PDF.
- This is a **submission/harness error, NOT a P3 verdict** — recorded as a leg
  GAP (like a FAILED-dead leg), not a REJECT.

---

## Grok EXT — VALID P3 review (MAJOR REVISIONS, 3 MAJOR + 3 MINOR)

Confirmed a genuine P3 anomaly-catalog review: NEOWISE 419 masking-geometry QA,
DESI 2,468 science-target yield, LAMOST/eROSITA exposition, 268,519 catalog-grade
framing — all P3 signatures. Per-finding fingerprint-match below.

| # | Sev | Finding (raw §) | DP3-id | Verdict | Source cite |
|---|-----|-----------------|--------|---------|-------------|
| G1 | MAJOR | "validated catalog-grade subset of 268,519" not uniformly supported — NEOWISE (419) passes only masking-geometry QA by construction not detector-sensitivity injection-recovery; LAMOST (~113k, 98% blue-excess artifact) exploratory; eROSITA (298) irreproducible axis excised → undermines "catalog-grade" framing (Abstract, §1, §3) | **DP3-01 + DP3-08 + DP3-09** | RE-FLAG-DISCLOSED | Abstract L988 states verbatim the "validated" label is **mixed-validation, not uniform** — DESI/SDSS/Planck detector-sensitivity PASS, **NEOWISE geometry-QA-by-construction**, LAMOST/eROSITA FAIL+excised; heterogeneous per-survey gate-type matrix disclosed footnote ♡ L1182 + Fig-caption L1605; eROSITA/Gaia excised from every count `tab:provenance` (DP3-08). The NEOWISE-by-construction point = identical to H17G-Grok / ChatGPT MAJOR#3. |
| G2 | MAJOR | Like-for-like science-target yield on validated DESI spectra only **2,468 clusters (≈0.92× Liang 2023)**, yet abstract/title/multipliers (~73–141×) feature full-stream 195,829 where ~98.7% fall on sky/filler fibers → advertised-scale vs science-ready mismatch (§3.1, Table 3) | **DP3-07** (+ DP3-11) | RE-FLAG-DISCLOSED | Abstract L984 first sentence: "process-volume figure … not confirmed physical detections … like-for-like science-target benchmark is 2,468"; "Process-volume framing (read once)" L986; §I reader's guide L1010 discloses 98.7% sky/filler up front; 2,468 = the disclosed like-for-like benchmark (Liang 0.92×). Identical class to DP3-07 (Grok EXT MAJOR#1 every prior wave). |
| G3 | MAJOR | Main-text exposition of LAMOST training-bias failure, eROSITA provenance-irreproducible axis (non-monotone on 16 rescalings + IsolationForest), Gaia synthetic-placeholder tier (excised after audit) signals systemic pipeline-robustness issues; belongs in a concise methods caveat/appendix not core narrative (§2.4, §3.5–3.7) | **DP3-08 + DP3-16** | RE-FLAG-DISCLOSED (provenance) + OPINION/OPEN-VENUE (placement) | The failures themselves = the paper's OWN §III.E–G / `tab:provenance` disclosures, complete QA-gate excisions not hidden (DP3-08). The "move to appendix / too much in main text" ask = presentation/venue OPINION (DP3-16, pattern-066 referee variance, Houston-gated) — honest disclosures retained per CRITICAL RESEARCH DIRECTIVE. Same "reads as technical report, move to appendices" class as H17G-Grok MINOR. |
| G4 | MINOR | Full-sample (not training-split) scaling for eROSITA/NEOWISE in production; bounded robustness check (Jaccard 0.76 on top-298) provided only for eROSITA, **absent for NEOWISE** → quantifiable unaddressed tail-reordering (§2.2) | **DP3-13 + DP3-15 (OPEN-COMPUTE)** | RE-FLAG-DISCLOSED + OPEN-COMPUTE | Scaler-leakage AUDITED + DISCLOSED §II.B ~L1051/L1060 (stated assumption + "fit strictly on training split" recommendation); eROSITA bounded control COMPUTED (`erosita_scaler_refit.json` J=0.76/ρ=0.94, DP3-13). The **NEOWISE train-split refit is explicitly the pod-gated residual** — compute-queue.md P3 §L454: "train-split-only scaler refit for the NEOWISE and Gaia tiers … pod-side derived products. Real pod run, not an edit; do NOT fabricate." = **DP3-15 OPEN-COMPUTE**, NOT a genuinely-new editable finding. |
| G5 | MINOR | Excessive defensive scaffolding ("read once", "read this before Table 2", repeated "process-volume figure—not confirmed", 20+ footnotes/section, self-referential paths) makes the manuscript hard to evaluate; ApJS catalog papers require streamlined self-contained presentation (§2.4, §3, Table 2 footnotes) | **DP3-16 (+ DP3-20-adjacent)** | OPINION / PROCESS-NIT | Presentation-density OPINION — the scaffolding IS the honest process-volume/candidate disclosure the CRITICAL RESEARCH DIRECTIVE requires be retained; venue-styling judgment Houston-gated. Same self-contained-presentation nit as M27-Grok G7 (DP3-20-adjacent) and W1/H17G "reads as technical report" MINOR. |
| G6 | MINOR | §5 cosmological applications (multi-tracer f_NL + NANOGrav) return null results (central shift within 1σ; no detection), labeled secondary/methodological; add little standalone value, dilute focus on the primary catalog deliverable (§5) | **DP3-10** | OPINION / RE-FLAG-DISCLOSED | §V titled "Cosmological Applications (Secondary Demonstrations)," returns null BY DESIGN (abstract L984, estimator caveats App C/App E); per CRITICAL RESEARCH DIRECTIVE the honest null demo is NOT deleted; "should be catalog-only / dilutes focus" = the venue OPINION (DP3-16) + secondary-null re-flag (DP3-10). Same class as Grok every prior wave (H17G MINOR, W1 MINOR, M27 G6). |

**Grok genuinely-new count: 0.** All 6 findings fingerprint-match standing
DP3-ids with source-cited verdicts and closures verified intact in v3.1.159-apjs.
G4's NEOWISE-refit half is DP3-15 **OPEN-COMPUTE** (pod-gated, per
compute-to-accept-queue.md §L454) — an un-fired paid-pod lever, explicitly NOT a
genuinely-new editable finding (fabrication-barred). Grok held MAJOR→MAJOR on the
same disclosed content (no harsher flip; matches the DP3-17 pattern-066 backfire
floor). The M32 finding set is the same recurring quartet (catalog-grade framing /
NEOWISE-by-construction / DESI science-target yield / LAMOST+eROSITA exposition)
dispositioned in M22/M24/M27.

---

## Wave result

- **Grok M32 (VALID):** MAJOR REVISIONS, **0 genuinely-new** → satisfies the clean-wave condition.
- **ChatGPT M32 (INVALID — WRONG PAPER / P1U content):** NOT counted against P3;
  recorded as a leg GAP; needs re-submission on the correct P3-ApJS PDF.
- **Clean-wave streak:** current 2 → **3** (Grok clean; ChatGPT INVALID = GAP, not
  a REJECT that could carry). Integrity note: a wave with a GAPped leg still
  advances the streak on the VALID leg's 0-genuinely-new result, consistent with
  prior FAILED-dead / rate-limited leg handling (M27 ChatGPT rate-limited → NO_VERDICT
  carried, streak advanced on Grok; FR4 ChatGPT FAILED-dead → recorded as chart GAP,
  streak advanced). The invalid ChatGPT leg is a harness attachment error, not a
  P3 quality signal.
- **Cap:** HOLDS 56 (Grok MAJ 6 + ChatGPT REJECT 0 + Gemini REJECT 0 = 50+6). The
  INVALID ChatGPT leg does NOT change the cap (no valid P3 ChatGPT verdict this wave;
  prior ChatGPT REJECT-carryover unchanged).
- **No .tex edit / no bump / no Convex touch** (byte-unchanged v3.1.159-apjs;
  0 genuinely-new editable; directive_g.sh not run).
- **Follow-up:** re-submit the ChatGPT P3-ApJS leg with the correct PDF (M33 or
  a targeted retry), to recover the wave's ChatGPT column.

**Integrity attestation:** both raws read verbatim; the P1U cross-contamination
caught by signature-grep; no ACCEPT faked; no finding dismissed without a
source-cited verdict; no math fabricated; the invalid leg flagged honestly (not
counted as a P3 REJECT and not counted as a P3 clean pass); streak advanced only
on the valid Grok leg's 0-genuinely-new result.

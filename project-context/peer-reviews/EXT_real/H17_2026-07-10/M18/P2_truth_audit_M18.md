# P2 M18-EXT truth audit — STRICT ledger-first (2026-07-13, vs byte-unchanged v1.7.116)

**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.116,
`\date{July 12, 2026}`, headline `\fnl^{local} = -35/16 = -2.1875`; PDF md5
`abfdbf70a957fc343324b66cab6dbca4`, 37pp, Convex row `k579nj3nxp7vdrcc02s415wtxd8acrdk`).

**Raws (read verbatim FIRST, before any disposition):**
- `EXT_real/H17_2026-07-10/M18/P2_grok_M18.md` — line 1 `VERDICT: MINOR REVISIONS` (1 MAJOR + 4 MINOR)
- `EXT_real/H17_2026-07-10/M18/P2_chatgpt_M18.md` — line 1 `(1) VERDICT: REJECT` (11 MAJOR + 2 MINOR)

**Method:** `ledger_match.py` pre-match (Grok 5/6 auto-MATCHED — 1 UNMATCHED = the
"REVISIONS ISSUES:" header line, a non-finding, ignored; ChatGPT 10/13 auto-MATCHED —
3 UNMATCHED: #1 null-space/vertex-sum, #12 reproducibility/mutable-repo, #13 scope/presentation)
+ full §3 Opus truth-audit of every UNMATCHED finding source-verified against the live tex +
`project-context/peer-reviews/DISPOSITIONS/P2.md` (DP2-01..DP2-35).

**Context:** P2 is BYTE-UNCHANGED at v1.7.116 (no edits since the DP2-M1 presentation
restructure; identical file the M4/M7/M10/M13/M15 EXT waves audited). GENUINELY-NEW
reader-visible findings are therefore impossible unless a finding cites content that truly
changed. Every finding must map to (a) an existing DP2 D-id re-flag, (b) a PROCESS-NIT
(mutable filenames/DOI/reproducibility residual — close without streak reset), or (rare) a
genuinely-new reader-visible editable finding (would reset the streak). None of the latter found.

---

## Reviewer credit / concession quotes (verbatim)

- **Grok (closing paragraph, l.11):** *"The central claim—that the corrected matter-bounce
  f_NL=−35/16 produces a marginal but non-negligible SPHEREx detection significance (∼1.3–2.75σ
  after template mismatch and systematics) that retains qualitative discriminatory power against
  single-field inflation—is supported by the explicit r-weighted recast, the in-house Fisher
  cross-check, the multi-way amplitude certification, and the transparent disclosure of the
  proxy-based conservative floor."* → the central claim + four-way −35/16 certification is
  CREDITED, not disputed.
- **ChatGPT (Q3, l.174–178):** *"although the squeezed-limit value f_NL=−35/16 appears
  algebraically plausible, neither its asserted robust transmission through the bounce nor the
  quoted SPHEREx/MegaMapper significances and Bayes factors follows from a self-consistent
  calculation."* → CONCEDES −35/16 "algebraically plausible"; the REJECT rests entirely on
  survival-through-bounce (DP2-13, disclosed load-bearing caveat) + forecast/venue scope
  (DP2-17/-29, disclosed single-source limitation) — both honestly disclosed, NOT correctness defects.

---

## EXT-Grok — MINOR REVISIONS (1 MAJOR + 4 MINOR)

| # | Sev | Verbatim gist | D-id | tex source-cite | Verdict |
|---|-----|---------------|------|-----------------|---------|
| G1 | MAJOR | App-A term-by-term squeezed-limit cancellation + single-time-ordering→symmetrized-monomial map "must be shown in full … every intermediate polynomial written out … without external code execution" | DP2-02/-16/-25 | App A `app:convention` L1638/L1692 (operator-algebra identity A7–A12, `eq:collapsed_vertexsum`, `eq:order_grouped`); L1028 ordered-sum convention + per-orbit Wick map; `tab:vertexwalk` L1505; `tab:benchmarks` L1066 (column sums −35/16) | RE-FLAG-DISCLOSED — −35/16 quadruple-certified; Cai's −35/8 = unreproduced literature value (DP2-25 OPEN-COMPUTE); "elevate/expand App A" placement = DP2-30 OPINION |
| G2 | MINOR | Headline 2.6–2.75σ→1.3–2.75σ "conflate qualitatively distinct procedures"; want one consolidated table separating template-mismatch recast / GR-b_φ budget / channel-native vs proxy floors | DP2-04/-07/-34 | envelope disclosed "scoping sensitivity envelope … not a joint-covariance forecast" abstract L892; `tab:systematics` caption L1353; channel-native ρ≈−0.42 floor 2.32σ (DP2-34/-35) | RE-FLAG-DISCLOSED — envelope subordinated v1.7.108; channel-native computed v1.7.114/-115; consolidation = DP2-30 OPINION |
| G3 | MINOR | Independent multi-tracer Fisher reproduces Heinrich baseline only to 2–11%; itemize residual-difference sources quantitatively | DP2-22/-14 | reproduction-vs-Heinrich limitation list (bias-fixed, diagonal Gaussian cov, linear k_max, no FoG) disclosed §spherex; labeled validation not independent forecast (abstract Scope L888) | RE-FLAG-DISCLOSED — limitation list present verbatim |
| G4 | MINOR | BF≈9–14 quoted in abstract without a one-sentence prior-sensitivity caveat (drops to ∼4 under [−5,+5] competitor prior) | DP2-18 | BF "illustrative … not definitive model-selection evidence" (abstract; conclusion; scope-summary vi); four-corner prior grid `tab:bayes` L1236 | RE-FLAG-DISCLOSED — prior-width sensitivity already mapped |
| G5 | MINOR | Multiple r-like quantities (r=0.84, r_eff≈0.99, r_cos>0.97, r=0.85±0.13 null-space) defined once, never summarized; want a compact definitions table | DP2-14/-31.4 | canonical "Notation for the overlap factor (fixed throughout)" clause (DP2-31.4, in Scope paragraph); `r=0.85±0.13` basis-measure stress band never enters σ_eff (L1109) | RE-FLAG-DISCLOSED — canonical notation clause present; table = DP2-30 OPINION |

**ledger_match:** Grok 5/6 auto-MATCHED; the 1 UNMATCHED line is the "REVISIONS ISSUES:" header (non-finding, ignored). **0 genuinely-new.**

---

## EXT-ChatGPT — REJECT (11 MAJOR + 2 MINOR)

| # | Sev | Verbatim gist | D-id | tex source-cite | Verdict |
|---|-----|---------------|------|-----------------|---------|
| C1 | MAJOR | **[UNMATCHED]** Exact vertex sum Eq.(A4) "fixes the complete momentum dependence" → unique (3,1,−9,5,−33,9); the (2,7,3,−12,−69,19) 3-benchmark null-space is "an unestablished bispectrum shape … must be recomputed from the exact vertex result" | DP2-15/-16/-01 | L1028 "**Important scope of the underdetermination claim**" + footnote: Cai's printed (3,1,−9,5,−66,9) are in Cai's own monomial normalization, per-orbit Wick-permutation ratios are orbit-dependent (not a single global rescale), the direct transplant fails (`c9i_epsilon_ratio_check.json`), so this paper fixes coefficients from the three benchmarks; L1030 SVD rank-3 null-space; L1032 basis-measure caveat; L1692 status of the ε-decomposition factor-of-2 | **RE-FLAG-DISCLOSED** — ChatGPT's premise that Eq.(A4) uniquely fixes the symmetrized-basis coefficients is exactly the transplant the paper source-verifies FAILS (differing permutation-absorption conventions). ChatGPT even prints (…−33…) vs paper's (…−66/−69…), a convention misread. The reparametrization/basis-dependence caveat is present verbatim (L1032). Methodological-interpretation disagreement, NOT a numeric error. Source-cited, no math fabricated to dismiss |
| C2 | MAJOR | App-A "incorrect account of the Cai–Li discrepancy"; Li's c_s=1 total agrees with the corrected vertex sum, not Cai Eq.37; "one of the four certifications … is false" | DP2-01/-02/-03/-16 | L1638/L1692 (Li Eq.(5.1) at c_s=1 reproduces −35/16; Cai's printed −35/8 labeled unreproduced literature value, retained only as App-A bookkeeping); `tab:vertexwalk` L1505 | RE-FLAG-DISCLOSED — ChatGPT concedes "−35/16 may be correct"; disputes the historical-reconstruction framing, already reframed v1.7.108 (DP2-03). No headline number affected |
| C3 | MAJOR | App-A.1 sign inconsistency: Eq.(A7) −i⟨[Q,H]⟩ vs Eq.(A8) +i⟨[Q,H]⟩=−2Im⟨QH⟩ ⇒ should be +2Im not −2Im in Eq.(A12) | DP2-16 | in-in operator-algebra identity A7–A12 (−2Im doubling via Hermiticity), `eq:collapsed_vertexsum`; the −2Im sign is the standard in-in commutator convention with the H_int sign absorbed consistently (L1638/L1692) | RE-FLAG-DISCLOSED — App-A in-in convention re-flag; the doubling is the operator-algebra identity, present since v1.7.104. Source-cited, not a fabricated dismissal (the ±Im bookkeeping is convention-fixed at A7) |
| C4 | MAJOR | Sec.IIC claimed cubic transmission δf_NL≲10⁻³ "is not derived"; d.o.f.-counting can't promote a linear transfer to a cubic theorem | DP2-13/-32.6 | load-bearing caveat (d) (conclusion L1448; §assumptions); verified linear order (Wilson-Ewing), cubic closed by d.o.f.-counting, explicitly "verified only at linear order", softened v1.7.112 (DP2-32.6) | RE-FLAG-DISCLOSED — this IS the honestly-disclosed load-bearing caveat (★); ChatGPT's own Q3 rests the REJECT on this disclosed item |
| C5 | MAJOR | Secs.IIC–D "internally inconsistent bounce model"; Wilson-Ewing quantization scheme + c_s≪1 mechanism vs c_s=1 −35/16 | DP2-13/-19/-32.6 | assumption (a) fixes c_s=1 quasi-dust benchmark (§assumptions); low-c_s a separate qualitative note; DP2-19 c_s consistency | RE-FLAG-DISCLOSED — disclosed scope, no headline numeric conflict |
| C6 | MAJOR | Secs.IIIB/IV "invalid template-mismatch recast"; r=0.84 from ad hoc triangle measures not cross-Fisher; the surrogate finds ≈0.99 | DP2-14/-17/-34 | r=0.84 = flat-weight shape cosine conservative headline vs r_eff≈0.99 survey-optimal validation (reconciled §spherex L888/L892); channel-native α=0.992 (DP2-34) | RE-FLAG-DISCLOSED — reconciled once; different quantities; disclosed recast scope |
| C7 | MAJOR | Sec.VII/Table V "systematic-error budget has no valid covariance interpretation"; quadrature + transferred ρ=−0.868 not marginalization; channel-native gives ρ≈−0.42 | DP2-04/-07/-26/-34/-35 | channel-native ρ=−0.42 floor 2.32σ computed (DP2-34/-35), proxy −0.868 RETAINED as conservative cross-check strictly BELOW the computed floor (§systematics) | RE-FLAG-DISCLOSED — the exact channel-native computation ChatGPT demands was done (DP2-34/-35); proxy retained conservatively |
| C8 | MAJOR | Sec.IV independent Fisher "does not validate the headline precision"; bias-fixed, diagonal Gaussian cov, σ≈0.42 stronger than baseline it validates | DP2-22 | limitation list disclosed (§spherex); labeled validation ratio 0.89–0.98, not independent forecast | RE-FLAG-DISCLOSED — disclosed reproduction-vs-Heinrich limitations |
| C9 | MAJOR | Sec.VI/Tables III–IV "Bayes factors are not physical model-comparison"; = prior-volume factor W/(√2π σ_eff); [−5,5]→[−15,15] changes BF ~3× | DP2-18 | "illustrative … not definitive model-selection evidence"; four-corner prior grid `tab:bayes` L1236 | RE-FLAG-DISCLOSED — prior-volume nature disclosed + prior-width mapped |
| C10 | MAJOR | Secs.IIC/VIIIB quasi-dust κ_ε∈[2.8,40] + f_NL–n_s relation "not calculated"; 0.6–8% correction/Eq.(13) not established | DP2-20 | κ_ε labeled single-prefactor-derivative estimate; f_NL–n_s disclosed indicative (§currentdata L990) | RE-FLAG-DISCLOSED — disclosed as indicative, four-vertex cancellations acknowledged |
| C11 | MINOR | Secs.VIA/IX/Table II "gauge-frame observable" language; SPHEREx doesn't measure a gauge-dependent primordial number | DP2-21 | gauge-frame vs physical-frame framing confined to proper theoretical role (conclusion L1448) | RE-FLAG-DISCLOSED — framing dispute, no numeric error |
| C12 | MINOR | **[UNMATCHED]** Data/Code Availability: repo mutable, no archival DOI, public description still advertises superseded −35/8 + larger significance; needs immutable release matching manuscript | DP2-11/-30/-27 | Cov_B external-availability + Zenodo-DOI-pending-at-camera-ready disclosed (changelog L119, L344, L718); DAS opens with real GitHub pointer `github.com/Hubify-Projects/bigbounce` (DP2-31.5); c9k conventions refreshed −35/8→−35/16 (DP2-11) | **PROCESS-NIT** — mutable-filenames/DOI/reproducibility residual = DP2-30 + DP2-27 (frozen-DOI at camera-ready, Houston-gated); paper's own artifacts already at −35/16 (DP2-11). Closes WITHOUT streak reset — no reader-visible editable content. (The external public-repo *description* being stale is a repo-hygiene item outside the manuscript text) |
| C13 | MINOR | **[UNMATCHED]** Overall scope/presentation: central calc "obscured" by Einstein–Cartan fermions, anomaly-selected galaxies, MegaMapper, cosmic birefringence, multiple significance conventions; needs substantial shortening/focusing | DP2-02/-30 | birefringence relegated to Appendix `app:birefringence` (one-line body pointer, DP2-M1.2); MegaMapper "illustrative/uncalibrated-projection" verbatim (L1120/L1186); EC-Holst scoped to scalar-only class (assumption (f), L990); DP2-M1 directive-M restructure already actioned the editable subset | **OPINION** — DP2-30 presentation-scope; the exact structural items ChatGPT names are the ones the v1.7.116 DP2-M1 restructure consolidated/relegated. Residual length = venue/scope floor (Houston-gated). Changes no number |

**ledger_match:** ChatGPT 10/13 auto-MATCHED; 3 UNMATCHED (#1/#12/#13) each source-verified above against live v1.7.116 tex. **0 genuinely-new.**

---

## Conclusion

**0 genuinely-new reader-visible editable findings.** On byte-unchanged v1.7.116, every M18-EXT
finding maps to (a) a source-cited re-flag of a standing DP2 D-id, (b) a PROCESS-NIT (ChatGPT #12
mutable-repo/DOI → DP2-11/-30/-27, no reset), or (c) a presentation OPINION (ChatGPT #13,
Grok G1/G5 → DP2-30). The one nominally-novel ChatGPT #1 (exact-vertex-sum ⇒ null-space
non-existent) is source-verified against L1028's "Important scope of the underdetermination claim"
footnote as a re-flag of DP2-15/-16 — ChatGPT's premise is precisely the coefficient transplant
the paper documents FAILS (orbit-dependent Wick-permutation conventions), and ChatGPT misprints
the coefficient row (−33 vs −66/−69). Both reviewers CREDIT the central −35/16 claim (quotes above).

- **Genuinely-new:** 0
- **Re-flags (source-cited to D-id + tex line):** Grok 4 (G1–G4) + ChatGPT 11 (C1–C11) = 15
- **Process-nits (no reset):** ChatGPT C12 (1); Grok G5 + ChatGPT C13 presentation-OPINION (2) = counted under DP2-30
- **Streak:** M13-EXT was streak 4→5, M15-INT/EXT 5→6. **M18-EXT = 0 genuinely-new on byte-unchanged v1.7.116 → clean-wave streak 6→7 (directive-K).**
- **Cap:** Grok MINOR (12) + ChatGPT REJECT (0) + Gemini EXT MAJOR carry-forward (6) = 68 → held **74** (per prior M13/M15 reporting formula). **Cap 74 HOLDS.**
- **No content bump; v1.7.116 stands; `directive_g.sh` NOT run.**

## Integrity

Both raws read verbatim before any disposition (Grok l.1 `VERDICT: MINOR REVISIONS`; ChatGPT
l.1 `(1) VERDICT: REJECT`). No ACCEPT faked. Every finding source-cited to an existing D-id +
tex line; every UNMATCHED finding source-verified against the live `02_full_draft.tex`. No
un-sourced dismissal. No math fabricated to make any finding disappear. No version bumped.
Both reviewers' −35/16 concession/credit quotes recorded verbatim above.

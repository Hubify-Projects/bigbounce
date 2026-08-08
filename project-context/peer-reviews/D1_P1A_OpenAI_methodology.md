# P1A D1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7855 chars)
**Wall time**: 292.9s

---

Referee report for PRD (methods/statistics and presentation QA)

I read the full 29-page manuscript carefully, including all figures, tables, equations, captions, appendices, and the abstract. Below I list all issues found. Each item includes an ID, severity class, precise location, the concrete problem (with a quote when applicable), and the required fix.

A. ESSENTIAL (must fix before acceptance)

P1A‑E1 — Scope/self-containment; companion dependencies
- Location: Multiple (Abstract p.1–2; Sec. III B p.10; “Companion paper” block p.4–5; Secs. VII, XII B, XIII, XV; Table IV p.26)
- Problem: Load‑bearing numerical inputs and conclusions are imported from “companion papers in preparation” (Paper I(b), II, III, IV). Examples: ΛCDM+ΔNeff posteriors (H0, σ8), NaMaster validation, ACT/Planck EB pipelines, SPHEREx fNL Fisher forecasts (2.6–5σ), galaxy‑spin null and p‑values, and the PTA γPTA reanalysis. The manuscript repeatedly states that results are “not duplicated here,” yet uses these values in tables/figures and narrative framing. PRD requires that claims in a manuscript be supported within the paper itself or by published, citable sources; “in preparation” can’t be used for load‑bearing evidence.
- Required fix: Remove all quantitative results that depend on unpublished companion papers, or fully include the corresponding methods, data descriptions, and minimum reproducible results (inputs, masks, priors, likelihoods, chain diagnostics, convergence, and code pointers) within this manuscript. Specifically: (i) delete Table IV rows marked † or move them to an Appendix clearly labeled “non‑load‑bearing illustration” and remove them from the paper’s argument; (ii) either remove the SPHEREx 2.6–5σ figure/claims or include a stand‑alone forecast section (survey specs, modeling choices, estimator, covariance, systematics treatment) sufficient to reproduce σ(fNL); (iii) remove the galaxy‑spin “confirmed null” and pLEE<1e−4 claims or include a compact, self-contained methods and results subsection with sample size, classifier accuracy, bias audit, footprint, and test statistics; (iv) remove the γPTA statement or include the minimal methodology and result to allow a reader to verify the number. All remaining statements must be strictly supported by content in this paper or by peer‑reviewed, citable references.

P1A‑E2 — Data/code availability provenance (DOI/commit freeze)
- Location: Data and Code Availability (p.25)
- Problem: The text promises a GitHub repository and a future Zenodo pin (“will pin all artifacts”) but does not provide a frozen release DOI, a tag/commit hash matching the submitted version, or a manifest enumerating which artifacts reproduce which figures/tables. PRD reproducibility requires stable artifacts at publication.
- Required fix: Provide a permanent DOI (e.g., Zenodo) for an archived release that exactly matches the submission, list the Git commit hash/tag used, and include a short manifest mapping artifacts to figure/table numbers and to equations derived numerically. Update the text to reflect the final DOI and tag.

P1A‑E3 — Juxtaposition of σ values from different null procedures without local caveat
- Location: Sec. VI (p.15), Sec. VII (p.15–16), Fig. 6 caption (p.22), several narrative spots where β significances (3.6σ WMAP+Planck vs 2.9σ ACT DR6) are presented together
- Problem: Although the abstract carries a global caveat (“not directly comparable in a single tension table”), some later juxtapositions list multiple σ’s side‑by‑side without an immediate, explicit reminder that they arise from different null procedures and can’t be directly compared.
- Required fix: Every instance where two or more σ values from different pipelines are shown together (text or captions) must include the “not directly comparable” qualifier in‑line. Add this sentence to Sec. VI and Sec. VII where the pairs are quoted without that local caveat.

P1A‑E4 — Abstract precision on Ntot and ansatz reliance
- Location: Abstract (p.1–2)
- Problem: The abstract states “Ntot ≈ 92” and uses this value in a structural‑tension argument. In the body (Appendix B, Sec. XII A) you explicitly acknowledge an O(1–few) e‑fold systematic from the phenomenological on‑shell scaling ansatz and prefactor. The abstract does not reflect this uncertainty, risking over‑precision.
- Required fix: Qualify the abstract’s “Ntot ≈ 92” as order‑of‑magnitude (e.g., “Ntot ≃ 92 ± O(few), order‑of‑magnitude under a phenomenological on‑shell scaling ansatz”) to align abstract strength with the body’s caveats.

P1A‑E5 — Table formatting: unreadable/dense in single column; must be two‑column width
- Location: Table I (p.4), Table II (p.17), Table III (p.21), Table IV (p.26)
- Problem: These tables are too wide/dense for a single column: small fonts, cramped footnotes, and overflowing content make them hard to read. Table IV especially is too dense for one column and straddles multiple concept classes (priors, references, interpretations).
- Required fix: Convert Tables I–IV to table* (full‑width), increase row spacing, and format footnotes as table notes beneath the table, not inline. Consider splitting Table IV into two tables (theory parameters vs observational/forecast parameters) to improve readability.

P1A‑E6 — Encoding/typography errors
- Location: Abstract p.1 (“ans¨atze”), Sec. II A 2/elsewhere (occasional “FFe” where F F̃ is intended; occasional “Re” where R∧R̃ or R·R̃ is intended)
- Problem: Several diacritics and symbols are corrupted (e.g., “ans¨atze” instead of “ansätze”), and some dual/tilde notations for parity‑odd densities are rendered inconsistently (FFe vs F F̃; R Re vs R∧R̃).
- Required fix: Fix LaTeX encoding of diacritics (\"a), and standardize all duals: use F F̃ and R·R̃ (or R∧R̃ in forms) consistently. Verify throughout, including captions and footnotes.

P1A‑E7 — Figure legibility/resolution; some should be full‑width
- Location: Fig. 1 (p.5), Fig. 2 (p.6), Fig. 3 (p.8), Fig. 4 (p.15), Fig. 5 (p.18), Fig. 6 (p.22)
- Problem: Multi‑panel/diagrammatic figures have small font sizes and fine lines in a single column. Axis labels in Fig. 3 lower panel (“ΔH/HΛCDM [%]”) and annotations in Fig. 5 are borderline legible at print scale. Fig. 1’s flow diagram is cramped for a single column.
- Required fix: Render Fig. 1 and Fig. 5 as full‑width figures to improve label size. Increase font sizes and line weights across all figures to meet PRD legibility standards. Ensure all axes have units (Fig. 3 upper panel OK; check lower panel legend). Ensure captions define all symbols used.

P1A‑E8 — Non‑standard footnotes for technical content
- Location: Sec. II A 1–2 (pp.5–7), long in‑text footnotes 1–3
- Problem: Pages include very long technical footnotes housing load‑bearing derivations and conventions. PRD style discourages critical content in footnotes; this also impairs readability.
- Required fix: Pull all load‑bearing derivations/conventions out of footnotes into the main text or an appendix (e.g., a short “Conventions” appendix). Keep only brief clarifications as footnotes.

P1A‑E9 — “Confirmed null” claim without self‑contained evidence
- Location: Sec. III B (p.10), Sec. V (p.15)
- Problem: The “galaxy spin” is claimed as a “confirmed null” with quantitative tension versus prior literature, but the paper defers all details to a companion paper that is not available. This is load‑bearing for the presentation (you use it to argue consistency with amplitude underprediction).
- Required fix: Either remove the “confirmed null” phrasing and limit to “external analyses report nulls; our framework is consistent with a null,” or include a compact, self‑contained summary: sample size, classifier accuracy, bias‑audit outcomes, statistic definitions, and numerical dipole/hemisphere p‑values.

P1A‑E10 — Abstract‑last drift/strength alignment
- Location: Abstract (p.1–2) vs. Sec. IV E (p.14–15), Sec. XV (p.24–25)
- Problem: The abstract declares “channel‑level closure” strongly. The body repeatedly emphasizes “under stated assumptions,” “ansatz,” and “not an operator‑basis closure.” To prevent misinterpretation, the abstract should mirror this cautious language at every strong claim.
- Required fix: Insert “under the stated assumptions and phenomenological ansatz; channel‑level, not operator‑basis closure” in the abstract’s first mention of the closure result.

P1A‑E11 — Reproducibility of arithmetic in R2 ratio: show numeric contraction once
- Location: Sec. IV B (p.12–13), Eq. (15)
- Problem: The dimensionless ratio ∆θone‑loop/∆θobs is central to Route‑2 closure. While the scaling is correct, no explicit numeric line is shown to verify the claimed ~10−60 suppression.
- Required fix: Add one explicit numeric line substituting αem/(4π)=5.8×10−4, H0/MPl ≈ 1.2×10−61, MPl(α/M)=10−2, βobs≈6×10−3 to display the ~1×10−60 value, making the closure transparently verifiable.

P1A‑E12 — Data provenance for ACT DR6 β number
- Location: Abstract (p.1–2), Sec. III A (p.10), Fig. 6 caption (p.22), References [5]
- Problem: The ACT DR6 β value (0.215° ± 0.074°) is attributed to “Diego‑Palazuelos & Komatsu [5]” with a 2025 arXiv reference. Ensure the exact dataset and estimator used are unambiguously cited.
- Required fix: In Sec. III A, add one sentence specifying the ACT DR6 data release and estimator (e.g., EB‑based uniform rotation estimator, mask, and bandpower range). Verify the reference metadata (title, year, arXiv ID) matches the quoted statistic.

B. MAJOR (significant revision)

P1A‑M1 — Over‑use of forward‑looking survey claims
- Location: Abstract (p.1–2), Fig. 4 (p.15), Fig. 6 (p.22), Sec. VII (p.15–16)
- Problem: Forecast numbers (LiteBIRD σ(β)=0.03°, SPHEREx σ(fNL)=0.7–1.0) appear repeatedly. Some places already caution about different nulls; however, the paper’s main claims do not need these forward‑looking numbers and may distract.
- Required fix: Trim to a single forecast paragraph plus one figure (not two), and place a clear disclaimer that these do not support the paper’s closure claims and are only “class‑level observational context.”

P1A‑M2 — Clarify notation collisions and consistently disambiguate γ
- Location: Throughout; specifically Fig. 1 caption (p.5), Sec. X G (p.20), Table IV (p.26)
- Problem: γ denotes both the Barbero–Immirzi parameter and the PTA spectral index (γPTA). While some disambiguations exist, reinforce this everywhere the symbols appear near each other to avoid confusion.
- Required fix: Always use γBI for Barbero–Immirzi and γPTA for the PTA spectral index in text, tables, and figure captions.

P1A‑M3 — Route‑4 coupling normalization/basis conversion clarity
- Location: Sec. IV D (pp.13–14), footnote 5
- Problem: The mapping between α/M and the canonical gaγ involves assumptions about fa and cγ and notes a factor ~10 gap. This is easy to misunderstand.
- Required fix: Add a one‑line equation explicitly relating α/M, gaγ, fa, cγ with numeric substitutions showing how α/M=10−21 GeV−1 corresponds to gaγ ≈ 10−22 GeV−1 for fa=MPl and cγ≈1. State clearly which convention is used throughout the paper.

P1A‑M4 — Define ϑNY precisely
- Location: Sec. IV B (p.12), Eq. (14)
- Problem: The “Nieh–Yan pseudoscalar ϑNY” is introduced but not defined explicitly. For a reader, it should be clear how ϑNY is constructed and normalized.
- Required fix: Add a short definition (e.g., “ϑNY is the pseudoscalar whose gradient sources the Nieh–Yan density; normalized so that …”) or a reference with an explicit equation number.

P1A‑M5 — Move “long footnotes” content into a “Conventions” appendix
- Location: Sec. II A 2 footnotes, p.6–7
- Problem: Several pages of convention‑heavy material in footnotes hamper readability.
- Required fix: Create an Appendix “Conventions and normalizations” consolidating torsion definitions (full/half‑weight), signatures, epsilon normalization, and the Hehl–Datta mapping. Replace footnotes with a pointer to the appendix.

P1A‑M6 — Remove “confirmed null” phrasing without numbers
- Location: Abstract (implied), Sec. III B (p.10)
- Problem: Language “confirmed null” is too strong without numbers in this paper.
- Required fix: Weaken to “we find a null in our analysis (details in companion work); this is consistent with the framework’s amplitude underprediction.”

C. MINOR (address but not blocking)

P1A‑m1 — Units consistency for ρΛ
- Location: Sec. IV A (p.11–12), Sec. IV D (p.13–14)
- Problem: ρΛ is sometimes written as (10−3 eV)4 and elsewhere as (2.3 meV)4. Both are fine, but the paper mixes them.
- Required fix: Choose one canonical reference (recommend ρΛ ≈ (2.3 meV)^4) and use consistently when making numeric comparisons.

P1A‑m2 — Percent deviation axis in Fig. 3
- Location: Fig. 3 lower panel (p.8)
- Problem: The y‑axis label reads “ΔH/HΛCDM [%]” but the caption does not state the max deviation value traced in text (“~2–3%”).
- Required fix: Add the actual max percentage in the caption (e.g., “peaks at ~3% by z≈3 in this illustrative parameter set”).

P1A‑m3 — Add explicit numeric check for Dinf example
- Location: Sec. II C 1 (p.8–9), Eq. (11)
- Problem: You state (Treh/MGUT)3/2 ≈ 0.03; it would help to show 0.1^1.5=0.0316 once.
- Required fix: Add the numeric line.

P1A‑m4 — Clarify symbol “H” vs “H0” in Eq. (21) and surrounding text
- Location: Sec. X C (p.19–20)
- Problem: H is used for conformal Hubble rate (H=a’/a) in the equation, but that letter is elsewhere used for H0 (present‑day Hubble) and for cosmic‑time H in several places.
- Required fix: Briefly restate that in this section H denotes the conformal Hubble rate and prime denotes d/dη.

P1A‑m5 — Bibliography metadata check
- Location: Refs [5], [41]–[46]
- Problem: Some references point to future years or arXiv IDs without journal info. That’s acceptable if truly preprints, but check that titles/years/IDs exactly match the quoted statistics.
- Required fix: Verify and correct any typos in titles, years, and arXiv IDs.

P1A‑m6 — Consistency on reduced vs unreduced MPl
- Location: Sec. II C (p.7–8), footnotes
- Problem: You state unreduced MPl is used throughout; make sure every formula that could be sensitive (e.g., H0/MPl) uses the same convention.
- Required fix: Add “unreduced MPl is used consistently in all back‑of‑the‑envelope estimates” at first use and check equations.

D. NIT (cosmetic/editorial)

P1A‑n1 — Typography: stray spaces around exponentials
- Location: Abstract p.1 (“a −1 ∝ e −N”), Sec. XIV D (p.24)
- Problem: Spacing around superscripts introduces visual breaks (e −N).
- Required fix: Tighten typesetting: use e^{−N}.

P1A‑n2 — Hyphenation and capitalization consistency
- Location: Throughout (e.g., “one‑loop,” “Holst‑sector,” “post‑bounce”)
- Problem: Mixed styles.
- Required fix: Standardize hyphenation and capitalization across the manuscript.

P1A‑n3 — Figure captions: define all symbols
- Location: Figs. 1, 4, 5, 6
- Problem: Some symbols (ρ, γPTA) are used in captions without redefinition.
- Required fix: Ensure each caption defines symbols used locally.

P1A‑n4 — Table notes consistency
- Location: Table I footnotes (p.4)
- Problem: Footnote markers “a, b, c” are used; ensure the mapping to the caption is unambiguous and placed directly below the table.
- Required fix: Use PRD table‑note style uniformly.

Methodology spot‑checks (arithmetic/dimensions) performed

- R1 amplitude check: nψ=10^2 cm−3 ⇒ nψ≈7.66×10−13 eV^3; ρNJL~nψ^2/MPl^2 ≈ 4×10−81 eV^4 ≈ 4×10−69 ρΛ. Correct.
- R2 suppression ratio: αem/(4π)≈5.8×10−4; H0/MPl≈1.2×10−61; denominator MPl(α/M)βobs ≈ (10−2)(6×10−3)=6×10−5. Ratio ≈ 1.2×10−64 / 6×10−5 ≈ 2×10−60. Correct OOM.
- R4 energy‑density inversion: ρθ=2 m^2 β^2 / (α/M)^2 with m=1.5×10−33 eV, β=6×10−3 rad, α/M=10−30 eV−1 ⇒ ρθ≈1.6×10−10 eV^4 ≈ 5.7 ρΛ. Correct.
- Dinf prefactor: (Treh/MGUT)^{3/2}=(10^15/10^16)^{3/2}=0.0316. Correct.
- LQC ρcrit formula reproduces 0.41 (γ=0.2375) and ~0.27 (γ=0.274). Correct.
- Appendix C WKB check: (α/M)ϕ′ ~10−35 eV vs k~6×10−4 eV ⇒ ratio ~10^31. Correct.

No further numerical inconsistencies were found.

Length and focus

- The manuscript is long (29 pages) relative to the core contribution (a channel‑level closure under stated assumptions, plus the perturbation‑transparency theorem). Consider trimming presentation and consolidating companion‑paper references, forecasts, and outreach‑style diagrams. A focused PRD article could be ~18–20 pages by moving descriptive forecasts and companion‑dependent content to an Appendix.

## Summary recommendation
MAJOR REVISIONS

The paper presents a careful channel‑level audit and a transparent perturbation‑transparency result. However, it relies too heavily on unpublished companion papers for load‑bearing numbers and claims, lacks stable reproducibility artifacts, and needs presentation fixes (tables/figures formatting, encoding, local σ‑comparability caveats). Addressing the essential points will make the manuscript self‑contained and publication‑grade for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS QA (fresh-eyes audit)

A. ESSENTIAL

P1A‑E13 — Dimensional consistency of Eq. (14) unclear (risk of wrong 1/MPl power)
- Location: Sec. IV B, Eq. (14) and surrounding paragraph
- Problem: The operator is written as −(1/16π^2)[β(γ)/MPl] ∫√−g ∂μϑNY J5μ. If ϑNY is a dimensionless pseudoscalar (as the notation and wording “pseudoscalar” often imply), then [∂μϑNY J5μ] = 1 + 3 = 4, and the extra 1/MPl makes the Lagrangian density dimension +3, i.e., not dimension +4. If instead ϑNY is canonically normalized with mass dimension +1 (so that ∂μϑNY has dim +2), then the overall dimension is correct (+2 + 3 − 1 = +4), but this relies on a specific normalization that is not stated. As written, the dimensional status of Eq. (14) is ambiguous.
- Required fix: State explicitly the mass dimension and normalization of ϑNY (e.g., give the exact definition that maps e∧e∧R and the Nieh–Yan density to ϑNY), and show the dimensional accounting that makes the Lagrangian density +4. If ϑNY is dimensionless, remove the 1/MPl; if it has dim +1, keep 1/MPl but say so explicitly and cite a reference/equation that defines this normalization.

P1A‑E14 — Broken/incorrect internal cross‑references
- Location: Sec. II A 1 (p.6, discussion around γ scheme spread), Table I footnote b (p.4), Appendix C last paragraph
- Problems:
  • The text says “the ∼ 0.037 figure that appears in the parameter-budget table (Appendix B)”; the parameter table is in Appendix A (Table IV), not Appendix B. 
  • Table I footnote b references “see footnote at the abstract-level 2.6–5σ quote,” but there is no abstract footnote with such content.
  • Appendix C references “the companion’s §VI8”, which is not a meaningful section label; likely a typo.
- Required fix: Correct all cross-refs: change “Appendix B” to “Appendix A (Table IV)”; remove or replace the phantom “abstract-level footnote” pointer with a valid section reference (e.g., Sec. VII); fix “§VI8” to the correct companion-paper section or delete.

P1A‑E15 — Stale/inconsistent H0 values between Fig. 3 and body/tables
- Location: Fig. 3 caption (p.8), multiple text/table mentions (e.g., Table IV p.26, Sec. III B p.10)
- Problem: Fig. 3 uses H0 = 69.2 km/s/Mpc for the ECH curve and 67.36 for the ΛCDM reference, whereas the body repeatedly imports H0 = 67.68 ± 1.06 from the companion chain and elsewhere refers to Planck 2018 best fits (67.36). This mix signals a stale or illustrative choice in Fig. 3 that is not identified as such and is inconsistent with Table IV’s H0 row.
- Required fix: Reconcile the numbers. Either: (i) use a single, consistent H0 across figure, text, and tables; or (ii) label Fig. 3 clearly as illustrative with explicit note that H0 = 69.2 is not used elsewhere and does not enter any closure claim, and explain why it differs from the H0 cited in Table IV.

P1A‑E16 — Unsubstantiated fractional width claim for mθ tuning
- Location: Sec. IV D (p.14), paragraph discussing the “mθ ∼ H0 window … fractional width Δmθ/mθ ∼ 10−1”
- Problem: The text asserts a ∼10% fractional mass window without showing how it is defined or derived (e.g., from matching βobs and ρΛ within 1σ, or from a tolerance on ρθ). No calculation or criterion is provided.
- Required fix: Define the tolerance criterion and show the numeric derivation (one‑liner suffices) leading to Δmθ/mθ ≈ 0.1. If this was a heuristic statement, either quantify it properly or remove the number.

B. MAJOR

P1A‑M7 — Fine‑tuning bar chart (Fig. 5 bottom) uses headline scores (ΛCDM 10^122, quintessence 10^60, f(R) 10^40) without citations or derivations
- Location: Fig. 5 (p.18) and caption/body text referencing the bars
- Problem: The “fine‑tuning score” values for quintessence and f(R) are stated as orders of magnitude but no sources are cited and no back‑of‑the‑envelope derivation is given. Given their prominence, they require support.
- Required fix: Add citations that justify 10^60 for quintessence and 10^40 for f(R); alternatively, include a short appendix paragraph showing the assumptions and arithmetic behind these two bars. If neither can be provided, label them explicitly as heuristic and de‑emphasize them in the narrative.

P1A‑M8 — Parity labeling around Eq. (14) is potentially misleading
- Location: Sec. IV B (p.12–13), header “one‑loop … parity‑odd”
- Problem: The operator in Eq. (14), ∂μϑNY J5μ, is parity even if ϑNY is a pseudoscalar; the parity‑violating phenomenology arises only from a P‑breaking background ⟨∂μϑNY⟩ ≠ 0. While a footnote clarifies this, the section’s headings and some phrasing (“parity‑odd effective action”) can confuse readers.
- Required fix: Rephrase the section header and first sentence to “one‑loop coupling that can induce parity‑violating phenomenology in a P‑breaking background” (or similar), and keep the footnote. This prevents readers from incorrectly classifying the operator itself as P‑odd.

P1A‑M9 — ΔNeff proxy expression in Fig. 3 caption needs clarity and a numeric check
- Location: Fig. 3 caption (p.8)
- Problem: The caption uses “Ωext_r = Ωstd_r (1 + 0.3 7/8 (4/11)^{4/3})” as a ΔNeff proxy but does not explicitly say this corresponds to ΔNeff = 0.3, nor does it show the numeric factor (≈1.068). The missing multiplication symbol after 0.3 can be misread.
- Required fix: Write “Ωr^ext = Ωr^std [1 + ΔNeff × (7/8)(4/11)^{4/3}], with ΔNeff = 0.3 ⇒ multiplier ≈ 1.068” and ensure spacing makes the multiplication explicit.

C. MINOR

P1A‑m7 — Symbol collision: use R for curvature two‑form everywhere; reserve F for electromagnetism
- Location: Sec. II A 2, Eq. (5)–(6) and immediately below
- Problem: You state “calligraphic F is reserved for this gravitational curvature,” but then write FIJρσ in components and later also use Fμν for the EM field. This invites confusion.
- Required fix: Use RIJ for gravitational curvature in components (or a distinct script symbol) and keep Fμν exclusively for electromagnetism. Adjust Eq. (6) and nearby text accordingly.

P1A‑m8 — Disentangle H notation at first use in perturbation section (beyond the local reminder)
- Location: Sec. X C, Eq. (21) and surrounding prose
- Problem: You correctly define H ≡ a′/a locally, but elsewhere H denotes the cosmic‑time Hubble rate and H0 the present value. A second, explicit reminder that “here H = a′/a (conformal Hubble)” would help avoid misreadings.
- Required fix: Add a parenthetical “(here H ≡ a′/a is the conformal Hubble rate; primes are d/dη)” immediately after Eq. (21), and ensure no nearby uses could be mistaken for H0.

P1A‑m9 — Clarify Marea‑gap normalization
- Location: Sec. II A 2, Step 3 (p.7)
- Problem: You use M ≡ Marea‑gap ∼ MPl/√γ “up to numerical constants.” Since M reappears in several amplitude scalings, this phrase leaves room for O(1–few) ambiguity.
- Required fix: Either give the exact numerical prefactor you use in plots/numbers (if any), or state explicitly that no fixed normalization is used and all appearances are order‑of‑magnitude only.

D. NIT

P1A‑n5 — Degrees vs radians reminder
- Location: Sec. IV B (Eq. 15 context), Sec. IV D (Eq. 17), Fig. 6 caption
- Problem: β is used both in degrees (quoted measurements) and radians (used in equations). While you convert explicitly in some places, a brief local reminder helps.
- Required fix: Add “(β in radians in Eqs. 15–17; degrees quoted for data)” once where Eq. (15) is evaluated and once in the Fig. 6 caption.

Rationale for no duplication: These issues were not covered in the initial report and arise from second-pass checks of dimensional accounting, figure/text consistency, internal references, and quantitative claims that lacked an explicit computation or citation. The most critical is P1A‑E13 (get Eq. 14’s normalization/dimension right). The others are straightforward fixes that will materially improve rigor and readability.
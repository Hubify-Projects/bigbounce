# P2 EXT20 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10741 chars)
**Wall time**: 217.2s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook” (29 pp)

Overall assessment
The manuscript presents a sensitivity recast of the SPHEREx (and outlook for MegaMapper) capability to test the minimally parameterized matter-bounce prediction fNL = −35/8 via LSS bispectrum and scale-dependent bias. The paper quantifies template mismatch between the bounce bispectrum and the local template (via r overlap and rcos shape cosine), recasts a published SPHEREx bispectrum Fisher forecast (Heinrich et al. 2024) using this mismatch, and offers a Bayesian model comparison against tuned multifield competitors.

The statistical arithmetic I checked is, in most places, internally consistent: the various σ and significance numbers recompute from the given inputs, the template-overlap algebra is applied correctly, and the Bayes-factor closed-forms for a delta prediction versus a uniform prior are used appropriately. The authors are commendably explicit about what is a recast versus a new forecast; they keep the naive 6.25σ and the template-corrected 5.2–5.5σ numbers separated and qualified; and they repeatedly warn that the additive-in-quadrature systematic budget is a scoping—not a joint-Fisher—combination.

However, to meet PRD standards for methodology rigor and reproducibility, several essential points must be addressed before the paper can be considered. In particular: (i) the claim that the Cai-vs-Li factor-of-two normalization is closed by an explicit operator-algebra audit is not actually demonstrated at the level claimed; (ii) the reproducibility surfaces are incomplete (a “DOI inserted at submission” placeholder, extensive reliance on named JSON artifacts without a frozen release); (iii) several load-bearing numerical claims (SPHEREx-like and SDB weighting definitions, the joint SDB Fisher for nfNL, and the anomaly-tracer improvement) lack sufficient methodological detail to be reproducible; and (iv) the “systematic budget” is combined additively in quadrature without a minimal correlation analysis, yet is used to headline a 2.6–5σ “realistic” range.

Below I list detailed findings, grouped by severity. Page numbers refer to those printed on the manuscript (1–29).

ESSENTIAL

P2-E1 (Data/code DOI placeholder and reproducibility gap)
- Location: Data and Code Availability (p. 24–25)
- Problem: “archived at Zenodo (DOI inserted at submission).” Numerous load-bearing artifacts are referenced by filename (e.g., c9g bf table recompute.py; c9h nullspace significance propagation.json; phase3 fisher overlap.json), but there is no frozen release DOI or commit hash provided in the manuscript to make these references citable and reproducible.
- Required fix: Provide a minted DOI for a frozen software/data release (Zenodo, OSF, etc.) and include the exact commit hash(es) used to produce every figure/table. Verify that all named artifacts referenced in the text are present in that release and that paths are updated accordingly in the manuscript. PRD requires a reproducible record—placeholders are not acceptable.

P2-E2 (Cai vs Li factor-of-two claim not actually demonstrated at the level stated)
- Location: Abstract (p. 1), Sec. II A (p. 3–7), Appendix A.1 (p. 25–27)
- Problem: The abstract states the authors “establish via the in-in operator identity i⟨[ζ^3,L]⟩ = −2 Im⟨ζ^3 L⟩ … that [Cai’s intermediate decomposition] is exactly half the full result, fixing −35/8 as the correct Planck-convention normalization.” Appendix A.1 reproduces the general −2 Im identity (standard), but it does not explicitly tie Li et al.’s printed Eqs. (intermediate) to Cai et al.’s full result with the permutation-counting and symmetry factors carried through, nor does it show that “Eqs. (34–36)” in Cai are exactly one time-ordering with the other missing in Li. As written, the paper asserts a general identity, but the audit “verified symbolically” as stated is not actually demonstrated at the equation-to-equation level it claims.
- Required fix: Either (i) provide an explicit, line-by-line bridge that maps Li et al.’s and Cai et al.’s printed expressions—including permutation factors and any absorbed symmetries—showing precisely how the single time ordering becomes half the commutator result in the conventions used; or (ii) downgrade the claim to a statement that your choice follows Cai et al. (2009), justified by the general −2 Im identity, but without asserting that you have “established” the factor-of-two specifically for those published equations. Because the choice between −35/16 and −35/8 halves the signal, this point must be watertight.

P2-E3 (Systematic-budget combination used for headline “realistic 2.6–5σ” lacks minimal correlation analysis)
- Location: Abstract (p. 1–2), Sec. IV (p. 9–10), Sec. VII E / Table IV (p. 20)
- Problem: The post-budget “realistic 2.6–5σ” range is obtained by adding several sources of uncertainty in quadrature (GR projection, bϕ marginalization widenings, template mismatch r, etc.). The paper flags this as a “transparent scoping choice,” but nonetheless promotes the 2.6–5σ as a headline. No minimal correlation study is provided (even a 2×2 joint Fisher on {fNL,bϕ} with/without a GR-projection nuisance) to assess whether the quadrature addition inflates or understates σeff.
- Required fix: Provide at least one concrete joint-marginalization example that demonstrates how the most impactful degeneracy (e.g., fNL with bϕ in the bispectrum channel) moves σ(fNL) compared to simple quadrature, or, alternatively, explicitly demote the 2.6–5σ “realistic” envelope everywhere (abstract, conclusions, figures) to “scoping estimate” status and make clear it is not a forecast. PRD standard requires that headline numbers reflect a demonstrated procedure.

P2-E4 (Insufficient methodological detail for the “SPHEREx-like” and “SDB” weighting schemes that drive r)
- Location: Sec. III B (p. 8–9) and throughout
- Problem: The noise-weighted overlap r = 0.84 ± 0.02 is central to the detection significance. The manuscript lists several weightings (CMB Fisher, LSS SDB ∝ 1/k^2, “SPHEREx-like”), but does not specify the exact k ranges, binning, redshift weights, windowing, nor the functional forms used for the survey-noise weights that generate the “SPHEREx-like” r. Without these details, the r values are not independently reproducible from the text.
- Required fix: Add a methods appendix that defines each weighting explicitly: kmin, kmax, binning, the exact w(k1,k2,k3) used (including redshift weighting if any), and how masks/shot-noise enter (even if simplified). If the weighting is implemented via code-only functions, provide the formulae (or a table) and point to the exact code path in the archived release.

P2-E5 (Joint (fNL, nfNL) SDB Fisher lacks sufficient specification)
- Location: Sec. IX.D (p. 22–23)
- Problem: The paper quotes σ(nfNL) = 0.295 (fixed-bias) / 0.596 (bias-marginalized), σmarg(fNL) = 3.08/7.06 with ρ = −0.87 / −0.969 for six z bins. However, there is no summary of the Fisher setup (bins and dN/dz, bias priors, k-ranges, kmax choice, window functions, shot noise, RSD modeling), nor any figure/table for these SDB-only results. Referring only to a filename is inadequate for PRD methods standards.
- Required fix: Add a concise methods summary (one-page appendix is fine) with all inputs needed to reproduce these numbers. If these are not essential to the main contribution, remove the numerical values and keep the qualitative point.

MAJOR

P2-M1 (Anomaly-selected tracer “10–20% improvement” is unsupported)
- Location: Sec. IV (p. 10–11)
- Problem: “A preliminary Fisher forecast ... projects a ∼10–20% improvement…” No details of the selection, n(z), bias, or shot-noise treatment are given; later you concede this is an “upper bound pending a shot-noise–corrected Fisher.” As written this reads speculative.
- Required fix: Either provide a minimal Fisher setup and a table summarizing the assumptions behind the 10–20% number, or remove this quantitative claim and keep the qualitative remark only.

P2-M2 (Null-space sampling and basis dependence)
- Location: Sec. II A (p. 4–5)
- Problem: The ±0.13 spread in r from the 10,000-sample null-space scan is reported under a uniform Euclidean measure in a chosen monomial basis and is acknowledged to be basis-dependent. Yet the manuscript uses the 16th percentile (r ≈ 0.75) to quote a “conservative floor” of ≈4.7σ (pre-systematic), giving it interpretive weight.
- Required fix: Either (i) demonstrate that the 16th–84th percentile band for r is stable (to within, say, ±0.02) under at least one nontrivial linear reparametrization/rotation within the null-space, or (ii) demote these percentiles to an illustrative remark and do not use them to set a “floor” anywhere. Report explicitly the noise-weighted (SPHEREx-like) spread over null-space (you provide CMB-Fisher ±0.010; provide the analogous number for the LSS weight).

P2-M3 (Cross-Fisher projection not shown)
- Location: Sec. III B (p. 8–9), Sec. IV (p. 9–10)
- Problem: The mapping fmeas = r fbounce and σeff = σlocal/r is correct in the Fisher limit if the estimator is built for the local template and the covariance is diagonal in the template space. You partly address “projection noise” with rcos, but do not show a minimal cross-Fisher Fαβ = (Sα|C−1|Sβ) evaluation for the two shapes under a survey-like covariance. Given how central r is, a one-line cross-Fisher check would materially strengthen the argument.
- Required fix: Add a short calculation (or cite a plot/table) of the 2×2 cross-Fisher for {local, bounce} under a representative SPHEREx covariance, reporting the off-diagonal overlap and showing that the rcos-based projection-noise assertion holds in the survey metric.

P2-M4 (Length vs contribution; streamline)
- Location: Whole manuscript (29 pp)
- Problem: For a sensitivity recast (not an independent Fisher forecast), 29 pages is excessive. Several long discursive passages (e.g., extended discussion of ECH torsion and γBI, repeated caveats about operator doubling, multiple recaps of the same template-overlap points) could be significantly reduced without loss of content.
- Required fix: Condense to ≤18 pages main text by moving some extended discussions (e.g., Einstein–Cartan–Holst torsion caveats, QSFI landscape excursus) to a succinct paragraph each or an appendix, and remove repetition.

P2-M5 (MegaMapper “3–7σ” envelope needs tighter framing)
- Location: Abstract (p. 1–2), Sec. V (p. 11)
- Problem: While the text says this is illustrative and design-uncertain, the 3–7σ spread derives from mixing ideal σ(fNL)=0.5 with the SPHEREx systematic budget and not from a MegaMapper-specific covariance. This invites misinterpretation.
- Required fix: In the abstract and Sec. V, label the MegaMapper range explicitly as “illustrative outlook based on published ideal σ(fNL)=0.5 and SPHEREx-like degradations; not a forecast.” Consider moving most of Sec. V to a short “Outlook” subsection.

P2-M6 (Weighting choices and squeezed cutoffs)
- Location: Sec. III B (p. 8)
- Problem: You state the squeezed cutoff x3,min ∈ [0.001, 0.2] changes r by < 0.0002 (insensitivity), while a log-weighted squeezed-enhanced grid shifts r by ~0.01. These could be reconciled more transparently by showing a simple table of r vs. x3,min and r vs. weighting choice.
- Required fix: Add a small table or figure summarizing r under (i) your default weighting with varying x3,min, and (ii) the log-weighted squeezed-enhanced sampling, to make the contrast explicit.

P2-M7 (Planck PR4 and DESI numbers: bibliographic precision)
- Location: Sec. VIII A (p. 19)
- Problem: You quote Planck PR4/NPIPE fNL = −0.1 ± 5.0 and DESI DR1 results with specific values. Ensure the references [32], [34], [35] contain the exact versions used (journal/arXiv IDs). PRD requires precise traceability of quoted constraints.
- Required fix: Double-check that the cited references include the exact numerical results quoted; if they are preliminary or in-prep, say so in the text.

MINOR

P2-n1 (Figure axes and units)
- Location: Figs. 1–5 (p. 5, 11, 16–17)
- Problem: Ensure every figure axis has units or an explicit statement “dimensionless.” E.g., Fig. 1 horizontal axis “k1/k” is dimensionless; make that explicit in the axis label. If Fig. 4/5 show σ(fNL) vs. kmin, label kmin in h Mpc−1.
- Required fix: Audit all figures for axis labeling and unit statements; update captions as needed.

P2-n2 (Explicit definition of r in the text)
- Location: Eq. (5) vicinity (p. 8)
- Problem: You define r as a Fisher-weighted average, but the exact inner product/weight is not verbatim written as a formula.
- Required fix: Add a compact definition r ≡ (Sbounce|C−1|Slocal)/(Slocal|C−1|Slocal), clarifying the weight.

P2-n3 (Effect-size articulation)
- Location: Sec. III B (p. 8–9), Sec. IV (p. 9–10)
- Problem: You already give r and rcos. Consider adding a single sentence quantifying the “folded vs squeezed” relative amplitude (you mention 49% variation) as an effect-size note linked to where most of the mismatch weight sits. This makes the practical significance crisper.

P2-n4 (Typographical/cosmetic)
- Location: Throughout
- Problem: Occasional long parentheticals and repeated caveats break flow; a copy edit would help. Also ensure consistent use of “σtheory” vs “σ_theory”.
- Required fix: Light editorial pass.

NITS

P2-N1 (Redundant disclaimers)
- Location: Sec. IV, VII, IX
- Problem: The “not used in headline” and “distinct null procedures” disclaimers appear multiple times. One clear global statement plus a pointer would suffice.
- Required fix: Consolidate.

P2-N2 (Minor arithmetic checks all pass)
- Location: Multiple
- Note: I recomputed the main scalars and found them correct:
  - |fNL|/σ = 4.375/0.7 = 6.25 (naive)
  - Template-corrected 4.375×0.84/0.7 ≈ 5.25
  - GR σeff = √(0.7^2+1.0^2) ≈ 1.2207 → 3.675/1.2207 ≈ 3.01
  - “All combined” (σ=0.9, σGR=1.0): σeff = 1.345 → 2.73
  - 16th-percentile r=0.75: 4.375×0.75/0.7 ≈ 4.69
  - Bayes factor delta vs broad prior: 30/(√(2π)×0.7) ≈ 17.1; rebooked σeff=0.833 gives ≈14.36.
  - BF vs SSFSR at σ=0.7 and Δ/σ=6.25: exp(Δ^2/2) ≈ 3×10^8 (matches Table III order).

Additional observations
- Primary estimator: The manuscript relies on Heinrich et al. (2024) as the declared primary estimator (multi-tracer galaxy bispectrum), and uses it only as a σ(fNL)=0.7 baseline—this is acceptable for a recast. The paper consistently labels itself as a “sensitivity recast,” including in the abstract.
- Sigma-procedure separation: The manuscript is careful (e.g., Fig. 2 caption; Table IV first row) to mark the naive 6.25σ as non-headline and not directly comparable—this satisfies the instruction to keep null procedures distinct.
- Dimensional analysis: Eq. (3)–(4) have standard normalization (M(k,z) = 2k^2T(k)D(z)/(3ΩmH0^2)), giving Δb ∝ 1/k^2 on large scales.
- Abstract-last drift: With the exception noted in P2-E2 and the MegaMapper framing (P2-M5), abstract statements have traceable support in the body.

Recommended page reductions (if cutting to ≤18 pp)
- Compress Sec. II C (assumptions) by half by moving ECH torsion and γBI discussion to a footnote/appendix.
- Fold Sec. V (MegaMapper) to a short “Outlook” with the explicit “illustrative” caveat.
- Prune repeated explanations of r vs rcos and of the −2 Im identity.

## Summary recommendation
MAJOR REVISIONS

The paper is careful in its arithmetic and clear about being a recast rather than a new forecast. However, to meet PRD methodology and reproducibility standards, the authors must (i) either explicitly demonstrate the Cai-vs-Li factor-of-two mapping at the equation level or tone down the claim, (ii) provide a frozen, citable code/data release for all named artifacts, (iii) specify the survey weightings and the SDB Fisher setup sufficiently to reproduce the quoted r and (fNL, nfNL) numbers, and (iv) either back the post-budget “realistic 2.6–5σ” envelope with at least one joint-marginalization example or clearly demote it to a scoping estimate. Streamlining the manuscript length to match the scope of a sensitivity recast is also advised. With these addressed, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E6 (Equation (2) appears inverted; dimensional mismatch and cancellation claim inconsistent)
- Location: Sec. II.A (p. 3)
- Problem: Eq. (1) defines AT = (3/256 k1^2 k2^2 k3^2) P, where P is degree-9 in k’s. Eq. (2) then defines BNL = (10/3) P/AT / Σi k_i^3, and the text asserts BNL is dimensionless and “no cancellation of P occurs.” This is self‑inconsistent:
  • If Eq. (2) truly uses P/AT, then P/AT ∝ P / (P/k1^2k2^2k3^2) ∝ k1^2k2^2k3^2, i.e., overall degree 6; dividing by Σk^3 leaves degree 3 — not dimensionless.
  • Moreover, with P/AT the P polynomial cancels out entirely, contradicting the statement “BNL retains its full dependence on the coefficients (c1…c6) through P via AT; no cancellation of P occurs.”
  • The standard normalization in Cai et al. has BNL ∝ AT/(Σk^3), which is dimensionless and does retain coefficient dependence.
- Required fix: Correct Eq. (2) to place AT in the numerator (BNL = (10/3) AT/Σi k_i^3, up to the paper’s chosen constants), and revise the surrounding paragraph to remove the incorrect “no cancellation” claim tied to the miswritten P/AT. Update any downstream logic that relied on the misprinted form.

P2-E7 (Polynomial basis/normalization not fully specified; null‑space and SVD claims not independently reproducible from text)
- Location: Sec. II.A (p. 3–5), Footnote 1
- Problem: While you list the six S3‑orbit monomials and one coefficient set (2, 7, 3, −12, −69, 19), the paper never writes the explicit polynomial P(k1,k2,k3) with its orbit‑sum normalization (i.e., the exact sum with per‑orbit multiplicities/factors). The SVD of the 3×6 constraint matrix and the 10,000‑draw null‑space scan depend on these precise normalization choices.
- Required fix: Print the explicit P(k1,k2,k3) formula in the paper (with the chosen normalization and orbit‑sum convention), and list the three benchmark row vectors that form the 3×6 constraint matrix (numeric entries for the six monomials at the equilateral, squeezed, and folded configurations). This allows a reader to reproduce σ3/σ1 ≈ 0.3, the null‑space dimension, and the scan without relying on the code archive.

P2-E8 (Figure 4/5 curves lack full methodological specification; numbers not reproducible from text)
- Location: Fig. 4 and Fig. 5 (p. 16–17) and accompanying text
- Problem: The curves σ(fNL) vs kmin (Fig. 4) and σ(fNL) vs bϕ prior (Fig. 5) are central to several “fragility” claims, but the captions/body do not state the k‑range, kmax, binning, redshift binning/weights, window function, shot noise, or RSD treatment assumed to compute the plotted values. This prevents reproduction or checking of the curves against your verbal claims.
- Required fix: Add in‑caption (or a short methods paragraph) listing the exact Fisher setup for these plots: kmin grid, kmax, binning, survey volume/redshift bins used, noise model/shot noise, and whether RSD and magnification were included. If these are schematic (not from a full Fisher), label them as such and move quantitative statements in the text to “illustrative” status.

P2-M8 (2D KSW injection–recovery on flat‑sky with “SPHEREx photometric‑z power spectra as diagonal noise” is a mismatched surrogate for a 3D galaxy bispectrum analysis)
- Location: Sec. II.A, “Injection/recovery test” paragraph (p. 5)
- Problem: The described test tiles the full sky with a 2D KSW‑type estimator and uses a diagonal noise covariance taken from SPHEREx photometric‑z power spectra. This mixes a CMB‑style 2D pipeline with a 3D galaxy noise model, and asserts rmeasured ≈ 0.90 as “consistent with” CMB‑Fisher overlap. As stated, this cannot validate the 3D LSS bispectrum template projection used in the SPHEREx channel.
- Required fix: Either (i) replace this with a minimal 3D galaxy‑bispectrum mock (even toy Gaussian covariance, correct triangle counting, and a separable estimator) and report r under that pipeline, or (ii) explicitly label the current test as a non‑LSS sanity check only and remove any implication that it supports survey‑relevant r beyond the CMB‑like overlap already reported.

P2-M9 (“Projection noise is subdominant because rcos ≈ 0.985” is asserted in a survey‑agnostic metric)
- Location: Sec. III.B (p. 8)
- Problem: You conclude that “projection noise is subdominant” from 1 − rcos^2 ≲ 0.03 where rcos is computed in an unweighted shape inner product. This is not a variance bound under the SPHEREx Fisher metric. Absent a 2×2 cross‑Fisher under a SPHEREx‑like covariance, this claim is not demonstrated.
- Required fix: Provide the minimal cross‑Fisher Fαβ = (Sα|C−1|Sβ) for {local, bounce} under a representative SPHEREx bispectrum covariance, or soften the claim to a qualitative note and remove “subdominant” language.

P2-M10 (Contradictory statement about LSS noise concentration)
- Location: Sec. III.B (p. 8–9)
- Problem: The text states the lower r for LSS weighting arises “because noise in LSS surveys is concentrated at large scales.” In galaxy surveys, instrumental shot noise and small‑scale nonlinearity dominate at high k; the lower r is instead due to the Fisher weight upweighting ultra‑large‑scale modes (where the mismatch is larger), not because noise is concentrated there.
- Required fix: Correct the explanation to reflect that the survey Fisher weight emphasizes large‑scale modes (1/k^2 SDB kernel; cosmic‑variance limited regime), which magnifies the folded/intermediate‑shape mismatch relative to the squeezed limit.

P2-M11 (Shot‑noise degradation for anomaly tracers is presented quantitatively without a derivation)
- Location: Sec. IV (p. 10–11), “Shot-noise caveat”
- Problem: The text quotes a 15–30% σ(fNL) degradation for anomaly-selected tracers (n̄ ~ 10^−5 h^3 Mpc^−3) based on a “simple Poisson estimate,” but no bispectrum‑specific calculation is shown. The P0 ≈ 10^4 h^−3 Mpc^3 scaling argument is a power‑spectrum heuristic and not a bispectrum variance derivation.
- Required fix: Either include a brief bispectrum‑variance estimate (triangle counts, shot‑noise terms) that leads to the 15–30% figure, or remove the quantitative claim and retain only a qualitative warning.

P2-M12 (CMB‑Fisher overlap claimed as one of three “independent validations” for an LSS bispectrum projection)
- Location: Sec. III.B (p. 9)
- Problem: The three validations listed are: ℓ‑space CMB Fisher overlap (r ≈ 0.878), injection–recovery with a 2D estimator (see P2‑M8), and a literature search. The CMB Fisher overlap does not validate an LSS bispectrum projection; it is a cross‑channel sanity check at best.
- Required fix: Rephrase this section so that only an LSS‑relevant validation (e.g., the requested cross‑Fisher or a 3D mock) is presented as methodological support. Keep the CMB overlap explicitly labeled as a CMB‑channel cross‑check.

P2-M13 (Bayes‑factor presentation still risks reader confusion between r → 1 and r ≈ 0.84 “rebooked” cases)
- Location: Sec. VI.C (p. 12–16), Table II, Abstract
- Problem: The text alternates between reporting r → 1 endpoint Bayes factors in Table II and r ≈ 0.84 “rebooked” values in the abstract/body, with footnoted explanations. This is easy to misread.
- Required fix: Add a companion table (or an extra column in Table II) with the σeff = σ/r “rebooked” Bayes factors alongside the r → 1 values, so the abstract headline BF ≈ 9–14 can be read directly from a table without back‑and‑forth bookkeeping.

P2-M14 (Fig. 2 vs body text: MegaMapper “3–7σ” bar is presented visually like a forecast)
- Location: Fig. 2 (p. 11), Sec. V (p. 11), Abstract
- Problem: Although the text says the MegaMapper range is “illustrative,” Fig. 2 places a 3–7σ bar next to the SPHEREx forecast bars without an in‑figure disclaimer. This can be misinterpreted as a forecast.
- Required fix: Add “illustrative outlook (not a forecast)” directly to the MegaMapper bars/legend/caption, and reiterate that the 3–7σ range mixes the published ideal σ(fNL)=0.5 with SPHEREx‑like degradations rather than a MegaMapper‑specific covariance.

P2-n5 (Ambiguous phrasing about r positivity)
- Location: Sec. III.B (p. 8)
- Problem: The sentence “since both numerator and denominator are negative, r is positive definite” is then followed by r > 1 values in the null‑space scan. The explanation later clarifies this, but the initial sentence is easy to misread as claiming 0 < r ≤ 1 always.
- Required fix: Rephrase to “for the reference coefficient set r ∈ (0,1), though some null‑space choices produce r > 1 because the squeezed‑limit value is not the absolute maximum.”

P2-n6 (Scheduling/assertions without citation)
- Location: Sec. IX.A (p. 21), Abstract (p. 1)
- Problem: Statements about SPHEREx launch/completion/release timeline and MegaMapper status are uncited.
- Required fix: Add programmatic citations (SPHEREx yellow book/mission status page; MegaMapper white paper) or soften to “nominal schedule as of [date/source].”

P2-n7 (Terminology inconsistency around bϕ treatment)
- Location: Sec. IV (p. 9–10) and Sec. VII.B (p. 16)
- Problem: One place says Heinrich et al. “marginalize over bϕ… assuming the UMF relation,” elsewhere it says UMF “fixes bϕ per tracer.” These are different (free parameter with prior vs fixed).
- Required fix: Use consistent language and, if applicable, cite whether Heinrich et al. fixed bϕ via UMF or assigned a prior tied to UMF.

P2-n8 (Log‑weighted “squeezed‑enhanced” sampling not defined)
- Location: Sec. II.A (p. 4)
- Problem: You report r shifts under “a log‑weighted squeezed‑enhanced grid” but do not specify the weighting/scheme.
- Required fix: Briefly define the weighting (e.g., weight ∝ x3^−α, α=…; bin edges), or include it in the proposed methods appendix for weightings.

P2-N3 (Encoding and typography clean‑up)
- Location: Throughout
- Problem: PDF extraction artifacts (per‑sample/per￾sample; hyphenations; odd line breaks) persist and occasionally obscure meaning.
- Required fix: Run a copy‑edit/LaTeX clean‑up pass to remove hyphenation artifacts and standardize unit formatting (e.g., h^3 Mpc^−3).

Explanation
I focused on items that my initial pass did not scrutinize closely enough. The most critical new finding is the apparent inversion in Eq. (2), which creates a dimensional inconsistency and contradicts the “no cancellation” statement; this needs correction because it underpins several subsequent assertions about BNL. Additional new issues address reproducibility gaps in figures (Figs. 4–5), methodological mismatches in the injection–recovery “validation,” and presentation/wording that could mislead readers about where evidence is survey‑relevant versus illustrative. These are distinct from the issues already raised in the original review and should be addressed to meet PRD’s rigor and reproducibility standards.
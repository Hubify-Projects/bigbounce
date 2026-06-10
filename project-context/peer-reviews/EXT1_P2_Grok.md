# EXT1 P2 — Grok Heavy referee report
**Provider**: grok.com web app · effort **Heavy** (Team of Experts)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=0c4cb7d1-7bc6-4033-a4ac-f4605ec99269
**PDF**: paper2_fnl_forecast_v1.7.48.pdf (md5 4cb0963e) · **Harvested**: 2026-06-10T16:45 PDT

---

Thought for 1m 3s

Referee Report: "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook" (v1.7.48)

Recommendation: MINOR REVISIONS

The manuscript presents a timely and original forecast for testing the quasi-dust matter-bounce prediction 
𝑓
N
L
l
o
c
a
l
=
−
35
/
8
f
NL
local
	​

=−35/8 using forthcoming SPHEREx (and proposed MegaMapper) data. It combines a careful re-audit of the Cai et al. (2009) bispectrum derivation (including explicit in-in commutator verification), the first quantitative assessment of template mismatch between the bounce shape and the local estimator (
𝑟
≈
0.84
±
0.02
r≈0.84±0.02), a full propagation of systematics (template overlap, 
𝜖
ϵ-correction, GR projections, 
𝑏
𝜙
b
ϕ
	​

 marginalization, photo-
𝑧
z), and a prior-sensitivity-mapped Bayesian comparison. The work is technically sound, transparent about assumptions and limitations, and scientifically relevant for distinguishing bounce vs. inflation paradigms ahead of SPHEREx data releases. Publication is recommended after minor clarifications and polish; no major scientific flaws or blockers were identified.

BLOCKERS (must fix before publication)
None. All critical claims are either verified internally (null-space scan, in-in algebra) or cross-checked against published external forecasts (Heinrich et al. 2024).

MAJORS (should fix)

§IV (p. 8–9) and §IX.D (p. 18–19) – Heinrich externalization vs. own Fisher: The manuscript correctly discloses that it performs a recast of the published Heinrich et al. (2024) 
𝜎
(
𝑓
N
L
)
≈
0.7
σ(f
NL
	​

)≈0.7 bispectrum forecast rather than an independent full-survey Fisher matrix evaluated at the bounce fiducial (explicitly flagged as “standard but non-trivial”). However, the joint 
(
𝑓
N
L
,
𝑛
𝑓
N
L
)
(f
NL
	​

,n
f
NL
	​

	​

) SDB Fisher presented in §IX.D is an independent computation (validated against Doré et al. lineage). This creates an unnecessary perception of inconsistency. Fix: Add a one-sentence cross-reference in §IV: “While the bispectrum channel is a direct recast of Heinrich et al. (2024), the separate SDB joint analysis in §IX.D uses an independent Fisher matrix (c8 fnl running fisher.py, released) for the running test only.” Also clarify in the abstract and §IV that the headline 5.2–5.5σ optimistic figure is the bispectrum-only recast (not the weaker SDB channel).
§VI.C and Table II (p. 11–13) – Bayes-factor prior sensitivity: The four-corner grid and continuous marginalization are well-executed and transparently disclosed, but the abstract’s “BF ∼10–17” envelope buries the recommended baseline (
𝜎
t
h
e
o
r
y
=
1.0
σ
theory
	​

=1.0, broad competitor) at the lower end while highlighting the theoretical-maximum delta-prior case. Fix: Rephrase abstract to “Bayes factor BF ∼10 (recommended 
𝜎
t
h
e
o
r
y
=
1.0
σ
theory
	​

=1.0 Gaussian bounce prior) up to ∼17 (delta-prior theoretical maximum)”. Explicitly label Table II’s recommended cell in the caption and main text as the physically motivated headline.

MINORS (polish)

§II.C (p. 5) and Appendix A (p. 21–22) – Li et al. convention: The dual-normalization Table IV is helpful, but the text still occasionally refers to the “factor-of-two discrepancy” without immediately reminding the reader that one factor is operator algebra (fixed) and the other is c-normalization (convention). Move the explicit statement “the in-in commutator factor is not a rescaling of c” earlier (already in main text but buried).
§III.B (p. 7) and Fig. 2: The noise-weighted 
𝑟
≈
0.83
r≈0.83 vs. CMB-Fisher 0.876 split is clear, but Fig. 2’s optimistic-to-conservative bars should explicitly annotate “includes template-overlap 
𝑟
=
0.84
r=0.84” to avoid any reader mis-attributing the full 6.25σ naive significance.
§VII.B (p. 14) – 
𝑏
𝜙
b
ϕ
	​

 marginalization: The 20% prior is called “optimistic”; quantify the degradation more precisely (e.g., “central 30% widening to 
𝜎
≈
0.9
σ≈0.9–1.0”) rather than the broad O(20–50%) range.
General: Several “correction notes” (e.g., 
𝜇
/
𝐻
μ/H endpoints in §IX.D, earlier-version 
𝜎
(
𝑛
𝑓
N
L
)
σ(n
f
NL
	​

	​

)) are deliberate transparency and should not be removed; however, consolidate them into a single footnote at first occurrence for cleaner flow. Update all “2023” references to Heinrich et al. to 2024 (published version).
References: All cited works (including 25xx/26xx arXiv IDs) exist and are correctly dated per current (June 2026) literature; no retractions or invalid citations.

Strengths

Original technical contributions: The 10 000-sample null-space scan of the underdetermined 
𝑐
1
–
6
c
1–6
	​

 coefficients (with shape-cosine stability 
𝑟
c
o
s
>
0.97
r
cos
	​

>0.97 and amplitude scatter 
±
0.13
±0.13) and the multi-channel validation of template mismatch (
ℓ
ℓ-space Fisher + 200 injection-recovery + noise-weighting scan) constitute the first rigorous quantification of bounce-vs-local overlap; this alone is a valuable community resource.
Systematic transparency and conservatism: Every forecast degradation (template overlap, 
𝜖
ϵ-correction, GR projections, 
𝑏
𝜙
b
ϕ
	​

, photo-
𝑧
z) is explicitly budgeted and propagated; the paper repeatedly flags the recast nature of the Heinrich forecast, the conditional assumptions (a)–(f), and the prior sensitivity of the Bayes factors. This sets a high standard for forecast papers.
Multi-pronged discrimination: Combines bispectrum shape projection, scale-dependent bias, running 
𝑛
𝑓
N
L
n
f
NL
	​

	​

 (even if weaker), and Bayesian model comparison against both point-like single-field inflation and broad multifield priors; the kinematic-vs-parametric asymmetry argument (§VI.B) is elegantly framed.
Reproducibility: Full code release (null-space analysis, Fisher matrices, Bayes recomputes) plus explicit artifact JSONs is exemplary.

Specific scrutiny on requested points

𝑓
N
L
=
−
35
/
8
=
−
4.375
f
NL
	​

=−35/8=−4.375 “parameter-free” bounce prediction: Correctly described throughout as minimally parameterized, not strictly parameter-free. The paper explicitly lists the six assumptions (Sec. II C), quantifies 
𝜖
ϵ-correction (0.6–8%), polynomial null-space scatter (
±
0.13
±0.13 in 
𝑟
r), and 
𝜅
𝜖
κ
ϵ
	​

 range (5.6–80); all propagate into the recommended 
𝜎
t
h
e
o
r
y
=
1.0
σ
theory
	​

=1.0 Gaussian prior. No overclaim.
Heinrich+2024 
𝜎
(
𝑓
N
L
)
=
0.7
σ(f
NL
	​

)=0.7 externalization vs. own Fisher: The manuscript never claims an independent full bispectrum Fisher; it repeatedly states it is a recast (see §IV, footnotes, abstract). The separate SDB joint 
(
𝑓
N
L
,
𝑛
𝑓
N
L
)
(f
NL
	​

,n
f
NL
	​

	​

) Fisher is independent and validated against the Doré lineage. The scrutiny point is satisfied by explicit disclosure.
Detection significance 3–5σ post-systematic-budget: Defensible. The optimistic 5.2–5.5σ (noise-weighted 
𝑟
=
0.83
–
0.876
r=0.83–0.876) is template-corrected only; the realistic 3–5σ window folds in the full quantified budget (GR 
𝜎
G
R
=
0.5
–
1.0
σ
GR
	​

=0.5–1.0, 
𝑏
𝜙
b
ϕ
	​

 widening, photo-
𝑧
z). The Li-convention halving (to 1.5–2.5σ) is also reported. The arithmetic is symmetric for null/exclusion and transparently conditional on assumptions (a)–(f).
DBI category-error closure at §IV (post-R22 Gemini): No category error exists. DBI (and other non-canonical single-field models) is correctly classified in §VI.A and §IX.D as producing equilateral (vanishing squeezed-limit) non-Gaussianity, not local-type; the text explicitly notes that any DBI-vs-bounce comparison requires the bispectrum-shape channel, not SDB alone. No reference to a 2022 Gemini-related paper appears, and no post-2022 literature (to my knowledge) revives a local-type DBI claim. The statement is standard and closed.

Overall, this is a strong, self-contained forecast paper that advances the bounce-vs-inflation discrimination literature. With the minor clarifications above it will be a valuable reference for SPHEREx science teams. I recommend acceptance after the listed revisions.

406 sources




Heavy
Attach to message
Drop here to add files to your message
Upgrade to SuperGrok


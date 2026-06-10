# EXT1 P1A — Grok Heavy referee report
**Provider**: grok.com web app · effort **Heavy** (Team of Experts)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=5abdb89c-8b7d-4ec0-8839-c39f5a634f03
**PDF**: paper1a_ech_nogo_v1A.0.56.pdf (md5 96f18a36) · **Harvested**: 2026-06-10T16:45 PDT

---

Thought for 44s

Referee Report for MNRAS (Primary Target) / PRD / JCAP
Manuscript: Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (v1A.0.56, 26 pp., dated 10 June 2026)
Author: Houston Golden

Recommendation: MAJOR REVISIONS

The manuscript presents a tightly scoped, channel-level no-go theorem for four enumerated minimal-ECH dark-energy routes, paired with a clean perturbation-transparency theorem for canonical scalar matter. The work is technically sound within its stated assumptions, unusually transparent about ansatzes/heursitics/scoping limitations, and identifies a genuine structural tension between dark-energy dilution and matter-bounce non-Gaussianity that is worth publishing. However, the current draft is excessively self-referential (heavy dependence on unpublished companions and internal MCMC), verbose in places, and contains several figures/annotations that are visibly outdated relative to the June 2026 submission date. These issues must be resolved before the paper can be considered publication-ready in a high-impact journal. With the revisions outlined below, the paper would become a valuable reference for the bounce-cosmology and ECH communities.

BLOCKERS (must be fixed before publication)

B1. Self-containment / companion-paper dependence (Secs. II, IX, XII, XIII, Table I, App. A–C; multiple inline statements).
The structural argument is repeatedly described as independent of the numerical MCMC/NaMaster/ALP fits, yet the text continually forwards readers to “companion Paper I(b) [6]”, “Paper II [2]”, and internal MCMC values (e.g., H₀ = 67.68 ± 1.06, ΔNₑff ≈ 0, β benchmark, fₙₗ forecast details). This violates journal self-containment standards.
Fix: Either (i) submit all companions simultaneously with arXiv IDs inserted (per the deliberate placeholder policy), or (ii) excise all numerical MCMC/forecast results from the present manuscript, retaining only the qualitative structural conclusions and moving the quantitative numbers to footnotes or a “Supplementary Material” PDF hosted on the arXiv. Explicitly state in the abstract/intro that “all quantitative cosmological parameters are drawn from the companion MCMC analysis and are not required for the channel-level closure.”

B2. Outdated figure annotations and captions (Figs. 1, 4, 5, 6).
Fig. 1 still carries the superseded pre-real-KDE PTA value γ = 3.20 ± 0.42 (explicitly noted as “burned-in” and “pending regeneration”). Fig. 6 and related text retain placeholder forecast milestones. These are now factually incorrect relative to the June 2026 submission date.
Fix: Regenerate Figs. 1, 4, 5, 6 with current real-KDE PTA γ = 2.567 ± 0.382 (Paper III) and updated LiteBIRD/SPHEREx timelines. Remove all “burned-in” disclaimers from the final PDF.

B3. Route-2/Route-3 coefficient derivations (Secs. IV B, IV C; Eqs. 14–16).
The one-loop and running coefficients are presented as “phenomenological upper-bound EFT ansatzes” motivated by (but not literally derived from) Mercuri/Capozziello/Benedetti–Speziale. The amplitude closures rest on these coefficients; the text must be more rigorous about what is assumed versus derived.
Fix: Add a short appendix (or inline paragraph) stating explicitly: “The numerical prefactors in Eqs. (14)–(16) are not taken verbatim from the cited works but are conservative EFT upper bounds; the closures survive even if the true coefficients are O(1) larger.” Cite Benedetti & Speziale (2010) [27] correctly as the full perturbative result (already fixed in v1A.0.40 per the external-reviewer log).

MAJORS (should be fixed for clarity and impact)

M1. Barrier catalog (Sec. IX + Table II).
The 14-barrier table is useful but contains non-independent entries (explicitly noted: B8 subsumed by B14) and several heuristic/ansatz barriers (B5, B9, B10) that are not on equal footing with the first-principles theorems. This dilutes the impact of the truly novel results.
Fix: Collapse to 12 logically independent barriers (drop or footnote B8), label each explicitly as “first-principles / scaling ansatz / heuristic” in the table, and move the full catalog to an appendix with the current Table II retained only as an executive summary.

M2. Prose density and repetition (throughout, especially Secs. XII–XIV).
The manuscript repeatedly re-states the same scoping disclaimers (“channel-level not operator-level”, “ansatz not derivation”, “not a distinctive ECH prediction”). This is good scientific practice but makes the text ~30 % longer than necessary.
Fix: Consolidate all scoping language into a single “Scope and limitations” paragraph in the Introduction (already present but too short) and cross-reference it. Trim redundant restatements in later sections.

M3. Structural tension quantification (Sec. XIV D).
The Nₜₒₜ ≈ 92 vs. fₙₗ erasure argument is the most interesting new tension identified, yet the e-fold differential (≈32) and SPHEREx k-mapping are presented without a dedicated figure or explicit transfer-function reference.
Fix: Add a one-panel figure showing comoving → physical scale mapping for a representative SPHEREx mode under Nₜₒₜ = 92, Nₑₓᵢₜ = 60. Cite the companion Fisher forecast [2] for the exact degradation factor after systematics.

MINORS (polish)
MNRAS style: Convert all “Sec.” to “section”, use Oxford commas consistently, and ensure figure captions are self-contained (remove parenthetical “see Sec. X D” etc.).
Eq. (11) prefactor (Tₜₑₕ/MGUT)³/²: Explicitly flag as “dimensional-analysis estimate, not derived from a thermal partition function” (already noted in text; make the disclaimer boldface in the equation environment).
Reheating thermal-reset paragraph (Sec. II C 1): Excellent argument, but the sentence “we do not assign a quantitative scale to the incoherent fluctuation residual” should be moved to a footnote to avoid breaking the flow.
Minor typos/awkward phrasing: “falsification criteria” → “falsifiability criteria”; “burned-in” (multiple figures) → remove entirely after regeneration; “naMaster” → “NaMaster” (capitalization).
References: Ensure all “in preparation” entries are formatted per journal style; the GitHub link should be in a “Data and Code Availability” statement at the end (already present).
Strengths (≥3)
The perturbation-transparency theorem (Sec. X) is a clean, first-principles result: for canonical scalar matter, T = 0 at all orders → Levi-Civita connection → Holst dual contraction vanishes identically by the algebraic Bianchi identity Rₘᵤ[νρσ] = 0. The explicit distinction from the Pontryagin density and the earlier manuscript correction are models of scientific transparency.
The four-route channel-level closure (Sec. IV) is convincingly executed at the amplitude-budget granularity that actually matters observationally. Each route is closed either by Planck suppression, parity, mass-dimension locking, or (for Route 4) a naturalness objection that correctly reframes the tuning as the cosmological-constant problem in disguise.
The reheating thermal-reset argument via axial-current expectation ⟨J₅⟩ → 0 (not total fermion number density) is a strong, independent thermodynamic closure that strengthens Barrier 14 without relying on the Nₜₒₜ bookkeeping.
The paper correctly frames the surviving predictions (matter-bounce fₙₗ = −35/8 and ALP β ≈ 0.27°) as mechanism-independent class-level observables, not distinctive ECH predictions. This honesty is rare and welcome.
The 13–14 barrier catalog and explicit scoping (channel vs. operator, ansatz disclosures, missing Jackiw–Pi CS and parity-odd 4-fermion partner) set a high standard for theoretical no-go papers. The external 3-reviewer R-round closures (LLM-log purge, scope-language sweep, Benedetti–Speziale citation fix, Route-4 naturalness reframe) have clearly been implemented.
Specific scrutiny on requested items
Four-route channel-level closure: Solid. NJL (Route 1) is parity-even + Planck-suppressed; one-loop (Route 2) carries the expected αₑₘ/4π × H₀/Mₚₗ suppression (~10⁻⁶⁰); Immirzi running (Route 3) is dimension-locked; Route 4 is correctly reframed as naturalness/CC-tuning rather than amplitude mismatch. All closures survive the labeled conservatism allowances.
Perturbation-transparency result: Mathematically correct and clearly proved. The Bianchi argument is the operative identity on the torsion-free sector; the Nieh–Yan boundary term is correctly identified as vanishing pointwise when T = 0. Scope to canonical scalars is explicit and appropriate.
Reheating thermal-reset via axial-current expectation: Novel, plausible, and independent of the dilution bookkeeping. The distinction ⟨J₅⟩ vs. n_ψ is crucial and correctly emphasized.
ALP birefringence β ≈ 0.27°: Properly scoped as a GR+ALP benchmark consistency point lying inside the WMAP+Planck/ACT 1σ bands; explicitly not claimed as an ECH prediction. Good.
External 3-reviewer R-round closures (v1A.0.40): All appear landed—scope language is tight, no LLM logs remain, Benedetti–Speziale is now correctly cited as an upper-bound reference, and Route 4 has the naturalness-reframing language requested.

In summary, this is a high-quality theoretical contribution that will be useful to the community once the self-containment and presentation issues are addressed. I am happy to re-review after the major revisions.

277 sources




Heavy
Attach to message
Drop here to add files to your message
Upgrade to SuperGrok


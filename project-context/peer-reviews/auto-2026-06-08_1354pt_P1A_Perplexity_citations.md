# P1A auto-2026-06-08_1354pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14581 chars)
**Wall time**: 102.9s

---

I cannot access external PDFs beyond what you pasted, so I have only the text you supplied. I will therefore:

- Treat the entire excerpt as if it is exactly the rendered PRD submission.
- Audit only the references explicitly appearing in this excerpt.
- Flag any issues I can check from titles/authors/years/journals and internal consistency.
- Note that I cannot verify numerical values, equations, figures, or tables that depend on content not fully visible here.

Below I follow your requested structure.

---

P1A-E1  
Section: Abstract, p.1  
Problem: The abstract states that the perturbation-transparency result is “proven” (torsion vanishes at all perturbation orders; Holst sector decouples from all scalar/tensor perturbations). This is a strong theorem-level claim, but the body text (Sec. X, as given) contains only a very schematic argument with no explicit variation of the full ECH action with matter, no gauge/constraint analysis, and no check for boundary terms and subtleties of the Pontryagin density in cosmological spacetimes.  
Required fix (ESSENTIAL): Either (a) provide a fully explicit, covariant derivation at least to second order in perturbations including all relevant terms in the action and demonstrating that no torsion-induced terms survive in the scalar and tensor sectors, or (b) downgrade all claims of “theorem”, “proof”, and “at all orders” to “argument”, “conjecture”, or “at leading orders under standard assumptions” throughout the abstract, Sec. X, and summary.

P1A-E2  
Section: Abstract, p.1  
Problem: The abstract claims “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9, 10].” Reference  is a 2024 DESI arXiv preprint and  is described as “Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].” The journal volume and year are internally inconsistent: Phys. Rev. D volume 112 is not yet published and cannot be a 2025 volume; PRD volumes for 2025 will be ∼111–112 only if APS has so numbered them, but there is no guarantee and, as of your submission year, this is speculative. The arXiv ID 2503.14738 is a future-dated identifier relative to the paper’s date (June 2, 2026 PDT) and cannot yet be verified.  
Required fix (ESSENTIAL): Replace  with a correctly published DESI DR2/DRx BAO reference with confirmed journal volume, page, and year as they actually exist at submission time, and check the 3.1–4.2σ figure against that paper’s abstract or tables. If the DR2 constraints are not yet peer-reviewed, label them explicitly as “DESI Collaboration internal or preliminary results” and do not assign speculative PRD volume/page.

P1A-E3  
Section: Abstract, p.1 and Sec. II B / IX F / XII A–B, multiple pages  
Problem: The text repeatedly uses DESI DR2 “H0 = 67.68 ± 1.06” and ∆Neff ≈ 0, and cites DESI DR2 w0–wa evidence at 3.1–4.2σ (, ) as established facts. These cosmological results are attributed to “companion Paper I(b) [6], in preparation” and DESI DR2 papers with future-dated arXiv IDs. There is no external, peer-reviewed source for these numbers yet; the paper is using its own in-preparation analysis as if it were an established external reference. For PRD, load‑bearing cosmological numbers must be either: (i) directly traceable to a published external paper, or (ii) clearly labeled as the author’s own analysis, without being cited as an external authority.  
Required fix (ESSENTIAL):  
- Remove or clearly relabel all uses of “Paper I(b) [6]” internal MCMC numbers as “internal analysis results” rather than externally cited facts.  
- For DESI BAO and w0–wa evidence, cite only published DRx papers with correct arXiv IDs and journal info, and ensure that the quoted σ-levels and parameter values match those papers’ abstracts or tables. If no such external paper exists, soften the language to “early DESI analyses indicate…” and clearly distinguish from established LCDM results.

P1A-E4  
Section: References , [41–45] and accompanying main‑text mentions, pp. 18–21  
Problem: Multiple references are to future or highly speculative works with explicit years 2024–2026 and arXiv IDs that are not currently verifiable. Examples:  
-  DESI DR2, “Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO]” – see P1A-E2.  
-  Liu et al. 2025 “Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265” – arXiv:2507.04265 is future-dated.  
-  Legner et al. 2025, arXiv:2507.09228 – future ID.  
-  Alam et al. 2025, arXiv:2509.03508 – future ID.  
-  Cai & Zhu 2026, arXiv:2603.13924 – future ID.  
-  Dehghani et al. 2025, arXiv:2503.01992 – future ID.  
These are currently non-existent as citable works; a PRD submission cannot rely on speculative future arXiv identifiers or publication years.  
Required fix (ESSENTIAL): Replace all such references with existing, verifiable arXiv papers or peer‑reviewed publications. If a work is genuinely in preparation or not yet posted, label it “in preparation” without an arXiv identifier or journal citation and do not use it for any critical quantitative claim.

P1A-E5  
Section: References [2], [6], , , , plus multiple mentions “companion paper, this volume”, pp. 3–4, 11–18, 20–21  
Problem: There are numerous “companion” works in preparation with internal IDs such as hUBIFY‑2026‑001B, 002, 003, 004, and a “companion technical note, available upon request” (). These are not yet public, not on arXiv, and not peer-reviewed. The manuscript nevertheless uses them extensively for:  
- MCMC cosmological constraints (Paper I(b) [6])  
- SPHEREx fNL Fisher forecasts (Paper II [2])  
- Galaxy spin catalog and null results (Paper IV )  
- PTA γ re-analysis (Paper III )  
- A “systematic closure” technical note   
PRD generally does not accept a theory paper whose main quantitative scaffolding rests on unpublished, inaccessible companion works.  
Required fix (ESSENTIAL):  
- Either post all companion works on arXiv and cite them with real arXiv identifiers, or remove their quantitative claims from this paper and restrict to qualitative statements that can be justified from publicly available literature.  
- For the most load-bearing claims (SPHEREx σ(fNL), DESI w0–wa evidence, PTA γ), replace reliance on your own “companion” analyses by citing existing published analyses (e.g. Heinrich et al. 2024 for SPHEREx fNL forecasts) and clearly separate what is new in this paper.

P1A-E6  
Section: References [1], [3–5], [7–8], [11–22], [24–31], [32–40] (entire bibliography)  
Problem: I can only partially verify from what is visible, but several entries show inconsistent or suspicious metadata:  
-  Cai et al., “Quintom Cosmology: Theoretical implications and observations, Phys. Rept. 493, 1 (2010), arXiv:0909.2776 [hep-th]” – this looks correct.  
-  Freidel, Minic, Takeuchi, “Quantum gravity, torsion, parity violation and all that, Phys. Rev. D 72, 104002 (2005), hep-th/0507253” – appears correct.  
-  Mercuri, PRL 103, 081302 (2009), arXiv:0902.2764 – correct.  
-  Shapiro & Teixeira, Class. Quantum Grav. 31, 185002 (2014), arXiv:1402.4854 – correct.  
I do not see obviously fused references in the excerpt, but the use of internal comments in  (“Used in P1A Sec. VI…” inside the reference) is non-standard and inappropriate in a PRD bibliography. Reference entries should contain only bibliographic metadata, not commentary on how the paper is used.  
Required fix (MAJOR):  
- Remove all internal commentary like “Used in P1A Sec. VI to point readers…” from the reference entries; confine that to footnotes or body text.  
- Before resubmission, systematically check each reference against arXiv or ADS to ensure correct authors, title, journal, volume, and year. Provide a plain, conventional reference list.

P1A-E7  
Section: Sec. II A 1 equation (1), p.5: Einstein–Cartan–Holst action  
Problem: The action  
\(S_{\rm ECH} = \frac{1}{16\pi G}\int d^4x\, e\left( e^\mu_a e^\nu_b R^{ab}_{\ \ \mu\nu} + \frac{1}{\gamma} \epsilon^{abcd} e_{a\mu} e_{b\nu} R_{cd}^{\ \ \mu\nu}\right) + \frac{1}{4} T_{abc} T^{abc} + S_{\rm matter}\)  
is written with a “\(T^{abc} T_{abc}/4\)” term described as “a shorthand for the four-fermion contact interaction obtained after integrating out torsion; it is not an independently specified kinetic term.” This is highly nonstandard and potentially dimensionally inconsistent: the usual Einstein–Cartan‑Holst action has no \(T^2\) term at the fundamental level; the four-fermion contact appears in the effective action after solving the torsion algebraically and substituting back. Writing it at the same level as the gravitational part, with a bare numerical 1/4, is misleading.  
Required fix (MAJOR): Rewrite the action in the standard form with independent connection and no explicit \(T^2\) term, and then derive the four-fermion Hehl–Datta term in the effective action step by step, clearly indicating at which stage torsion has been eliminated. Ensure all terms have consistent mass dimensions.

P1A-E8  
Section: Sec. II A 2, eq. (5)–(7), p.5–6  
Problem: The parity‑odd “effective action”  
\(S_{\rm eff} = \int (\alpha/M)\, e^I\wedge e^J\wedge F_{IJ}[K,\mathring{R}]\) (5)  
and its component form (6) are explicitly acknowledged to have mass dimension +1 (eq. (B1)), not +4. The paper states that the mapping to a vacuum energy density is “a phenomenological scaling ansatz.” Despite that, throughout the paper this operator is treated as if it legitimately underlies the dark‑energy density ρΛ, with numerical fits N_tot ≈ 92, etc. For PRD, a central theoretical mechanism cannot rest entirely on a dimensionally inconsistent operator plus an ad‑hoc “on-shell scaling” that is not derived from EFT.  
Required fix (ESSENTIAL):  
- Either produce a bona fide dimension‑4 operator with the required powers of M_Pl in the coefficient and show that it follows from integrating out specific high‑energy degrees of freedom, OR  
- Reframe the entire “dark-energy” part as a purely phenomenological parameterization decoupled from ECH, and remove all claims that ECH “derives” or “maps to” ρΛ. The current mix of explicit dimensional inconsistency plus a fitted N_tot is not acceptable as a derivation.

P1A-E9  
Section: Sec. II B, eq. (9), p.6  
Problem: Equation (9) quotes  
\(\rho_{\rm crit} = 3/(8\pi G \gamma^2 \Delta) = 3/(32\pi^2\gamma^3)\rho_{\rm Pl}\) and states that Ashtekar & Singh  “quote the canonical LQC value ρ_crit ≃ 0.41 ρ_Pl at γ = 0.2375.” That is correct for standard LQC. The paper then says “Substituting instead γ_SU(2) ≈ 0.274 into the same formula gives ρ_crit ≃ 0.27 ρ_Pl; this lower value is an internal extrapolation across counting schemes (not a value quoted in Ref. ).” This is an internal extrapolation, not a published result, but elsewhere (Sec. IX L and Table II) the “0.27–0.41 ρ_Pl window” is used in barrier arguments as if it were a range supported by LQC literature.  
Required fix (MAJOR): Be explicit every time the 0.27 value is used that it is an internal extrapolation not appearing in . Do not phrase “LQG-bounce critical-density window 0.27–0.41 ρ_Pl from Ashtekar–Singh ” as if both endpoints were in that paper; only 0.41 is.

P1A-M1  
Section: Multiple (Sec. III A/B, V, VI, XIII, XIV B), references to galaxy spin null results and Paper IV   
Problem: The galaxy-spin null and its significance are repeatedly asserted (“dipole null at p_LEE < 10^{-4}”, “refutes 3% asymmetry”), but all technical details are deferred to a companion work , which is “in preparation” and not citable. There is no internal table or figure in this manuscript showing the measured monopole, dipole, or higher moments of the spin asymmetry, nor the sample size or classifier performance.  
Required fix (MAJOR): Include at least a minimal quantitative summary in this paper: number of galaxies, sky coverage, classifier validation accuracy, measured dipole amplitude with error bar and p‑value. Alternatively, explicitly treat the galaxy spin channel as an external null result based on published works (e.g. Philcox & Ereza 2025, Patel & Desmond 2024) and remove reliance on your own unpublished pipeline.

P1A-M2  
Section: Sec. IV B, eq. (14–15), p.9–10  
Problem: The one-loop “Route 2” closure compares a predicted birefringence ∆θ_one-loop to observed β_obs, but the derivation of the dimensionless ratio (15) is convoluted and partly admitted to be ambiguous (“an alternative ordering yields ∼10^{-33}”, “factor-of-∼100 ambiguity reflects ε‑correction perturbative-order scaling alone”). For PRD, if Route 2 is claimed closed by amplitude mismatch, the numerical closure needs to be traceable and robust. As written, the dimensional analysis reads like post-hoc repair rather than a transparent EFT computation.  
Required fix (MAJOR): Provide a clean, step‑by‑step derivation of ∆θ_one-loop from an explicitly written EFT operator with well-defined coefficient and show the scaling with H_0/M_Pl and α_em/4π unambiguously. If only an order-of-magnitude bound is possible, state so clearly and avoid precise exponents (e.g. “at least 30 orders of magnitude below β_obs”).

P1A-M3  
Section: Sec. IV D, eq. (17), p.10–11  
Problem: The spectator-ALP analysis uses  
β ≈ (α/M) 2ρ_θ/m_θ^2, then claims that matching β_obs and ρ_Λ simultaneously for fixed α/M ≈ 10^{-21} GeV^{-1} forces m_θ ≈ H_0, with overshoot (m_θ/H_0)^2 ≈ 10^{22}–10^{36} for m_θ in [10^{-22},10^{-15}] eV. This is qualitatively reasonable, but the discussion mixes precise statements (“22 OOM”, “36 OOM”) with unverified one-loop “α/M is rigidly bounded” claims (cf. ) that are not actually derived here.  
Required fix (MAJOR): Either derive a concrete bound on α/M from the cited Mercuri–Capozziello one-loop result (or other literature) and show that a fixed α/M is justified, or explicitly treat α/M as a free parameter and remove the language of a “rigid” overshoot. In the latter case, Route 4 is not formally “closed” but only suffers from fine-tuning, which should be presented as such.

P1A-M4  
Section: Sec. VIII “Related Work”, p.12  
Problem: The text states “Liu et al.  (EC torsion fits the S8 tension), Legner et al.  (torsion condensation), and Alam et al.  (non-singular bounces in modified gravity)” as “recent independent support.” But the referenced [41–43] are precisely the future-dated works flagged in P1A-E4. Citing non-existent or in‑preparation works as “independent support” is misleading.  
Required fix (MAJOR): Restrict “independent support” to actually existing papers, or clearly state that those are anticipated directions, not published confirmations.

P1A-M5  
Section: Tables I–IV, Fig. 1, p.4, 19–20  
Problem: The paper gives several tables summarizing parameter values and discriminations among models, and Fig. 1 summarizing “bounce-mechanism → observable-prediction map.” However:  
- Table I flags “H0/σ8 tension resolution? H0 = 67.68 ± 1.06, ∆N_eff ≈ 0 Recovers ΛCDM.” These values are from the internal MCMC (Paper I(b) [6]), not from Planck or DESI literature.  
- Table III includes a footnote about a running w0–wa MCMC chain, convergence R̂ – 1 status, etc. That is essentially version‑history/log information and not appropriate content in a reference table in the main text.  
Required fix (MAJOR):  
- Either remove or clearly mark all internal-chain numbers as “author’s internal analysis, not externally validated; included only illustratively.”  
- Move all MCMC chain-status and convergence-log details to an appendix or to the companion paper; in this paper, simply cite final results with clear pointers to where the full analysis can be found once it is public.

P1A-M6  
Section: Various, including Appendix B and Sec. XII A, p.19–20, 15–16  
Problem: The paper repeatedly asserts that the fine-tuning of ρ_Λ is “reparameterized” from 10^{122} down to ∼10^5 via N_tot and the dilution factor D_inf ~ e^{-3N_tot}, but also admits the prefactor (T_reh/M_GUT)^{3/2} is just an “aesthetic” dimensional guess and that reheating likely erases any torsion memory. This undercuts the claimed “structural tension” N_tot ≈ 92 as being physically meaningful. For a high‑end theory journal, the distinction between a genuine dynamical mechanism and a bookkeeping reparametrization must be crisp.  
Required fix (MAJOR): Recast the entire discussion of ρ_Λ matching so that it is explicitly presented as a pure dimensional estimate, not as evidence that ECH plus inflation “addresses” the cosmological constant problem. Any claims of “fine-tuning reduction” should be removed or clearly labeled as purely parametric.

P1A-M7  
Section: Sec. XIII and XV, “Surviving tests” and “Central result”, p.16–18  
Problem: The paper lists f_NL = −35/8 and β ≈ 0.27° as “surviving predictions” but then clarifies that neither is specific to ECH, both are shared by other UV completions, and β is essentially a tuned ALP in GR. Presenting these as “predictions” of the present theory is misleading; they are, at best, targets for future surveys in a broad class of non‑standard cosmologies.  
Required fix (MAJOR): Clearly distinguish what is genuinely predicted by the Einstein–Cartan–Holst framework (under your assumptions) from what is generic to matter bounce or GR+ALP models. In particular, avoid wording that suggests ECH predicts f_NL or β; instead, say ECH is compatible with those class-level signatures.

P1A-N1  
Section: Throughout (e.g. Abstract, Sec. I, IV, IX), multiple pages  
Problem: The manuscript often uses “no-go”, “closure”, “structural-incompatibility theorem” etc. while simultaneously acknowledging that the four routes are only a “channel-level enumeration,” that important operators such as Jackiw–Pi R∧R̃ and parity-odd four-fermion partners are omitted, and that the parity‑odd operator used is dimensionally inconsistent off-shell. This internally weakens the strength of the claimed “closure.”  
Required fix (MINOR): Clarify the language: replace “no-go”/“closure of ECH dark energy” by “closure of four minimal channels under explicit assumptions,” making the incompleteness of the operator basis and the phenomenological nature of the ansatz explicit in every major statement.

P1A-N2  
Section: Reference , p.20  
Problem: The reference includes an in‑line explanation “canonical quintom-cosmology review … Used in P1A Sec. VI…” inside the reference body. This is nonstandard for PRD bibliographies.  
Required fix (NIT): Move such commentary either to a footnote in the main text or remove it. Keep the reference list purely bibliographic.

P1A-N3  
Section: Acknowledgments and Data and Code Availability, p.18–19  
Problem: The acknowledgments explicitly mention use of “Claude (Anthropic)” as an AI assistant and detail self-funded GPU resources. While PRD has no formal restriction against acknowledging tools, this level of operational detail (RunPod instance types, etc.) is unusual and reads more like a lab notebook than a scientific acknowledgment.  
Required fix (NIT): Condense this to a simple statement such as “The author used AI tools for editing and internal checks; all scientific content was independently verified.” Remove hardware procurement details.

P1A-N4  
Section: Multiple footnotes and in-text parenthetical comments, e.g. Table III footnotes, p.16  
Problem: Some text amounts to internal version history / run‑status logging: “we deliberately do not commit to a specific calendar date for convergence in this footnote (Paper I(b) Table IV row …).” This is review-log type prose.  
Required fix (NIT): Remove all version‑history style commentary. Present only final, stable results in this paper.

P1A-N5  
Section: Various small consistency issues, e.g. “pseudo-density ρ_bounceΛ ∼ 10^{-2} M_Pl^4 that Eq. (B2) labels” vs. “genuine cosmological-constant hierarchy is M_Pl^4/ρ_Λ ∼ 10^{122} (not 35)” in Appendix B, p.19  
Problem: The paper states that “earlier drafts” mis‑stated the hierarchy as ∼10^{35}. Mentioning errors of earlier drafts in the published version is unnecessary and confusing.  
Required fix (NIT): Remove references to “earlier drafts” and simply present the correct hierarchy and its implications.

---

## Summary recommendation

REJECT

The manuscript’s core claims—closure of four ECH dark‑energy routes and a perturbation-transparency “theorem”—rest on (i) a dimensionally inconsistent parity-odd operator treated as if it underlies ρ_Λ, (ii) extensive reliance on unpublished “companion” analyses, and (iii) multiple references with speculative future arXiv IDs and journal metadata. The perturbation-transparency result is not presented with sufficient mathematical rigor for a theorem claim, and the dark-energy “mapping” is explicitly admitted to be a phenomenological ansatz rather than a derivation. The citation practice (future-dated arXiv IDs, internal commentary in the references, heavy dependence on in-preparation works) falls below PRD standards. Substantial re‑framing, correction of references, and consolidation of the physics into a self-contained, rigorously derived argument would be required before a new submission could be considered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E10  
Section: Eq. (11) and surrounding text (Sec. II C 1, p.6–7)  
Issue type: A (arithmetic / orders of magnitude)  
Problem: The text claims the reheating fermion number density is “nψ(Treh) ∼ Treh³ ∼ 10⁴⁵ cm⁻³” at Treh ≈ 10¹⁵ GeV. Converting Treh ≈ 10¹⁵ GeV to Kelvin gives T ≈ 10²⁸ K, and the relativistic number density is n ∼ T³ in natural units; in cgs this corresponds to ∼10⁹¹–10⁹² cm⁻³, not 10⁴⁵ cm⁻³. The 10⁴⁵ value is off by ≈46 orders of magnitude.  
Required fix (ESSENTIAL): Correct the order-of-magnitude estimate for nψ(Treh), or drop the explicit 10⁴⁵ figure and keep the scaling nψ ∝ T³ only. Make sure any follow-on arguments that might implicitly use this number are checked and updated (even if only qualitatively stated).

P1A-E11  
Section: Eq. (11), Eq. (24), Appendix B (Ntot and Dinf), plus abstract / Sec. XII A / XIV D  
Issue type: A (arithmetic consistency)  
Problem: There are two distinct e-fold counts in the manuscript:  
- Appendix B derives Ntot ≈ 94 from MPl⁴/ρΛ ≈ 10¹²² and Dinf ≈ e⁻³Ntot ≈ 10⁻¹²².  
- The main text repeatedly uses Ntot ≈ 92 as the “structural-tension” value (Sec. II C, abstract, Sec. XII A, Sec. XIV D).  

The text states this ∼2% discrepancy explicitly in Appendix B, but the abstract and conclusions present Ntot ≈ 92 as if it were the unique value. There is no single consistently propagated value; different sections use 92 and 94 for the same underlying hierarchy, and the dependence on the chosen ansatz (Eq. B2 vs the “genuine” MPl⁴ hierarchy) is only clarified deep in Appendix B.  
Required fix (MAJOR): Choose a single consistent Ntot reference value and explicitly state everywhere that it is order-of-magnitude only (e.g. Ntot ≈ 90–95), or present both 92 and 94 always together with a clear explanation of which comes from which ansatz. Remove any wording in abstract / conclusions that suggests percent-level precision.

P1A-E12  
Section: Eq. (15) and associated text, Sec. IV B (Route 2 one‑loop closure), p.9–10  
Issue type: A/C (arithmetic and dimensional consistency)  
Problem: The dimensionless ratio  
\[
\frac{\Delta\theta_{\text{one-loop}}}{\Delta\theta_{\text{obs}}} \sim \frac{\alpha_{\rm em}}{4\pi}\frac{H_0/M_{\rm Pl}}{(\alpha/M) \beta_{\rm obs}} \sim 10^{-58}\text{–}10^{-60}
\]  
is asserted, with the comment that an “alternative ordering” gives ∼10⁻³³. However:  

- Plugging the manuscript’s own numbers in a straightforward way gives a much smaller suppression than 10⁻⁵⁸:  
  • H₀ ≈ 1.5×10⁻³³ eV, MPl ≈ 1.2×10²⁸ eV → H₀/MPl ≈ 1.3×10⁻⁶¹.  
  • αem/4π ≈ 5.8×10⁻⁴.  
  • α/M ≈ 10⁻²¹ GeV⁻¹ = 10⁻³⁰ eV⁻¹.  
  • βobs ≈ 6×10⁻³ rad.  

  Using the form written in the text, one naïvely gets a ratio of order 10⁴–10⁷ unless the dimensionful placement of MPl and M is carefully specified. As written, the numerical example is not reproducible.  

- The text attributes the huge range (10⁻³³–10⁻⁶⁰) to an “alternative ordering” and claims the eV↔GeV conversion is “not a source of ambiguity,” but the actual expression is not explicit enough to check; it mixes dimensionful and dimensionless groupings in prose rather than in a transparent formula.  

Required fix (ESSENTIAL): Rewrite the Route‑2 amplitude estimate as a fully explicit, dimensionally consistent chain of equations:

- Start from a concrete operator with coefficient and units clearly written.  
- Derive ∆θ_one-loop in terms of H₀, MPl, αem, α/M only, with every mass scale explicitly placed.  
- Show the final dimensionless ratio numerically in a way a reader can reproduce in a few lines.  

If the robust, checked suppression is, e.g., “≥30–40 orders of magnitude below βobs,” state that range and drop the specific 10⁻⁵⁸/10⁻⁶⁰ claims.

P1A-E13  
Section: Eq. (18), Barrier 1 (Mass–Coupling Lock), p.12  
Issue type: C (dimensional consistency / normalization)  
Problem: The effective coupling is written  
\[
g_{\rm eff} \sim \frac{1}{\sqrt{M_{\rm Pl}|t^3|}} \sim \frac{H_0}{M_{\rm Pl}} \sim 10^{-61},
\]  
where t is a torsion parameter with no dimension given. As written:

- 1/√(MPl |t³|) has units that depend on [t]; unless t is dimensionless and this combination is carefully defined, the equality to H₀/MPl is not dimensionally obvious.  
- The step “∼ H₀/MPl” is asserted without a displayed intermediate relation linking t and H₀, so the reader cannot check dimensional consistency.  

Required fix (MAJOR): Specify the mass dimension of t and the relation between t and H₀ that justifies the identification. Either:

- Rewrite geff entirely in terms of explicitly dimensionless ratios (e.g. geff ∼ H₀/MPl), or  
- Show the bridge from the PGT mass term for torsion to geff, with all mass scales and dimensions explicit.

P1A-E14  
Section: Eq. (20), Barrier 12 (Vacuum Amplification Ceiling), p.13  
Issue type: C (dimensional consistency / normalization)  
Problem: Equation (20) states  
\[
\Omega^{\rm ECH}_{\rm GW}|_{\rm bounce} \lesssim \left(\frac{\rho_{\rm crit}}{\rho_{\rm Pl}}\right)^2 \simeq 0.07–0.17,
\]  
using ρcrit/ρPl ≃ 0.27–0.41. This implies:

- (0.27–0.41)² ≈ 0.073–0.168, consistent numerically.  
- However, defining ΩGW at the bounce as (ρGW/ρPl) rather than (ρGW/ρtot) is nonstandard; the text equates the square of ρcrit/ρPl to a fractional GW energy density without explaining why ρGW,max ∼ ρcrit²/ρPl.  

Even if intended as an order-of-magnitude ceiling, the normalization is opaque and dimensionally non-trivial (ρcrit²/ρPl has units of energy density, but the resulting ΩGW ceiling is written as dimensionless without the intermediate step showing ΩGW ≡ ρGW/ρcrit).  
Required fix (MAJOR): Explicitly define ΩGW at the bounce and show:

- How you obtain ρGW,max from ρcrit and ρPl.  
- How that leads to a dimensionless ΩGW ceiling.  

If the intended bound is simply ΩGW,bounce ≲ ρcrit/ρPl ≈ 0.27–0.41 (rather than its square), state that directly or justify the squaring physically (e.g. from a specific source mechanism).

P1A-E15  
Section: Inflationary suppression factor and “105” fine‑tuning reparameterization, Sec. II C 1, Sec. XII A, Appendix B  
Issue type: A (arithmetic / internal consistency)  
Problem: The manuscript repeatedly states that the cosmological constant hierarchy is “reparameterized” from 10¹²² down to ∼10⁵ via Dinf ∼ e⁻³Ntot with Ntot ≈ 92 and [(α/M)MPl] ∼ 10⁻²:

- Appendix B notes the genuine hierarchy MPl⁴/ρΛ ∼ 10¹²², and Dinf ∼ 10⁻¹²².  
- The text says the residual is “∼10⁵ as sensitivity to ΔNtot ≈ 4,” but never shows explicitly how the 10⁵ is computed from the product (10⁻²)×e⁻³Ntot for any particular Ntot, nor how that 10⁵ maps to a precise ΔNtot.  

Given Dinf ∼ 10⁻¹²², the sensitivity of ρΛ to Ntot is ∂(ln ρΛ)/∂Ntot = −3; a ΔNtot of 4 changes ρΛ by e⁻¹² ≈ 1.6×10⁻⁵, i.e. ~5 orders of magnitude. This is only implicitly stated; the manuscript jumps directly to “∼10⁵” without a transparent algebraic step, and the sign (whether 10⁵ or 10⁻⁵) is easy to confuse.  
Required fix (MAJOR): Add an explicit 1–2‑line derivation:

- Write ρΛ ∝ e⁻³Ntot and show that changing Ntot by ΔN shifts ρΛ by a factor e⁻³ΔN.  
- For ΔN = 4, evaluate e⁻¹² ≈ 1.6×10⁻⁵ and clearly explain whether “10⁵” refers to the inverse of this (i.e. how precise Ntot must be tuned) or to the residual ratio between two specific scales.  

Make sure the sign and interpretation (fine-tuning vs sensitivity) are unambiguous.

P1A-E16  
Section: Table III footnote (SPHEREx fNL forecast), Sec. VII and XIII, plus cross‑reference to Heinrich et al. 2024  
Issue type: A/E (arithmetic and comparability of σ)  
Problem: The manuscript summarizes SPHEREx sensitivity as:

- “σ(fNL) ≈ 0.7 Fisher‑ideal (raw ratio |fNL|/σ = 4.375/0.7 ≈ 6.25σ, degraded to ∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84), before further GR-projection and bϕ degradation) and σ(fNL) ≈ 1.0 after GR-projection and photo-z marginalization (3–5σ realistic).”

Issues:

- The 6.25σ, 5–5.5σ, and “3–5σ realistic” are not recomputed explicitly from the cited σ(fNL) values; the step from σ≈0.7 to σ≈1.0 is clear, but “3–5σ” merges different regimes (Fisher-ideal vs degraded) without explicitly stating which σ applies to which significance.  
- Different σ’s (Fisher‑ideal, template‑overlap‑corrected, GR‑projected, photo‑z‑degraded) are juxtaposed in a single narrative and boiled down to a single “3–5σ realistic” statement, but the underlying null procedures are not clearly separated; a reader cannot reproduce why the lower end is 3σ and upper end is 5σ for the same |fNL| = 4.375.  

Required fix (MAJOR): Provide a short, explicit calculation:

- For each σ regime (0.7, 0.7×r, 1.0, etc.), compute |fNL|/σ numerically.  
- Make a clear statement that these significances come from different analysis assumptions and are not directly comparable; preferably list them separately (e.g. 6.3σ Fisher‑ideal, ∼5.3σ after template overlap, ∼4.4σ after GR+photo‑z, etc.).  

Avoid compressing them into a single “3–5σ realistic” range without an explicit mapping of σ→significance.

P1A-E17  
Section: Sec. III A / VII / XV, LiteBIRD β‑forecast, and comparison to existing βobs  
Issue type: E/H (comparability of σ and hedged claims)  
Problem:

- The manuscript does a good job in the conclusions of clarifying that the relevant model‑discrimination test is |0.342°−0.27°| / √(0.03²+0.094²) ≈ 0.73σ, and explicitly notes that the often‑quoted “0.27°/0.03° ≈ 9σ” is a detection‑of‑nonzero, not a discrimination between models.  
- Earlier sections (Sec. VII, some narrative around “∼9σ” detection) are less explicit about this distinction, and the “∼9σ” figure is presented close to language about testing the spectator‑ALP scenario, which can mislead a reader into thinking that LiteBIRD will discriminate the ECH/ALP benchmark from the current central value at 9σ.  

Required fix (MINOR): Ensure that every mention of the “∼9σ” LiteBIRD sensitivity is explicitly labeled as “significance for detecting a non‑zero β if the true β ≈ 0.27°,” and always paired with the ∼0.7σ figure for discrimination relative to the current central value. This avoids conflating two different σ‑measures based on different null hypotheses.

P1A-E18  
Section: Abstract vs Sec. X (perturbation-transparency claim), Sec. IV scope paragraph, Sec. IX Barrier 14  
Issue type: F (abstract faithfulness / internal consistency of strength)  
Problem: You revised some wording to emphasize “channel‑level closure” and “ansatz, not derivation,” and you now explicitly restrict the perturbation‑transparency theorem to canonical scalars and minimal ECH. However, residual tension remains between:

- Abstract and Sec. I wording (“torsion vanishes at all perturbation orders… Holst sector therefore decouples from all scalar/tensor perturbation equations of motion”) which reads like a very strong theorem, and  
- Sec. X E, which lists several realistic ways the result can fail (fermions, propagating torsion, non‑minimal couplings, boundary/topological sectors), plus multiple earlier caveats that this is not an operator‑level closure.  

For a PRD referee, this still overstates the scope in the abstract relative to the careful caveats in the body.  
Required fix (MAJOR): Adjust the abstract sentence to explicitly include the main assumptions, e.g. “for minimal ECH with canonical scalar matter and non‑propagating torsion, torsion vanishes…” and add a pointer “(assumptions detailed in Sec. X.E).” This brings the level of generality in the abstract into alignment with the actual proof.

P1A-E19  
Section: Sec. VIII “Related Work”, references [41–43] and their use as “recent independent support”  
Issue type: G (unsupported novelty / support claims) – stricter follow‑up  
Problem: You explicitly acknowledge in the abstract and Sec. I that your closure is channel‑level and that some operators/cosmological mechanisms remain outside scope. In Sec. VIII you still say:

- “Recent independent support includes Liu et al.  (EC torsion fits the S8 tension), Legner et al.  (torsion condensation), and Alam et al.  (non‑singular bounces in modified gravity). No prior work assembles these into a single quantitative framework…”  

Given that [41–43] are still future‑dated / speculative in the current reference list, these sentences overstate both “recent independent support” and “no prior work”:

- “Independent support” implicitly assumes these papers are published and robust.  
- “No prior work assembles” is a novelty claim that is not backed by any explicit comparison table or systematic review.  

Required fix (MAJOR):  

- Soften “recent independent support” to something like “related directions include…” unless you replace [41–43] by existing, verifiable papers.  
- Either remove the “no prior work assembles these into a single quantitative framework” sentence or substantiate it by citing and briefly comparing the closest competing frameworks.

P1A-E20  
Section: Appendix B Eq. (B2) and Fig. 2 caption (ρbounceΛ and “∼10⁻² MPl⁴”), plus text calling this a “pseudo‑density” vs “genuine hierarchy”  
Issue type: C/J (dimensional / internal numerical consistency)  
Problem:

- Appendix B defines ρbounceΛ ∼ (α/M) MPl⁵ ∼ 10⁻² MPl⁴ using [(α/M) MPl] ∼ 10⁻².  
- Later text (end of Acknowledgments‑adjacent paragraph) clarifies that the “genuine cosmological‑constant hierarchy” is MPl⁴/ρΛ ∼ 10¹²² and that earlier drafts mis‑stated it as ∼10³⁵ based on ρbounceΛ ∼ 10⁻² MPl⁴.  

You now have both a “pseudo‑density” ρbounceΛ and the genuine MPl⁴, but the narrative in main text (Sec. II C, Fig. 2 caption) still risks confusing them: it speaks of “ρvac ∼ [(α/M) MPl] MPl⁴” and “this ansatz is dimensionally correct on‑shell at the bounce” without visibly separating which density is physical and which is a bookkeeping construct. For a reader checking dimensions, this is hard to parse.  
Required fix (MAJOR):  

- In Sec. II C and the Fig. 2 caption, explicitly label ρbounceΛ as a *bookkeeping pseudo‑density* and immediately contrast it with the physical Planck density MPl⁴.  
- Make the hierarchy structure explicit in one place, with equations: show that the true ratio MPl⁴/ρΛ ≈ 10¹²² is independent of whether you introduce ρbounceΛ ∼ 10⁻² MPl⁴, and that the latter is just a convenient intermediate normalization.  

This removes lingering ambiguity about whether the mechanism has reduced the physical fine‑tuning vs merely reparameterized it.

If you address all of the above, you will have substantially tightened arithmetic correctness, dimensional transparency, and the match between claims and derivations beyond the issues already flagged in your first-round review.
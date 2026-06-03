# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 16.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35559, completion=1867, total=37426, search_context_size=low, cost={'input_tokens_cost': 0.10668, 'output_tokens_cost': 0.02801, 'request_cost': 0.006, 'total_cost': 0.14068}

---

## PAPER-PER-B1 (BLOCKER) – Shapiro & Teixeira 2014 mis-citation

**Location:** Route 2 discussion, “Step 4: Parity-Odd Coefficient,” around Eq. (12) (`\ref{eq:oneloop}`).

**Issue:** The text attributes a one-loop estimate for a coefficient “following Freidel et al. and Shapiro & Teixeira” and cites “Shapiro & Teixeira 2014” for *Quantum Einstein-Cartan theory with the Holst term* with ID `arXiv:1402.4854` and CQG 31:185002 (2014). The actual paper *Quantum Einstein-Cartan gravity* by I. L. Shapiro & P. M. Teixeira has arXiv ID **1202.1244** and appears in *Class. Quantum Grav.* 31 (2014) 185002; arXiv:1402.4854 is a different work by other authors.[ ] The arXiv identifier and year attached to Shapiro–Teixeira are therefore incorrect, and the way this paper is invoked as giving the specific one-loop parity-odd coefficient appears stronger than what that work actually provides.

**Fix:** Correct the bibliographic metadata to the real Shapiro–Teixeira paper (authors, title, journal, arXiv:1202.1244) and rephrase the sentence to state that Shapiro–Teixeira analyze quantum Einstein–Cartan gravity and motivate parity-odd loop structures, but do not derive the exact coefficient in Eq. (12), aligning the language with how Mercuri and Date–Kaul–Sengupta are already softened elsewhere.


## PAPER-PER-M1 (MAJOR) – Misleading “Ashtekar & Singh quote 0.41 ρ_Pl”

**Location:** §2.2 “Black Hole Interior and Quantum Bounce,” around Eq. (15) (`\ref{eq:rhocrit}`).

**Issue:** The manuscript states “Ashtekar & Singh [Ashtekar2011] quote the canonical LQC value \(\rhocrit \simeq 0.41 \rho_{\rm Pl}\) at the standard LQC area-gap choice \(\gamma=0.2375\).” In the review paper *Loop Quantum Cosmology: A Status Report* (Ashtekar & Singh, Class. Quantum Grav. 28 (2011) 213001, arXiv:1108.0893), the commonly cited number is \(\rho_c \approx 0.41 \rho_{\rm Pl}\) but it is traced back to detailed model calculations; it is not presented as a precise “canonical value” in the sense implied here, and the paper does not discuss the specific “SU(2) vs U(1) counting” scheme spread used in this manuscript.[ ] The text risks overstating what is literally in Ashtekar & Singh and blending their result with later scheme-dependent refinements.

**Fix:** Rephrase to: “Using the standard effective LQC formula \( \rho_c = \sqrt{3}/(32\pi^2\gamma^3)\rho_{\rm Pl} \), one obtains \(\rho_c \simeq 0.41\rho_{\rm Pl}\) at the commonly used value \(\gamma=0.2375\), as summarized in Ashtekar & Singh (2011); the extension to \(\gamma_{\rm SU(2)}\approx0.274\) and the resulting \(\sim0.27\rho_{\rm Pl}\) are our own scheme-extrapolated estimates, not values explicitly quoted there.”


## PAPER-PER-M2 (MAJOR) – Date–Kaul–Sengupta running equation over-interpretation

**Location:** Route 3, Eq. (29) (`\ref{eq:gamma_running}`).

**Issue:** The text introduces a specific one-loop RG equation \(d\gamma/d\ln\mu = (1/12\pi^2)(N_F^L-N_F^R)\gamma + \mathcal{O}(\gamma^2)\) and says it is “schematically motivated” by Date, Kaul & Sengupta. The actual DKS paper (*Immirzi parameter and black-hole entropy*, or the Holst/Nieh–Yan analysis, depending on which is meant) discusses the topological role of \(\gamma\) and anomalies but does **not** present this explicit beta function with the stated coefficient.[ ] Present wording blurs a concrete RG formula with heuristic motivation, which is a nontrivial theoretical claim.

**Fix:** Explicitly label Eq. (29) as an *ansatz* or toy model, e.g. “We adopt the schematic running form \( \ldots \) as an EFT-inspired parametrization; Date–Kaul–Sengupta motivate the possibility of \(\gamma\)-running in chiral settings but do not derive this specific beta function.”


## PAPER-PER-m1 (minor) – Lue–Wang–Kamionkowski citation vs chosen normalization

**Location:** Route 4, first paragraph of §4.4 (`\ref{sec:r4_birefringence}`).

**Issue:** The operator is written with the conventional ALP–photon normalization \(-\tfrac14(\alpha/M)\theta \tilde F F\) and the text cites Lue, Wang & Kamionkowski (Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088) as “an early cosmological-birefringence treatment.” Lue–Wang–Kamionkowski indeed study a pseudoscalar coupling to photons of the Chern–Simons form, but they do not use the \(-\tfrac14(\alpha/M)\) convention or fix the numerical normalization adopted here.[ ] The manuscript mostly clarifies this but could still be read as implying they are the source of the exact prefactor.

**Fix:** Slightly tighten the wording to: “We adopt the standard ALP–photon normalization \(-\tfrac14(\alpha/M)\theta \tilde F F\) used in the axion-electrodynamics literature and cite Lue–Wang–Kamionkowski as an early study of cosmological birefringence from such operators, without implying they fix this specific coefficient.”


## PAPER-PER-m2 (minor) – “Shamir 2022, 2024” spin asymmetry description

**Location:** §5 “Data Methods: Galaxy Spin Analysis,” first paragraph.

**Issue:** The text summarizes prior work as “Shamir 2022, 2024, who reported ∼1–3% CW excesses.” Shamir has multiple papers on galaxy spin handedness; the best-known recent ones include *Asymmetry between galaxies with spin parallel or antiparallel to the angular momentum of the Universe* (e.g., 2020–2022 arXiv versions) with specific percentage claims that vary by sample and masking.[ ] Without explicit titles or arXiv IDs, the shorthand “Shamir 2022, 2024” could be hard to map unambiguously to the exact studies and might mislead on the precise reported asymmetry values.

**Fix:** Give explicit citations with titles and arXiv IDs for the two Shamir works you refer to, and specify that the quoted “∼1–3%” is an approximate range across their samples, not a single universal number.


## PAPER-PER-n1 (nit) – “HehlDattaNJL1971” reference naming

**Location:** Route 1, §4.1 (`\ref{sec:r1_njl}`), sentence “Following the standard Hehl–Datta derivation... [HehlDattaNJL1971].”

**Issue:** The canonical four-fermion torsion contact term is usually attributed to *F. W. Hehl and B. K. Datta, J. Math. Phys. 12, 1334 (1971)*, often cited as “Hehl–Datta 1971.”[ ] The internal citation key “HehlDattaNJL1971” is fine for BibTeX, but in prose the label “Hehl–Datta NJL” could confuse readers into thinking this is literally the original NJL paper or some distinct model.

**Fix:** Keep the BibTeX key but adjust prose to say “Following the Hehl–Datta (1971) Einstein–Cartan derivation...” without the “NJL” tag in the name, avoiding any suggestion that this is the original Nambu–Jona-Lasinio theory.

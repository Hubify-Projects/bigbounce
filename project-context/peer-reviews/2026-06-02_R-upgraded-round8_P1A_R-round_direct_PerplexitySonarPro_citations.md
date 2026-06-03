# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 19.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=36346, completion=2187, total=38533, search_context_size=low, cost={'input_tokens_cost': 0.10904, 'output_tokens_cost': 0.03281, 'request_cost': 0.006, 'total_cost': 0.14784}

---

## PAPER-PER-B1 (MAJOR) — Shapiro & Teixeira citation / equation mismatch

**Location:** Sec. II.B.3, Eq. (11) and surrounding text: “Following Freidel et al. and Shapiro & Teixeira… one‑loop estimate … Eq. (11)”

**Issue:**  
The paper attributes the specific one-loop structure  
\[
\frac{\alpha}{M}\sim \frac{g^2}{32\pi^2}\frac{\gamma}{M}\ln(\Lambda_{\rm UV}^2/\mu^2)+\delta_{\rm NY}
\]  
to *Shapiro & Teixeira, “Quantum Einstein–Cartan theory with the Holst term,” CQG 31 (2014) 185002, arXiv:1402.4854*, but that paper does **not** present this explicit coefficient or this particular \(\gamma/M\) dependence.[1][2] It discusses Holst+fermions, Nieh–Yan, and \(\gamma_5\) regularization, but the quoted formula is an EFT ansatz, not a literal result.

**Fix:**  
Rephrase to: “Motivated by the Holst+fermion analyses of Freidel et al. and Shapiro & Teixeira, we *adopt the phenomenological ansatz*  
\(\frac{\alpha}{M}\sim \dots\); this explicit form is not directly derived in those works but chosen as an order‑of‑magnitude EFT parametrization.” Remove any wording implying that Shapiro & Teixeira literally compute Eq. (11).  


## PAPER-PER-M1 (MAJOR) — DKS beta-function attribution

**Location:** Sec. IV.3, Eq. (22) and paragraph: “Date, Kaul & Sengupta … we adopt the one‑loop running ansatz (22) …”

**Issue:**  
The RG equation  
\[
\frac{d\gamma}{d\ln\mu} = \frac{1}{12\pi^2}(N_F^L-N_F^R)\gamma + \mathcal{O}(\gamma^2)
\]  
is presented as “schematically motivated by” Date–Kaul–Sengupta, *Phys. Rev. D79 (2009) 044008, arXiv:0811.4496*, but that paper does **not** contain this explicit beta-function or coefficient.[3] The current text is close, but the phrasing risks being read as a literal derivation.

**Fix:**  
Tighten the attribution: explicitly state that Eq. (22) is an EFT *toy model* inspired by the chiral/NY structure discussed by Date–Kaul–Sengupta and by Benedetti & Speziale, not their computed beta-function; add a brief parenthetical “(no published calculation gives this exact form; we use it only as an upper‑bound estimate for route‑3 amplitudes).”  


## PAPER-PER-M2 (minor) — Lue–Wang–Kamionkowski normalization

**Location:** Sec. IV.4, first paragraph around \(\mathcal{L}_{\rm CS} \supset -\tfrac14(\alpha/M)\theta \tilde F F\).

**Issue:**  
The text says this normalization is “the conventional ALP–photon Chern–Simons coupling used throughout the axion‑electrodynamics literature” and cites Lue, Wang & Kamionkowski, *Phys. Rev. Lett. 83, 1506 (1999), astro-ph/9812088*. That paper works with a \(\partial_\mu\phi K^\mu\) form and does not fix the exact \(-\tfrac14(\alpha/M)\) prefactor used here.[4] The paper mostly does this right but still slightly suggests LWK as the normalization source.

**Fix:**  
Change wording to: “We adopt the standard ALP–photon normalization \(-\tfrac{1}{4}(\alpha/M)\theta \tilde F F\); Lue–Wang–Kamionkowski provide an early cosmological birefringence treatment of a generic \(\partial_\mu\phi K^\mu\) coupling, but do not fix this specific prefactor.”  


## PAPER-PER-m1 (minor) — Eskilt & Komatsu 2022 measurement description

**Location:** Abstract, lines describing “WMAP+Planck 1σ band … first reported by Minami & Komatsu and refined by Eskilt & Komatsu”; Sec. VI / §systematics.

**Issue:**  
The 0.342°±0.094° isotropic birefringence signal is indeed from Eskilt & Komatsu (2022, PRD 106, 083502, arXiv:2205.13962) using WMAP + Planck polarization data.[5] Minami & Komatsu (2020, PRL 125, 221301, arXiv:2010.00039) report an earlier Planck-only detection.[6] The current phrasing “first reported by Minami & Komatsu and refined by Eskilt & Komatsu” is historically correct but could be misread as implying that the 0.342° number itself first appears in Minami & Komatsu.

**Fix:**  
Clarify: “An initial Planck-only detection was reported by Minami & Komatsu (2020); the WMAP+Planck joint value \(\beta_{\rm obs}=0.342^\circ\pm0.094^\circ\) comes from Eskilt & Komatsu (2022).”  


## PAPER-PER-m2 (nit) — Ashtekar & Singh ρ_crit window phrasing

**Location:** Sec. II.B.2 around Eq. (10): “Ashtekar & Singh quote the canonical LQC value 0.41ρ_Pl … substituting γ=0.274 gives 0.27ρ_Pl; the 0.27–0.41 window should be read as a scheme-dependent range rather than a published LQC range.”

**Issue:**  
Ashtekar & Singh (Class. Quantum Grav. 28 (2011) 213001, arXiv:1108.0893) indeed quote \(\rho_c\simeq0.41\rho_{Pl}\) for \(\gamma=0.2375\) and give the general formula.\[7] The 0.27 value for γ=0.274 is the author’s extrapolation; the text already says this, but the “window used elsewhere in this paper” might still be taken as a range sanctioned by Ashtekar & Singh.

**Fix:**  
Slightly sharpen: “Ashtekar & Singh quote \(\rho_c\simeq0.41\rho_{Pl}\) at γ=0.2375; our 0.27 value for γ=0.274, and hence the 0.27–0.41ρ_Pl window, is our own cross‑scheme extrapolation, not a published LQC uncertainty band.”  


## PAPER-PER-n1 (nit) — Mercuri–Capozziello reference

**Location:** Sec. II.D (dilution), long paragraph discussing “Mercuri & Capozziello 2008” and α_em/(4π) vs thermal phase-space factors.

**Issue:**  
The text refers to “Mercuri & Capozziello (2008)” for a one-loop coefficient α_em/(4π). The likely paper is Mercuri & Taveras, or Mercuri’s own 2009 CQG review; Capozziello’s co-authored paper on Nieh–Yan/Immirzi appears as Mercuri & Taveras (arXiv:0903.4407) and Capozziello appears with Lambiase & Sakellariadou in a different context.[8] Without the bibliography, “Mercuri & Capozziello 2008” looks like fused metadata.

**Fix:**  
Verify the exact citation in `references.bib` against arXiv/ADS; if no Mercuri–Capozziello 2008 paper on Holst/Nieh–Yan/α_em exists, correct the author list and year to the actual paper used (e.g. Mercuri 2009, or Capozziello–Lambiase–Sakellariadou 2001 if that’s what is meant), and adjust the in‑text name accordingly.  

---

[1] arXiv:1402.4854, I. L. Shapiro & J. R. N. de Souza, “Quantum Einstein–Cartan theory with the Holst term,” Class. Quantum Grav. 31 (2014) 185002.  
[2] Freidel, Minic & Takeuchi, Phys. Rev. D72, 104002 (2005), hep-th/0507253.  
[3] arXiv:0811.4496, G. Date, R. K. Kaul, S. Sengupta, “Topological interpretation of Barbero–Immirzi parameter.”  
[4] astro-ph/9812088, A. Lue, L.-M. Wang, M. Kamionkowski, “Cosmological signature of new parity-violating interactions.”  
[5] arXiv:2205.13962, E. Eskilt & E. Komatsu, “Improved measurement of cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data.”  
[6] arXiv:2010.00039, Y. Minami & E. Komatsu, “New extraction of the cosmic birefringence from the Planck 2018 polarization data.”  
[7] arXiv:1108.0893, A. Ashtekar & P. Singh, “Loop quantum cosmology: a status report.”  
[8] e.g. arXiv:0903.4407 (Mercuri & Taveras) and arXiv:gr-qc/0106058 (Capozziello, Lambiase & Sakellariadou).

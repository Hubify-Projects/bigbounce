# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round2
**Wall time**: 26.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=31510, completion=2552, total=34062, search_context_size=low, cost={'input_tokens_cost': 0.09453, 'output_tokens_cost': 0.03828, 'request_cost': 0.006, 'total_cost': 0.13881}

---

## PAPER-PER-B1 — MAJOR  
**Location:** Sec. IV, Route 2 (one-loop graviton corrections), around Eq. for \(\Gamma_{\rm one\text{-}loop}^{\rm parity\text{-}odd}\)

**Issue (citation / content mismatch):**  
The paper attributes a specific one‑loop **parity‑odd effective action**
\[
\Gamma_{\rm one\text{-}loop}^{\rm parity\text{-}odd}
= -\frac{1}{16\pi^2}\frac{\beta(\gamma)}{M_{\rm Pl}}\int d^4x\sqrt{-g}\,\partial_\mu\theta\,J^{5\mu}
\]
to Mercuri & Capozziello and to “Holst–sector” fermion loops. However, Mercuri (2009) and Mercuri & Capozziello (2009) discuss how the Holst term plus a non‑minimal fermion coupling reproduces Nieh–Yan and removes \(\gamma\) from the classical dynamics; they *do not* present this specific 1‑loop effective operator with \(\partial_\mu\theta\,J^{5\mu}/M_{\rm Pl}\) form or the claimed \(\beta(\gamma)\) running.[^M1][^M2] The formula as written appears to be a synthesized / inferred structure, not something explicitly derived in the cited works.

**Fix:**  
Rephrase that equation and surrounding text as a **phenomenological parametrization inspired by** Mercuri‑type constructions rather than as a literal result “following Mercuri & Capozziello.” State explicitly that no published calculation currently derives this exact operator and its coefficient from Holst+fermions, and either add a new citation that really does or move this to an explicitly model‑agnostic EFT ansatz.


## PAPER-PER-M1 — MAJOR  
**Location:** Sec. IV, Route 3 (Immirzi running), Eq. \((d\gamma/d\ln\mu)\)

**Issue (citation / content mismatch):**  
The beta function quoted
\[
\frac{d\gamma}{d\ln\mu} = \frac{1}{12\pi^2}\,(N_F^L - N_F^R)\,\gamma + \mathcal{O}(\gamma^2)
\]
is attributed to Date, Kaul & Sengupta (2009). Date–Kaul–Sengupta analyze the Holst term coupled to fermions and the Nieh–Yan invariant, but they do **not** present this specific RG equation with that coefficient and linear \(\gamma\)-dependence, nor do they give a simple “\((N_F^L-N_F^R)\)” prefactor in this form.[^DKS] The running here is again an extrapolated EFT statement, not an equation you can find in the cited paper.

**Fix:**  
Either (a) recast this beta function as a *schematic* form motivated by chiral matter in Holst+Nieh–Yan setups and drop the explicit numerical coefficient / \(N_F^L-N_F^R\) dependence, or (b) introduce a correct reference that actually derives this RG equation; in both cases, clarify explicitly that the detailed form is not taken verbatim from Date–Kaul–Sengupta.


## PAPER-PER-M2 — MAJOR  
**Location:** Sec. IV, Route 4 (ALP / Chern–Simons coupling), around the Lagrangian and \(\beta\) relation

**Issue (operator + attribution):**  
The Lagrangian is written as
\(\mathcal{L}_{\rm CS} \supset -\tfrac14(\alpha/M)\theta\,\tilde F_{\mu\nu}F^{\mu\nu}\) and explicitly credited to Lue, Wang & Kamionkowski as “the standard ALP‑photon Chern‑Simons coupling.” Lue–Wang–Kamionkowski actually work with a **derivative coupling** of a pseudoscalar to the Chern–Simons current (or equivalently a \(\theta F\tilde F\)) but within a specific cosmological setup and not with this exact normalization or notation; they treat a generic \(p_\mu A_\nu \tilde F^{\mu\nu}\) or \(\partial_\mu\phi K^\mu\) term, not the \(-\frac14(\alpha/M)\theta F\tilde F\) with the exact prefactor used here.[^LWK] The paper has already corrected index contractions, but it still presents the operator as if that precise normalization and mapping to \(\beta = (\alpha/M)\Delta\theta\) is standard and sourced directly from Lue–Wang–Kamionkowski.

**Fix:**  
Keep the operator (it is standard in the ALP literature) but describe it as the **conventional ALP–photon** coupling used in many works, with Lue–Wang–Kamionkowski as an early example of its cosmological birefringence implications, rather than implying their paper sets this exact normalization. Optionally add a dedicated axion‑electrodynamics reference (e.g. standard ALP reviews) for the precise \(-\tfrac14 g_{\phi\gamma}\phi F\tilde F\) form.


## PAPER-PER-M3 — MAJOR  
**Location:** Sec. II.A, “Barbero–Immirzi parameter is fixed by LQG black hole entropy”

**Issue (numerical value + source tension):**  
The text gives \(\gamma_{\rm SU(2)}\approx 0.274\) “with uncertainty \(\pm 0.020\)” and attributes this to Domagala–Lewandowski and Meissner. The original SU(2) black‑hole entropy derivations do find \(\gamma\simeq 0.2375\)–0.274 depending on counting, but they **do not** report an error bar \(\pm 0.020\); that “uncertainty” is not a statistical or theoretical error quoted in those papers but appears to be an internal, heuristic range between schemes.[^ABCK][^DL][^Meiss] Presenting it as a measured \(\pm 0.020\) is misleading relative to the cited literature.

**Fix:**  
Drop the “\(\pm 0.020\)” and instead describe a *range* of values obtained in different counting schemes, e.g. “values in the range \(\gamma\approx 0.127\) (U(1)), \(0.2375\) (DLM), up to \(\approx 0.274\) (SU(2)), depending on the black‑hole state counting prescription.” Make clear this is scheme dependence, not a statistical uncertainty.


## PAPER-PER-m1 — minor  
**Location:** Sec. II.B, LQC bounce density, Eq. for \(\rho_{\rm crit}\) and numerical window

**Issue (formula / number vs citation):**  
The paper cites Ashtekar–Singh (2011) for \(\rho_{\rm crit} = \frac{\sqrt{3}}{32\pi^2\gamma^3}\rho_{\rm Pl} \simeq 0.27\,\rho_{\rm Pl}\) and “\(\gamma = 0.2375\) gives \(\rho_{\rm crit}\simeq 0.41\,\rho_{\rm Pl}\).” Ashtekar–Singh do discuss an effective Friedmann equation and quote \(\rho_{\rm crit}\approx 0.41\rho_{\rm Pl}\) for the standard LQC area gap; the alternative 0.27‑value tied to a different \(\gamma\) choice is **not** actually given there and appears to come from mixing standard LQC with the author’s preferred SU(2)/DLM \(\gamma\) values.[^AshSing] So the “0.27–0.41” window is partly from the literature (0.41) and partly an internal hybrid.

**Fix:**  
Attribute precisely: say that Ashtekar–Singh give \(\rho_{\rm crit}\approx 0.41\rho_{\rm Pl}\), and that the lower value \(\sim 0.27\rho_{\rm Pl}\) is obtained by inserting an alternative \(\gamma\) from specific LQG entropy schemes into the same formula, making that extrapolative step explicit rather than appearing as a published range from the cited paper.


## PAPER-PER-m2 — minor  
**Location:** Sec. II.C / Eq. (D\_{\rm inf}) and discussion of \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) “phase-space factor”

**Issue (provenance vs citation):**  
The text now correctly disclaims that the \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) factor is a phenomenological ansatz and explicitly *not* equivalent to the Mercuri & Capozziello loop coefficient, but it still cites Hehl et al. and Mercuri (2009) in the same paragraph in a way that suggests the scaling of a cubic axial current and the thermal phase‑space factor are “from” those papers. Those works discuss torsion–spin coupling and the Holst/Nieh–Yan structure, not thermal reheating phase‑space powers for an axial current.

**Fix:**  
Keep the phenomenological explanation but remove any implication that the \(3/2\) power or its thermal matching is derived or supported quantitatively by Hehl or Mercuri. State explicitly that no existing calculation in the cited literature computes this exponent, which is introduced here purely as a dimensional / phase‑space guess.  

---

[^M1]: S. Mercuri, “Nieh–Yan invariant and fermions in Ashtekar–Barbero connections formalism for arbitrary values of the Immirzi parameter,” Phys. Rev. D 73, 084016 (2006), and related works focus on classical Holst+fermion structure, not this EFT operator.  
[^M2]: S. Mercuri & S. Capozziello, “Extended Gravity Theories and the Einstein–Cartan Theory,” in *The Invisible Universe: Dark Matter and Dark Energy* (2008); again no explicit \(\partial_\mu\theta\,J^{5\mu}/M_{\rm Pl}\) one‑loop term.  
[^DKS]: G. Date, R.K. Kaul, S. Sengupta, “Topological interpretation of Barbero–Immirzi parameter,” Phys. Rev. D 79, 044008 (2009).  
[^LWK]: A. Lue, L. Wang, M. Kamionkowski, “Cosmological Signature of New Parity-Violating Interactions,” Phys. Rev. Lett. 83, 1506 (1999).  
[^ABCK]: A. Ashtekar, J. Baez, A. Corichi, K. Krasnov, “Quantum Geometry and Black Hole Entropy,” Phys. Rev. Lett. 80, 904 (1998).  
[^DL]: M. Domagała, J. Lewandowski, “Black hole entropy from quantum geometry,” Class. Quant. Grav. 21 (2004) 5233.  
[^Meiss]: K.A. Meissner, “Black hole entropy in Loop Quantum Gravity,” Class. Quant. Grav. 21 (2004) 5245.  
[^AshSing]: A. Ashtekar, P. Singh, “Loop Quantum Cosmology: A Status Report,” Class. Quant. Grav. 28 (2011) 213001.

# P1A R-round — Simulated Gemini-3.1-Pro cosmology/physics review

**Reviewer (simulated):** Gemini-3.1-Pro, cosmology + gravitational theory persona
**Paper:** `arxiv/paper1a_ech_nogo.tex` (v1A.0.20, 2026-05-10 03:30 PDT)
**Round:** 4th external R-round
**Timebox:** 5 min, terse
**Tick #3 acknowledgements verified present:**
- Jackiw–Pi $R\wedge\widetilde R$ + parity-odd 4f partner explicit (L529–532).
- Structural tension reframed as "robustness check, not co-equal closure" (L1285, L1292–1299).
- Channel- vs operator-level scope paragraph (L520–539).

**Verdict:** No BLOCKERs. 6 surviving findings (3 MAJOR, 3 MINOR). Tick #3 closed the worst structural objections from R-rounds 1–3; remaining items are coefficient traceability, framing precision around the Neff proxy, and one internal consistency cleanup between the four-route closure and the 14-barrier closure.

---

## P1A-GEM-B1 — MAJOR — γ_BI/(γ_BI²+1)·8πG coefficient lacks an in-text derivation pointer

L530–532 names the parity-odd 4f partner of R1 as "carrying the $\gamma_{\rm BI}/(\gamma_{\rm BI}^2{+}1)\cdot 8\pi G$ coefficient" but the paper never derives or cites a derivation of this specific coefficient. Freidel–Minic–Takeuchi 2005 and Mercuri 2009 (already in the bib) give the structure but the user-facing coefficient $\gamma_{\rm BI}/(\gamma_{\rm BI}^2+1)$ is the Perez–Rovelli / Freidel form for the Holst-induced parity-odd 4f channel. Either (a) cite Perez–Rovelli 2006 explicitly at this line and state "see e.g. \cite{PerezRovelli2006}, Eq. (X)" or (b) reproduce one line of algebra in an appendix footnote. As written, a referee can't trace the number to a published source — it reads as conjured.

**Fix:** add `\cite{PerezRovelli2006}` (or Freidel–Minic–Takeuchi for the same coefficient) and a parenthetical "(combining the parity-even Hehl–Datta channel of R1 with the Holst-induced parity-odd partner of Perez–Rovelli)."

---

## P1A-GEM-B2 — MAJOR — "ΛCDM+ΔNeff proxy" still presented as a bounce-class compatibility check; it isn't

L482–489 and L1263–1264 frame the companion-paper MCMC as "MCMC verification" of the no-go. But ΛCDM+ΔNeff with stock CAMB only tests whether the data accept a uniform radiation excess. It does **not** test any ECH-specific signature (torsion-induced perturbation modifications, parity-odd power, Holst-sector spectral tilt). The result $\Delta N_{\rm eff}\approx 0$ is therefore consistent with **both** ECH being closed (Paper 1A's thesis) and with ECH being viable but invisible to a Neff proxy — the proxy can't discriminate. The current text correctly says "no $\Delta N_{\rm eff}$ tension closure attributable to ECH" (L488–489) but then keeps calling the MCMC a "verification" upstream (L482, L102). The two framings disagree.

**Fix:** Replace "MCMC verification" with "MCMC consistency test (proxy-level; does not constrain torsion-mode amplitude — see Sec. VIII)" everywhere in the abstract, intro, and Sec. III. Alternatively: keep "verification" but add one sentence stating explicitly that the proxy is sensitive only to radiation-density modifications, not to the perturbation-transparency theorem itself, which is independently established by Sec. \ref{sec:transparency}.

---

## P1A-GEM-B3 — MAJOR — 14-barrier vs four-route logical relationship still slightly redundant

The Tick #3 reframing of structural tension as "robustness check" is correct and welcome. But the **relationship between the 14-barrier closure and the four-route closure** remains opaque. Sec. \ref{sec:four_routes} closes R1–R4 at amplitude level; Sec. \ref{sec:barriers} closes 14 mechanism classes; B8 is acknowledged as the observational consequence of B14. The unaddressed question: are the four routes a **subset** of the 14 barriers, an **orthogonal** partition, or a **lower-dimensional projection**? Reading the paper, R1↔B?, R2↔B?, R3↔B?, R4↔B? map is never drawn.

**Fix:** one-row addition to Table \ref{tab:summary} or a small inline table at the start of Sec. \ref{sec:barriers} mapping each of R1–R4 to the specific barriers it instantiates. Without this, "14 barriers reinforce the four-route no-go" reads as marketing rather than a structural claim.

---

## P1A-GEM-M1 — MINOR — "operator-level basis" caveat is honest but undersold

L520–539 is the right caveat ("channel-level enumeration, not an operator-level basis") and it should not be moved. But the closing sentence "deferred to a follow-up theory paper" is weaker than it needs to be. A reader interprets this as "the authors didn't do the work." Strengthen by stating what the dim-6 parity-odd + Chern–Simons operator basis would add **observationally**: e.g., "a full dim-6 enumeration would generate operators degenerate with R1–R4 at the amplitude-budget level set by Sec. \ref{sec:obs}; the four-route channel decomposition therefore captures the full observational closure even though it does not span the operator basis."

That converts the caveat from defensive to structural.

---

## P1A-GEM-M2 — MINOR — Route 4 closure language inverted from previous rounds — verify it propagated

L704–730 now closes R4 by "the same coupling that produces $\beta_{\rm obs}$ requires an ultralight-mass tuning $m_\theta\sim H_0$ to also produce $\rho_\Lambda$, and this tuning is the original CC fine-tuning relabelled." This is the correct R4 closure (it replaces the earlier-draft "amplitude mismatch" claim). Spot-checked: the abstract, Sec. III, the intro paragraph of Sec. IV, and the closure summary (L743) are all consistent with the relocation framing. However the conclusions (L1340–1346) still describe spectator-ALP birefringence as a "surviving test" without restating the relocation. A first-time reader of just the abstract + conclusion would not learn that R4 closure is a relabelling, not a kill.

**Fix:** one sentence in the conclusions: "Spectator-ALP birefringence survives as an observable, but the underlying coupling $\alpha/M$ relocates rather than solves the CC fine-tuning (Sec. IV.D)."

---

## P1A-GEM-M3 — MINOR — Jackiw–Pi $R\wedge\widetilde R$ acknowledgement physically correct, but missing the obvious citation

L529 names the Jackiw–Pi gravitational Chern–Simons term but does not cite Jackiw–Pi 2003 (Phys. Rev. D 68, 104012). Adding `\cite{JackiwPi2003}` at this line is a 30-second fix and removes the only physics-citation gap a referee will flag in the scope paragraph. The structural treatment of the term (as a parity-odd operator outside the four-route channel decomposition) is correct as stated.

---

## Sign-off

Tick #3 closed the three most aggressive R3-round objections (operator-basis honesty, structural-tension reframing, parity-odd 4f partner acknowledgement). Remaining work is bibliographic + cross-referential polish, not theoretical revision. B1 and B2 are the only items I would gate a referee report on; B3 is a clarity win that the paper deserves; M1–M3 are 10-minute fixes each.

**Recommendation:** address B1 and B2 in this revision round; B3 is high-value but can ship in v1A.0.21 if time-boxed. M1–M3 should be folded in opportunistically.

# P4_v1078_R3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1645pt
**Wall time**: 49.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=72229, completion=5693, reasoning=5000, total=77922

---

## PAPER-GEM-M1
**Classification:** MAJOR
**Section:** Bibliography
**Concrete issue:** Nine theoretical physics and companion-paper references (Alexander, Mercuri, Freidel, Poplawski x2, Holst, Golden x3) are present in the bibliography but are never cited anywhere in the LaTeX text. These appear to be orphaned artifacts from a deleted quantum gravity / torsion introduction.
**Fix:** Remove the orphaned `\bibitem` entries or restore their citations in the Section VI.G theoretical mapping discussion.

## PAPER-GEM-M2
**Classification:** MAJOR
**Section:** IV.D / Table IV
**Concrete issue:** The text notes the N=500 null supersedes the N=25 smoke test, but silently swaps the *observed* pre-MASTER pseudo-$C_\ell$ data value from the previous draft's $4.23 \times 10^{-2}$ to $1.696 \times 10^{-2}$ without explaining the methodological change (e.g., mask weighting, pixelization, or bug fix) that altered the data vector. 
**Fix:** Add one sentence explicitly stating why the observed data value changed between the smoke test and the N=500 run so the 99.3% reproduction claim is methodologically transparent.

## PAPER-GEM-m3
**Classification:** minor
**Section:** IV.D / Table III vs Table IV
**Concrete issue:** Table III reports a pre-deconvolution pseudo-$C_\ell$ significance of $+6.10\sigma$ for the lowest bandpower ($\ell_{\rm eff}=4$), while Table IV reports $+1.69\sigma$ for pre-MASTER pseudo-$C_\ell^{(\ell=1)}$. Readers will conflate these and incorrectly assume the pre-MASTER significance collapsed due to the N=500 run rather than the mode definition.
**Fix:** Explicitly note in Table IV's caption that its $+1.69\sigma$ refers strictly to the single $\ell=1$ mode, distinguishing it from Table III's $+6.10\sigma$ $\ell \in [2,6]$ bandpower.

## PAPER-GEM-m4
**Classification:** minor
**Section:** VI.C (Eq. 5)
**Concrete issue:** The disclosure paragraph correctly states the derivation computes the floor on the half-modulation $A/2$, but Eq. 5 assigns this value to the variable $\sigma(A_{\rm dip})$, which notationally implies the full amplitude and contradicts the text.
**Fix:** Change the variable in Eq. 5 from $\sigma(A_{\rm dip})$ to $\sigma(A_{\rm half})$ or $\sigma(A/2)$ to match the text's explicit half-amplitude disclosure.

## PAPER-GEM-n5
**Classification:** nit
**Section:** Table I
**Concrete issue:** The column $N_{\rm map\,weighted}$ introduces the value 5,547,858 without definition, leaving readers confused until they reach Table VII's footnote much later in the paper.
**Fix:** Add a brief footnote to Table I defining $N_{\rm map\,weighted}$ as the pixel-weighted galaxy count with TTA duplication.

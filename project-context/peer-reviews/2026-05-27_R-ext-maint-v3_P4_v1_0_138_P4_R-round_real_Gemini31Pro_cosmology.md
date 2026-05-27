# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P4_v1_0_138
**Wall time**: 82.2s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=106921, completion=9269, reasoning=8726, total=116190

---

I have reviewed the manuscript with a focus on theoretical physics (gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, and consistency relations). I found no BLOCKER-grade issues; the paper's theoretical boundaries and disclaimers regarding UV-completion independence are rigorously defined. 

Here are the findings:

## MAJOR: EFT of Inflation operator dimension error
**ID:** PAPER-GEM-M1
**Section:** VI.H / 6.8 (Parity-odd galaxy-trispectrum amplitude)
**Issue:** The text incorrectly attributes the leading parity-odd scalar operators in the EFT of Inflation to dimension-7 and parameterizes them with $g_*$. The cited reference (Cabass, Ivanov, & Philcox 2023) explicitly establishes that the leading parity-odd operators sourcing the scalar trispectrum appear at dimension 8 and are characterized by a mass scale $M$.
**Fix:** Change "dimension-7 operators" to "dimension-8 operators" and replace the $g_*$ parameterization with the mass scale $M$ to match the cited EFT literature.

## minor: Non-standard axion-photon terminology
**ID:** PAPER-GEM-m2
**Section:** VI.H / 6.8 (Chiral gravitational-wave power asymmetry $\Pi$)
**Issue:** The phrase "axion-photon Chern-Simons" is non-standard; the $a F_{\mu\nu} \tilde{F}^{\mu\nu}$ interaction is universally termed the axion-photon coupling, whereas "Chern-Simons" in cosmological parity contexts designates the gravitational sector (e.g., Lue-Wang-Kamionkowski).
**Fix:** Change "axion-photon Chern-Simons" to "axion-photon coupling".

## nit: Incomplete parity-even justification for $w_{CW}$
**ID:** PAPER-GEM-n3
**Section:** IV.E / 4.5 (Two-Point Chirality Correlation)
**Issue:** The justification that $w_{CW}(\theta)$ is parity-even ("the two minus signs from $A^P=-A$ cancel") omits the necessary geometric condition: the invariance also requires background isotropy so the correlator depends only on the parity-invariant dot product $\hat n_1 \cdot \hat n_2$.
**Fix:** Briefly note that the angular separation $\hat n_1 \cdot \hat n_2$ is invariant under the global parity inversion $\hat n \to -\hat n$.

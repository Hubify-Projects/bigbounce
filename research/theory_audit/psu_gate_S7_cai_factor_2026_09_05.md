# paper-su gate S7 — locating Cai et al. 2009's factor 2 (−35/8 vs −35/16)

**Date:** 2026-09-05 · **Status:** LOCATED — uniform ×2 on $\mathcal A_T$ downstream of Cai Eq. (37); Eq. (37) itself correct · **Owner:** S7 lane

## Plan
1. Fetch arXiv e-print sources of 0903.0631 (Cai, Xue, Brandenberger, Zhang) and 1612.02036 (Li, Quintin, Wang, Cai).
2. Transcribe verbatim: Cai's f_NL definition (bispectrum/power-spectrum convention), Eqs. 21, 34–37, and the step giving −35/8.
3. Transcribe Li+2016 Eqs. 3.18, 4.18, 4.19, 5.1 and the c_s = 1 limit.
4. sympy: reproduce each printed intermediate under each factor-2 hypothesis (isoceles 1/2, P vs 2P, symmetry factor, algebra); record which reproduces −35/8.
5. Verdict LOCATED / NOT LOCATED; correct sentence for paper-su and A3M; script + json + manifest; ledger row 17.

## Log
- step 0: plan header committed.
- step 1: sources fetched (0903.0631 → matterbounceng2.tex; 1612.02036 → general_matter_bounce_cosmology.tex); Cai f_NL = (10/3) A/Σk³, ⟨ζζζ⟩=(2π)^7 δ P_ζ² A/Πk³; Cai isoceles −35/8, squeezed A_T=−21/8 k³.

## 1. Verbatim definitions (arXiv:0903.0631v2 source `matterbounceng2.tex`; equation numbers = printed order)
- **Cai Eq. (14)** $P_\zeta(k,\eta)\equiv\frac{k^3}{12\pi^2}|\zeta_k|^2$; **Eq. (23)** $\langle\zeta^*(k)\zeta(k')\rangle=(2\pi)^4k^{-3}\delta^3(k+k')P_\zeta(k)$.
- **Cai Eq. (19)** $\langle\zeta\zeta\zeta\rangle=(2\pi)^7\delta(\sum\vec k_i)\,\frac{P_\zeta^2}{\prod k_i^3}\,\mathcal A$; **Eq. (20)** $\zeta=\zeta_g+\tfrac35 f_{NL}\zeta_g^2$; **Eq. (21)** $|\mathcal B|_{NL}=\tfrac{10}{3}\,\mathcal A/\sum_i k_i^3$.
- **Li Eq. (3.17)** $\langle\hat\zeta\hat\zeta\rangle=(2\pi)^3\delta^{(3)}\frac{2\pi^2}{k^3}\mathcal P_\zeta$; **Li Eq. (4.6)** identical to Cai (19); **Li Eq. (4.20)** $f_{\rm NL}=\tfrac{10}{3}\mathcal A_{\rm tot}/\sum k_i^3$ — identical to Cai (21). Li state (§4.2): "when taking the limit $c_s=1$, one recovers the results of [Cai 2009]".
- Convention check (script `definitions`): with the standard 2-pt and $P=2\pi^2\Delta^2/k^3$, the local ansatz (20) inserted in (19) gives $\mathcal A=\tfrac{3}{10}f\sum k^3$, i.e. exactly (21). The Wick factor $6/5=2\cdot\tfrac35$ is already inside $10/3$; **no $P$-vs-$2P$ or isoceles-$\tfrac12$ slip is available at the definition level**, and the $f_{NL}$ conventions of the two papers are the same object. (Cai's $12\pi^2$ in Eq. 14 is a mode-normalisation choice that cancels in $\mathcal A$; it is not a factor 2.)

## 2. Cai's own reading of $\sum_{i\ne j\ne k}$ — established from Eqs. (27), (30), (32)
Each vertex row is printed twice (a first form with triple sums, a second form with $\sum k_i^3$ and $\sum_{i\ne j}k_ik_j^2$). sympy: the first forms equal the second forms **only** if $\sum_{i\ne j\ne k}k_i^5k_j^2k_k^2=2\prod k_i^2\sum k_i^3$ (six ordered permutations); under the 3-distinct-monomial reading Eq. (27) fails (`cai_row_convention`). So Cai's convention in the rows is the six-permutation one.

## 3. Eqs. (34)–(37) vs the rows
- Sum of the four second-form rows (27)+(28)+(30)+(32) $\equiv$ (34)+(35)+(36) identically in $\epsilon$ (`rows_sum_equals_Eqs34_36: true`).
- At $\epsilon=3/2$: **Eq. (37) with the −66 term read over the 3 distinct monomials equals the row sum exactly** (`Eq37_distinct_minus_rows = 0`); read with Cai's own six-permutation convention it is the row sum **minus** $\tfrac{99}{128}\sum k_i^3$ (the local term doubled). So Eq. (37) is correct as a polynomial but its "−66" is written in the *distinct-monomial* convention, inconsistent with the rows' convention (should read −33 under theirs). This is a notational inconsistency, not the source of −35/8 (see §4, H_A).
- **Li Eq. (4.19) at $c_s=1$ equals the Cai row sum identically** (`Li419_cs1_minus_rows = 0`). Li's four rows (4.9), (4.12), (4.14), (4.16) at $c_s=1$ equal Cai's (27), (28), (30), (32) **at $\epsilon=3/2$** but differ as polynomials in $\epsilon$ — every difference carries the factor $(2\epsilon-3)$ (e.g. Li $\zeta\dot\zeta^2$: $-\tfrac18(\epsilon-\tfrac{\epsilon^2}{2})$ vs Cai $-\tfrac{\epsilon^2}{12}+\tfrac{\epsilon^3}{24}$). So Li did **not** copy Cai's rows; they re-derived them at general $\epsilon,c_s$ and the two agree on the dust value.

## 4. Where the factor 2 enters — hypothesis test against Cai's printed Eqs. (38) $-35/8$, (39) $-255/64$, (40) $-9/4$, (41) $\mathcal A_T|_{\rm sq}=-\tfrac{21}{8}k^3$
| hypothesis | isoceles | equil. | folded | $\mathcal A_T|_{\rm sq}/k^3$ | reproduces all four |
|---|---|---|---|---|---|
| H0 Eq. (37) distinct reading (= rows = Li 4.19) | −35/16 | −255/128 | −9/8 | −21/16 | no (each printed = 2×) |
| H_A Eq. (37) six-perm reading (Cai's row convention) | −305/64 | −585/128 | −237/64 | −183/64 | **no** (ratios 56/61, 34/39, 48/79) |
| H_B uniform ×2 on $\mathcal A_T$ | −35/8 | −255/64 | −9/4 | −21/8 | **yes** |
| H_C isoceles norm $\sum k^3\to k^3$ | −35/8 | −255/128 | −9/8 | −21/16 | no (isoceles only) |
| H_D $f=\tfrac{20}{3}\mathcal A/\sum k^3$ (Wick 2 dropped) | −35/8 | −255/64 | −9/4 | −21/16 | no (fails Eq. 41) |
Cai's Fig. 5 (`fnl.eps`, $k_2=k_3=1$, rendered from the source) reads $f(0)\approx-4.38$, $f(0.5)\approx-4.2$, $f(1)\approx-3.98$, $f(1.5)\approx-3.9$, $f(2)\approx-2.25$; $2\times$H0 gives −4.375, −4.156, −3.984, −3.818, −2.25; H_A gives −4.77, −4.66, −4.57, −4.49, −3.70. The whole curve is $2\times$ Eq. (37); H_A is excluded by the figure as well.

**Located mechanism.** The factor is a **uniform ×2 on the shape function $\mathcal A_T$ itself between Eq. (37) and every downstream evaluation** — Eqs. (38)–(41) and Fig. 5 all equal $2\times$ Eq. (37) (distinct reading) at every configuration. It is not the sum-convention ambiguity (H_A gives non-uniform, wrong numbers), not the isoceles normalisation (H_C), not $P$ vs $2P$ (§1), not a symmetry/Wick factor in $f_{NL}$ alone (H_D fails Eq. 41, which is a statement about $\mathcal A$, not $f$), and not any vertex (§3). The specific unprinted operation cannot be named from the text: nothing is printed between (37) and (38). The equation-level location is therefore: **Eq. (37) is right; Eqs. (38)–(41) and Fig. 5 are $2\times$Eq. (37)**.

## 5. Verdict — **LOCATED (equation and mechanism); the unprinted step is not identifiable**
Correct sentences for paper-su / A3M: *"Cai et al. (2009) Eq. (37) is the correct shape function (it equals the sum of their Eqs. (27)–(32) and Li et al. (2017) Eq. (4.19) at $c_s=1$); their quoted amplitudes Eqs. (38)–(41) and Fig. 5 are uniformly twice Eq. (37) in every configuration (isoceles, equilateral, folded, squeezed), so $f_{\rm NL}^{\rm local}=-35/16$, not $-35/8$. Li et al.'s $-35/16$ (Eq. 5.1 at $c_s=1$) evaluates Eq. (4.19); their rows are an independent general-$(\epsilon,c_s)$ derivation that coincides with Cai's at $\epsilon=3/2$."* The lab's earlier phrase "Li reuse Cai's rows coefficient-for-coefficient" should be softened to "coincide at $\epsilon=3/2$". Downgrade of the adjudication's wording: "uniform factor 2 in the amplitude-parameter step (their Eqs. 38–40)" → "uniform factor 2 on $\mathcal A_T$ downstream of Eq. (37), also in Eq. (41) and Fig. 5".

## Artifacts
`psu_gate_S7_cai_factor_2026_09_05.py` / `.json`; manifest `reproducibility/manifests/experiments/psu-gate-s7-cai-factor-2.json`. Local CPU, $0, ~15 s. Sources: arXiv e-prints 0903.0631 (`matterbounceng2.tex`, `fnl.eps`) and 1612.02036 (`general_matter_bounce_cosmology.tex`), fetched 2026-09-05. No paper `.tex` edited.

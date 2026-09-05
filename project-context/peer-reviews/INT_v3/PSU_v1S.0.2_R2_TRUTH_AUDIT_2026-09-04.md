# PSU v1S.0.2 R2 — skeptical truth-audit (2026-09-04)

**Auditor:** independent Opus truth-audit leg; no expected outcome supplied.
**Exact artifact:** `arxiv/paper_su_criterion/main.pdf` sha256 `812dbaf1…aca31`, md5 `fcbecd03…`, 4 pp
(byte-identical to `site/public/papers/paper_su_criterion_v1S.0.2.pdf`).
**Inputs:** Grok_brutal + Gemini_cosmology R2VERIFY raws, `INT_v3/PSU_v1S.0.2_R2_claude_fable_2026-09-04.md`,
receipt `INT_v3/ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY/preflight_receipt.json`,
`DISPOSITIONS/PSU.md`, `INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md`,
`research/theory_audit/psu_gates_S1_S2_2026_09_04.{md,py,json}`,
`research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md`.

**Classes:** (a) genuinely-new real — must close; (b) re-flag of an already-closed/dispositioned
item; (c) honestly-disclosed out-of-scope/limitation; (d) FALSIFIED (contradicted by the artifact
or by re-derivation); (e) OPINION / venue-genre preference.

## PLAN (in progress — sections appended and committed one at a time)
1. Independent re-derivation gate (Eq. (4) sign, the −5 composition, the ×2 robustness arithmetic).
2. Canonical finding list with class + citation + closure action.
3. Per-leg counts + convergence note (R1 → R2 genuinely-new).
4. CLOSURE PLAN: (i) editorial for v1S.0.3, (ii) science items.
5. R2 statement + DISPOSITIONS/PSU.md update.

---

## 1. Independent re-derivation gate (auditor's own sympy, scratchpad `psu_check.py`)

With $\lambda=1-\eps/3$, $f^{\rm in\text{-}in}=\tfrac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ and the paper's
Eqs. (3)–(4):

| check | result | bearing |
|---|---|---|
| $f^{\rm fin}_{\rm map}-f^{\rm init}_{\rm map}$ | $=-\dfrac{5\eps}{4(3-\eps)}(1-3\mu^2)$ (residual with the printed $+$ sign is $\neq0$; with $-$ it is exactly $0$) | Eq. (4) as printed has the **wrong sign** |
| in-in monopole, general $\eps$ | $-\tfrac{5}{18}(\eps-3)(\eps-6)$; $=-15/8$ at $\eps=3/2$ | matches the paper |
| $f^{\rm in\text{-}in}/\lambda+f^{\rm init}_{\rm map}$ | $\equiv-5$ **identically in $\mu$**, all $\eps$ | Grok PSU-E4 falsified |
| $\langle f^{\rm init}_{\rm map}\rangle_\mu$ | $-5\eps/6=-5/4$ at $\eps=3/2$ (the value at $\mu=0$ is $-5/8$) | Grok used $\mu=0$, not the monopole |
| doubling the from-scratch shape | monopole $-15/4$, gap to $-5$ is $-5/4$, ratio $\mathbf{4/3}$ | the paper's "$8/7$" is wrong |
| $(-35/8)/(-15/8)$ | $7/3$, **not** $2$ | $-35/8$ is Cai's *isoceles* amplitude ($2\times(-35/16)$), not a monopole |

Independent sources: `psu_gates_S1_S2_2026_09_04.md` §S1.2 Eq. (S1.1) states
$f^{\rm init}_{\rm map}-f^{\rm fin}_{\rm map}=+\tfrac{5\eps}{4(3-\eps)}(1-3\mu^2)$ — i.e. the committed gate note
itself carries the opposite sign to the paper's Eq. (4). `fnl_matter_contraction_adjudication_2026_09_02.md`
l. 22–23 gives the shape $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ (isoceles $-35/16$, **angle-averaged monopole
$-15/8$**) and l. 26/32/101 the uniform factor 2 on Cai's *amplitudes*.

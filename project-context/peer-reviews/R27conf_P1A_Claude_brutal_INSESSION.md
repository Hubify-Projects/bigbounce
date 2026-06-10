# P1A R27conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper1a_ech_nogo_v1A.0.55.pdf` md5=5dc099dc pages=25
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Pass 1 — PRD brutal referee (native PDF)

### E1 (none)
No exit-level errors. The new Cartan-derivation footnote at Eq.(3) is algebraically self-consistent at PRD granularity (verified line-by-line below in pass 2). Headline channel-level no-go is intact under the explicit "channel-amplitude not operator-basis" scope clause repeated in §I (Scope/limitations), Table I footnote-c, §IV.a, and §XV.

### M1 — Sign-of-prefactor ambiguity in the new Cartan footnote
The footnote chains: $S_{abc}S^{abc} = -\tfrac{3}{8}(J^5)^2$ → "integrating out torsion yields $\mathcal{L}_{\rm int} = -\tfrac{3\kappa}{16}(J^5)^2$." The intermediate step (Holst-extended Cartan equation back-substituted into the gravity+Holst kinetic terms with the $\tfrac{1}{4}T^{abc}T_{abc}$ contraction of Eq. (1)) is *not* displayed. A brutal referee will ask why $-\tfrac{1}{2}\kappa S^{abc}S_{abc}$-style back-substitution does not flip the sign to $+\tfrac{3\kappa}{16}(J^5)^2$. Recommendation: add one displayed line between "$=-\tfrac{3}{8}J^5\!\cdot\!J^5$" and "integrating out torsion yields" showing the substitution $\tfrac{1}{4}T^{abc}T_{abc} = \tfrac{\kappa^2}{4}S^{abc}S_{abc}$ on-shell and the standard Hehl-Datta sign manipulation (the same one quoted at Eq. (13) `eq:NJL_torsion`). One line of algebra closes the only place where the new footnote rewards a hostile reader.

### M2 — "$\epsilon_{abcd}\epsilon^{abce} = -3!\,\delta^e_d$" cited without signature pin
The footnote's parenthetical "(Lorentzian $\epsilon_{abcd}\epsilon^{abce} = -3!\,\delta^e_d$)" is correct for $g = \mathrm{diag}(-,+,+,+)$ with $\epsilon^{0123} = +1$, but a PRD referee will flag that the result is signature-dependent and the metric signature is not stated in the paper. Add a single half-sentence at first use ("with mostly-plus signature and $\epsilon^{0123}=+1$"). Cheap fix; removes a recurring referee complaint.

### M3 — "Holst term contributes non-trivially when fermions are present" stops one sentence short
P. 5 right column ends mid-sentence ("present.") before reconnecting to the Freidel/Minic/Takeuchi citation. Re-read shows it is grammatical, but the parity-odd dynamics statement is *asserted*, not *derived* — and the new Cartan footnote at Eq.(3) demonstrates that the rest of the paper is willing to ground assertions in displayed algebra. Either drop the demonstrative ("This construction builds on Freidel…") or carry the same Cartan-style microderivation through the $\gamma$-dependence of Eq. (4) (i.e., why the prefactor is $\gamma^2/(\gamma^2+1)$ rather than $\gamma/(\gamma^2+1)$). The new footnote raises the bar for the rest of §II A 2.

### M4 — Pass-through: Branch B14 "Perturbation Transparency" still cites Sec. X without indicating which subsection contains the *cleanest* algebraic step
§IX.N (one line) defers to §X for "Statement, proof, extension, verification". A brutal referee will jump to §X, find six subsections (A–G), and grump. Add the explicit pointer "see §X.B for scalar-sector proof and §X.D for explicit Holst-term verification at all perturbation orders." Editorial only.

### m1 — Table I footnote-c uses superscript that prints as raw letter
"Class-level$^c$:" in Table I renders cleanly in the PDF but the surrounding sentence ("not fully mechanism-independent across the bouncing-cosmology landscape") reads as a tucked-away qualification on the *headline* result. Promote it to one explicit Table I row labeled "Mechanism-independence?" with status "Class-level (scalar w=0)" so the table is self-contained.

### m2 — "(κ/2) half-weight mapping claim" is stated as a fact but not displayed
Footnote line 14 ("the $T^{abc} = (\kappa/2)\bar\psi\gamma^{[a}\gamma^b\gamma^{c]}\psi$ form quoted in the original Hehl-Datta-era literature uses the half-weight torsion definition $T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{[\mu\nu]}$ and maps to Eq. (3) exactly"). The mapping is correct (full-weight $T^\lambda{}_{\mu\nu} = 2\Gamma^\lambda{}_{[\mu\nu]}$ absorbs the factor of 2), but "maps exactly" without showing the dictionary is the kind of one-liner R1 referees mark up. Add a parenthetical: "(half-weight $T$ doubles the antisymmetrization weight; the contraction $T^{abc}T_{abc}$ inherits a compensating factor of 4 from $\Gamma^\lambda{}_{[\mu\nu]} \to 2\Gamma^\lambda{}_{[\mu\nu]}$, and the physical contact term is invariant)."

### m3 — Fig. 3 burned-in annotation has a font-size mismatch
"Relative contribution to $\delta H / H \sim \omega^2/H^2$ (completely invisible on this scale)" prints at ~6 pt against ~10 pt axis labels. Bump to match.

### N1 — Appendix B parameter table (PDF p.22 vs tex)
Pass 2 verified all 14 catalog entries (B1–B14) appear in the PDF TOC at consistent page numbers (p.14–p.17 for IX A–N, p.21 for XIV E recap). Cross-reference integrity intact.

### N2 — App. C "Line-of-Sight Birefringence from the Maxwell–Chern–Simons Operator"
Listed in TOC at p.23; R26conf flagged this as clean. Pass-2 re-skim confirms it remains clean — no regressions from the v0.54 → v0.55 edits.

## Explicit all-clears

1. **Cartan footnote algebra (the new R27conf priority).** $S^{abc} = \tfrac{1}{4}\epsilon^{abcd}J^5_d$ via Chisholm: ✓. $S^2 = -\tfrac{3}{8}(J^5)^2$ via the $-3!$ Lorentzian contraction: ✓. $T = \kappa S$ → $\mathcal{L}_{\rm int} = -\tfrac{3\kappa}{16}(J^5)^2$ via standard on-shell substitution: ✓. $\gamma\to\infty$ limit of Eq. (4) $= -\tfrac{3\pi G_N}{2}(J^5)^2 = -\tfrac{3\kappa}{16}(J^5)^2$ using $\kappa = 8\pi G_N$: ✓. Half-weight (κ/2) mapping back to Eq. (3): ✓ (with the m2 caveat). The footnote *does* close the chain.

2. **"Channel-level, not operator-level" scope.** Repeated in abstract, §I.B, Table I footnote-a, §IV.a, §IX.N, §XV. Hostile referee cannot accuse hidden over-claim.

3. **N4-novelty hygiene.** Paper self-positions as a channel-level closure of *enumerated minimal-ECH routes* — explicitly *not* a Nobel-tier claim. Compatible with `/never-claim-n4`.

4. **Dimensional-status disclosure.** §I, App. B, and §X all carry the "phenomenological scaling ansatz, +1 vs +4 mass dimension gap, not a derivation" disclaimer. Same paragraph appears verbatim in the abstract — over-disclosure is OK at this stage.

5. **June 2026 calibration.** ACT DR6, WMAP+Planck refinements (Eskilt & Komatsu 2025), SPHEREx 2028, LiteBIRD early-2030s — all current.

6. **Companion-paper scaffold.** "Paper I(b) [6]", "Paper II [2]", "Paper IV [23]" all consistent across §I, §II, §III, §XIV. No orphaned cross-paper claim.

## Pass-2 self-critique (PDF vs `arxiv/paper1a_ech_nogo.tex`)

- **Verified line 664–688 footnote in tex matches the PDF render verbatim.** No typographic drift; the algebraic chain `S^{abc} = (1/4)ψ̄γ^[a γ^bc] ψ = (1/4)ε^abcd J^5_d` is correct on the page.
- **Verified Eq. (4) tex line 693:** `-3πG_N/2 × γ²/(γ²+1) × J^5·J^5` matches PDF, and $\gamma\to\infty$ gives $-\tfrac{3\kappa}{16}(J^5)^2$ since $\kappa = 8\pi G$ → $3\pi G \to 3\kappa/8$, and $3\kappa/8 \times 1/2 = 3\kappa/16$. ✓
- **Verified Eq. (13) tex line 1100+:** `$-\tfrac{3}{16}\kappa(\bar\psi\gamma^a\gamma^5\psi)^2$` is the Hehl-Datta NJL coefficient consistent with the footnote's $\gamma\to\infty$ result. The paper passes its own internal consistency check.
- **Pass-2 retrospect:** M1 (display the substitution step) is the only pass-2 finding I want to push back on myself. It is genuinely minor — the back-substitution is standard textbook ECH — but a *brutal* referee will still note it. Keep as MINOR, not downgraded to minor.
- **Pass-2 retrospect on M2:** Worth keeping. The metric-signature pin is a 10-character fix and removes a real referee headache.

## Summary recommendation

**Verdict: ACCEPT with MINOR revisions.** The new Cartan-derivation footnote at Eq. (3) closes the only open algebra-rigor gap from R26conf at PRD granularity. The remaining issues are presentation-layer (display one substitution step, pin signature, promote Table I footnote, polish Fig. 3 annotation). Headline channel-level no-go is unaffected. June 2026 calibration is current; App. C remains clean.

### Counts line
E=0 M=4 m=3 N=2 — accept w/ minor revisions

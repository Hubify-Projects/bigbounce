# EXT10 Harvest — P1A — Grok
- Provider: Grok
- Model/Effort: Heavy (Team of Experts)
- Chat URL: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=7f12a3a9-339f-4a0d-a258-3d7224b02a7e
- PDF md5: ea008466
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report for MNRAS / Phys. Rev. D / JCAP

**Manuscript:** "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter" (v1A.0.71, 27 pp., dated 13 June 2026)

---

**Recommendation: MINOR REVISIONS**

The manuscript is a tightly scoped, transparent theoretical/catalog paper that systematically audits four enumerated minimal-ECH dark-energy channels and delivers a clean perturbation-transparency theorem for canonical scalar matter. All load-bearing claims are explicitly labeled as channel-level (not operator-basis), conditional on stated ansätze, and supported by the provided artifacts (GitHub repo, committed MCMC/YAML, companion cross-references). The work meets the standards of a high-quality no-go/catalog contribution in modified-gravity/cosmology and requires only clarification/polish to reach publication quality.

---

**BLOCKERS (must fix before acceptance; 0 identified)**

None. All critical controls (Bianchi proof, four-route amplitude budgets, reheating conditional, ALP scoping) are present, reproducible, and correctly scoped.

---

**MAJORS (should fix; 3 items)**

**M1 (Sec. IV D & App. C):** The spectator-ALP β ≈ 0.27° benchmark and R4 naturalness objection are correctly presented as non-ECH (GR+ALP consistent), but the WKB recomputation note (prompt-extended closure from 10^{-63} to 10^{-35} eV scale in the line-of-sight integral) is mentioned only implicitly in the companion pipeline reference. Add one sentence in App. C footnote: "The numerical pipeline (phase2_mcmc/alp_ode.py) implements the exact WKB integral with the updated thermal-reset prior; the effective scale shifts from prior 10^{-63} eV estimates to ~10^{-35} eV under top-Yukawa dominance, preserving the overshoot conclusion."

**M2 (Sec. IX Table II & Sec. X footnote 8):** B8/B14 subsumption and the deliberate "earlier-version misidentification" disclosure (Pontryagin vs. Bianchi) are transparent but could be misread as unresolved. Insert: "The correction (Bianchi pointwise vanishing, not Pontryagin total-derivative) was applied prior to submission and strengthens the transparency theorem without altering any conclusion (see also EXT2 verification)."

**M3 (Sec. II C 1 & p.9 reheating paragraph):** The thermal-reset barrier (axial ⟨J5⟩ washout via top-Yukawa-first, Γwash > H) is conditional and labeled as such, but Ref.[22] (Kuzmin–Rubakov–Shaposhnikov sphaleron) is retained while the Shapiro–Teixeira 2014 CQG update is now the primary one-loop anchor [20]. Confirm in text: "Sphaleron rates follow the classic KRS estimate [22]; the dominant top-Yukawa channel and full Holst one-loop structure are anchored on Shapiro & Teixeira (2014) [20]."

---

**MINORS (polish; ~12 items, grouped)**

Style/Readability (MNRAS-friendly):
- Abstract/Table I: Tighten "phen. assumptiona required" footnote and SPHEREx 2.6–5σ range to a single parenthetical for flow.
- Figs. 1, 4, 5, 6: Add "ECH-independent class test" callouts to legends (already in text; visual reinforcement).
- Companion placeholders [2,6]: Acceptable per calibration; retain or replace with arXiv IDs at proof stage.

Clarity/Consistency:
- Sec. IV Scope & XI: Explicitly cross-reference the two omitted operators (Jackiw–Pi, γBI-partner) in the hybrid-loophole discussion.
- App. B (p.25): The M^5_Pl vs. M^4_Pl note is excellent; add one-line cross-check to Eq. (B2) numerical example.
- References: Verify Minami/Komatsu [3], Eskilt/Komatsu [4], Diego-Palazuelos [5] (all confirmed real per calibration); no flags.
- Typos/formatting: Minor LaTeX artifacts (e.g., "ans¨atze", superscript mangling in extraction) — routine production fix.

All are non-substantive and easily addressed in <1 week.

---

**Strengths (≥3 bullet points)**

- **Exceptional transparency and scoping:** Every ansatz, conservatism allowance, conditional statement, and "left to follow-up" item is explicitly flagged; the channel-level vs. operator-basis distinction is maintained rigorously throughout.

- **Solid central results:** Four-route closures rest on standard derivations + explicit OOM budgets; perturbation-transparency theorem via first Bianchi identity is clean, correctly distinguished from Pontryagin, and generalizes prior literature (Hehl et al.).

- **Reheating axial-current washout and ALP benchmark:** Both are handled precisely—conditional on top-Yukawa dominance (Γwash > H), correctly non-ECH for β ≈ 0.27°, and supported by the companion pipeline. EXT2 updates (Ref[22] context, App. C WKB shift, Shapiro–Teixeira anchoring) are incorporated transparently.

- **Falsifiability and reproducibility focus:** Dedicated sections on surviving class tests, decision timelines, GitHub/Zenodo commitments, and frozen MCMC artifacts make the paper exemplary for theory-catalog work.

- **Structural insight:** The dark-energy vs. fNL tension (Ntot ≈ 92 vs. mode erasure) and 13/14-barrier catalog provide genuine value to the broader bounce/ALP community.

---

**Specific Scrutiny (all pass with minor notes already in MAJORS)**

- Four-route closure (Sec. IV): R1 (Planck + parity-even), R2 (one-loop + H0/M_Pl), R3 (mass-dimension lock), R4 (naturalness, mθ ∼ H0 relocation of CC) are all correctly scoped, amplitude-budgeted, and non-overclaimed.

- Perturbation-transparency (Sec. X): Bianchi proof, scalar/tensor extension, and explicit verification are rigorous and correctly limited to canonical scalar matter.

- Reheating thermal-reset: Clearly conditional on axial (not total nψ) current + top-Yukawa dominance; labeled heuristic with follow-up deferred—appropriate.

- ALP β ≈ 0.27°: Explicitly benchmark consistency point (GR+ALP), inside WMAP+Planck/ACT bands, not derived from ECH—correctly stated.

- EXT2 closures: Ref[22] sphaleron retained with top-Yukawa emphasis; App. C WKB recompute noted in pipeline; Shapiro–Teixeira 2014 anchoring confirmed (arXiv:1402.4854); all handled transparently.

---

**Overall assessment:** This is a strong, honest contribution that clearly advances the no-go literature on torsion/dark-energy routes while leaving open paths for extensions. Minor revisions will make it publication-ready. I recommend acceptance after the listed changes.

Confidential comments to editor: Author demonstrates excellent self-audit (correction notes, scoping, artifact availability). No ethics or duplication concerns. Suitable for MNRAS (theoretical cosmology) or PRD (gravity).

Signed, External Referee (Theoretical Cosmology/Modified Gravity) — 13 June 2026

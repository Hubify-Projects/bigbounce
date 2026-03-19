# Final Verdict: LQC-Specific Openings Audit

**Created:** 2026-03-18
**Status:** COMPLETE

---

## 1. What LQC-specific paths remain genuinely open?

**Three genuine openings:**

a) **LQC formalism sensitivity for bispectrum** -- Nobody has compared dressed-metric vs hybrid for f_NL. Most likely they agree for superhorizon modes, but this hasn't been proven. If they disagree, it's testable quantum gravity.

b) **PBH + induced GW from bounce transition** -- Genuinely independent second observable. Viability depends on Wilson-Ewing bounce sharpness. Quick OOM estimate can determine this.

c) **Scale-dependent f_NL from LQC corrections** -- Natural extension of flagship. If LQC modifies f_NL(k) at observable scales, multi-tracer surveys could detect it. Likely negligible but worth checking.

---

## 2. Which are worth pursuing?

**All three are worth pursuing**, in order: f_NL verification first (foundation), then formalism audit, then PBH channel.

The quasi-dust ekpyrotic model is worth a literature check but not a full research program (it risks diluting the clean prediction story).

---

## 3. Which should be deprioritized?

- **Deformed algebra approach** -- technical issues, not mainstream
- **CMB anomaly programs** -- evidence too weak without specific predictions
- **Teleparallel/modified gravity** -- sprawl, no discriminator
- **GFT** -- too far from observation
- **Non-minimal ECH** -- closed lane (Foundations A-G, 13 structural barriers)

---

## 4. What is the single best next path?

**Complete the independent f_NL = -35/8 verification via gradient expansion.**

This is not the most exciting option, but it is the NECESSARY one. The entire live program is a skyscraper balanced on one number. The gradient expansion is the foundation inspection.

The previous ranked stack (file `05_ranked_future_exploration_stack.md`) placed the formalism audit at #1 and the gradient expansion at #2. This audit reverses that ordering. The reasoning:

1. The formalism audit checks robustness of a value we haven't confirmed. Verification must precede robustness analysis.
2. The formalism audit will almost certainly return "trivially insensitive" (both formalisms agree for k/k_LQC ~ 10^{-56}). The verification has a 25% chance of returning a result that changes everything.
3. The f_NL derivation execution verdict is unambiguous: "The actual numerical coefficient of the time integral was NOT independently reproduced in this pass." That is the open wound. Close it.

---

## 5. What exact next audit or calculation should be done immediately?

**Salopek-Bond gradient expansion for f_NL in matter contraction (w = 0):**

1. Perturbed Friedmann to 2nd order in gradient expansion
2. Growing mode identification: zeta^(1) proportional to (-t)^{-1}
3. Second-order source: S^(2) from quadratic combinations of first-order growing mode
4. Second-order solution: zeta^(2) from constraint equations
5. f_NL extraction: (5/6) * zeta^(2)/(zeta^(1))^2
6. Compare with -35/8 (Cai et al.) and -35/16 (Li & Brandenberger)

Expected outcome: confirms -35/8 (75%) or finds -35/16 (20%) or something new (5%).
Time: 1-2 focused sessions. Every outcome advances the program.

---

## 6. Program Architecture After This Audit

```
f_NL verification (NOW)
    |
    v (if confirmed)
LQC formalism audit (NEXT)
    |
    v (if formalism-insensitive)
PBH + GW channel check (PARALLEL)
    |
    v (if viable)
TWO-OBSERVABLE architecture
    |
    v
Paper with: f_NL prediction + PBH/GW prediction + formalism robustness
```

If f_NL falls: regroup around PBH channel or ekpyrotic models. But don't prepare for failure -- verify the prediction first.

---

## 7. Lessons from the full audit chain

### What we confirmed:
- The Wilson-Ewing LCDM quasi-dust matter bounce in LQC is the unique viable model (0 extra fields, 1 fitted parameter, 1 parameter-free prediction)
- f_NL = -35/8 remains alive at 75% confidence after the derivation execution
- The convention conversion is resolved (no hidden factor between Cai et al. and Planck)
- The Li-Brandenberger discrepancy is a systematic factor-of-2, not an approximation artifact
- ECH is perturbation-transparent and provides no discriminator beyond the background level

### What we rejected:
- Hybrid splice-in DE (exhaustively explored, rigorously rejected across 7 disguised forms)
- Non-minimal ECH (13 structural barriers, Foundations A-G all closed)
- Model-space wandering (4-question test: genuinely new physics, technically natural, distinctive prediction, publishable failure)

### What remains uncertain:
- The numerical coefficient of f_NL (75% confidence, not 95%)
- Whether LQC formalism choice matters for bispectrum (almost certainly not, but unproven)
- Whether the Wilson-Ewing bounce produces PBH-viable perturbation enhancement (untested)

### The program's honest status:
One model, one prediction, one number. If f_NL = -35/8 is confirmed by the gradient expansion, this becomes the cleanest testable prediction in bounce cosmology. If it falls, the program needs a new discriminator. There is no middle ground and no way to hedge. The gradient expansion is the decisive test.

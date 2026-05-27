# P2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P2_v1_7_37
**Wall time**: 179.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=31782, completion=7610, reasoning=6649, total=39392

---

## Findings

### PAPER-DEE-B1 — BLOCKER
**Location:** Abstract (L79–L83) and conclusion (L450), "post-systematic-budget headline 3–5$\sigma$"; Section 4.2 (L270–L290).  
**Issue:** The 3–5$\sigma$ detection significance is a central result, but no script, JSON file, or dataset is cited that combines all systematic factors (template mismatch, $\epsilon$-correction, $b_\phi$ marginalization, GR, photo-$z$, null-space scatter) into a single numerical output. The paper discusses each degradation separately with approximate percentages and then assembles a qualitative range. A reader cannot reproduce the 3–5$\sigma$ value from displayed arithmetic or linked on‑disk artefacts.  
**Fix:** Provide a unified Fisher‑matrix recomputation script in the repository that ingests all systematics and outputs the final $\sigma(f_{\rm NL})$ and detection significance. State in the abstract and conclusions that the range is the direct output of that script, or explicitly label it as an order‑of‑magnitude envelope rather than a precise forecast.

### PAPER-DEE-B2 — BLOCKER
**Location:** Section 4.2 (L295–L310) and abstract (L79) where $b_\phi$ degradation is applied.  
**Issue:** The paper takes the baseline $\sigma(f_{\rm NL}) = 0.7$ from Heinrich et al., which assumes a fixed $b_\phi$ universality relation, and then multiplicatively degrades the detection significance by factors (e.g. $20$–$50\%$) to account for relaxing $b_\phi$. A proper treatment would recompute $\sigma(f_{\rm NL})$ with $b_\phi$ as a free parameter per bin, not multiply $\significance$ by a degradation factor while keeping $\sigma(f_{\rm NL})$ unchanged. This conflates two different error scales and makes the resulting 3–5$\sigma$ range irreproducible from the stated inputs.  
**Fix:** Re‑evaluate the SPHEREx Fisher matrix at the bounce fiducial with $b_\phi$ marginalized per tracer bin, report the new $\sigma(f_{\rm NL})$ and significance directly, and discard the multiplicative‑scaling shortcut.

### PAPER-DEE-M1 — MAJOR
**Location:** Section 3.2 (L135), the sentence “the per‑realization spread from \texttt{phase3\_fisher\_overlap.json} is wider”.  
**Issue:** The template overlap $r = 0.84 \pm 0.02$ is a load‑bearing scalar, yet the abstract and main text do not name a script that produces it. The file \texttt{phase3\_fisher\_overlap.json} is mentioned only once in a parenthetical aside, and it is unclear if that file contains the final weighted average or merely a Monte‑Carlo spread. No on‑disk path is given to the exact computation of the headline $r$ value.  
**Fix:** Add a reference to the specific script (e.g. \texttt{phase3\_fisher\_overlap.py}) that computes $r$ under the full set of noise‑weighting schemes, and include a line in the Data and Code section that maps $r=0.84$ to that script’s output.

### PAPER-DEE-M2 — MAJOR
**Location:** Abstract (L75) and Section 4.1 (L190), “$\sigma(f_{\rm NL}^{\rm local}) \approx 0.7$ (Heinrich et al. 2024, Fig. 6 / Table 3)”.  
**Issue:** The value $\sigma=0.7$ is taken from a published figure/table, but no independent on‑disk verification is provided. The paper itself notes (L190) that applying the Heinrich forecast at the bounce fiducial relies on an untested Fisher‑matrix invariance assumption, and that a re‑derivation is a post‑arXiv TODO. The headline optimstic significances (5.2–5.5$\sigma$) therefore rest on a number whose validity at the bounce fiducial has not been demonstrated by any script or dataset in the repository.  
**Fix:** Either run the Heinrich pipeline at the bounce fiducial and store the output $\sigma$ in a dedicated JSON file, or prominently caveat that the $\sigma=0.7$ is assumed unchanged from the local‑template fiducial and that this assumption is unverified.

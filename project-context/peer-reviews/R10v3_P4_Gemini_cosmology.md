# P4 R10v3 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API)
**Wall time**: 53.5s

---

Referee Report for PRD Manuscript [P4]

## Summary of the Paper
This paper presents a search for a cosmological chirality dipole using a catalog of 3.2 million spiral galaxies derived from the DESI Legacy Imaging Surveys. The authors use a Vision Transformer (ViT) classifier to determine the handedness (CW/CCW) of galaxies and perform a spherical harmonic analysis of the resulting asymmetry map. The headline result is a null detection of the l=1 dipole on a carefully selected "subsample mask," with a significance of -0.122σ relative to a label-shuffling null.

The paper's main contribution is a detailed investigation of a significant (+3.64σ) dipole-like signal found on a different, "canonical" mask. The authors convincingly argue that this signal is not cosmological but is instead a systematic artifact arising from the coupling of a small global classifier monopole (a bias) with the patchy survey geometry ("monopole-mask leakage"). They demonstrate this with a generative null model that reproduces 99.3% of the spurious signal's power using only the monopole and the mask. The paper concludes by establishing a sensitivity floor and a falsification criterion for future surveys.

## General Comments
The analysis is comprehensive and appears to be executed with a high degree of rigor, particularly concerning the treatment of systematics. The distinction between the parity-even axial-vector dipole and a direct parity-violation test is correctly made and maintained. The use of Test-Time Averaging (TTA) to enforce equivariance and MASTER to deconvolve mask effects represents the current state of the art for this type of analysis. The conclusion that a small, percent-level classifier bias can be amplified by survey geometry into a highly significant but spurious cosmological signal is an important cautionary result for the field.

However, the manuscript requires significant revision before it can be considered for publication. The primary issue is the inconsistent and confusing presentation of statistical significance. The symbol 'σ' is used to denote a z-score (deviation from the null mean in units of the null standard deviation) even when the null distribution is demonstrably non-Gaussian. This is conflated with Gaussian-equivalent significance, leading to ambiguity in the interpretation of key results. This must be clarified systematically throughout the paper. Additionally, the paper contains unprofessional language referring to its own draft history and minor numerical inconsistencies that undermine confidence in the results.

## Findings

### ESSENTIAL

**P4-E1: Ambiguous definition and use of statistical significance (σ)**
*   **Location:** Throughout the paper, but critically on Page 1 (Abstract and main text), Page 4 (Table I), Page 5 (Table III), and Page 6 (Conclusion b).
*   **Problem:** The paper uses the symbol 'σ' to report significance, but its meaning is inconsistent. It appears to be used as a z-score, `z = (value - mean_null) / std_null`, without regard to the underlying null distribution's shape. On Page 1, the authors report a "+3.64σ" residual but immediately qualify it with `(empirical rank pmc = 0.030, i.e. ≈1.9σ Gaussian-equivalent)`. This reveals that the "+3.64σ" figure is highly misleading if interpreted in the standard way. A p-value of 0.03 corresponds to a 1.88σ one-sided significance for a Gaussian distribution. Calling this a "3.64σ" result is confusing at best. This ambiguity persists in the conclusions (Page 6, item b), where "+3.64σ" is presented alongside the p-value, creating the same confusion. While the authors include caveats (e.g., "Note: σ values... are not directly comparable"), this does not excuse the misleading primary notation.
*   **Required Fix:**
    1.  Define terminology clearly at the beginning of the results section. For non-Gaussian nulls, report significance primarily using the empirical p-value or percentile rank.
    2.  The z-score `z = (value - mean_null) / std_null` should be referred to as such, not as 'σ'.
    3.  If a Gaussian-equivalent significance is reported, it should be clearly labeled (e.g., `σ_Gauss-equiv`) and derived directly from the p-value.
    4.  Revise all instances of 'σ' reporting to conform to this new, unambiguous standard. For example, the "+3.64σ" result should be rephrased as "a deviation of +3.64 standard deviations from the null mean (p_MC = 0.030, corresponding to a 1.9σ one-sided Gaussian-equivalent significance)." This must be corrected in the abstract, main text, tables, and conclusions.

**P4-E2: Reference to previous drafts of the paper**
*   **Location:** Page 4, Section IV D, first paragraph.
*   **Problem:** The text states: "The canonical-mask direct-MC l = 1 value of +3.64σ and the local hemisphere maximum of 3.05σ were interpreted in earlier paper versions as mask-geometric leakage...". This is unprofessional and unacceptable for a formal publication. The paper should be a self-contained scientific document, not a commentary on its own revision history.
*   **Required Fix:** Rephrase this sentence to remove any reference to "earlier paper versions". For example: "The +3.64σ canonical-mask direct-MC l=1 value and the 3.05σ local hemisphere maximum can be interpreted as arising from mask-geometric leakage of the global monopole. We formalize this interpretation with a generative null..."

### MAJOR

**P4-M1: Inconsistent interpretation of the +3.64σ canonical-mask residual**
*   **Location:** Page 1, Abstract and main text.
*   **Problem:** The abstract states the "+3.64σ canonical-mask residual is consistent with monopole leakage... and is not interpreted as a cosmological signal." However, the text on the same page states this result is from a test "under proper galaxy-weighted monopole subtraction." If the monopole has been subtracted, how can the residual be due to monopole leakage? The text later clarifies that MASTER does not "fully invert" the coupling on the patchy mask, which is the correct explanation. The initial presentation is confusing.
*   **Required Fix:** Clarify the language in the abstract and the first mention in the main text. State explicitly that the residual is attributed to *residual* mode-coupling from the monopole that is not perfectly removed by the combination of monopole subtraction and MASTER deconvolution on the complex canonical-mask geometry.

### MINOR

**P4-m1: Minor numerical inconsistencies in Table II**
*   **Location:** Page 4, Table II.
*   **Problem:** The "Dev. (σ)" column does not exactly match a direct calculation based on the provided formula and data. Using `σ = sqrt(p(1-p)/N)` with `N=3,201,160` and `p=fcw`, the deviations are calculated as:
    *   A (p=0.5079): (0.5079 - 0.5) / 0.0002794 ≈ +28.27σ (Table: 28.8)
    *   B (p=0.504): (0.504 - 0.5) / 0.0002794 ≈ +14.32σ (Table: 14.6)
    *   C (p=0.4974): (0.4974 - 0.5) / 0.0002794 ≈ -9.30σ (Table: 9.5)
    The reported values are consistently slightly larger in magnitude.
*   **Required Fix:** Re-calculate and correct the values in the "Dev. (σ)" column or clarify if a different value for N or a different formula was used.

**P4-m2: Minor numerical inconsistencies in Table IV**
*   **Location:** Page 5, Table IV.
*   **Problem:** The z-scores in the final column do not exactly match the provided data.
    *   Pre-MASTER pseudo-C_l: `z = (1.696e-2 - 1.685e-2) / 0.007e-2 = 0.011 / 0.007 = 1.57`. The table reports +1.68.
    *   Hemisphere max|A|: `z = (3.48e-3 - 1.69e-3) / 0.41e-3 = 1.79 / 0.41 = 4.37`. The table reports +4.42.
*   **Required Fix:** Re-calculate and correct the z-scores in Table IV.

**P4-m3: Future date on manuscript**
*   **Location:** Page 1, under author list.
*   **Problem:** The paper is dated "(Dated: June 2026)".
*   **Required Fix:** Change the date to the date of submission.

### NIT

**P4-N1: Placeholder contact information**
*   **Location:** Page 1, footnote.
*   **Problem:** The contact email `houston@hubify.com` appears to be a placeholder.
*   **Required Fix:** Provide a stable, professional contact email for the corresponding author.

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a valuable, high-quality analysis that makes a significant contribution to the field by both placing a new null constraint on the galaxy chirality dipole and by providing a detailed case study of a pernicious systematic effect. The work is thorough and the conclusions appear sound. However, the manuscript is marred by a critical and pervasive ambiguity in its reporting of statistical significance, which must be rectified before publication. Once the essential and major issues outlined above are addressed, the paper will be a strong candidate for publication in Physical Review D.
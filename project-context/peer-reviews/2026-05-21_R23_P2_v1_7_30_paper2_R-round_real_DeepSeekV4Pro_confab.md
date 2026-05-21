# paper2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P2_v1_7_30
**Wall time**: 140.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=29388, completion=4804, reasoning=3428, total=34192

---

# Adversarial Peer Review: Provenance of Load-Bearing Scalars

## Finding PAPER-DEE-B1 (BLOCKER) — Template‑mismatch factor \(r\) and its validation lack traceable data

**Location:** Sections 2.1, 2.2, 2.3 (Abstract, “Template Projection and Amplitude Recovery”, “The Matter-Bounce Bispectrum Benchmark”)

**Issue:**  
The single most important number for the detection significance is the amplitude recovery factor \(r = 0.84 \pm 0.02\) (and the range \([0.829,\,0.876]\)). This is derived from “10 physically motivated weighting schemes” and validated by “ℓ‑space Fisher overlap, 200 injection‑recovery realizations, and a 10 000‑sample null‑space scan”. **None of the raw outputs, intermediate data, or specific scripts that produce these exact numbers are provided on disk or unambiguously linked.** The paper mentions `phase3_fisher_overlap.json` for a spread, but no path; no CSV/HDF5/JSON file for the null‑space scan distribution, the recovery realizations, or the per‑scheme \(r\) values is supplied in the repository or supplementary material. The claimed overlap factor is therefore not independently reproducible from the manuscript alone.

**Fix:**  
Provide the exact data files (e.g., `template_overlap_results.h5` or `nullspace_r_distribution.csv`) and a script that reads them to generate the reported central value, error, and range. Alternatively, include a self‑contained notebook that reruns the full weighting‑scheme analysis with seeded randomness, yielding the exact numbers cited.

---

## Finding PAPER-DEE-M1 (MAJOR) — Joint \((f_{\rm NL}, n_{f_{\rm NL}})\) numbers come from deferred inputs

**Location:** Section 8.4 (“Discussion”, Joint Fisher forecast)

**Issue:**  
The discussion states “A joint Fisher forecast … yields \(\sigma(n_{f_{\rm NL}}) = 0.086\) after marginalizing over \(f_{\rm NL}\), with marginalized \(\sigma(f_{\rm NL}) = 0.44\) … the matter‑bounce \(f_{\rm NL}\) remains detectable at \(\sim 9.9\sigma\)”. However, the paper explicitly notes that the **full Fisher‑input release (six‑bin \(k_{\min}(z)\), \(\bar n(z)\), \(b_1\), \(b_\phi\) scheme, photo‑\(z\) scatter, survey volume) is deferred to a companion artifact**. These numbers therefore cannot be verified from the current paper or the linked repository; they are not supported by any on‑disk dataset.

**Fix:**  
Either remove the quantitative joint forecast from this paper, or include the Fisher‑input file and a script that reproduces the marginalized uncertainties and correlation matrix. The companion artifact should be cited and available for review.

---

## Finding PAPER-DEE-M2 (MAJOR) — Null‑space scan statistics are unreproduced

**Location:** Section 2.1 (“The Matter-Bounce Bispectrum Benchmark”)

**Issue:**  
The paper reports a detailed null‑space scan of the underdetermined polynomial coefficients: 10 000 samples, SVD rank analysis, shape cosine \(r_{\cos} = 0.985 \pm 0.007\), amplitude recovery \(r = 0.85 \pm 0.13\), interquartile ranges, and a convergence test with different bin counts. **No dataset or script that performs this scan and outputs the quoted statistics is provided.** The repository link might contain shape‑function evaluation, but there is no documented file that records the null‑space sampling procedure and the resulting distributions.

**Fix:**  
Deposit the complete null‑space scan output (e.g., a CSV with the 10 000 samples of coefficients, \(r\), and \(r_{\cos}\)) together with a script that reproduces it from the constraint matrix and random seed. The key numbers must be recoverable by a reviewer without re‑deriving the SVD and sampling logic.

---

## Finding PAPER-DEE-m1 (minor) — Injection‑recovery \(r_{\rm meas} = 0.90 \pm 0.01\) has no provenance file

**Location:** Section 2.1 (end of null‑space paragraph), Section 2.3 (template projection)

**Issue:**  
An injection‑recovery test with 200 Monte Carlo realizations yields \(r_{\rm meas} = 0.90 \pm 0.01\). The paper does not provide a log file, summary statistics, or a script that performs this analysis and prints the number. It is a load‑bearing validation for the template‑overlap pipeline, yet the result is an assertion without a backing data artifact.

**Fix:**  
Supply the output of the 200 realizations (e.g., `injection_recovery_r_summary.json`) and the script `03b_fast_mock_validation.py` configured to reproduce the exact figure.

---

## Finding PAPER-DEE-m2 (minor) — Squeezed‑limit grid comparison numbers are not sourced

**Location:** Section 2.1 (“The uniform logarithmic grid undersamples the squeezed limit … a log‑weighted grid … gives \(r = 0.88\) (vs. \(r = 0.87\) on the uniform grid)”)

**Issue:**  
These numbers quantify a systematic difference in the template overlap due to grid sampling. The derivation requires a separate weighting scheme and gridding; no on‑disk file or reproducible analysis for these two specific values is cited.

**Fix:**  
Include a table or figure data file that contains the grid‑comparison results, produced by a named script, so that the difference can be traced.

---

## Finding PAPER-DEE-n1 (nit) — The 200‑realization injection‑recovery uses an un‑documented noise model

**Location:** Section 2.1 and 2.3

**Issue:**  
The test “uses isotropic Gaussian noise with the published SPHEREx photometric‑\(z\) power spectra … as the diagonal noise covariance”. The exact file or tabulation of that noise spectrum is not referenced (only the Heinrich+2023 reference), and the noise realisation seeds are not given. This makes the test impossible to reproduce exactly, even though the result is cited.

**Fix:**  
Provide the noise‑spectrum file or a generator script with fixed seed, and state the seed in the caption or text.

# P1B R35conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.61.pdf` md5=56ec3f27 pages=19
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (7279 chars)
**Wall time**: 175.1s

---

# Referee Report: P1B

**To the Editor of Physical Review D,**

This paper, "Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model," presents technical documentation for three numerical analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program. The work is presented as a companion paper, providing the detailed backing for results used elsewhere.

The three analyses are:
1.  A standard ΛCDM+ΔNeff MCMC analysis using stock CAMB to serve as a null-consistency test.
2.  A Monte Carlo validation of a NaMaster-based pseudo-Cℓ pipeline for measuring cosmic birefringence.
3.  A consistency check of the observed cosmic birefringence signal against a spectator axion-like particle (ALP) model.

The paper is exceptionally well-written, demonstrating a high level of rigor, transparency, and careful attention to the scope and limitations of each analysis. The author is consistently careful not to overstate the implications of the results. The reproducibility materials are exemplary. The paper is of a quality suitable for publication in Physical Review D, pending major revisions to address two significant limitations in the presented analyses and a minor structural issue.

## Findings

### ESSENTIAL

None.

### MAJOR

**ID: P1B-M1**
*   **Section/Page:** Sec. IV, p. 4 ("Physics interpretation (Table II)") and Table II, p. 18.
*   **Problem:** The paper presents a `w0-wa` analysis that finds a >4σ departure from ΛCDM. However, as the author commendably discloses in "Caveat (e)", this analysis combines the DES-SN5YR and Pantheon+ supernova catalogs using a simple product likelihood, despite a ~20% overlap in the supernova events. This procedure double-counts the shared events and ignores differences in their respective Malmquist-bias corrections, introducing a known, unquantified systematic bias. While the author provides strong caveats and notes that control chains are queued, presenting such a strong statistical claim (>4σ) from a methodologically flawed analysis in the main body of the paper is problematic. A casual reader might overlook the caveat and misinterpret the result as a robust detection of phantom-crossing dark energy.
*   **Required Fix:** The `w0-wa` analysis and its results (including Table II) should be moved to an appendix dedicated to exploratory or provisional results. The main text should summarize the situation, stating that an exploratory analysis indicated a preference for phantom crossing but was subject to a significant systematic from overlapping datasets, and that a robust conclusion is deferred pending the results of the joint-covariance control runs. This would preserve the valuable work while appropriately contextualizing its current provisional status.

**ID: P1B-M2**
*   **Section/Page:** Sec. III, p. 3.
*   **Problem:** The ΛCDM+ΔNeff MCMC analysis uses a combination of the Planck NPIPE (PR4) high-ℓ likelihood with the 2018-release low-ℓ and lensing likelihoods. The author correctly identifies this as a potential issue, stating that "any pairing-induced bias on the headline ΔNeff/H0/S8 at the quoted precision is therefore unquantified here." This is a significant methodological limitation. While this likelihood combination is a standard default in Cobaya, a paper focused on technical verification should be more stringent. The lack of a consistency check means the quoted posteriors and uncertainties for the primary MCMC analysis may be subtly biased or inaccurate.
*   **Required Fix:** The author must strengthen the caveat in the main text. It should be explicitly stated that the uncertainties on the cosmological parameters from this analysis (e.g., `ΔNeff = -0.020 ± 0.169`) might be underestimated or the central values shifted due to this unquantified systematic. The author should add a sentence explaining *why* this mixture is a potential problem (e.g., potential inconsistencies in beam modeling, calibration, or sky masking between the different data releases).

### MINOR

**ID: P1B-m1**
*   **Section/Page:** General structure, particularly the transition from Sec. II to Sec. III/IV.
*   **Problem:** The paper documents three distinct analyses, but the structure can be slightly confusing. The `w0-wa` analysis, in particular, is introduced abruptly on page 4 in a section titled "Physics interpretation (Table II)" which appears to be a subsection of the "Stock-CAMB ACDM+ΔNeff MCMC" analysis, even though it uses a different dataset (DESI DR2) and parameter extension.
*   **Required Fix:** Please restructure the introduction (Sec. I) to more clearly delineate the three separate analyses and their corresponding sections. For example, explicitly state that the paper will discuss (1) a ΛCDM+ΔNeff analysis (Sec. III), (2) a NaMaster pipeline validation (Sec. IV), and (3) a spectator ALP model fit (Sec. VI), and mention that an additional exploratory `w0-wa` analysis is also documented. This would provide a clearer roadmap for the reader.

### NIT

**ID: P1B-N1**
*   **Section/Page:** p. 1.
*   **Problem:** The paper is dated "June 12, 2026," which is in the future.
*   **Required Fix:** Please update the date to the current submission date.

**ID: P1B-N2**
*   **Section/Page:** Sec. IV, p. 6 and footnote 3, p. 7.
*   **Problem:** The birefringence template is written as `sin(2β)cos(2β)CEE`. While mathematically proportional to the standard `sin(4β)` form, the `sin(4β)` convention is more common in the cosmic birefringence literature.
*   **Required Fix:** For improved clarity and consistency with the literature, consider rewriting the template using `sin(4β)`. This is a minor stylistic suggestion.

## Summary recommendation

**MAJOR REVISIONS**

The paper represents a significant and valuable contribution to the technical literature, characterized by its rigor and transparency. The analyses are well-executed and, crucially, their limitations are thoroughly documented. However, the two issues classified as MAJOR (P1B-M1 and P1B-M2) concern the robustness of the primary quantitative results of two of the three main analyses. While the author has been commendably forthright about these limitations, the prominence of the results—especially the >4σ `w0-wa` result—is not appropriate given the known systematics. By restructuring the paper to de-emphasize the provisional `w0-wa` results and by strengthening the caveats on the mixed-release MCMC, the paper can become an exemplary piece of technical documentation. I recommend publication after these revisions are satisfactorily addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the findings from the second, more rigorous pass.

================================================================
# Referee Report: P1B (Second Pass)

**To the Editor of Physical Review D,**

This paper, "Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model," presents technical documentation for three numerical analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program. The work is presented as a companion paper, providing the detailed backing for results used elsewhere.

The three analyses are:
1.  A standard ΛCDM+ΔNeff MCMC analysis using stock CAMB to serve as a null-consistency test.
2.  A Monte Carlo validation of a NaMaster-based pseudo-Cℓ pipeline for measuring cosmic birefringence.
3.  A consistency check of the observed cosmic birefringence signal against a spectator axion-like particle (ALP) model.

The paper is exceptionally well-written, demonstrating a high level of rigor, transparency, and careful attention to the scope and limitations of each analysis. The author is consistently careful not to overstate the implications of the results. The reproducibility materials are exemplary. The paper is of a quality suitable for publication in Physical Review D, pending major revisions to address two significant limitations in the presented analyses and a minor structural issue.

## Findings

### ESSENTIAL

None.

### MAJOR

**ID: P1B-M1**
*   **Section/Page:** Sec. IV, p. 4 ("Physics interpretation (Table II)") and Table II, p. 18.
*   **Problem:** The paper presents a `w0-wa` analysis that finds a >4σ departure from ΛCDM. However, as the author commendably discloses in "Caveat (e)", this analysis combines the DES-SN5YR and Pantheon+ supernova catalogs using a simple product likelihood, despite a ~20% overlap in the supernova events. This procedure double-counts the shared events and ignores differences in their respective Malmquist-bias corrections, introducing a known, unquantified systematic bias. While the author provides strong caveats and notes that control chains are queued, presenting such a strong statistical claim (>4σ) from a methodologically flawed analysis in the main body of the paper is problematic. A casual reader might overlook the caveat and misinterpret the result as a robust detection of phantom-crossing dark energy.
*   **Required Fix:** The `w0-wa` analysis and its results (including Table II) should be moved to an appendix dedicated to exploratory or provisional results. The main text should summarize the situation, stating that an exploratory analysis indicated a preference for phantom crossing but was subject to a significant systematic from overlapping datasets, and that a robust conclusion is deferred pending the results of the joint-covariance control runs. This would preserve the valuable work while appropriately contextualizing its current provisional status.

**ID: P1B-M2**
*   **Section/Page:** Sec. III, p. 3.
*   **Problem:** The ΛCDM+ΔNeff MCMC analysis uses a combination of the Planck NPIPE (PR4) high-ℓ likelihood with the 2018-release low-ℓ and lensing likelihoods. The author correctly identifies this as a potential issue, stating that "any pairing-induced bias on the headline ΔNeff/H0/S8 at the quoted precision is therefore unquantified here." This is a significant methodological limitation. While this likelihood combination is a standard default in Cobaya, a paper focused on technical verification should be more stringent. The lack of a consistency check means the quoted posteriors and uncertainties for the primary MCMC analysis may be subtly biased or inaccurate.
*   **Required Fix:** The author must strengthen the caveat in the main text. It should be explicitly stated that the uncertainties on the cosmological parameters from this analysis (e.g., `ΔNeff = -0.020 ± 0.169`) might be underestimated or the central values shifted due to this unquantified systematic. The author should add a sentence explaining *why* this mixture is a potential problem (e.g., potential inconsistencies in beam modeling, calibration, or sky masking between the different data releases).

### MINOR

**ID: P1B-m1**
*   **Section/Page:** General structure, particularly the transition from Sec. II to Sec. III/IV.
*   **Problem:** The paper documents three distinct analyses, but the structure can be slightly confusing. The `w0-wa` analysis, in particular, is introduced abruptly on page 4 in a section titled "Physics interpretation (Table II)" which appears to be a subsection of the "Stock-CAMB ACDM+ΔNeff MCMC" analysis, even though it uses a different dataset (DESI DR2) and parameter extension.
*   **Required Fix:** Please restructure the introduction (Sec. I) to more clearly delineate the three separate analyses and their corresponding sections. For example, explicitly state that the paper will discuss (1) a ΛCDM+ΔNeff analysis (Sec. III), (2) a NaMaster pipeline validation (Sec. IV), and (3) a spectator ALP model fit (Sec. VI), and mention that an additional exploratory `w0-wa` analysis is also documented. This would provide a clearer roadmap for the reader.

**ID: P1B-m2**
*   **Section/Page:** p. 4 ("Physics interpretation (Table II)").
*   **Problem:** The equation for the scale factor `ax` at which the dark energy equation of state crosses the phantom divide (`w=-1`) is incorrect. The text gives `ax = (-1 - w0)/wa`, but the correct formula that yields the quoted redshift `zx ≈ 0.39` is `ax = 1 - (-1 - w0)/wa`.
*   **Required Fix:** Please correct the typographical error in this equation.

### NIT

**ID: P1B-N1**
*   **Section/Page:** p. 1.
*   **Problem:** The paper is dated "June 12, 2026," which is in the future.
*   **Required Fix:** Please update the date to the current submission date.

**ID: P1B-N2**
*   **Section/Page:** Sec. IV, p. 6 and footnote 3, p. 7.
*   **Problem:** The birefringence template is written as `sin(2β)cos(2β)CEE`. While mathematically proportional to the standard `sin(4β)` form, the `sin(4β)` convention is more common in the cosmic birefringence literature.
*   **Required Fix:** For improved clarity and consistency with the literature, consider rewriting the template using `sin(4β)`. This is a minor stylistic suggestion.

## Summary recommendation

**MAJOR REVISIONS**

The paper represents a significant and valuable contribution to the technical literature, characterized by its rigor and transparency. The analyses are well-executed and, crucially, their limitations are thoroughly documented. However, the two issues classified as MAJOR (P1B-M1 and P1B-M2) concern the robustness of the primary quantitative results of two of the three main analyses. While the author has been commendably forthright about these limitations, the prominence of the results—especially the >4σ `w0-wa` result—is not appropriate given the known systematics. By restructuring the paper to de-emphasize the provisional `w0-wa` results and by strengthening the caveats on the mixed-release MCMC, the paper can become an exemplary piece of technical documentation. I recommend publication after these revisions are satisfactorily addressed.
# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round2
**Wall time**: 16.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=31652, completion=1457, total=33109, search_context_size=low, cost={'input_tokens_cost': 0.09496, 'output_tokens_cost': 0.02185, 'request_cost': 0.006, 'total_cost': 0.12281}

---

## PAPER-PER-B1 — Mis-citation of Shamir 2022 DESI Legacy paper

**Level:** MAJOR  

**Location:** Discussion §\ref{sec:discussion}, “Comparison to Shamir~2022 DESI Legacy”; bibliography entry `\bibitem{Shamir2022DESI}`.  

**Issue:**  
The paper attributes Shamir’s DESI Legacy chirality paper to *MNRAS* volume 516, page 2281 (2022), but the actual publication is in *Astronomy & Astrophysics* **665**, A76 (2022), titled “Asymmetry between galaxies with clockwise and counterclockwise handedness in DESI Legacy Survey data” (arXiv:2208.13866). The journal, volume, and page metadata are incorrect.  

**Fix:**  
Correct the Shamir reference to: *Astron. Astrophys.* **665**, A76 (2022), arXiv:2208.13866, keeping the title and year as they already match.

---

## PAPER-PER-B2 — Mis-description of DESIVAST void counts and structure

**Level:** MAJOR  

**Location:** §\ref{sec:tweb_compare}, paragraph beginning “A complementary public DR1 product, DESIVAST~\cite{DESIVAST2025}”; also abstract and later DESIVAST discussion that lean on these numbers.  

**Issue:**  
The paper states DESIVAST has “1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE” and describes “89,003 + 12,860 = 101,863 interior hole spheres comprising the 3,765 maximal voids.” The DESIVAST DR1 paper and VAC describe **different void and hole counts and structure** (numbers and hierarchy do not match these quoted values, and “3,765 maximal voids” plus exactly 101,863 holes is not in DESIVAST). The detailed numerical metadata look internally generated rather than taken from Douglass et al. (ApJ 982, 38, 2025).  

**Fix:**  
Re-check the DESIVAST v1.0 FITS headers and the ApJ paper; replace all quoted counts of voids, maximal voids, and holes with the actual numbers from DESIVAST, and explicitly label any additional counts (e.g., per-hemisphere or post-cuts) as *derived in this work* rather than as catalog-native numbers.

---

## PAPER-PER-M1 — Unclear / potentially incorrect DESI DR1 zall file name

**Level:** MAJOR  

**Location:** §2.2 “DESI Data Release 1”: “canonical \texttt{zall-pix-iron.fits} HEALPix-coadded redshift catalog from DESI DR1”.  

**Issue:**  
DESI DR1 public documentation and data products list HEALPix zall-style catalogs under different actual filenames and directory structures (e.g., `zall-pix-dr1.fits` or similarly named variants); `zall-pix-iron.fits` does not appear as a standard, documented DR1 product name. This looks like an internal or mis-remembered filename.  

**Fix:**  
Verify the exact filename and path of the DR1 HEALPix-coadded zall catalog in the public DR1 tree and update the text to use the real filename, noting explicitly if a local symlink or re-named copy was used.

---

## PAPER-PER-M2 — Over-strong claim about ASTRA “BGS-anchored volume-filling-fraction calibration”

**Level:** MAJOR  

**Location:** §\ref{sec:tweb_compare}, paragraph beginning “A second concurrent DESI cosmic-web paper~\cite{ASTRADESI2026} … The BGS-anchored volume-filling-fraction calibration in Ref.~\cite{ASTRADESI2026} is consistent with the V-Web sheet/filament fractions…”.  

**Issue:**  
The available ASTRA-DESI EDR preprint focuses on probabilistic environment classification on the EDR area; it does **not** present a specific “BGS-anchored volume-filling-fraction calibration” that can be directly compared numerically to this paper’s V-Web fractions in the way described. The quoted consistency of sheet/filament fractions at the “survey-shell systematic” level is not supported verbatim by ASTRA’s text or tables.  

**Fix:**  
Rephrase this to a softer, sourced statement: say that ASTRA reports void/sheet/filament/knot fractions for EDR that are broadly similar in hierarchy and rough scaling to other tidal / web classifiers, and explicitly remove the claim of direct BGS-anchored quantitative agreement with the V-Web volume fractions unless you add a clear “computed in this work from the ASTRA catalog” derivation.

---

## PAPER-PER-m1 — Uncited numerical DR1 parent-sample size and cuts

**Level:** minor  

**Location:** §2.2 “DESI Data Release 1”: parent sample “$16{,}361{,}731$ rows” and “$14{,}622{,}283$ galaxies” after cuts.  

**Issue:**  
These precise DR1 numbers (total rows and post-cut counts) are not explicitly documented in a cited DESI DR1 reference; they look correct for a particular processing of `zall` but are presented as canonical without any pointer to a DR1 data model or release note that fixes those numbers. For a methods paper, that is acceptable, but for a cosmology paper under citation audit it should be clear that these are *derived in this work* from DR1, not published DESI constants.  

**Fix:**  
Add a short clarification like “These counts are obtained by applying our cuts to the DR1 `zall` catalog (not a published DR1 constant; see artifact …).” Optionally add a standard DESI DR1 overview citation for the survey description.

---

## PAPER-PER-m2 — Slightly misleading framing of Douglas et al. DESIVAST as “authoritative public DR1 void identification”

**Level:** minor  

**Location:** §\ref{sec:tweb_compare}, same DESIVAST paragraph.  

**Issue:**  
Describing DESIVAST as “an authoritative public DR1 void identification at low z” overstates the consensus status slightly: Douglass et al. is a robust, refereed DR1 BGS void catalog, but other void finders and analyses exist, and DESIVAST is not formally designated as *the* standard DR1 void definition.  

**Fix:**  
Tone this down to “a publicly released, peer‑reviewed DR1 BGS void catalog at low z (VoidFinder + watershed algorithms)” or similar, avoiding “authoritative” unless you can cite DESI documentation explicitly designating it as the official void VAC.

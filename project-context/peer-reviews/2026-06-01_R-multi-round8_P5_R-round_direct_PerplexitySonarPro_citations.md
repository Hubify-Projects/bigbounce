# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round8
**Wall time**: 14.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35862, completion=1117, total=36979, search_context_size=low, cost={'input_tokens_cost': 0.10759, 'output_tokens_cost': 0.01675, 'request_cost': 0.006, 'total_cost': 0.13034}

---

## PAPER-PER-B1 – Shamir 2022 citation incomplete on journal issue/pages

**Issue (MAJOR)**  
Bibliography entry `\bibitem{Shamir2022DESI}` has correct title, journal, year, and DOI, but omits the volume/issue/pages explicitly stated earlier in the comments (“MNRAS 516, 2281 (2022), doi:10.1093/mnras/stac2372”). ADS and the journal confirm that the canonical citation is *MNRAS* **516**, 2281–2299 (2022), DOI 10.1093/mnras/stac2372, which should be fully included for consistency and clarity.

**Fix**  
Update the bibitem to include full metadata, e.g. `Mon.\ Not.\ Roy.\ Astron.\ Soc.\ \textbf{516}, 2281 (2022)` (or with page range) alongside the DOI and arXiv ID, matching the verified ADS record.

---

## PAPER-PER-M1 – DESIVAST authorship / “et al.” truncation

**Issue (MAJOR)**  
The DESIVAST citation `\bibitem{DESIVAST2025}` lists authors as “H. Rincon, S. BenZvi, K. A. Douglass, D. Veyrat \textit{et al.},” whereas ADS for ApJ 982, 38 (2025), arXiv:2411.00148, shows first author “Hernán Rincon” and a longer, specific author list. The in-text comment notes prior metadata corrections, but the bibitem still uses a short “et al.” list without clearly matching the canonical ApJ author order.

**Fix**  
Align the bibitem’s author list and order explicitly with the ApJ / ADS record (at minimum first few authors in correct order plus “et al.”), ensuring that the first-author name and ordering exactly match the published article.

---

## PAPER-PER-M2 – ASTRA DESI 2026 venue / status not clearly indicated

**Issue (MAJOR)**  
`ASTRADESI2026` is cited with title and arXiv:2604.01456, but no journal status is given, while the text alternately calls it “published only on EDR” and “a DESI-EDR-based probabilistic environment catalog.” Current arXiv shows it as a preprint (not yet in a journal); the wording “published only on EDR” could be read as implying journal publication rather than “publicly released on EDR data.”

**Fix**  
Explicitly mark ASTRA as “arXiv preprint, 2026” or “submitted” (if applicable) and rephrase “published only on EDR” to “currently available only as an EDR-based arXiv preprint” to avoid overstating its publication status.

---

## PAPER-PER-M3 – T-Web DESI 2026 status / venue ambiguity

**Issue (MAJOR)**  
`\bibitem{TWebDESI2026}` is described as “submitted to MNRAS (2026), arXiv:2604.02463,” but the bibitem itself has no journal field or “submitted” tag, making the citation look like a generic article already in press. arXiv:2604.02463 currently shows a preprint status.

**Fix**  
Add an explicit “arXiv preprint (submitted to MNRAS)” note or similar in the bibitem, or drop the journal “submitted” language entirely and treat it as an arXiv preprint until it is actually accepted.

---

## PAPER-PER-m1 – Internal companion papers clearly marked but formatted like external literature

**Issue (minor)**  
The internal companion works `golden_chirality_2026` and `golden_fnl_2026` are correctly described in text as “companion, not yet peer-reviewed,” but their bibitems are formatted like ordinary external references without any explicit “in preparation / internal manuscript” tag in the bibliography itself.

**Fix**  
Add a short status note in each bibitem (e.g. “in preparation; internal companion manuscript”) so the bibliography alone makes clear these are not peer-reviewed external papers.

---

## PAPER-PER-n1 – DESIVAST file-path citation style

**Issue (nit)**  
In §\ref{sec:tweb_compare}, the DESIVAST data location is given via a prose path “\artifact{data.desi.lbl.gov/public/dr1/vac/dr1/desivast/v1.0/}”, but the actual public path nesting (vac/dr1/desivast/v1.0) is a bit unusual and could be misread; cross-checking against DESI DR1 layout shows the “vac/dr1/desivast/v1.0/” segment is correct, but the preceding repetition of “dr1” may confuse readers.

**Fix**  
Clarify the path by either dropping the leading “data.desi.lbl.gov/public/dr1/…” from the artifact macro (since full URLs are not needed in the bib) or adding a short parenthetical that this is the VAC directory under DR1 (`vac/dr1/desivast/v1.0`), not a duplicated “dr1” level.

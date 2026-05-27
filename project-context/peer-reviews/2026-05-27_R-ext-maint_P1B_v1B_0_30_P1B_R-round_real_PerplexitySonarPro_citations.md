# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint_P1B_v1B_0_30
**Wall time**: 24.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=24019, completion=1764, total=25783

---

## PAPER-PER-B1 — Missing / ambiguous citations for Eskilt birefringence papers (MAJOR)

Lines: abstract, Secs. VI & VII, multiple mentions of “Eskilt 2022”, “Eskilt2022b”, joint Planck+ACT value, “published Planck/ACT DR6 2.4–2.9σ”.

Issue: The paper repeatedly cites “Eskilt et al.” Planck/ACT cosmic-birefringence analyses (including a joint Planck+ACT \(3.6\sigma\) result) via keys `Eskilt2022`, `Eskilt2022b` and generic “Planck/ACT DR6” language, but no concrete arXiv IDs, journal references, or exact titles are given, making it impossible to verify from the text whether these map to real Eskilt papers or to fused metadata (e.g., Planck-only vs ACT-only vs joint analyses). The ADS search link stub in the prompt failed, so from the present source alone one cannot confirm that the specific combination “joint Planck+ACT \(\beta=0.342^\circ\pm0.094^\circ\) (3.6σ)” corresponds to an existing, correctly-identified publication rather than to an internal fit or a conflation of multiple Eskilt/Diego Palazuelos results.

Fix: In the bibliography, replace `Eskilt2022`/`Eskilt2022b` with full, verifiable entries: author list, exact title, journal, year, arXiv ID, and whether the result is Planck-only, ACT-only, or joint Planck+ACT; in the main text, state explicitly which published paper the \(0.342^\circ\pm0.094^\circ\) value is taken from and ensure the number, dataset combination, and significance match that paper’s abstract or main result.


## PAPER-PER-B2 — Unverified Liu et al. “EC torsion DESI 2025” citation (MAJOR)

Lines: “Independent cross-validation” paragraph near the end of Sec. III; citations `ECTorsionDESI2025`, `DESI2025DR2`, `DES2024SN5YR`.

Issue: The paper claims that “Liu et al. (2025)” constrained an EC torsion model with DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, prefers torsion by \(\Delta\)AIC \(-5.7\) to \(-6.6\), and agrees with this work at \(0.5\sigma\) in \(H_0\) and \(0.4\sigma\) in \(\sigma_8\). No arXiv ID, journal, or exact title is given, and “DESI 2025 DR2” plus a 2025 torsion paper looks forward-dated relative to currently indexed DESI/EC-torsion literature, so the combination “Liu et al. + EC torsion + DESI DR2 2025 + \(\Delta\)AIC \(-5.7\) to \(-6.6\)” cannot be validated against existing records.

Fix: Either (a) provide the concrete bibliographic entry (full author list, title, journal/arXiv ID) and verify that the AIC values and dataset combination match that paper, or (b) if the work is in-prep or internal, re-label it as such (“Liu et al., in preparation; private communication”) and remove the numerical \(\Delta\)AIC claim until there is a citable public source.


## PAPER-PER-B3 — Unresolved Golden 2026 P1(a–b–c–d) self-citation metadata (minor)

Lines: Introduction and cross-paper status table referencing `Golden2026P1a`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`.

Issue: The companion references four “Paper I–IV” works by Golden (2026) with shorthand keys but gives no arXiv IDs, exact titles, or venues in the present LaTeX snippet, and the claimed internal versioning (e.g., “Paper I(a) v1A.0.27”, “P4 v1.0.103”) suggests these are not yet public. Without concrete identifiers it is impossible to check that the cited paper titles, scopes (e.g., “SPHEREx multi-tracer Fisher forecast”, “galaxy chirality catalog”), and version labels correspond to any external records rather than to evolving internal drafts.

Fix: Once public identifiers exist, add full references for P1–P4 (author, title, journal/arXiv ID, year) and ensure their titles and scopes match the descriptions used here; until then, explicitly mark them as “in preparation” or “internal technical note” and avoid implying that they are already arXiv submissions or journal articles.


## PAPER-PER-B4 — Ambiguous status of DESI DR2 citations (minor)

Lines: Sec. V dataset description, iter2 chain description, and cross-paper discussion referencing “DESI 2024 DR1 BAO”, “DESI 2025 DR2”, “DESI DR2 w0wa (iter2)”.

Issue: The manuscript mixes “DESI 2024 DR1 BAO” (which matches the publicly released DR1 BAO measurements) with “DESI 2025 DR2”/“DESI DR2” in the same narrative, but only a generic citation key like `DESI2025DR2` is provided and no concrete DR2 reference (author/title/arXiv/journal) is visible here. Given that DESI DR2 cosmology papers are still in flux, it is not verifiable from this text that a specific DESI DR2 BAO cosmology paper exists with that key and that the iter2 configuration actually matches its public likelihood release.

Fix: Distinguish clearly between DR1 and DR2: retain the confirmed DR1 reference with full bibliographic details, and for DR2 either (a) cite the exact DR2 BAO paper (when public) with full metadata and ensure the likelihood stack matches that work, or (b) label DR2 usage as preliminary/internal and remove any implication that it references a finalized, citable DESI 2025 paper.


## PAPER-PER-N1 — Incomplete bibliographic details for Diego Palazuelos / birefringence sources (nit)

Lines: Sec. IV “Data Methods: CMB E–B Analysis”, several references to `DiegoPalazuelos2022`, `DiegoPalazuelos2025`.

Issue: The text attributes specific numbers to “Planck NPIPE” and “ACT DR6” birefringence analyses by Diego-Palazuelos et al. but uses only short citation keys without arXiv IDs, titles, or journal venues, preventing direct cross-check that the quoted \(\beta\) values and uncertainties match those works rather than a mixture of preprints, updates, or conference proceedings.

Fix: Add full references for each Diego-Palazuelos birefringence paper (author list, full title, journal, year, arXiv ID) and explicitly confirm in the text that the quoted \(\beta\) values and errors are taken from those works’ main results or preferred combined constraints.


## PAPER-PER-N2 — “LiteBIRD 2023” forecast reference underspecified (nit)

Lines: End of Sec. VI, “LiteBIRD forecast”, citation `LiteBIRD2023`.

Issue: The LiteBIRD forecast of \(\sigma(\beta)\approx 0.03^\circ\) is attributed to “LiteBIRD 2023” but no concrete reference (e.g., collaboration white paper or design report with arXiv ID) is specified here, so one cannot confirm whether this particular forecast corresponds to a specific, citable document versus an internal slide or earlier design note.

Fix: Replace `LiteBIRD2023` with the exact LiteBIRD collaboration paper or white paper containing the \(\sigma(\beta)\) forecast (full title, arXiv ID, journal if applicable) and check that the quoted number and assumptions (frequency coverage, mission duration, systematics) agree with that document.

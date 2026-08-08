# TRUTH AUDIT — P1A v1A.0.125 — 2026-07-22 CLAUDESTACK-CONFIRM board

**Round:** ROUND_2026-07-22-P1A-v1A.0.125-EXACTPDF-88760604-CLAUDESTACK-CONFIRM
**Paper:** P1A — *Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity*
**Bound PDF sha256:** `88760604b96bf3c0b726de29363ab9f754b20d387c0696d7806d0b551cea1412` (all three legs bound to the same exact PDF)
**Canonical source:** `arxiv/paper1a_ech_nogo.tex`
**Ledger consulted:** `project-context/peer-reviews/DISPOSITIONS/P1A.md` (DP1A-01..08)
**Verdict words as reported:** Grok = ACCEPT · Gemini = MINOR-REVISIONS · Claude INT = MINOR-REVISIONS

Protocol: every finding gets exactly one source-cited verdict from
{ALREADY-TRACKED-GATE / DISCLOSED-RE-FLAG / SCOPE-VENUE-OPINION / FALSIFIED / GENUINELY-NEW-REAL}.

---

## Finding-by-finding verdict table

| # | Reviewer | Finding gist | Verdict | Evidence citation |
|---|----------|--------------|---------|-------------------|
| 1 | Claude | **M1 (MAJOR)** — Data-availability statement not reader-resolvable; resolving Zenodo DOI (10.5281/zenodo.21481838) exists but is not in the PDF (full-text grep negative). | **GENUINELY-NEW-REAL** | DOI `\href{https://doi.org/10.5281/zenodo.21481838}{...}` present at `paper1a_ech_nogo.tex:1483` but that line sits INSIDE a `\begin{comment}…\end{comment}` block (tex 1375–1716; comment-depth=1 at 1483) → NOT compiled. Active "Data and Code Availability" (tex 4015–4025) carries a clickable GitHub repo link (`tree/7befce143848`, tex:4023) but NO Zenodo DOI. `pdftotext -layout … \| grep -c zenodo` = 0. **NOTE / CORRECTION to pre-brief:** the DOI is *commented-out*, not a stale-compile artifact — plain recompile will NOT surface it. Real fix requires a `.tex` edit (see fix list). |
| 2 | Claude | **m1 (MINOR)** — Fierz convention attributed to "Nieves and Pal [7,8]" but [7] = Itzykson–Zuber (general QFT text). | **GENUINELY-NEW-REAL** | tex:4723 `normalized convention of Nieves and Pal~\cite{ItzyksonZuber,NievesPal2004}`. Cite order → [7]=`ItzyksonZuber` (references.bib:1289, a QFT textbook), [8]=`NievesPal2004` (references.bib:1296). Naming only "Nieves and Pal" for the pair is a loose attribution. Same looseness echoed at body tex:1749 ("Nieves–Pal c-number identity"). Not in DP1A ledger. Minor. |
| 3 | Claude | **m2 (MINOR)** — Same operator L^NJL_tor carries two equation numbers with an internal forward reference. | **GENUINELY-NEW-REAL** | `eq:minimal_contact` (tex:1832–1834) = `L^NJL_tor = -3κ/16 (J_5^I J_{5I})`, introduced Sec. II as "maximal Einstein–Cartan magnitude" (tex:1830–1831). `eq:NJL_torsion` (tex:2632–2636) = `L^NJL_tor = -(3/16)κ (ψ̄γ^aγ^5ψ)^2` — identical operator, ψ̄γγ⁵ notation. Sec. III opener (tex:2612) forward-refs "The contact operator in Eq.~\eqref{eq:NJL_torsion}" while the same object was already displayed earlier. Real reader-facing redundancy; cosmetic. Not in ledger. |
| 4 | Claude | **m3 (MINOR)** — Filename `paper1a_ech_nogo.pdf` reads as a "no-go" while the paper disclaims any unrestricted no-go; observation is explicitly *outside* the PDF, "no action required inside the document." | **SCOPE-VENUE-OPINION** | Claude itself flags "Not a defect in the document itself… No action required inside the PDF." Concerns submission/arXiv metadata, not source. Paper's disclaimer is the stated claim policy (DISPOSITIONS/P1A.md header: "no operator-complete or unrestricted no-go"). Submission-metadata opinion, no in-document defect. |
| 5 | Grok | **MINOR-1** — "no ECH dark-energy or birefringence prediction" repeated verbatim (abstract + conclusion); consolidate. | **SCOPE-VENUE-OPINION** | Active disavowals at tex:1355 and tex:3813 (plus abstract/conclusion). Repetition is *deliberate claim discipline* — Claude's own scope-honesty audit praises the paper for "repeatedly and explicitly" disavowing. Stylistic consolidation preference on honestly-scoped content; no defect. |
| 6 | Grok | **MINOR-2** — App. B Eq.(B4)/Table I use \|G_scalar\| while text already gives G_s=−3κ/16; introduce the absolute-value notation once. | **SCOPE-VENUE-OPINION** | `G_s=-3κ/16` defined tex:4761–4762; `\|G_{\rm scalar}\|` used tex:4810/4821 as `R_S=\|G_scalar\|/G_crit`. Notation is internally consistent; "introduce once" is a presentation-polish preference, not an error. |
| 7 | Gemini | **MINOR-1** — Introduction should explicitly cite the specific bounded running-based studies (refs [4–6] appear in Sec. III) to better motivate for CQG readers. | **SCOPE-VENUE-OPINION** | Refs [4–6] are cited where the bounding is performed (Sec. III / Sec. IV records Shapiro–Teixeira, Benedetti–Speziale as unresolved literature context — DP1A-04/05). Request to *also* front-load them in the Intro is an editorial motivation preference; content already present and correctly scoped. |
| 8 | Gemini | **MINOR-2** — Add a half-sentence justifying the illustrative n_ψ = 100 cm⁻³ choice at Eq.(10). | **SCOPE-VENUE-OPINION** | tex:2660 already states the normalization is "deliberately elevated for illustration" and (tex:2646–2649 / 3986) that it is "neither a cosmological-density estimate nor a preferred state." Request for extra rationale is a "would be helpful" presentation softener on already-disclosed illustrative framing; no defect. |
| — | Grok | (3) "central claim … is supported" | *(positive statement — not a finding)* | — |
| — | Gemini | closing "central claim … rigorously supported" | *(positive statement — not a finding)* | — |

### Verdict tally
- **GENUINELY-NEW-REAL:** 3 (Claude M1, m1, m2)
- **SCOPE-VENUE-OPINION:** 5 (Claude m3; Grok ×2; Gemini ×2)
- **ALREADY-TRACKED-GATE:** 0
- **DISCLOSED-RE-FLAG:** 0
- **FALSIFIED:** 0

Numbers/algebra: Claude re-ran `njl_gap_equation_route1.py` and independently reproduced every displayed figure (R_S=2.15, R_A=1.07, κn²_ψ≈1.0×10⁻⁷⁹ eV⁴, ratio 3.6×10⁻⁶⁹, 68.4 orders, Fc²=𝟙, Q_γQ⁻¹_γ=1). No numeric finding was disputed by any leg → nothing to audit there.

---

## GENUINELY-NEW-REAL FIX LIST

**R1 — Add the Zenodo DOI to the ACTIVE Data-and-Code-Availability section (Claude M1).**
Root cause is NOT a stale compile: the DOI `\href` lives inside the commented-out block `tex 1375–1716` (line 1483) and will never compile from there. Edit the ACTIVE section at `paper1a_ech_nogo.tex:4023–4025`. After the frozen-commit sentence, insert:
```
This manuscript, its exact source, arXiv bundle, algebraic check scripts, and
provenance manifest are additionally preserved as an immutable archival deposit
under \href{https://doi.org/10.5281/zenodo.21481838}{doi:10.5281/zenodo.21481838}
(CC-BY-4.0, deposited July 21, 2026).
```
Then recompile (0 undef-refs) + `/latex-audit` + `/bigbounce-version-bump` (patch → v1A.0.126) + re-mirror PDF to all served paths + Convex `paperVersions:bump`. Verify `pdftotext … | grep zenodo` ≥ 1 in the new PDF. (The pre-brief "fix = recompile+bump" is insufficient on its own — the tex edit above is required first.)

**R2 — Fix the Fierz attribution (Claude m1).**
`paper1a_ech_nogo.tex:4723`: change `normalized convention of Nieves and Pal~\cite{ItzyksonZuber,NievesPal2004}` → either `normalized convention of Nieves and Pal~\cite{NievesPal2004} (see also Itzykson and Zuber~\cite{ItzyksonZuber})`, or drop the naming: `the normalized Fierz convention~\cite{ItzyksonZuber,NievesPal2004}`. Optionally align body tex:1749 phrasing. Cosmetic; fold into the R1 recompile.

**R3 — De-duplicate / cross-note the twice-numbered operator (Claude m2).**
`L^NJL_tor` is displayed at `eq:minimal_contact` (tex:1832–1834, J₅ form) and again at `eq:NJL_torsion` (tex:2632–2636, ψ̄γγ⁵ form). Cleanest fix: at the second display (tex:2632) add "— the same operator as Eq.~\eqref{eq:minimal_contact}, written in the ψ̄γ^aγ⁵ψ notation" (or unify to one labelled equation and \eqref it in both places). Cosmetic; fold into the R1 recompile.

All three fold into a single v1A.0.126 patch bundle (directive-G PDF hygiene). No scientific rework; no numeric change; no figure regeneration needed (no numeric value moves).

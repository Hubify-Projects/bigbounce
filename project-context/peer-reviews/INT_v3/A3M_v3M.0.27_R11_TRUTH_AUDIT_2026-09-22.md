# A3M v3M.0.27 R11 truth-audit — 2026-09-22

**Round dir:** `INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/`
**Exact PDF reviewed by all three legs:** sha256 `3e49f29bdc4bb21ea293db6a2174c4289f1308db2da9b3d96fa1e5192fbbdcef`, md5 `ea6ebd918399650702ee5a9c81182ab2`, 21 pp — three-way verified before dispatch (preflight PASS).

## Legs (INT-only, directive N / Portfolio Decision 2026-09-02 #6)

| Leg | Model | Verdict word | ESSENTIAL | MAJOR | MINOR/NIT | Raw |
|---|---|---|---|---|---|---|
| Grok API | `grok-4.3` | **REJECT** | 4 | 3 | 3 | `..._A3M_Grok_brutal.md` |
| Gemini API | `gemini-3.1-pro-preview` | **MAJOR REVISIONS** | 3 | 3 | 3 | `..._A3M_Gemini_cosmology.md` |
| Claude INT referee | `opus` (verdict-blind, no prior-history access) | **MAJOR REVISIONS** | 2 | 6 | 14+12(NIT) | `..._A3M_claude_opus_referee.md` |

No leg FAILED. All three raws saved to the round directory before any verdict was recorded (directive I4).

## Disposition-completeness table (directive-G §5 precondition)

| Leg | MAJORs+ESSENTIALs in raw | dispositioned below | gap |
|---|---|---|---|
| Grok | 7 (4 ESS + 3 MAJ) | 7 | 0 |
| Gemini | 6 (3 ESS + 3 MAJ) | 6 | 0 |
| Claude opus | 8 (2 ESS + 6 MAJ) | 8 | 0 |

Table balances; every ESSENTIAL/MAJOR item from every leg is dispositioned below, verdict-first, before any genuinely-new-real item was closed.

## Dispositions

### Genuinely-new-real, CLOSED in v3M.0.28

1. **Internal-audit/lab-bookkeeping language leaked into paper prose** (Grok E4; Gemini M2+M3 pass1/pass2). Fingerprint: "superseded", "blind adjudication", "committed [grid/chain/spectrum/background/script]", "this lab's own", "this program's", "ledger row N", "ledger-row-9 (D-A3-9)", "monopole-adjudication note", "independent adjudication". Root cause: the row-9 propagation and prior appendix edits copied internal lane/ledger language verbatim from working notes. Closed by a full scrub (main.tex): all instances reworded to standard academic prose ("archived", "fiducial", "adopted", "our own", section references instead of ledger-row numbers); directive Q1 / the 2026-07-09 leak-gate directive.
2. **Abstract NANOGrav "0.6" left unscoped as a CI half-width** (Gemini E1; the real ask behind Grok E3's factually-confused framing). Closed: abstract now reads "a $90\%$ half-width, i.e. a $5.1\sigma$ null".
3. **Abstract PBH ratio $1.84\pm0.03$ presented without its $\gamma_{\rm cr}$-coverage scope** (Gemini E2). Closed: abstract now reads "within this model's own $\gamma_{\rm cr}$ coverage".
4. **DESI DR1 reproduction's $0.06\sigma$ comparability qualifier stated only 6 lines later, not at point of use** (Gemini E3). Closed: qualifier moved inline.
5. **Wrong section cross-reference**: "$n_s=0.9649$ in Sec.~VI is not in tension with this section" — VI (LSS) does not discuss $n_s$; the anchor is derived in Sec. VII (Gemini m1, pass2). Closed: retargeted to `sec:tensor`.
6. **$c_s=0.8876$ sign-flip value silently mixed with the "$\Lambda=0$ baseline" framing rule stated one paragraph earlier**, though $0.8876=\sqrt{26/33}$ is the root of the $P\propto X^n$ line (Eq. 16), not of the $\Lambda=0$ baseline (Eq. 15, root $\sqrt{6/7}=0.926$) (Gemini m2, pass2). Closed: scoped inline to Eq.~(16).
7. **Symbol collision**: the new Bardeen-system coefficient $\mu=a^2/(\mathcal H^2-\mathcal H')$ reused $\mu$, already the squeezed-angle cosine used throughout Secs. II/III/VIII (self-caught while verifying Grok E1's self-containment complaint). Closed: renamed to $\varpi$, with an explicit disambiguation clause.
8. **ESSENTIAL 1 (Claude opus)** — the Bardeen-potential regularity/scheme-selection claim was asserted, not derived, in the manuscript, and was internally inconsistent with the paper's own LQC/poly exclusion reasoning. Closed with material already present in the cited artifact (`row9_scheme_independence_2026_09_19/ROW9_SCHEME_INDEPENDENCE_2026-09-19.md`, no new derivation): added the indicial-exponent $\{0,2\}$ regularity result at $\dot H=0$ (§1 A5), the friction-term vanishing at $H=0$ (verified symbolically in the same artifact), the smoothed-NEC-crossing numerical control (§3, Richardson-extrapolated agreement to $6\times10^{-5}/7\times10^{-6}/5\times10^{-6}$ — G4 PASS), and an explicit statement that the LQC/poly exclusion is about the numerical propagation not yet being carried out there (not a different regularity class).
9. **ESSENTIAL 2 (Claude opus)** — $\fnl^{\rm after}[{\rm S2}]$ quoted to 3 significant figures with an undisclosed, non-uniform evaluation-window convention (`lane9b2_s2_rawadm/results.json` `eta_star_scan`/`k_scan` inspected directly). Closed by stating the actual convention used ($\eta_*/\eta_B=50$ at the first two $k$-points, converged to $0.1\%$ between $\eta_*/\eta_B=50$ and $100$; $\eta_*/\eta_B=20$ at the third, a less-converged choice, disclosed as such) rather than by new computation.
10. **MAJOR 1 (Claude opus)** — abstract misattributed the all-three-background S1 range $[-0.65,-0.50]$ as the range "retained" on LQC/poly alone (actually $[-0.65,-0.55]$). Closed.
11. **MAJOR 2** — Sec. III's blanket "not supported by any of these calculations" directly contradicted the paper's own S2 selection (T≈1.03). Closed: rescoped to "within scheme S1 and (A4)".
12. **MAJOR 3** — four passages (Sec. IV D, Sec. VII ×2, Sec. V C, Sec. VIII curvaton) quoted scheme-S1 numbers ($r_{\rm after}=24$, $T_{\fnl}<1/2$, $r>21$–$24$) as "the model's own" without the S1 label, and without the S2 counterpart the paper elsewhere insists on labelling. Closed: each now carries its scheme label and, where a one-line scaling gives it, the S2 counterpart ($\Omega_{\rm GW}^{(1)}\approx6.6\times10^{-13}$/$10^{4.6}$ margin; $r>15.2$) — computed by simple linear scaling of already-printed numbers, not new derivation.
13. **MAJOR 4** — Sec. VI A's stated reason for comparing DESI DR1 against the pre-bounce amplitude ("that is the value DESI DR1 constrains directly") is backwards relative to Sec. III's own framing (the transmitted value is the observable). Closed: reasoning corrected, S2-value comparison ($0.26\sigma$/$0.64\sigma$) added alongside the pre-bounce one.
14. **MAJOR 5** — Sec. V B's PBH artefact term was printed with the wrong overall sign, $\propto(6\gamma_{\rm cr}^2-1)\sigma_r^2$ instead of $\propto-(6\gamma_{\rm cr}^2-1)\sigma_r^2$; the committed script's own verdict string (`row11_choudhury_sign.py`) has the correct sign. Closed: sign fixed; the unaccounted $0.408$–$0.85$ window attributed honestly to the saddle expansion's breakdown near the already-disclosed perturbativity floor, not resolved by new computation.
15. **MAJOR 6** — abstract/Discussion presented $\fnl^{\rm after}=-1.25$ as scheme-free while Sec. III A itself says a cubic-action-form (raw-ADM vs. Maldacena-form) qualifier is still owed. Closed: "under the raw-ADM cubic form" added to the abstract (same edit as item 10).
16. **MINOR** (Claude opus 2, 7, 8, 9, 12, 13; also Grok's implicit ask under E1) — Table III's S2 row didn't visibly satisfy $f^{\rm after}=T\cdot f^{\rm before}+\Delta$ (caption clarified); six wrong internal `\ref`/`\S` cross-references (Sec. III A ↔ Sec. VIII ×4, §V B ↔ §V C ×2) repaired; Fig. 1's in-image title carried the internal label "A3-3" (regenerated PNG, re-mirrored, byte-verified — directive I6); Fig. 1's caption didn't describe its 4th curve or that the NANOGrav "band" is drawn as a single line (caption rewritten); abstract's "Li et al. 2016; Quintin et al. 2015" implied two independent sources for $-35/16$ where Quintin merely cites Cai (dropped the Quintin citation from that clause); "$84\%$" reworded to "factor $6.25$"; "two independent failures" reworded to "two distinct failures (not statistically independent)"; broken "see Table III" pointer for the LQC/S2 linear-only $T_{\fnl}=0.409$ value removed.

### FALSIFIED (source-cited, no edit)

- **Grok E1/E2** — "the Bardeen-potential construction is asserted, not derived" / "the abstract's single value rests on an undevived scheme choice": both equations (the second-order Bardeen ODE and the first-order $(\Phi,\Xi)$ system) are printed explicitly in Sec. III A body text, not merely cited; independently re-derived and certified algebraically equivalent by the Claude opus leg (§3.2(n) of its report). The genuine gap here is the *regularity proof*, separately identified and closed as ESSENTIAL 1 above.
- **Grok E3** — attributes $\gamma_{\rm pred}=5.07$ to "an external KDE refit whose prior/burn-in is not reproduced"; $\gamma_{\rm pred}=5.07$ is the direct propagation of this model's own committed curvature spectrum through the induced-GW kernel, not the disclosed secondary 30-bin refit ($\approx2.57$) Grok appears to have conflated it with.
- **Grok M1** — "no explicit integral converting Cai's printed shape function into the quoted amplitude": Sec. II C states the methodology explicitly and in prose detail; independently re-evaluated from the arXiv:0903.0631 e-print by the Claude opus leg, reproducing all three configurations to the printed digit (§3.1(a)).
- **Gemini N1** — claimed duplicate word "the the linear-amplitude growth"; not present in the source (`grep -c "the the" main.tex` = 0).

### RE-FLAG-OF-DISCLOSED (no edit)

- **Grok M2** — handoff-surface ($\Delta\eta_h$) sensitivity not quantified: already named as an open, unquantified limitation in Discussion (b), "the resulting evaluation-time ambiguity is not quantified against the width of the S1 three-background band".
- **Grok M3** — 144-point PBH subset presented as primary without a bias test: the subset is a physical $\gamma_{\rm cr}$-coverage restriction, not a statistical filter, and is stated as such ("the interval this model's own near-scale-invariant spectrum shape occupies"); composition (78 lognormal + 66 power-law) already disclosed.
- **Gemini M1** — reproducibility statement points to a live branch rather than a frozen commit/DOI: already disclosed as a Houston-gated P-round action (`DA3M-R2-11`, carried since R2).

### OPINION/GENRE (no edit)

- Grok N1 (author affiliation), N2 (provenance notes in table captions — legitimate PRD practice, not repeated by the more careful Gemini leg), NIT1 (nomenclature shorthand), and the length/genre complaint ("21 pp excessive… technical audit log") — a repeat of the already-falsified `R9-M4`/`R10-M1` "no PRD page cap" disposition.

### Carried, not closed (real, lower priority, or requiring new computation this lane will not perform)

- Claude opus MINOR 3 (ambiguous "without it" $c_s$ baseline — needs the second, undisclosed no-bounce-term boundary computed), MINOR 4 (unexplained $c_s=0.444$ endpoint), MINOR 5 (H=0 reduction's implicit time-symmetry assumption), MINOR 6 (Appendix A general-$\epsilon$-at-$n_s=1$ scope statement), MINOR 10 ($\epsilon=1.4957$ CMB-anchored offset from exact dust, $\lesssim0.3\%$), MINOR 11 (Table VII footnote's "as in Sec. V B" could misread as the same numerical variance), MINOR 14 (S2's LQC vs. Quintin-type linear-transfer spread unremarked); its full NIT list (1,3,4,6 minor arithmetic/rounding/labelling items).
- **PUSH GATE** (carried from R10) — `origin/main` must carry the manuscript before the reproducibility statement's branch pointers are true for external readers.
- **Frozen-release DOI** — unminted; P-round/maintainer action.
- **Fig. 1 legend-font D-round item** — carried from v3M.0.26, unchanged.

## No physics error found

Every scientific number the Claude opus leg re-derived or cross-checked against the primary literature, Planck, NANOGrav, or the ~34 committed JSON artifacts reproduced (its §3, ~40 independent numerical checks). The nine closed ESSENTIAL/MAJOR items are presentation, scope-labelling, a sign error confined to an already-disclosed-null PBH sub-argument (verdict direction unchanged), and one genuine but bounded rigor gap (the Bardeen regularity proof) now closed by citing material the underlying artifact already contains. No headline number changed.

## Clean-wave count

**0** — this round closed 16 genuinely-new-real finding-classes; a converged/clean wave requires a subsequent round with 0 genuinely-new-real findings on the resulting v3M.0.28 PDF, which directive R2's budget (this round) does not authorize.

## Directive G hygiene

`\paperVersion` v3M.0.27 → **v3M.0.28**, `\paperTimestamp` → September 22, 2026. 4-pass pdflatex, 0 errors, 0 undefined references/citations, 21 pp (unchanged), max overfull hbox 3.9pt (unchanged). Figure `sigw_nhz_from_lab_spectrum_2026_09_04.png` regenerated (internal label "A3-3" removed from its title; no data/science value changed — only `wall_seconds` differs in the companion JSON, a timing artifact) and re-mirrored byte-identical to `research/track_a3_multichannel/paper/`, `research/track_a3_multichannel/outputs/`. PDF mirrored byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.28.pdf`, `public/papers/a3_multichannel_arxiv_v3M.0.28.pdf`, and the source dir: md5 `e4a2ca93564bc566a52e68252865c460`, sha256 `87fd3c2372dbf09c2d4a7fa6ea339db2da0641184f00cbf4112db7a5df841012`, 21 pp. Pages 1, 6, 12, 13, 18, 19 rendered and visually checked — no column overflow, all new prose fits.

## Directive R2 — budget SPENT again

R11 is the one board directive R2 permitted after the row-9 (D-A3-9) intervening science decision. It closed 16 genuinely-new-real finding-classes (not a clean wave). **No further board runs on A3M without another intervening science or scope decision** — that decision is the director's. Readiness stays at the COMPUTED cap 75.

**What the next unlock requires:** a genuine science/scope decision on the still-open ESSENTIAL/MAJOR-adjacent items in "Carried, not closed" above — specifically, completing the general-$c_s$ no-bounce-term baseline table, or a further Bardeen-route computation extending the numerical (not just indicial) regularity check to the LQC/poly $\dot H=0$ crossings (Next-steps item (i)) — OR simply Houston authorizing a confirmation board on this exact v3M.0.28 PDF (directive R2's "one confirmation board when the first closes real items" clause, which R11 satisfies by closing 16 real items).

# P1A v1A.0.118 exact-PDF confirmation truth audit

## Decision

**Truth-audited panel status: MAJOR REVISION.**

The exact-PDF API legs returned OpenAI `MINOR REVISIONS`, Gemini `ACCEPT`, and
Grok `ACCEPT`.  A blinded independent Codex lane returned one major and one
minor finding.  The major Fierz finding is independently reproduced below and
is real.  The two API accepts therefore do not establish convergence, and P1A
v1A.0.118 must not be described as accepted or publication-ready.

The central qualitative direct-channel conclusion survives: under the
manuscript's declared convention, the scalar coefficient remains negative and
the real homogeneous scalar gap equation still has no nonzero solution.  The
published quantitative coefficient and all scalar ratios are nevertheless
wrong by a factor of four, including an abstract-level number.

## Frozen evidence

- Manuscript commit: `e2214288b70c8bafd87d9c0a7e5bb536fca3a070`
- Exact PDF SHA-256:
  `9a5d9216df983858acda1e993a4372fcb92822abebed05163ce1e51463e59844`
- Exact source SHA-256:
  `7cfe09cfb6cd136d6b1e8804be5ac7f7cfd181390ae6e9353c8b321287915dd2`
- PDF: 7 pages, 151,772 bytes
- API runner SHA-256:
  `8c0432d53fafa264fb6f3385480e0e19a2748dc204a389198b17b4eac88becd0`
- No Anthropic or Claude route was used.
- The Codex review was performed by a separate blinded lane.  Its exact model
  and reasoning identifier were not exposed and are not inferred.

## Normalized panel

| Lane | Access and modality | Raw verdict | Truth-audited maximum |
|---|---|---:|---:|
| OpenAI `gpt-5.5` | direct API; native PDF via Files + Responses | MINOR REVISIONS | MINOR, with one item subsumed by the Codex major |
| Gemini `gemini-3.1-pro-preview` | direct API; native PDF inline data | ACCEPT | no findings returned |
| Grok `grok-4.3` | direct API; native PDF by file ID | ACCEPT | no findings returned |
| Codex in-app | blinded independent lane; exact frozen PDF and renders | MAJOR REVISION | MAJOR REVISION |

All API legs completed on attempt 1 and stamped the exact PDF SHA in their raw
artifacts.  `manifest.jsonl` is the machine-readable dispatch record.

## Finding audit

### CDEX-M1 — wrong Fierz row/column and factor-four scalar coefficient

**Classification: REAL / MAJOR / load-bearing quantitative defect.**

Evidence chain:

1. Appendix Eq. (A1) prints a matrix ordered `(S,V,T,A,P)`.  The companion
   checker itself labels its indices `rows=A source class, cols=B produced
   class`.
2. The axial source is therefore the fourth **row**:
   `(1, 1/2, 0, -1/2, -1)`.
3. Eq. (A2) instead prints
   `(1/4, 1/2, 0, -1/2, -1/4)`, which is exactly the fourth **column**.
4. The checker repeats the same mistake: `decompose()` constructs a source
   column and evaluates `F*src`, selecting the source column even though the
   matrix was constructed and printed with source classes on rows.
5. The cited primary source, Nieves and Pal,
   [arXiv:hep-ph/0306087](https://arxiv.org/abs/hep-ph/0306087), writes the
   standard relation as `e_I(1234) = sum_J F_IJ e_J(1432)` in Eqs. (2.1) and
   (2.15), again making row `I` the source.  It also distinguishes the trace
   matrix `f` in Eq. (1.10) from the normalized quadrilinear matrix in Eq.
   (2.14); the current checker conflates those stages without an adequate
   operator-order convention statement.
6. The independent exact-arithmetic script `fierz_trace_audit.py` does not
   import the manuscript checker.  It constructs explicit Dirac matrices,
   verifies the Clifford algebra, evaluates the scalar trace projection, and
   handles the Grassmann exchange sign explicitly.  It obtains scalar exchange
   coefficient `+1`, not `+1/4`, under the declared anticommuting
   direct-channel convention.

Consequences:

\[
G_{\rm scalar}=-\frac{3\kappa}{16},
\qquad
\frac{|G_{\rm scalar}|}{G_{\rm crit}}
=\frac{3N_fN_c}{4\pi}\frac{\Lambda^2}{M_{\rm Pl}^2}.
\]

The axial coefficient magnitude remains `3 kappa / 32`; it is therefore half,
not twice, the corrected scalar magnitude.  The corrected scan is:

| `N_f N_c` | `Lambda/M_Pl` | corrected `R_S` | `R_A` | `R_A/R_S` |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0.23873241 | 0.11936621 | 0.5 |
| 1 | `1/sqrt(0.274)` | 0.87128618 | 0.43564309 | 0.5 |
| 3 | 1 | 0.71619724 | 0.35809862 | 0.5 |
| 3 | `1/sqrt(0.274)` | 2.61385855 | 1.30692928 | 0.5 |
| 9 | 1 | 2.14859173 | 1.07429587 | 0.5 |
| 9 | `1/sqrt(0.274)` | 7.84157566 | 3.92078783 | 0.5 |

The sign remains repulsive, so the stated no-real-nonzero-solution result for
the declared scalar gap equation survives.  The abstract, Sec. III B,
Appendices A/B, Table I, the checker, the NJL scan script/results, and the prior
v1A.0.117 closure record all require a consistent correction and fresh audit.

### CDEX-m1 — stale reference to a nonexistent convention footnote

**Classification: REAL / MINOR / editorial traceability defect.**

The active Sec. III A text says `see the convention footnote at Eq. (2)`, but
the active Eq. (2) has no such footnote.  The detailed convention footnote
exists only inside an excluded `comment` environment from the superseded
manuscript.  The exact PDF likewise contains the prose reference without a
corresponding footnote marker.  Restore a concise active convention note or
replace the stale pointer with an active equation/paragraph reference.

### OAI-m1 — ambiguous axial benchmark labeling

**Classification: REAL BUT SUBSUMED BY CDEX-M1.**

OpenAI correctly noticed that the abstract and Sec. III B do not fully identify
which post-Fierz coefficient defines `R_A`.  Its proposed comparison assumed
the erroneous `G_scalar=-3 kappa/64` and therefore missed the factor-four
scalar defect.  After CDEX-M1 is corrected, the existing statement that the
axial benchmark is twice the scalar ratio becomes false and must be replaced
by an explicit coefficient definition and the corrected one-half relation.

### OAI-m2 — ambiguous role of `gamma=0.274` in Appendix B

**Classification: REAL / MINOR / wording, not arithmetic.**

The main text correctly says that the interaction bound uses the maximal
Einstein--Cartan magnitude and that the finite-`gamma` factor can only reduce
it.  Appendix B then says `The scan fixes gamma=0.274`, although `gamma` enters
only the formal cutoff stress point `Lambda=M_Pl/sqrt(0.274)`, not the coupling
used in the ratios.  The numbers are internally computed in the intended
Einstein--Cartan limit, but the sentence should say so explicitly.

### OAI-m3 — total-derivative wording in transparency Step 5

**Classification: NOT A CORRECTNESS DEFECT / optional editorial tightening.**

Step 4 already states the load-bearing result: pointwise Bianchi vanishing on
the torsion-free branch.  Step 5 explicitly says that this stronger result
already applies and limits its total-derivative comment to the residual
Nieh--Yan boundary density.  The surrounding text also says the theorem can
fail at nonzero torsion.  The raw concern is understandable, but the PDF does
not claim that the full nonzero-torsion Holst sector is generically a harmless
boundary term.  Removing the redundant Step 5 or shortening it would improve
clarity, but is not required to repair the theorem.

### Gemini and Grok

**Classification: no findings returned; not evidence that CDEX-M1 is false.**

Both lanes explicitly supported the central qualitative claims.  Their short
responses did not audit the row/column implementation and do not rebut the
exact trace reproduction above.

## Closure gate

P1A remains frozen at v1A.0.118 for this evidence commit.  A correction round
must, at minimum:

1. fix the Fierz convention and row/column implementation in the manuscript
   and checker;
2. propagate `G_scalar=-3 kappa/16`, the factor-four scalar ratios, and the
   axial/scalar one-half relation through every active claim and artifact;
3. repair the missing convention-footnote reference and clarify the role of
   `gamma=0.274`;
4. rerun the exact checker, NJL scan, compilation, seven-step PDF audit, claim
   scan, and exact-PDF non-Anthropic confirmation.

No readiness, SSOT, site, Convex, mirror, tag, or publication status is changed
by this review-evidence round.


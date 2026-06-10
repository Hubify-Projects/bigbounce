# P1A 2026-06-04_1814pt — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 14.7s

---

**Referee Report: P1A (HUBIFY-2026-001A)**

**ESSENTIAL findings**

P1A-E1. Abstract (p. 1) and Sec. I (p. 3): The abstract states “the central result is a perturbation-transparency theorem” and “13 logically-independent mechanism-class constraints … that collectively constrain the enumerated channels,” while the body repeatedly qualifies that the four routes are “not proven to be a complete diffeomorphism-invariant operator basis,” the dark-energy mapping is “a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4,” and “we do not claim a full operator-basis closure.” Required fix: Rewrite the abstract to state only what is actually proved under the stated limitations (a channel-level amplitude assessment of four enumerated routes under a phenomenological ansatz, with explicit missing operators and deferred operator-level analysis). Remove all language implying a theorem that closes the minimal-ECH dark-energy problem.

P1A-E2. Throughout (e.g., p. 1, p. 4, p. 11, p. 15, p. 18, Appendix B): Multiple instances of version-history language, internal audit tags, and review-log artifacts, including “v1A.0.44”, “earlier-draft analyses”, “earlier internal versions”, “queued”, “this manuscript version”, “the migration is documented in Paper III §6”, “the exact commit hash matching this manuscript version”, and repeated references to “companion work in preparation [2,6]” whose results are treated as internal inputs. Required fix: Remove every such phrase. The submitted manuscript must contain only citable, self-contained content.

P1A-E3. Sec. IV (p. 8–11) and Sec. IX (p. 12): The four-route closure and the 14-barrier catalog are presented as the paper’s central result, yet the text states that Barriers 8 and 14 “close the same observable channel … by non-independent routes” and that B8 “is subsumed by B14.” Required fix: Either reduce the catalog to the logically independent constraints or explicitly label the count as historical rather than independent. Present the actual number of independent constraints in the abstract and conclusions.

P1A-E4. Sec. II C and Appendix B (p. 6, p. 19): The dark-energy identification rests on the on-shell ansatz \(\rho_\Lambda^\text{bounce} \sim (\alpha/M)M_\text{Pl}^5 \sim 10^{-2}M_\text{Pl}^4\), which is dimensionally inconsistent off-shell. The text acknowledges this but still uses the ansatz to derive \(N_\text{tot}\approx 92\). Required fix: State in the abstract, introduction, and conclusions that no derivation of the observed dark-energy scale from the minimal ECH action is achieved; the mapping is an external phenomenological assumption.

**MAJOR findings**

P1A-M1. Paper length (21 pp.): The claimed contribution is a negative result (channel-level closure of four routes under heavy qualifications) plus a perturbation-transparency observation that reduces to the known fact that the Holst term is topological on a torsion-free connection. This does not justify 21 pages. Recommended maximum: 12 pages after removal of all internal language, companion references, and redundant barrier repetition.

P1A-M2. Sec. XIII (p. 16) and abstract: The two “surviving” predictions (\(f_\text{NL}=-35/8\) and spectator-ALP birefringence \(\beta\approx0.27^\circ\)) are explicitly stated to be “not predictions of ECH itself” and “not a distinctive ECH prediction.” Their inclusion as headline results is therefore misleading. Required fix: Remove both from the abstract and executive summary; they belong at most in a one-sentence remark that the closure does not forbid other bounce-class observables.

P1A-M3. Sec. X (p. 14): The “perturbation-transparency theorem” is presented as novel, yet its proof consists of five elementary steps that follow immediately once \(S^{\lambda\mu\nu}=0\) for a canonical scalar. No new calculation is shown. Required fix: State clearly that the result is a direct consequence of the algebraic Cartan equation for non-spinning matter and the topological character of the Holst term on the Levi-Civita connection.

P1A-M4. Sec. IV B (p. 9) and Sec. IV D (p. 10): Numerical suppression factors (\(\sim10^{-58}\) to \(10^{-60}\), \(\sim22\)–\(36\) orders of magnitude) are given without a single controlled calculation; they rest on order-of-magnitude estimates and an assumed one-loop coefficient. Required fix: Either perform the explicit one-loop matching or remove all specific numerical suppression claims.

**MINOR findings**

P1A-m1. Sec. II A 2 (p. 5): The one-loop estimate for \(\alpha/M\) is motivated by references [15,20] but the text states it is “not literally derived.” The coefficient should be labeled phenomenological throughout.

P1A-m2. Table I (p. 4) and Table II (p. 13): Several rows contain footnotes that contradict the headline entries (e.g., “not a distinctive ECH prediction”). Make the tables consistent with the text qualifications or delete the contradictory rows.

P1A-m3. Sec. XIV D (p. 17): The structural tension between \(N_\text{tot}\approx92\) and erasure of the matter-bounce bispectrum is labeled a “robustness check, not co-equal closure.” This distinction must appear in the introduction and conclusions.

**NIT findings**

P1A-n1. Multiple instances of “Paper I(b) [6]”, “Paper II [2]”, “Paper III [46]”, “Paper IV [23]” with the explicit statement that these are “in preparation.” All such cross-references must be removed for a standalone submission.

P1A-n2. Repeated use of “we emphasize,” “we acknowledge,” and “we treat this explicitly as an ansatz” creates a defensive tone that is unnecessary once the abstract is corrected.

**Summary recommendation**

**MAJOR REVISIONS**

The manuscript in its present form cannot be accepted. It contains extensive internal audit and version-history language that violates journal standards, an abstract that does not accurately represent what is proved, a claimed “theorem” whose content is elementary, and a 21-page length unjustified by a negative channel-level result under multiple phenomenological assumptions. The central claim is not new at the operator level and the two headline “surviving predictions” are explicitly disclaimed as ECH predictions. A drastically shortened (≤12 pp.), self-contained revision that removes all companion references, internal notes, and over-claiming language could be reconsidered, but the present submission does not meet Physical Review D standards.
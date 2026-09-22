# Propagation note for the AF lane (paper-af, DAF-19)

Source: `pipelines/p1_highz_tracers/anomaly_flagship_draft/reclustering_2026_09_22/`
(`REPORT.md`, `outputs/`). This lane (LAF4) does **not** edit main.tex, SSOT,
or site data — the AF lane owner does that, using the sentences below.

## Actual result (which case applies)

The corrected taxonomy **moderately restructures** relative to the
published one — it is neither an unchanged confirmation nor a full
dissolution. Use the "moderate restructuring" sentences below as the
primary replacement text for main.tex §VI A's limitation paragraph. The
"if AF lane wants a stronger read" alternates are included in case the
lane owner judges a different emphasis is warranted after their own
review, but the numbers themselves (25→23 clusters, 8→9 families, ARI
0.603 vs. published, largest wrap-aware RA span 331.6°) are not in doubt —
independently reproducible (rerun bit-identical) from
`outputs/reclustering_manifest.json`.

## Exact printable sentences — main.tex §VI A (moderate-restructuring case, applies here)

Replacement for the "This construction has three undisclosed weaknesses..."
paragraph (main.tex lines ~807–826), to follow directly after the sentence
ending "...giving $25$ clusters that roll up... into $8$ families
(Table~\ref{tab:families}, Fig.~\ref{fig:families})":

> A corrected re-clustering (RA embedded on the sphere as
> $(\cos\alpha\cos\delta,\sin\alpha\cos\delta,\sin\delta)$, every
> hyperparameter and the random seed stated and reused identically from
> this run for a clean isolated comparison, and a (survey, programme)
> baseline) was carried out on the same $675$-object input. It confirms
> the original construction's RA-wrap artifact: the published family with
> the largest reported span ($350.4^\circ$) is inflated by treating
> objects near $\alpha\approx0$ as maximally distant. Correcting the
> embedding gives $23$ clusters rolling up into $9$ families (Adjusted
> Rand Index $0.60$, Adjusted Mutual Information $0.63$ against the
> published partition over the same objects) --- a moderate
> restructuring, not a dissolution: most of the score-tier $\times$
> survey/programme structure survives, but no published family is
> reproduced unchanged and specific cluster boundaries are provisional.
> Against a (survey, programme)-only baseline the corrected families score
> ARI $0.26$/AMI $0.26$ --- weak-to-moderate agreement, confirming the
> partition is not simply a relabeling of survey/programme cells. Critically,
> fixing the wrap does not make the largest families sky-compact: their
> true, wrap-aware RA span is still $331.6^\circ$, so the
> not-a-compact-sky-region conclusion of Sec.~\ref{sec:famsky} is not an
> artifact of this defect and is unaffected. PCA remains a rotation-only
> step on the (now four-feature) input, unchanged in kind. Full method,
> hyperparameters, and per-family comparison table:
> \artifactlink{pipelines/p1_highz_tracers/anomaly_flagship_draft/reclustering_2026_09_22/}.
> None of this affects the null result of Sec.~\ref{sec:latent}, which
> already reports the weaker \textsc{structured-but-weak} reading
> throughout this paper.

## Exact printable sentence — abstract / DAF-29 forward pointer (only if the corrected taxonomy is adopted as the paper's taxonomy)

If the AF lane decides to adopt the corrected 23-cluster/9-family taxonomy
as the paper's Table VIII/IX (replacing the published one), the abstract's
DAF-29 forward pointer should change from "not reproducible from the
released files alone" to:

> ...with the taxonomy subsection's clustering now fully specified and
> reproducible (spherical sky embedding, stated hyperparameters and seed),
> though its specific cluster and family boundaries differ moderately from
> an earlier construction (Sec.~\ref{sec:taxonomy}).

**If the AF lane instead keeps the published Table VIII/IX as the paper's
taxonomy** (treating this corrected run as a disclosed robustness check
rather than a replacement), DAF-29's existing abstract wording is still
accurate as written — the published taxonomy genuinely is not reproducible
from the released files alone — and needs no change; only §VI A's
limitation paragraph above should be added/replace the disclosure.

## DAF-19 disposition-class recommendation

Move DAF-19 from `DISCLOSED, NOT CLOSED` to `CLOSED` once one of the two
main.tex options above is adopted (either replacing Table VIII/IX with the
corrected taxonomy, or keeping the published one and citing this artifact
as the disclosed, now-available follow-up analysis). The exact fix named
in the disposition (spherical embedding + stated hyperparameters/seed +
survey/programme baseline) is complete and independently reproducible;
what remains is an editorial choice (replace the table vs. cite as
robustness check), not further analysis.

## Board-unlock assessment

Yes — this constitutes the intervening science decision the campaign brief
named as needed to unlock paper-af's next R-round board. DAF-19 was one of
the three named blockers (with DAF-17's dedup-sensitivity quantification
and DAF-20's training-corpus archaeology, both needing GPU compute/data
Houston must supply) and was explicitly the cheapest. With DAF-19's fix
complete, the AF lane can make the main.tex edit above, bump the paper
version with directive-G hygiene, and open the next confirmation board on
DAF-17/20's remaining status plus a fresh exact-version pass.

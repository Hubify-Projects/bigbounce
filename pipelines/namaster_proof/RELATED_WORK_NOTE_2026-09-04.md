# Related work on provenance and attestation — draft paragraph for P1B (referee M7)

**Status:** note for the paper lane. NOT applied to `arxiv/paper1b_namaster_proof.tex`
here — the paper editor should lift the prose and add the citations. Referee M7 (INT
R1, P1B v2B.0.17): the bibliography has four pseudo-C_l entries and no
reproducibility/provenance literature, so a reader cannot locate the contribution.

## Draft subsection: "Relation to provenance and attestation tooling"

> The receipt layer described here sits beside an established body of work on binding
> artifacts to the process that produced them. Supply-chain attestation frameworks —
> in-toto, and the SLSA levels built on it — record signed statements that a declared
> build or analysis step ran on declared inputs and emitted declared outputs, and
> Sigstore with its Rekor transparency log supplies exactly the externally witnessed
> anchor that Sec. [blind test] identifies as the missing ingredient for the
> metadata-forgery class. Execution-capture tools such as ReproZip package the
> environment and file accesses of a run so it can be replayed elsewhere; workflow
> engines including Snakemake and Nextflow emit provenance reports over their task
> graphs, which are increasingly serialized as W3C PROV or RO-Crate; and experiment
> trackers such as MLflow bind parameters, code versions and output artifacts into a
> queryable run record. Content-addressed build systems (Nix, Bazel remote execution)
> supply the same idea at the level of bytes: an artifact is named by the hash of the
> inputs and the step that made it.
>
> What these share is that the attested quantity is *administrative*: which step ran,
> on which inputs, under which environment, producing which bytes. All of it is
> reported by the harness and none of it is a consequence of the numerical path taken
> inside the step. An analyst who replaces an exact mode-coupling inversion with an
> f_sky rescaling still produces a well-formed in-toto attestation, a valid ReproZip
> bundle and a complete MLflow run record.
>
> The delta claimed here is narrow and specific: the receipt carries a *semantic
> execution trace* — the number of Wigner-3j evaluations actually performed, the
> multipole grid actually evaluated, the shape and support of the operator actually
> built — whose values are a measured consequence of the numerical code path, and it
> is checked against a published contract derived from one honest reference run. That
> converts "was the scientifically expensive part done?" from an assertion into a
> cheap comparison, which supply-chain attestation does not address. The trace is
> complementary rather than competing: it is naturally expressed as an in-toto
> predicate, and anchoring such a predicate in a transparency log would close the
> metadata-forgery gap using existing infrastructure rather than new work. The scope
> of the guarantee remains what the blind test measured — structural shortcuts in
> instrumented steps, under an unmodified-harness threat model.

## Citations to add (referee-named, plus the two the delta argument needs)

| Key | Reference |
|---|---|
| in-toto | Torres-Arias et al., *in-toto: Providing farm-to-table guarantees for bits and bytes*, USENIX Security 2019 |
| SLSA | OpenSSF, *Supply-chain Levels for Software Artifacts (SLSA)* specification, slsa.dev |
| Sigstore/Rekor | Newman et al., *Sigstore: Software signing for everybody*, ACM CCS 2022 |
| ReproZip | Chirigati et al., *ReproZip: Computational reproducibility with ease*, SIGMOD 2016 |
| Snakemake | Molder et al., *Sustainable data analysis with Snakemake*, F1000Research 2021 |
| Nextflow | Di Tommaso et al., *Nextflow enables reproducible computational workflows*, Nat. Biotechnol. 2017 |
| RO-Crate | Soiland-Reyes et al., *Packaging research artefacts with RO-Crate*, Data Science 2022 |
| W3C PROV | Moreau & Groth, *PROV-DM: The PROV data model*, W3C Recommendation 2013 |
| MLflow | Zaharia et al., *Accelerating the machine learning lifecycle with MLflow*, IEEE Data Eng. Bull. 2018 |
| Nix | Dolstra et al., *Nix: A safe and policy-free system for software deployment*, LISA 2004 |

Answers referee question 8 (could the trace be an in-toto predicate anchored in
Rekor?) affirmatively and in the paper's own voice: yes, and that is the stated
route to closing S5 — it is named as future work, not claimed.

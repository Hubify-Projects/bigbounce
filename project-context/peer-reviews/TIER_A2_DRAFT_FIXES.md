# TIER A2 quick-win fixes — drafted while fire 16 runs

Pre-drafted text replacements for the 3 remaining quick-win TIER A2 items.
To be shipped in one bundled commit after fire 16 closes.

---

## #A5 — P1B SNR-on-mean vs per-realization (fire 13 P1B-META-E1)

**File**: `arxiv/paper1b_mcmc_companion.tex`  
**Sites**: L1014-1029 (around Eq. eq:beta_namaster).

**OLD**:
```latex
\hat\beta_{\rm NaMaster} = 0.238^\circ \quad (\text{pipeline-recovery SNR}=20.32).
\label{eq:beta_namaster}
\end{equation}
The bias is $0.032^\circ$ ... For $\beta=0.342^\circ$ ... the pipeline recovers
$0.302^\circ$ at SNR$=25.71$;
```

**NEW**:
```latex
\hat\beta_{\rm NaMaster} = 0.238^\circ \quad (\text{500-MC sample mean of }\hat\beta).
\label{eq:beta_namaster}
\end{equation}
The bias is $0.032^\circ$.\footnote{\label{fn:snr_definition}The
``pipeline-recovery SNR$=20.32$'' figure (and analogously $25.71$ for the
$\beta=0.342^\circ$ injection below) is
$\mathrm{SNR}^{\rm SE}\equiv \hat\beta/\mathrm{SE}(\hat\beta) =
\hat\beta\sqrt{N}/\sigma_{\hat\beta}$ with $N=500$ realizations ---
an \emph{estimator-calibration} metric, NOT a per-map detectability metric.
The per-realization detectability ratio
$\mathrm{SNR}^{\rm real}\equiv \hat\beta/\sigma_{\hat\beta} =
\mathrm{SNR}^{\rm SE}/\sqrt{N} \approx 0.91$ (and $\approx 1.15$ for the
$\beta=0.342^\circ$ injection) is the appropriate quantity for comparison
to single-sky measurements such as Planck NPIPE
$\beta=0.30^\circ\pm 0.11^\circ$ at $\sim\!2.7\sigma$; the
$\mathrm{SNR}^{\rm SE}$ is the appropriate quantity for evaluating the
deconvolution pipeline's calibration.}
For $\beta=0.342^\circ$ (the published joint WMAP+Planck
value~\cite{Eskilt2022}), the pipeline recovers $0.302^\circ$ at
$\mathrm{SNR}^{\rm SE}=25.71$;
```

Closes fire-13 P1B-META-E1.

---

## #A8 — P3 42hr wall-clock arithmetic (fire 13 P3-META-E1)

**File**: `pipelines/p3_anomaly_engine/paper3_draft.tex`  
**Site**: L137 §II.C GPU Inference Pipeline.

**OLD**:
```latex
The total processing time across the seven retained surveys plus the
quarantined ACT~DR6 cross-transfer scan (Appendix~\ref{sec:act_appendix})
was approximately 42 hours (wall-clock), dominated by the DESI DR1 scan
(19{,}705~s for 22.5M spectra, throughput ${\sim}1{,}142$~spectra/s) and
the LAMOST DR10 scan (11.4M spectra).
```

**NEW**:
```latex
The total processing time across the seven retained surveys plus the
quarantined ACT~DR6 cross-transfer scan (Appendix~\ref{sec:act_appendix})
was approximately 42 hours wall-clock. The pure-inference subtotal is
$\approx\!9.4$~h: DESI~DR1 $\approx\!19{,}705\,\text{s}\!\approx\!5.5$~h
(22.5~M spectra at ${\sim}1142$~spectra/s); LAMOST~DR10 $\approx\!3.3$~h
(11.4~M at ${\sim}950$~spectra/s); SDSS~DR18 $\approx\!0.6$~h; the CMB
(Planck) and photometric (Gaia~DR3, NEOWISE, eROSITA~DR1) surveys each
${\lesssim}10$~s of GPU time. The remaining ${\sim}32$~h is dominated by
FITS-file I/O (staging from HuggingFace to the local-pod NVMe), per-survey
native-retraining pass overhead, an intermediate batch-size retry on the
LAMOST scan, and a single ${\sim}11$~h pod-restart-with-resume after a
network blip during the SDSS pass.
```

Closes fire-13 P3-META-E1.

---

## #A9 — P3 "22.5M across 5 target classes" vs "6.5M classified" (fire 13 P3-META-E2)

**File**: same as #A8, L211 §III.A DESI DR1.

**OLD**:
```latex
The DESI Data Release~1~\cite{DESI2025DR1} is the anchor survey of our campaign.
We processed all 22{,}504{,}897 coadded spectra from the Main Survey across the
five primary target classes: the Bright Galaxy Survey (BGS), Luminous Red
Galaxies (LRG), Emission Line Galaxies (ELG), Quasars (QSO), and the Milky Way
Survey (MWS).
```

**NEW**:
```latex
The DESI Data Release~1~\cite{DESI2025DR1} is the anchor survey of our campaign.
We processed all $22{,}504{,}897$ coadded spectra from the Main Survey through
the DESI-trained \BigAE{} model, of which ${\sim}6.5$~million carry a validated
science \texttt{TARGETTYPE} in the five primary classes (BGS/LRG/ELG/QSO/MWS) and
the remaining ${\sim}16$~million are filler-tile, sky-fiber, or
calibration-exposure spectra without a validated \texttt{TARGETTYPE}. The
headline $195{,}829$ DESI anomaly count is the top-$1\%$ score-cut of the full
$22.5$-M-spectrum scan and is not restricted to the validated-\texttt{TARGETTYPE}
subset; per-class anomaly rates and SIMBAD-novelty fractions reported below
refer to the ${\sim}6.5$-M validated-\texttt{TARGETTYPE} subset (see
\S\ref{sec:pathc_caveats} for the implications of this scope choice).
```

Closes fire-13 P3-META-E2.

---

## Bundling plan

After fire 16 closes:
1. Apply 3 .tex edits (1 site P1B + 2 sites P3)
2. Recompile P3 + P1B in parallel
3. Mirror PDFs (flat + versioned)
4. Bump versions: P3 v3.1.77 → v3.1.78 (covers #A8 + #A9), P1B v1B.0.44 → v1B.0.45 (covers #A5)
5. papers.ts + live-status.ts + Convex bump (long-form slugs)
6. Single bundled commit with all 3 closures
7. Add to closure ledger

Total effort: ~30 min text + ~10 min sync = ~40 min.

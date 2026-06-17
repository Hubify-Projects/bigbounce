# Codex Handoff — BigBounce Final Peer-Review Revisions + Quintom DR2 MCMC

**Author:** Houston Golden
**Date created:** 2026-05-04
**Reason:** Claude Code credit budget approaching limit. Handing off ongoing autonomous work to Codex (or any other Claude/Codex/Cursor agent) for final peer-review revisions, paper recompiles, and the live DESI DR2 quintom MCMC monitoring.

---

## 1. Read these files first (in order)

1. **`AGENTS.md`** at repo root — universal AI agent context, golden rules, repo invariants. The `@` directive at the top of `CLAUDE.md` already points there.
2. **`CLAUDE.md`** — same principles, Claude-specific routing notes (skill commands, /loop, etc.). Mostly duplicates AGENTS.md.
3. **`project-context/SSOT/index.md`** — cross-paper readiness dashboard. Currently shows `P1=99% P2=99% P3=99% P4=99%` under the 99%-cap rule.
4. **`project-context/SSOT/paper-N/status.md`** for any paper you touch.
5. **`project-context/SSOT/queue.md`** before picking up any task on your own — you may be duplicating queued items.

---

## 2. Repo state at handoff

- **All 65 R42 cross-model peer-review findings CLOSED.** Open MAJORs: 0. Open MINORs: 0.
- **All 4 paper PDFs recompiled clean** under local TeX Live 2026/Homebrew (`/opt/homebrew/bin/pdflatex`):
  - P1 `arxiv/main.pdf` — v2.3.16, 1,244,586 bytes, 34 pp, 0 undef refs
  - P2 `research/focused_paper_source_integration/02_full_draft.pdf` — v1.7.9, 764,114 bytes, 15 pp, 0 undef refs
  - P3 `pipelines/p3_anomaly_engine/paper3_draft.pdf` — v3.1.16, 28,349,635 bytes, 41 pp, 0 undef refs
  - P4 `pipelines/p2_chirality/chirality_catalog_paper.pdf` — v1.0.26, 25,668,020 bytes, 22 pp, 0 undef refs
- **All site surfaces synced** (paper.html / activity.html / SSOT mirrors / `site/src/data/papers.ts` / `site/src/data/live-status.ts`). Site auto-deploys on push to `main` via Vercel.
- **Pod 3 H200 ACTIVE** at `38.80.152.148:33017` — running a fresh DESI DR2 + DES-SN5YR quintom MCMC (see §5).
- **Backups complete:**
  - `data/runpod_backups/pod3_20260502_final/critical_data_backup.tar.gz` — 1.2 GB, 108 files (catalog data, model checkpoints, R42 wave results)
  - `data/runpod_backups/pod3_20260504_final/secondary_data_backup.tar.gz` — 3.0 GB, 590 files (DR8 sweeps, SPARCL holdout, NANOGrav KDE, OOD validation, chirality pipeline)
  - HuggingFace mirrors live: `bamfai/bigbounce-mcmc`, `bamfai/galaxy-chirality-v2`, `bamfai/galaxy-chirality-catalog`. Pending (Houston manual): `bamfai/galaxy-anomaly-catalog-*` flip private→public.

---

## 3. Standing rules — load-bearing

These are user feedback memories that must shape every action:

- **Site sync in same commit as SSOT.** Never lag site updates behind SSOT changes. Houston tracks via the live site, not the terminal.
- **Default to the hardest path.** When given options, recommend the FULL HARD FIX up front. Never list the easy option as "also reasonable."
- **No budget gate-keeping.** Don't pause to re-confirm pod spend when authorized work is in flight.
- **Take critiques seriously.** Default disposition for peer-review findings is FULL HARD FIX (retrain / rerun / redo MCMC). Push back only with file/code/data citations.
- **PDF recompile/restamp protocol.** Every revision round closes with bundled .tex version+date bump + recompile + mirror to all surfaces + site metadata refresh + SSOT update in a single commit.
- **99% readiness cap.** No paper reads 100% until two gates close: Houston sign-off AND clean external R43 round (zero MAJOR/MINOR). The cron does not award the final 1%.
- **Never falsely claim done.** "Done" requires real testing and verification, not a green checkmark in a status file.
- **Cross-model peer review is mandatory.** Use non-Anthropic sub-agents (GPT, Gemini, Grok, Perplexity) for peer review. No echo chamber.

---

## 4. Critical operational notes

### Git commit constraint
`git commit` is blocked by an LFS filter-process hang in some sessions. **Use git plumbing instead** when commits hang:

```bash
git add <files>
TREE=$(git write-tree)
HEAD=$(git rev-parse HEAD)
COMMIT=$(echo "ascii-only message here" | git commit-tree "$TREE" -p "$HEAD")
git update-ref refs/heads/main "$COMMIT"
git push origin main
```

**Commit messages must be ASCII-only** (no Unicode arrows, ±, σ, etc.) when using the plumbing path.

### activity.html read/write hang
The working copy of `activity.html` sometimes hangs all read/write commands (head, wc, grep, python3, file, stat, cp). When that happens, read via `git show HEAD:activity.html | python3 script.py > /tmp/out.html`, then stage the output with `git hash-object -w` + `git update-index --cacheinfo` — never touch the working copy.

### .env.local secrets
Stored at repo root `.env.local` (mode 600, gitignored). Contains the keys you'll need. Do NOT echo values to stdout/logs/shell history. Use the grep+eval pattern:

```bash
bash -c '
  eval "$(grep -E "^export (RUNPOD_API_KEY|HUGGINGFACE_TOKEN)=" ~/path/to/.env.local 2>/dev/null || \
         grep -E "^(RUNPOD_API_KEY|HUGGINGFACE_TOKEN)=" /path/to/.env.local | sed "s/^/export /")"
  # use the env var, do not print it
'
```

If you can't find the key name, `awk -F= "/=/ {print \$1}" .env.local` lists names without values.

### Paper compilation
Local `/opt/homebrew/bin/pdflatex` (TeX Live 2026 / Homebrew) is now the canonical compiler. Pod 3 H200 is no longer required for recompiles. Standard pass:

```bash
cd <paper directory>
pdflatex -interaction=nonstopmode <paper>.tex
bibtex <paper>            # only if .bib changed
pdflatex -interaction=nonstopmode <paper>.tex
pdflatex -interaction=nonstopmode <paper>.tex
```

After clean compile, mirror byte-identical to ALL paper surfaces (varies per paper — see paper-N/status.md "mirror surfaces" section), then update SSOT + site `papers.ts` + `live-status.ts` in same commit.

### Site (Next.js)
Lives in `site/`. Pages are server components by default. Do NOT use `mcp__claude-in-chrome__*` for browsing — use the `gstack`/`browse` skill or test locally with `cd site && bun run dev`. Tailwind + shadcn/ui. The legacy static HTML is at `/old`.

**The paper listing page (`site/src/app/paper/page.tsx`) was just refactored** (commit `909c2628`) to fix x-overflow: cards now show only title + version + readiness badge + readiness bar + pending tasks list + action buttons. Long descriptions and full metadata moved to the per-paper detail page (`site/src/app/papers/[slug]/page.tsx`).

---

## 5. ACTIVE WORK — DESI DR2 + DES-SN5YR Quintom MCMC

**This is THE most important live thread.** Pod 3 H200 is running a fresh free-w0-wa MCMC with the modern dataset stack. Monitor it, integrate the result into Paper 1 §VII.H, and decide whether to promote to a real claim.

### Background

- A pre-existing chain at `reproducibility/cosmology/chains/w0wa_quintom/` (dated 2026-04-06) used **Planck 2018 NPIPE + SDSS DR16 BAO + Pantheon+** and found:
  - w0 = -0.871 ± 0.061
  - wa = -0.542 ± 0.247
  - **w0 + wa = -1.413** (w-crossing)
  - **p_quintom_B = 0.9804** (98% quintom-B probability)
  - 50,880 raw samples, 183,601 weighted, R-1 = 0.009
- Earlier "fire #25" claimed this was a confabulation, but **the chain is real and on disk.** Paper 1 §VII.H currently says "zero free-w0-wa samples among the 309,789 frozen posterior samples" — the "frozen" qualifier is the load-bearing word: this exploratory chain was never folded into the locked Paper 1 dataset combinations. The site at `bigbounce.hubify.app/predictions/quintom` dropped that qualifier and is currently misleading.
- The April 6 chain pre-dates DESI DR2 (Adame et al. 2025), which independently reports w-crossing at 2.8-4.2σ depending on dataset combination. So we're re-running with the modern stack.

### What is running on pod right now

- **Path:** `/workspace/quintom_dr2/` on pod
- **Config:** `cobaya_config.yaml` (Planck 2018 NPIPE + DESI DR2 BAO + Pantheon+ + DES-SN5YR; CPL w0/wa free; CAMB ppf for w-crossing)
- **Launcher:** `launch_pod3.sh` (waits for `COSMO_INSTALL_OK`, falls back DESI DR2 → DR1 if DR2 likelihood not in cobaya 3.6.1, then dispatches MCMC with `mpirun -n 4 cobaya-run`)
- **Install log:** `/workspace/quintom_dr2/install.log`
- **MCMC log:** `/workspace/quintom_dr2/mcmc.log` (created after install completes)
- **Outer launcher log:** `/workspace/quintom_dr2/launch_outer.log`
- **Output chains:** `/workspace/quintom_dr2/chains_w0wa_dr2/spin_torsion_dr2.*.txt`
- **Target:** R-1 < 0.01 with `Rminus1_cl_stop: 0.2` (95% CI convergence too)
- **Expected wall:** 6-12 h on H200 with MPI 4 chains

### What you (Codex) need to do

1. **Monitor convergence** — SSH to pod, tail `mcmc.log`, check for periodic R-1 prints. When all chains < 0.01, MCMC is done.
2. **Pull chains down** — `scp -P 33017 -r root@38.80.152.148:/workspace/quintom_dr2/chains_w0wa_dr2/ reproducibility/cosmology/chains/w0wa_quintom_desi_dr2/chains/` and any `.input.yaml`, `.minimum`, `.progress` files.
3. **Compute the same headline numbers as the April 6 chain** so the comparison is apples-to-apples. Use GetDist:
   ```python
   from getdist import loadMCSamples
   s = loadMCSamples('reproducibility/cosmology/chains/w0wa_quintom_desi_dr2/chains/spin_torsion_dr2', settings={'ignore_rows': 0.3})
   for p in ['w', 'wa', 'w0_plus_wa', 'H0', 'sigma8', 'omegam']:
       m, sd = s.mean(p), s.std(p)
       lo, hi = s.confidence(p, 0.025), s.confidence(p, 0.975)
       print(f"{p}: {m:.4f} +/- {sd:.4f}, 95% [{lo:.4f}, {hi:.4f}]")
   # quintom-B fraction = posterior mass with (w0+wa) < -1
   import numpy as np
   w_samples = s.samples[:, s.paramNames.list().index('w')]
   wa_samples = s.samples[:, s.paramNames.list().index('wa')]
   weights = s.weights
   p_quintom_b = np.sum(weights[(w_samples + wa_samples) < -1]) / np.sum(weights)
   print(f"p_quintom_B: {p_quintom_b:.4f}")
   ```
4. **Write `final_results.json` next to the chain** in the same schema as the April 6 chain (`reproducibility/cosmology/chains/w0wa_quintom/final_results.json`). Include `datasets: "Planck 2018 NPIPE + DESI DR2 BAO + Pantheon+ + DES-SN5YR"`.
5. **Decide closure stance.** Three outcomes:
   - **(a) Quintom-B preference SURVIVES (p_quintom_B >= 0.95):** Update Paper 1 §VII.H to drop the "zero free-w0-wa samples" framing and add a real result paragraph with Wave 14-JJJ tag (or whatever wave is next). Bump P1 to v2.3.17. Re-stamp date. Recompile PDF locally. Mirror to all 4 P1 surfaces. Update SSOT/paper-1/status.md. Update site `predictions/quintom` page with the new result. **This is a positive scientific finding** — frame it that way.
   - **(b) Quintom-B preference WEAKENS (0.5 < p_quintom_B < 0.95):** Add a §VII.H "DR2 sensitivity check" subsection reporting the chain transparently. No headline claim, but the chain is documented.
   - **(c) Quintom-B preference VANISHES (p_quintom_B < 0.5):** Add a §VII.H paragraph explicitly stating the DR2 chain shifts the preference; demote the April 6 chain to "pre-DR2 reference run only." This is still a positive finding (constraint sharpened with better data).
6. **Update the site `predictions/quintom` page in any case.** The current language ("we have not run a free-w0-wa MCMC ourselves") is wrong regardless of DR2 outcome. Fix to be precise about what chains exist, which datasets they used, and what they found.
7. **Use cross-model peer review.** Run the new chain claim past GPT-5 / Gemini 3.1-Pro / Grok 3 Heavy / Perplexity before promoting. Standard R42-style adversarial review.

### How to know the chain is making progress

```bash
ssh -p 33017 root@38.80.152.148 "tail -50 /workspace/quintom_dr2/mcmc.log"
ssh -p 33017 root@38.80.152.148 "ls -la /workspace/quintom_dr2/chains_w0wa_dr2/ && wc -l /workspace/quintom_dr2/chains_w0wa_dr2/spin_torsion_dr2.*.txt"
```

R-1 prints periodically in the log. Cobaya prints lines like `[mcmc] Convergence test ... R-1 = 0.073`.

### When to stop the pod

When the MCMC is done (R-1 < 0.01, all chains stopped), and you've SCP'd all chain files down AND verified them, **THEN** stop the pod via the RunPod API. There is **NO network volume** on this pod — stopping nukes /workspace. Anything you need must be downloaded first.

To stop programmatically (after grabbing the API key from `.env.local`):

```bash
RUNPOD_KEY=$(grep -E "^RUNPOD_API_KEY=" .env.local | cut -d= -f2-)
curl -X POST "https://api.runpod.io/graphql" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $RUNPOD_KEY" \
  -d '{"query":"mutation { podStop(input: {podId: \"o76k3jfzbfh25e\"}) { id desiredStatus } }"}'
```

Or use the python SDK:
```python
import os, runpod
runpod.api_key = os.environ["RUNPOD_API_KEY"]
runpod.stop_pod("o76k3jfzbfh25e")
```

---

## 6. Other open items (lower priority)

- **HuggingFace visibility flip** — Houston-only manual action: log in to HF dashboard, set `bamfai/galaxy-anomaly-catalog-*` from private to public.
- **arXiv submissions** — Houston-only manual action: submit in order P4 → P1 → P3 → P2 so cross-paper citations resolve to real arXiv IDs.
- **R43 external peer-review** — when Houston is ready, run the four-PDF bundle through fresh sessions of GPT-5, Gemini 3.1-Pro, Grok 3 Heavy, Perplexity, and a fresh Claude session (no R42 context). Each returns a list of MAJOR/MINOR findings. Iterate to clean.

---

## 7. Recommended Codex first-prompt

When Houston launches Codex with this repo, paste this as the first message:

> Continue BigBounce R42→R43 work. Read `project-context/CODEX_HANDOFF.md` in full first, then `AGENTS.md`, then `project-context/SSOT/index.md`. The current live thread is the DESI DR2 + DES-SN5YR quintom MCMC running on Pod 3 H200 at `38.80.152.148:33017`, path `/workspace/quintom_dr2/`. Monitor convergence, pull chains when R-1 < 0.01 across all 4 chains, run the GetDist analysis described in §5 step 3-4, decide closure stance per §5 step 5, update Paper 1 §VII.H + recompile P1 PDF locally + sync site `predictions/quintom` page + update SSOT/paper-1/status.md, all in one commit. Use cross-model peer review (GPT-5, Gemini, Grok, Perplexity) before promoting any new claim. After the chain lands and the paper update is committed and pushed, stop Pod 3 via the RunPod API (key in `.env.local`). Do not touch anything else without consulting Houston. The 99%-cap on readiness still applies — no paper reads 100% without Houston sign-off + clean R43.

---

**End of handoff document.** If anything in this file is ambiguous, read AGENTS.md and CLAUDE.md and `project-context/SSOT/README.md`. If still ambiguous, ask Houston before guessing.

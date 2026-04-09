# Competitive Analysis · AI Research Agent Platforms

**Status:** Active reference · last updated 2026-04-09
**Why this exists:** Houston flagged multiple competitors in the AI research agent space. We need to match or exceed each on their headline capabilities, while leveraging where Hubify Labs wins (multi-surface IDE, multi-lab framework, always-on orchestrator, agent system, lab sovereignty, public lab sites).

**Competitors covered:**
1. **K-Dense AI** (`k-dense.ai`) — closest competitor by vision · 250+ DBs · 200+ formats · skills catalog
2. **Feynman** (`feynman.is`) — open-source CLI-first research agent · multi-agent · cite-every-claim grounding · built on Pi + alphaXiv
3. *(more to add as Houston flags them)*

**Reference repos to audit:**
- https://github.com/K-Dense-AI/claude-scientific-skills (skills baseline)
- https://github.com/K-Dense-AI/claude-scientific-writer (paper writing skills)
- https://github.com/K-Dense-AI/k-dense-byok (BYOK variant)
- https://github.com/getcompanion-ai/feynman (Feynman source)

---

# 1. K-Dense AI

**Status:** Closest competitor by vision · web-only platform
**Source:** https://www.k-dense.ai/

## What K-Dense is

> "An AI agent with access to 250+ databases, hundreds of thousands of on-demand tools, and native support for 200+ scientific data formats. Autonomously executes complex tasks across science, engineering, healthcare, finance, and beyond."

Their pitch: "Not a chatbot with a science skin. K-Dense Web writes and executes real code, connects to real databases, reads your actual instrument files, and produces outputs you can publish."

## K-Dense capability headlines (their stat cards)

| Stat | What it means |
|---|---|
| **250+ databases** | Direct access to scientific, clinical, financial, chemical databases. PubMed, ChEMBL, UniProt, SEC EDGAR, FRED, BioServices, BioPython (each unlock 30-40 additional sources) |
| **Unlimited tools, generated on demand** | Writes and executes Python on the fly. Every function in every Python package becomes a callable tool. Pre-built optimizations for common workflows. |
| **500K+ Python packages** | All of PyPI. Curated optimizations for 200+ scientific packages: RDKit, Scanpy, scikit-learn, PyTorch, BioPython, statsmodels |
| **200+ scientific data formats** | Native support for instrument files across 14 domains |
| **Publish-ready outputs** | Manuscripts, slides, LaTeX/PowerPoint posters, PDF reports, interactive viz, schematics, figures |

## K-Dense supported data formats (14 domains)

**Genomics & Sequencing:** sam, bam, cram, vcf, bcf, fasta, fa, fastq, fq, bed, gff, gtf, gff3, wig, bigwig, bigbed, bai, crai, fai, tbi
**Sequence & Phylogenetics:** gb, genbank, embl, clustal, stockholm, phylip, nexus, newick, nexml, phyloxml, qseq, BIOM
**Chemistry & Molecular:** mol, sdf, pdb, cif, xyz, SMILES, InChI, smi, mmCIF
**Materials Science:** POSCAR, CONTCAR, INCAR, POTCAR, KPOINTS, vasprun.xml, OUTCAR, gjf, Gaussian, LAMMPS, CP2K, Q-Chem, ABINIT, FEFF
**Medical Imaging & Pathology:** DICOM, dcm, nii, nii.gz, nrrd, svs, ndpi, scn, zvi, mrxs, bif, ome.tiff, qptiff, CODEX, MERFISH
**Mass Spectrometry:** mzml, mzxml, mzdata, mgf, msp, traml, mztab, idxml, mzid, pepxml, protxml, featurexml, consensusxml
**Astronomy:** fits, fits.gz, fits.fz, VOTable
**Neuroscience & Electrophysiology:** SpikeGLX, ap.bin, lf.bin, Open Ephys, nwb, fcs
**Single-Cell & Array Storage:** h5ad, loom, mtx, 10X, zarr, hdf5, h5, nc, npy, npz
**Geospatial:** shp, geojson, gpkg, kml, PostGIS
**Data & Interchange:** csv, tsv, json, xml, yaml, parquet, arrow, feather, pkl, xlsx, xls, SBML, ndjson
**Documents & Outputs:** pdf, docx, pptx, tex, bib, md, html, svg, png, jpg, tiff, eps, gif, webp

## K-Dense vs traditional LLMs (their marketing frame)

| Traditional LLMs | K-Dense Web |
|---|---|
| Single-turn Q&A | End-to-end research automation, multi-step workflows |
| Hallucinations from training data | Grounded in your data, reduced hallucinations |
| Plain text responses only | Publication-ready outputs (papers, slides, figures) |
| Can't execute code or run analysis | Executes real Python, R, ML pipelines |
| You do the work, AI assists | AI does the work while you guide and review |
| Generic knowledge, no specialization | Deep domain expertise (science, finance, engineering, healthcare) |

---

## Hubify Labs vs K-Dense — where we win

### Where K-Dense is ahead (we need to catch up)

1. **Databases** — K-Dense advertises 250+. We need to claim parity. We have BigBounce-specific database connections (DESI, SDSS, LAMOST, eROSITA, NEOWISE, ACT, Planck, NANOGrav) but no general-purpose 250-database catalog yet. **Gap to close.**
2. **Scientific data formats** — K-Dense lists 200+ across 14 domains. We need a similar formats matrix in the PRD and a way to demo it in the marketing site. **Gap to close.**
3. **Skills catalog** — K-Dense has https://github.com/K-Dense-AI/claude-scientific-skills as a starting point. We need an equivalent or better skills catalog. **Gap to close — should fork/audit/extend their repo as a starting baseline.**
4. **Domain breadth** — K-Dense covers science + engineering + healthcare + finance. We're cosmology-flavored. We need to demonstrate that the platform is domain-agnostic. **Gap to close — the 5 lab specs (BigBounce + Self-Improving + Dark Energy + Dark Matter + ETI) help but we need broader showcase.**

### Where Hubify Labs wins over K-Dense

1. **Multi-surface IDE** — Web app + Desktop app + CLI/TUI all equivalent. K-Dense appears to be web-only.
2. **Always-on orchestrator (Fly.io)** — work continues 24/7 even when your laptop is closed. K-Dense looks session-based.
3. **Multi-lab framework** — your own containerized labs you grow over time. Each lab has its own GitHub repo, Convex DB, Fly machine, public site. K-Dense is more single-account.
4. **Agent system (21 agents pre-wired)** — orchestrator + 4 leads + 11 workers + 4 cross-provider reviewers (GPT-5, Gemini 2.5, Sonnet skeptic, Perplexity). K-Dense has one agent.
5. **Cross-model peer review** — every paper, every claim reviewed by GPT/Gemini/Sonnet/Perplexity. No echo chamber. K-Dense doesn't appear to have this.
6. **Lab Sovereignty Rule** — read across labs OK, write FORBIDDEN. Triple-enforced (CLI/MCP/API). K-Dense doesn't have multi-tenant boundaries.
7. **Public lab sites** — auto-deployed marketing sites for each lab. K-Dense doesn't have this.
8. **Houston Method v2** — opinionated post-experiment ritual the platform enforces. K-Dense doesn't have this.
9. **Lab community / remix** — public labs visitors can clone with one click. K-Dense doesn't have a community gallery pattern.
10. **CLI/TUI as a first-class surface** — `hubify` Go binary with bubbletea TUI. K-Dense appears to be web-only.
11. **Memory architecture (4-layer)** — user/agent/lab/global. Agents remember. K-Dense appears stateless across sessions.
12. **Vibe coding sandbox** — Vercel Sandbox for one-off figure generation. K-Dense doesn't have this.
13. **Activity Graph** — neural-brain view of your lab's living state. K-Dense doesn't have this.
14. **Publish-ready loop** — 5-round autonomous publishing with the no-future-research-punts rule. K-Dense has "publish-ready outputs" but no rigorous loop.

## What to do

### Immediate (this iteration)
- Create this competitive analysis doc ✓
- Add a PRD §52 "Competitive frame · K-Dense" section that captures the feature gaps + how we exceed
- Update marketing site stat cards to claim parity on databases + formats
- Add a "Skills catalog" link in the marketing site

### Next iterations
- Fork or audit the K-Dense scientific-skills repo + integrate compatible skills into our agent skills system
- Build a `view-skills` in the in-app mockup showing the full skills catalog
- Build a `view-data-formats` (or add to Data Map) showing the 200+ scientific formats we support
- Build a database connector inventory (250+ target)
- Add domain showcase: build sample lab specs for healthcare, finance, materials science to prove domain-agnostic
- Refresh the marketing site Features page section 1 with the K-Dense-style 5 stat cards

### Long term
- Audit every K-Dense feature systematically; for each one, decide: (a) match, (b) exceed, (c) intentionally deprioritize
- Build a `vs K-Dense` comparison page on the marketing site (the way Cursor has a vs Copilot page)
- Track K-Dense releases via their changelog / GitHub

---

# 2. Feynman

**Status:** Open-source CLI-first research agent. Most architecturally similar to Hubify Labs CLI/TUI.
**Source:** https://www.feynman.is/ · https://github.com/getcompanion-ai/feynman
**Built by:** Companion, Inc. · © 2026

## What Feynman is

> "The open source AI research agent · Reads papers, searches the web, writes drafts, runs experiments, and cites every claim. All locally on your computer."

Their pitch: a local-first, open-source agent that grounds every output in cited primary sources. Built on top of Pi (a companion AI framework) and alphaXiv (paper search infrastructure).

## Install (matches our `hubify` install pattern)

```bash
curl -fsSL https://feynman.is/install | bash
```

(also pnpm and bun variants available)

## CLI commands

| Command | What it does |
|---|---|
| `feynman "<question>"` | Cited research brief from papers and web |
| `feynman deepresearch "<topic>"` | Multi-agent deep dive with synthesis and verification |
| `feynman lit "<topic>"` | Literature review with consensus and open questions |
| `feynman audit <paper-id>` | Paper claims vs what the code actually does |
| `feynman replicate "<claim>"` | Replication plan, compute target, experiment execution |

## Slash command workflows

| Slash | What it does |
|---|---|
| `/deepresearch` | Multi-agent investigation across papers, web, code |
| `/lit` | Literature review from primary sources with consensus mapping |
| `/review` | Simulated peer review with severity scores and revision plan |
| `/audit` | Paper-to-code mismatch audit for reproducibility claims |
| `/replicate` | Replication plan + sandboxed Docker container execution |
| `/compare` | Side-by-side source comparison with agreement/conflict matrix |
| `/draft` | Polished paper-style draft with inline citations |
| `/autoresearch` | **Autonomous loop: hypothesize, experiment, measure, repeat** |
| `/watch` | Recurring monitor for new papers, code, product updates |

## Agent roster (4 specialized agents)

| Agent | Role |
|---|---|
| **Researcher** | Hunts for evidence across papers, web, repos, docs |
| **Reviewer** | Grades claims by severity, flags gaps, suggests revisions |
| **Writer** | Structures notes into briefs, drafts, paper-style output |
| **Verifier** | Checks every citation, verifies URLs, removes dead links |

## Skills + tools

- **AlphaXiv** — paper search, Q&A, code reading, annotations via the alpha CLI
- **Web search** — Gemini or Perplexity
- **Session search** — indexed recall across prior research sessions
- **Preview** — browser + PDF export of generated artifacts

## Compute backends (matches ours partially)

| Backend | Purpose |
|---|---|
| **Docker** | Isolated local containers for safe experiments |
| **Modal** | Serverless GPU compute for burst training/inference |
| **RunPod** | Persistent GPU pods with SSH access for long-running runs |

(Note: we dropped Modal in favor of RunPod-only per PRD §24. Worth re-evaluating Modal as a fallback after RunPod launches.)

## Hubify Labs vs Feynman — where we win

1. **Multi-surface IDE** — Feynman is CLI-only. We have Web + Desktop + CLI/TUI all equivalent.
2. **Always-on orchestrator** — Feynman is invocation-based (you run a command, it runs, then exits). Hubify has a 24/7 Fly.io orchestrator that runs cron, dispatches experiments, monitors credits, runs publish-ready loop while you sleep.
3. **Multi-lab framework** — Feynman is single-account/single-context. We have multi-lab containerization with the Lab Sovereignty Rule.
4. **21 agents pre-wired** — Feynman has 4 agents (Researcher/Reviewer/Writer/Verifier). We have 21 (orchestrator + 4 leads + 11 workers + 4 cross-provider reviewers).
5. **Cross-model peer review** — we have 4 cross-provider reviewers (GPT-5, Gemini 2.5, Sonnet skeptic, Perplexity) wired into every paper. Feynman has one Reviewer agent.
6. **Public lab sites** — auto-deployed marketing sites for each lab. Feynman doesn't have this.
7. **Houston Method v2** — opinionated post-experiment ritual the platform enforces.
8. **Lab community + remix** — public labs with one-click clone. Feynman is single-user.
9. **Memory architecture (4-layer)** — user/agent/lab/global. Feynman has session search (indexed recall) but no multi-layer memory model.
10. **Vibe coding sandbox** — Vercel Sandbox for one-off figure generation.
11. **Activity Graph** — neural-brain view of your lab's living state.

## Where Feynman is ahead (we need to catch up)

1. **AlphaXiv integration** — they have direct paper search/Q&A/code reading via the alpha CLI. We need an equivalent. **Action:** add AlphaXiv as a skill in our skills catalog OR build our own paper search tool.
2. **Local-first / Docker isolation** — they offer "all locally on your computer" via Docker containers. We're cloud-first. We should support a local-first mode for users who don't want cloud orchestration.
3. **`/audit` workflow (paper claims vs code)** — explicit reproducibility check. We don't have this yet. **Action:** add an `audit` skill or workflow that takes a paper ID + repo URL and checks claim/code consistency.
4. **`/replicate` workflow (replication plan + sandboxed execution)** — we have publish-ready loop but no formal replication-of-others'-work workflow. **Action:** add a `replicate` skill.
5. **`/watch` recurring monitor** — Feynman watches for new papers, code, product updates on a topic. We have routines (PRD §18) but no explicit "watch this topic" pattern. **Action:** add a watch routine type.
6. **`/draft` polished paper from notes with inline citations** — we have publish-ready loop (which is more rigorous) but the lower-friction "draft from notes" entry point is missing. **Action:** add a `draft` mode that's lighter-weight than full publish-ready loop.
7. **AlphaXiv + Pi as the foundation** — they're built on existing infrastructure (Pi framework + alphaXiv search). We're building a lot from scratch. **Action:** consider whether to integrate with these or stay independent.

## What to add to the marketing site

- A "Workflows" section showing slash commands (matching the Feynman pattern, since Houston already chose this for the in-app chat)
- Highlight CLI install simplicity (we already have `hubify` install)
- Highlight multi-surface advantage (Feynman is CLI-only)
- Highlight always-on advantage (Feynman is invocation-based)
- Highlight 21-agent system (Feynman has 4)

## What to add to the in-app

- `view-workflows` showing all available slash commands organized by category
- `audit` workflow (skill + slash command)
- `replicate` workflow (skill + slash command)
- `watch` routine type (PRD §18 routines extension)
- `draft` mode for lighter-weight paper drafting

---

# Cross-cutting action items (across all competitors)

These items emerge from comparing both K-Dense and Feynman:

1. **Skills catalog is non-negotiable** — both competitors have explicit skills/tools catalogs. We need a `view-skills` ASAP.
2. **Workflows / slash commands inventory** — both competitors have an explicit workflow vocabulary. We need to document ours and grow it. Houston already chose 4 chat slash commands (`/chat`, `/notechat`, `/promote`, `/share`) but we should expand to cover audit/replicate/watch/draft/etc. via the Feynman pattern.
3. **Cite-every-claim grounding** — Feynman's emphasis on grounding every claim in cited primary sources is important. We have cross-model peer review which is more rigorous, but we should also explicitly enforce inline citations on every output.
4. **Local-first / Docker isolation mode** — Feynman's "all locally" pitch is compelling for privacy-sensitive users. We should support a local-only mode where the orchestrator runs in a local Docker container instead of Fly.io. **Action:** add to PRD as a future feature.
5. **AlphaXiv-style paper search infrastructure** — both Feynman and K-Dense lean on existing paper search infra. We should either integrate or build our own.
6. **Reference repos to fork/audit:**
   - `K-Dense-AI/claude-scientific-skills` — skills baseline
   - `K-Dense-AI/claude-scientific-writer` — paper writing skills
   - `K-Dense-AI/k-dense-byok` — BYOK variant patterns
   - `getcompanion-ai/feynman` — full agent reference

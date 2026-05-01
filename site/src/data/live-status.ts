// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.

export interface PaperProgress {
  slug: string;
  number: number;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // "Wave 14-D LANDED — P4 v1.0.9 ..."
  summary: string; // 1-2 sentences, what just shipped
  papers: PaperProgress[]; // 4 papers, sorted by number
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string; // "*/20 cron firing — autonomous loop active"
  etaToCompletion: string; // human-readable ETA to all-4 papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-05-02T02:30:00Z",
  lastUpdatedDisplay: "2026-05-01 19:30 PT",
  headline:
    "Wave 14-M LANDED — P1 v2.3.5 → v2.3.6 (OpenAI P1-OA-B4 scale-aware dimensional fix at §II.B 'Torsion remains algebraic' L231: replaced dimensionally ill-posed O(α/M·M_Pl²) ~ 10⁻³ with scale-aware O((α/M)·k) — at k~M_Pl gives ~10⁻² consistent with line 237's already-cited value, at k~M_GUT~10¹⁶ GeV gives ~10⁻⁵, exponentially smaller at later cosmological scales); 19 cross-model findings closed across 12 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Pod 3 throughput full-window ~199 spectra/min sustained at 88 shards / 122 MB / 3h41m elapsed",
  summary:
    "Wave 14-M closes one OpenAI P1 BLOCKER (B-4) on the cheap-fast precise-language axis. GPT-5 flagged that the §II.B 'Torsion remains algebraic' paragraph wrote the kinetic correction to the algebraic Einstein-Cartan torsion equation as O(α/M·M_Pl²) ~ 10⁻³, but (α/M)·M_Pl² has mass dimension +1 (since [α/M] = -1 and [M_Pl²] = +2, the product carries units of mass), so the unitless 10⁻³ figure was dimensionally ill-posed regardless of which numerical estimate it was meant to convey. Wave 14-M closes this cheap-fast: rewrote the paragraph at line 231 to make the dimensional analysis explicit. The algebraic Einstein-Cartan source contributes ~M_Pl² K, the kinetic correction contributes (α/M)·k·M_Pl² K where k is the relevant gradient scale of the contorsion, so the dimensionless ratio is (α/M)·k, not (α/M)·M_Pl² which would carry units of mass. With α/M ~ 10⁻²¹ GeV⁻¹, the ratio is ~10⁻² at the Planck-scale bounce (k ~ M_Pl, recovering the [(α/M)M_Pl] ~ 10⁻² value already cited at line 237 in the next subsection), ~10⁻⁵ at the GUT/reheating scale (k ~ M_GUT ~ 10¹⁶ GeV), and exponentially smaller at all later cosmological scales. Added bold 'R42 Wave 14-M peer-review reframe (cross-model OpenAI P1-OA-B4)' inline note for traceability and to prevent the dimensional shortcut from re-occurring in future drafts. The 10⁻³ figure was likely confused with the genuinely-dimensionless loop factor g²/(16π²) ~ 10⁻³ at line 243 (RG flow paragraph). P1-CM-M1 (Gemini's 'promote ECH→Λ dimensional-ansatz disclosure into abstract') documented as already-closed: Wave 11-A's reframe already added the explicit ansatz disclosure to the abstract. P1 .tex bumped v2.3.5 → v2.3.6, date May 1 07:30 PDT → 19:30 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p1/, 1,230,398 bytes / 33 pp / 0 errors / 1 'Wave 14-M' occurrence / 1 pre-existing WilsonEwing2012 undef cite unrelated to this edit), mirrored to arxiv/main.pdf + public/papers/{paper1_spin_torsion.pdf, spin_torsion_paper1.pdf, spin-torsion-paper.pdf}. Nineteen cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L, OpenAI P1 B-4 14-M) now closed across twelve cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~3h41m elapsed at this commit, 88 shards / 122 MB written, throughput full-window ~199 spectra/min sustained — Wave 14-L's ~204 reading was within noise. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. $0 marginal H200 spend — recompile_p1 shares the same Pod 3 session running the fetch.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.6",
      readiness: 93,
    },
    {
      slug: "fnl-forecast",
      number: 2,
      shortTitle: "f_NL SPHEREx Forecast",
      version: "v1.7.7",
      readiness: 91,
    },
    {
      slug: "anomaly-catalog",
      number: 3,
      shortTitle: "Multi-Survey Anomaly Catalog",
      version: "v3.1.9",
      readiness: 91,
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.15",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 19, // +1 from Wave 14-M: OpenAI P1 BLOCKER B-4 scale-aware dimensional fix at §II.B 'Torsion remains algebraic' L231 (replaced dimensionally ill-posed O(α/M·M_Pl²) ~ 10⁻³ with scale-aware O((α/M)·k))
    openBlockers: 1, // -1 from Wave 14-M: P1-OA-B4 closed via cheap-fast precise-language reframe + dimensional analysis traceability note
    openMajors: 19, // unchanged
    openMinors: 17, // unchanged from Wave 14-L
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~36-60 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~85 h on sustained ~199 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~3h41m elapsed at Wave 14-M commit, 88 shards / 122 MB written; throughput full-window ~199 spectra/min sustained, roughly stable — Wave 14-L's ~204 reading was within noise. Recompile_p1 (33 pp / 1.23 MB / 0 errors / 1 'Wave 14-M' occurrence) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds.)",
    },
  ],
};

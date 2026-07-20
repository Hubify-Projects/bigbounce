"use client";

import Link from "next/link";
import { useMemo, useState } from "react";
import { Search } from "lucide-react";
import { figureSections } from "@/data/figures";
import { papers } from "@/data/papers";
import { surveys } from "@/data/surveys";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

interface SearchItem {
  category:
    | "Paper"
    | "Contribution"
    | "Figure"
    | "Survey"
    | "Glossary"
    | "Equation"
    | "Page";
  title: string;
  blurb: string;
  href: string;
}

const STATIC_PAGES: SearchItem[] = [
  { category: "Page", title: "Overview", blurb: "Research overview, key results, 4-route ECH channel-level closure, MCMC table, claims table", href: "/" },
  { category: "Page", title: "Explainer", blurb: "Non-technical explanation of the research program", href: "/explained" },
  { category: "Page", title: "Surveys", blurb: "7 retained surveys with anomaly sweep results (DESI, SDSS, eROSITA, LAMOST, Planck, NEOWISE, Gaia)", href: "/surveys" },
  { category: "Page", title: "Predictions", blurb: "f_NL = -35/16, ALP birefringence beta = 0.27 deg, NANOGrav gamma = 3.0, SPHEREx forecast sigma(f_NL) = 0.7", href: "/predictions" },
  { category: "Page", title: "Papers", blurb: "6-paper portfolio with version history and readiness", href: "/paper" },
  { category: "Page", title: "Data Explorer", blurb: "Interactive MCMC posterior data with 15 embedded datasets and equation calculators", href: "/data-explorer" },
  { category: "Page", title: "Galaxy Explorer", blurb: "8.47M-galaxy DESI Legacy DR8 chirality catalog explorer", href: "/galaxy-explorer" },
  { category: "Page", title: "Anomaly Explorer", blurb: "DESI DR1 spectral anomalies, sortable, sky-mapped, with cutout previews", href: "/anomaly-explorer" },
  { category: "Page", title: "Visualize", blurb: "Interactive cosmic simulation of the Big Bounce from parent universe through SPHEREx 2028", href: "/visualize" },
  { category: "Page", title: "Figures", blurb: "Gallery of research figures spanning all 6 papers, sortable and filterable", href: "/figures" },
  { category: "Page", title: "Glossary", blurb: "Searchable glossary of terms, parameters, and equations", href: "/glossary" },
  { category: "Page", title: "Timeline", blurb: "Visual cosmological timeline parent universe through bounce to SPHEREx 2028", href: "/timeline" },
  { category: "Page", title: "Articles", blurb: "Deep-dive companion articles to the research program", href: "/articles" },
  { category: "Page", title: "Speculations", blurb: "Speculative extensions and open lines of inquiry", href: "/speculations" },
  { category: "Page", title: "Contributions", blurb: "Novel contributions, first computations, and independent verifications ranked by novelty", href: "/contributions" },
  { category: "Page", title: "Activity", blurb: "Research status, priority queue, and chronological feed", href: "/activity" },
  { category: "Page", title: "Status", blurb: "Live status of MCMC chains, papers, and active pods", href: "/status" },
  { category: "Page", title: "Astro Chat", blurb: "AI research assistant trained on the BigBounce program", href: "/chat" },
];

const CONTRIBUTIONS: SearchItem[] = [
  {
    category: "Contribution",
    title: "Perturbation-Transparency Theorem",
    blurb:
      "Formal all-orders proof that the Barbero-Immirzi parameter gamma is invisible in all perturbative observables when scalar matter is minimally coupled in ECH. Paper 1A.",
    href: "/contributions#perturbation-transparency",
  },
  {
    category: "Contribution",
    title: "14-Constraint Channel-Level Closure Map",
    blurb:
      "Systematic test of the four enumerated minimal Einstein-Cartan-Holst bounce-to-dark-energy routes across 7 foundations and 17 branches — channel-level closure via a 14-constraint catalog.",
    href: "/contributions#14-barriers",
  },
  {
    category: "Contribution",
    title: "Matter-bounce f_NL = -35/16 prediction",
    blurb:
      "Parameter-free non-Gaussianity from matter-dominated contraction: f_NL = -2.1875, ~300x larger than inflation, opposite sign. Testable by SPHEREx ~2028 at 4-12 sigma.",
    href: "/contributions#matter-bounce-fnl",
  },
  {
    category: "Contribution",
    title: "ALP birefringence beta = 0.27 deg prediction",
    blurb:
      "Planck-scale axion-like particle prediction matches observed 0.342 +/- 0.094 deg signal at 3.6 sigma. LiteBIRD tests at ~9 sigma by 2030. Bounce-mechanism independent.",
    href: "/contributions#alp-birefringence",
  },
  {
    category: "Contribution",
    title: "8.47M-galaxy chirality catalog (Paper 4)",
    blurb:
      "Largest survey-scale spiral-galaxy chirality catalog: CW/CCW/NOT_SPIRAL classification with equivariant DL ensemble, hemispheric asymmetry analysis, null result for large-scale parity violation.",
    href: "/contributions#chirality-catalog",
  },
  {
    category: "Contribution",
    title: "Public-ID anomaly-list recovery (Paper 3)",
    blurb:
      "Reproducible public-ID recovery of 181 DESI DR1 TARGETIDs from a frozen historical anomaly list (170 core + 11 lower-confidence) — an archive-recovery / provenance product, not a purity, novelty, or detection claim.",
    href: "/contributions#anomaly-catalog",
  },
  {
    category: "Contribution",
    title: "SPHEREx f_NL Fisher forecast (Paper 2)",
    blurb:
      "Multi-tracer Fisher forecast of sigma(f_NL) = 0.7 from SPHEREx galaxy bispectrum, giving 4.7-12 sigma detection of bounce f_NL = -2.1875 by 2027.",
    href: "/contributions#spherex-fisher",
  },
  {
    category: "Contribution",
    title: "DESI environmental chirality study (Paper 5)",
    blurb:
      "Cross-match of 2.23M DESI LSS galaxies with the chirality catalog to test environmental dependence of spiral spin direction across cosmic-web environments.",
    href: "/contributions#desi-environment",
  },
  {
    category: "Equation",
    title: "f_NL_local = -35/16 = -2.1875 (matter bounce)",
    blurb: "Closed-form, parameter-free local non-Gaussianity from matter-dominated contraction.",
    href: "/contributions#matter-bounce-fnl",
  },
  {
    category: "Equation",
    title: "beta_ALP = (3/4) * (alpha_em / 2pi) * (Lambda_QCD / M_Pl)^2 ~ 0.27 deg",
    blurb: "Cosmic birefringence rotation angle from Planck-scale axion-like particles.",
    href: "/contributions#alp-birefringence",
  },
];

const GLOSSARY_ITEMS: SearchItem[] = [
  { category: "Glossary", title: "Big Bounce", blurb: "Cosmological model where the universe transitions from contraction to expansion at finite density, avoiding the Big Bang singularity.", href: "/glossary" },
  { category: "Glossary", title: "Einstein-Cartan-Holst (ECH)", blurb: "Spin-torsion extension of general relativity with the Holst term; foundation for the specific bounce model in this program.", href: "/glossary" },
  { category: "Glossary", title: "Barbero-Immirzi parameter gamma", blurb: "Dimensionless parameter controlling the Holst term; invisible perturbatively when scalar matter is minimally coupled.", href: "/glossary" },
  { category: "Glossary", title: "f_NL", blurb: "Local non-Gaussianity amplitude; matter bounce predicts -35/16 = -2.1875.", href: "/glossary" },
  { category: "Glossary", title: "Cosmic birefringence", blurb: "Rotation of CMB polarization plane induced by axion-like particles or other parity-violating physics.", href: "/glossary" },
  { category: "Glossary", title: "Spin density", blurb: "Source of torsion in Einstein-Cartan theory; vanishes identically for scalar matter, which is the load-bearing step in the perturbation-transparency theorem.", href: "/glossary" },
  { category: "Glossary", title: "Holst term", blurb: "Parity-odd term in the gravitational action; reduces to the topological Nieh-Yan invariant in the absence of torsion.", href: "/glossary" },
  { category: "Glossary", title: "NANOGrav gamma", blurb: "Spectral index of the stochastic gravitational-wave background; bounce predicts 3.0 vs real-KDE free-spectrum 2.567 +/- 0.382 (+1.13 sigma consistent).", href: "/glossary" },
];

export function SearchClient() {
  const [query, setQuery] = useState("");

  const corpus = useMemo<SearchItem[]>(() => {
    const figureItems: SearchItem[] = figureSections.flatMap((section) =>
      section.items.map((fig) => ({
        category: "Figure" as const,
        title: `${fig.number} — ${fig.title}`,
        blurb: `${section.title} · ${fig.desc.slice(0, 200)}`,
        href: "/figures",
      })),
    );
    const paperItems: SearchItem[] = papers.map((p) => ({
      category: "Paper" as const,
      title: `${p.number} · ${p.title}`,
      blurb: p.tldr || p.description || "",
      href: `/paper#${p.slug}`,
    }));
    const surveyItems: SearchItem[] = surveys.map((s) => ({
      category: "Survey" as const,
      title: s.name,
      blurb: s.description,
      href: "/surveys",
    }));
    return [
      ...STATIC_PAGES,
      ...CONTRIBUTIONS,
      ...GLOSSARY_ITEMS,
      ...paperItems,
      ...surveyItems,
      ...figureItems,
    ];
  }, []);

  const results = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (q.length === 0) return [];
    return corpus
      .filter((item) =>
        [item.title, item.blurb, item.category]
          .join(" ")
          .toLowerCase()
          .includes(q),
      )
      .slice(0, 60);
  }, [corpus, query]);

  return (
    <div style={{ marginTop: 16 }}>
      <div
        className="figures-search"
        style={{
          display: "flex",
          alignItems: "center",
          gap: 10,
          padding: "10px 14px",
          border: "1px solid var(--border)",
          borderRadius: "var(--radius)",
          background: "var(--surface)",
          maxWidth: 720,
        }}
      >
        <Search aria-hidden="true" size={16} />
        <input
          autoFocus
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search papers, contributions, equations, figures, surveys, glossary…"
          aria-label="Search the BigBounce research program"
          style={{
            background: "transparent",
            border: "none",
            outline: "none",
            color: "var(--text)",
            width: "100%",
            fontFamily: "var(--font-sans)",
            fontSize: 14,
          }}
        />
      </div>

      {query.length === 0 ? (
        <p
          style={{
            marginTop: 16,
            color: "var(--text-muted)",
            fontFamily: "var(--font-sans)",
            fontSize: 13,
          }}
        >
          Try: <em>perturbation transparency</em>, <em>f_NL</em>, <em>ALP</em>,{" "}
          <em>chirality</em>, <em>NANOGrav</em>, <em>channel-level closure</em>.
        </p>
      ) : results.length === 0 ? (
        <Card style={{ marginTop: 16, padding: 16 }}>
          <p style={{ margin: 0, fontFamily: "var(--font-sans)", fontSize: 13 }}>
            No results for <strong>{query}</strong>. Try a different phrasing or
            browse the <Link href="/contributions">contributions</Link> page.
          </p>
        </Card>
      ) : (
        <div style={{ marginTop: 16, display: "grid", gap: 10 }}>
          {results.map((item, i) => (
            <Link
              key={`${item.href}-${item.title}-${i}`}
              href={item.href}
              style={{ textDecoration: "none", color: "inherit" }}
            >
              <Card
                style={{
                  padding: 14,
                  display: "grid",
                  gridTemplateColumns: "auto 1fr",
                  gap: 12,
                  alignItems: "start",
                }}
              >
                <Badge variant="outline" className="font-mono text-[10px]">
                  {item.category}
                </Badge>
                <div>
                  <div
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 13,
                      fontWeight: 600,
                    }}
                  >
                    {item.title}
                  </div>
                  <p
                    style={{
                      margin: "4px 0 0",
                      fontSize: 12,
                      color: "var(--text-muted)",
                      lineHeight: 1.5,
                    }}
                  >
                    {item.blurb}
                  </p>
                </div>
              </Card>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

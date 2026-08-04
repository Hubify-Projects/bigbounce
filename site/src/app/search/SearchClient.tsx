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
  { category: "Page", title: "Overview", blurb: "Three question-first research programs: bounce theory, DESI anomaly discovery, and galaxy chirality", href: "/" },
  { category: "Page", title: "Explainer", blurb: "Non-technical explanation of the research program", href: "/explained" },
  { category: "Page", title: "Surveys", blurb: "Legacy and superseded survey-pipeline records retained for methodology and archive context", href: "/surveys" },
  { category: "Page", title: "Predictions", blurb: "Conditional matter-contraction non-Gaussianity, birefringence and SGWB diagnostics, and future-survey context", href: "/predictions" },
  { category: "Page", title: "Research Programs", blurb: "Three scientific programs with versioned papers, supporting releases, and evidence readiness", href: "/paper" },
  { category: "Page", title: "Publication Map", blurb: "The definitive three-program plan for manuscripts, data, models, software, releases, and submission order", href: "/publish" },
  { category: "Page", title: "Data Explorer", blurb: "Interactive research data and equation calculators; historic MCMC records are not P1B's publication role", href: "/data-explorer" },
  { category: "Page", title: "Galaxy Explorer", blurb: "8.47M-galaxy DESI Legacy DR8 chirality catalog explorer", href: "/galaxy-explorer" },
  { category: "Page", title: "Anomaly Explorer", blurb: "Legacy DESI candidate records; candidate flags are not confirmed discoveries or bounce evidence", href: "/anomaly-explorer" },
  { category: "Page", title: "Visualize", blurb: "Interactive cosmic simulation of the Big Bounce from parent universe through SPHEREx 2028", href: "/visualize" },
  { category: "Page", title: "Figures", blurb: "Gallery of research figures across the retained evidence library, sortable and filterable", href: "/figures" },
  { category: "Page", title: "Glossary", blurb: "Searchable glossary of terms, parameters, and equations", href: "/glossary" },
  { category: "Page", title: "Timeline", blurb: "Visual cosmological timeline parent universe through bounce to SPHEREx 2028", href: "/timeline" },
  { category: "Page", title: "Articles", blurb: "Deep-dive companion articles to the research program", href: "/articles" },
  { category: "Page", title: "Speculations", blurb: "Speculative extensions and open lines of inquiry", href: "/speculations" },
  { category: "Page", title: "Contributions", blurb: "Novel contributions, first computations, and independent verifications ranked by novelty", href: "/contributions" },
  { category: "Page", title: "Activity", blurb: "Research status, priority queue, and chronological feed", href: "/activity" },
  { category: "Page", title: "Status", blurb: "Live status of research programs, selected artifacts, editorial decisions, and active pods", href: "/status" },
  { category: "Page", title: "Astro Chat", blurb: "AI research assistant trained on the BigBounce program", href: "/chat" },
];

const CONTRIBUTIONS: SearchItem[] = [
  {
    category: "Contribution",
    title: "Minimal-ECH Branch Clarification",
    blurb:
      "A narrow, convention-audited account of the stated minimal Einstein–Cartan–Holst branch; not a universal no-go theorem or dark-energy model. Paper 1A.",
    href: "/contributions#perturbation-transparency",
  },
  {
    category: "Contribution",
    title: "Archived ECH Route Map",
    blurb:
      "Historical route-mapping material preserved for provenance; it is not a selected P1A claim and does not close every minimal-ECH route.",
    href: "/contributions#14-barriers",
  },
  {
    category: "Contribution",
    title: "Matter-bounce f_NL = -35/16 prediction",
    blurb:
      "P2's conditional matter-contraction prediction: f_NL = -2.1875. SPHEREx may test it; no current survey result establishes a bounce.",
    href: "/contributions#matter-bounce-fnl",
  },
  {
    category: "Contribution",
    title: "Archived ALP birefringence exploration",
    blurb:
      "Exploratory ALP calculations retained as program provenance; they are not a selected scientific claim of P1A or P2.",
    href: "/contributions#alp-birefringence",
  },
  {
    category: "Contribution",
    title: "8.47M-galaxy chirality catalog (Paper 4)",
    blurb:
      "An 8,474,531-row observed-label catalog with a 890,069-row quality-controlled primary dipole result consistent with zero; not a physical parity bound.",
    href: "/contributions#chirality-catalog",
  },
  {
    category: "Contribution",
    title: "Integrated Supporting Data Release: DESI Public-ID Recovery (P3)",
    blurb:
      "P3 is the integrated Supporting Data Release: reproducible recovery of 181 DESI DR1 TARGETIDs from a frozen historical list, not a standalone discovery paper, purity claim, novelty claim, or detection claim.",
    href: "/contributions#anomaly-catalog",
  },
  {
    category: "Contribution",
    title: "Conditional SPHEREx sensitivity map (Paper 2)",
    blurb:
      "An illustrative map of the exact P2 shape into published survey sensitivity, with explicit covariance and nuisance dependence; not a guaranteed detection forecast.",
    href: "/contributions#spherex-fisher",
  },
  {
    category: "Contribution",
    title: "DESI environmental chirality study (Paper 5)",
    blurb:
      "Standalone AJ companion testing an exploratory DESI environment-label contrast alongside P4's lead chirality catalog result.",
    href: "/contributions#desi-environment",
  },
  {
    category: "Equation",
    title: "f_NL_local = -35/16 = -2.1875 (matter bounce)",
    blurb: "Closed-form local non-Gaussianity for P2's stated matter-contraction assumptions.",
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
  { category: "Glossary", title: "f_NL", blurb: "Local non-Gaussianity amplitude; P2 derives -35/16 = -2.1875 conditionally for matter contraction.", href: "/glossary" },
  { category: "Glossary", title: "Cosmic birefringence", blurb: "Rotation of CMB polarization plane induced by axion-like particles or other parity-violating physics.", href: "/glossary" },
  { category: "Glossary", title: "Spin density", blurb: "Source of torsion in Einstein-Cartan theory; vanishes identically for scalar matter, which is the load-bearing step in the perturbation-transparency theorem.", href: "/glossary" },
  { category: "Glossary", title: "Holst term", blurb: "Parity-odd term in the gravitational action; reduces to the topological Nieh-Yan invariant in the absence of torsion.", href: "/glossary" },
  { category: "Glossary", title: "NANOGrav gamma", blurb: "A legacy simplified slope comparison; it is not a bounce detection or current portfolio flagship.", href: "/glossary" },
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

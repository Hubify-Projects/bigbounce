// Sourced from /articles.html (regen: cd site && node scripts/extract-articles.mjs).
// NOTE: carries manual EXT18 copy polish — keep articles.html in sync before regenerating.

export interface Article {
  slug: string;
  title: string;
  summary: string;
  type: string;
  category: string;
  isNew: boolean;
}

export const articles: Article[] = [
  {
    "slug": "the-window",
    "title": "The Window: Why This Moment in Independent Research Will Never Come Again",
    "summary": "Five things had to be true simultaneously for an independent researcher to scan 22.5 million spectra before any major lab. All five are true right now. They won't be for long.",
    "type": "Essay",
    "category": "Research Strategy",
    "isNew": true
  },
  {
    "slug": "look-up",
    "title": "Look Up: Why AI Should Be Pointed at the Stars, Not at Itself",
    "summary": "Most AI labs are stuck optimizing benchmarks while the universe waits to be understood. One independent researcher's case for using AI as a research amplifier — and the cosmology results that prove it works.",
    "type": "Essay",
    "category": "AI & Science",
    "isNew": false
  },
  {
    "slug": "matter-bounce-blueprint",
    "title": "The Matter-Bounce Blueprint: Predictive Precision in Branch V Cosmology",
    "summary": "Why Branch V is the program's flagship — a strongly constrained prediction of fₙₗ = −35/8 (conditional on bounce-transition assumptions) testable by SPHEREx at 2.6–5σ, and the clearest route to a genuinely novel bouncing-cosmology observable.",
    "type": "Research",
    "category": "Branch V",
    "isNew": false
  },
  {
    "slug": "ech-bounce-phenomenology",
    "title": "The ECH Spin-Torsion Bounce and Matter-Bounce Phenomenology",
    "summary": "A comprehensive technical overview of the Einstein-Cartan-Holst framework: the quantum bounce at ρ_crit ≈ 0.27 ρ_Pl, the 14 structural barriers, and the surviving ALP birefringence and matter-bounce predictions (N3 novelty tier).",
    "type": "Technical",
    "category": "Framework",
    "isNew": false
  },
  {
    "slug": "students-guide-big-bounce",
    "title": "Beyond the Singularity: A Student's Guide to the Big Bounce",
    "summary": "No physics degree required. An accessible guide to why the universe may not have begun with a \"bang\" at all — and what torsion, spin, and the ECH framework have to say about it.",
    "type": "Explainer",
    "category": "Students",
    "isNew": false
  },
  {
    "slug": "technical-evaluation",
    "title": "Technical Evaluation: Spin-Torsion Cosmology Research Program",
    "summary": "A formal technical assessment of Project BigBounce — the 14 structural barriers, the 24 research branches, the surviving empirical successes, and the recommended next steps for the field.",
    "type": "Evaluation",
    "category": "Institutional",
    "isNew": false
  },
  {
    "slug": "publication-roadmap",
    "title": "Strategic Publication Roadmap: Spin-Torsion Cosmology Research Program",
    "summary": "How the program's assets — the Framework Paper, ALP standalone, Technical Note, and Branch V blueprint — fit into a phased publication strategy targeting high-impact journals.",
    "type": "Strategy",
    "category": "Publication",
    "isNew": false
  },
  {
    "slug": "evolution-of-rigor",
    "title": "The Evolution of Rigor in the Big Bounce Project",
    "summary": "A pedagogical case study in scientific self-correction. How a speculative manuscript became a rigorous closure map through seventeen rounds of adversarial peer review spanning five AI models.",
    "type": "Case Study",
    "category": "Pedagogy",
    "isNew": false
  },
  {
    "slug": "program-visual-guide",
    "title": "Spin-Torsion Cosmology: A Visual Guide to the Research Program",
    "summary": "Mind maps and infographics mapping the full architecture of the BigBounce program — from theoretical framework through structural barriers to observational validation and deliverables.",
    "type": "Visual Guide",
    "category": "Overview",
    "isNew": false
  }
];

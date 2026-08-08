import type { Metadata } from "next";
import Link from "next/link";
import "./final-review.css";

export const metadata: Metadata = {
  title: "Final Author Review · P2",
  description:
    "The exact P2 author-decision packet: contribution, limits, rendered PDF checkpoints, evidence, and approval response.",
};

const pdfHref = "/papers/02_full_draft_v1.7.130.pdf";

const checkpoints = [
  {
    pages: "Page 1",
    title: "Does the paper lead with the real contribution?",
    detail:
      "The title and abstract should read as an exact four-vertex contraction-phase derivation. The SPHEREx material must remain clearly conditional and subordinate.",
  },
  {
    pages: "Pages 2 and 8–11",
    title: "Is the algebraic result understandable and credible?",
    detail:
      "The core result is f_NL = −35/16 with ordered coefficients (3, 1, −9, 5, −33, 9). Figures, tables, Appendix B, and the vertex-by-vertex checks should make the discrepancy with the printed −35/8 value inspectable without overselling its origin.",
  },
  {
    pages: "Pages 3–4",
    title: "Are the model boundaries impossible to miss?",
    detail:
      "Faithful nonlinear cubic transmission through a specified bounce remains a load-bearing condition. The paper must not read as a complete or model-independent nonsingular-bounce calculation.",
  },
  {
    pages: "Pages 4–7",
    title: "Is the observational mapping framed honestly?",
    detail:
      "The 2.63σ arithmetic map and 3.5σ-to-0.4σ nuisance ladder are sensitivity diagnostics, not a detection forecast, guaranteed floor, or new survey likelihood.",
  },
  {
    pages: "Pages 7–12",
    title: "Is the final package professionally complete?",
    detail:
      "Check the conclusion, data/code availability, AI disclosure, acknowledgements, references, figure labels, tables, equations, links, and overall reading flow.",
  },
] as const;

export default function FinalReviewPage() {
  return (
    <>
      <p className="review-kicker">Final author decision · 1 of 5</p>
      <h1 className="review-title">P2 · Exact matter-contraction amplitude</h1>
      <p className="review-lede">
        This is the first selected manuscript in the approval sequence. The question is not whether every future bounce calculation is finished; it is whether this exact 12-page candidate makes its bounded algebraic contribution clearly, honestly, and professionally enough to submit to Physical Review D.
      </p>

      <section className="review-state" aria-label="Decision state">
        <p><strong>Current state:</strong> 95/100 · all agent gates recorded complete · Houston decision pending.</p>
        <p><strong>Exact candidate:</strong> v1.7.130 · SHA-256 <code>d3afe79fe70ce13cee5ec8149e84c4b42c78224ca6a90569058ec501222f5c2f</code>.</p>
        <p><strong>Scoring rule:</strong> there is no 96 state. Only an explicit approval moves this exact candidate to 100.</p>
      </section>

      <div className="review-actions">
        <a className="review-action review-action-primary" href={pdfHref} target="_blank" rel="noopener noreferrer">Open exact PDF</a>
        <a className="review-action" href="https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/SSOT/PRD_SUBMISSION_KIT_P2_2026-07-24.md" target="_blank" rel="noopener noreferrer">Submission kit</a>
        <a className="review-action" href="https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/FINALHASH_2026-08-03_P2_v1.7.130_P2_TRUTH_AUDIT.md" target="_blank" rel="noopener noreferrer">Final-hash audit</a>
      </div>

      <section className="review-section">
        <p className="review-section-index">01 · What this paper is for</p>
        <div className="review-definition">
          <div>
            <h2>The contribution</h2>
            <p>
              P2 re-sums the stated matter-contraction cubic action vertex by vertex, obtains the exact local amplitude <strong>f_NL = −35/16</strong>, and exposes the ordered polynomial and independent checks needed to reproduce it.
            </p>
          </div>
          <div>
            <h2>The boundary</h2>
            <p>
              It does not claim a detection, a complete nonsingular-bounce model, universal cubic transmission, or a new end-to-end SPHEREx likelihood. Those are explicitly future scientific conditions.
            </p>
          </div>
        </div>
      </section>

      <section className="review-section">
        <p className="review-section-index">02 · Read the PDF through five checks</p>
        <div className="review-checkpoints">
          {checkpoints.map((checkpoint, index) => (
            <article className="review-checkpoint" key={checkpoint.title}>
              <div className="review-checkpoint-number">{String(index + 1).padStart(2, "0")}</div>
              <div>
                <p className="review-pages">{checkpoint.pages}</p>
                <h2>{checkpoint.title}</h2>
                <p>{checkpoint.detail}</p>
              </div>
              <a href={`${pdfHref}#page=${checkpoint.pages.startsWith("Page 1") ? "1" : checkpoint.pages.match(/\d+/)?.[0] ?? "1"}`} target="_blank" rel="noopener noreferrer">Open pages ↗</a>
            </article>
          ))}
        </div>
      </section>

      <section className="review-section">
        <p className="review-section-index">03 · Independent visual-layout pass</p>
        <p className="review-copy">
          All 12 pages of the hash-bound candidate were rendered and inspected on August 4, 2026. No clipped text, column collisions, broken equations, unreadable tables, missing figures, or malformed glyphs were found. This is a layout check, not a substitute for your scientific and editorial judgment.
        </p>
      </section>

      <section className="review-section review-decision">
        <p className="review-section-index">04 · Your decision</p>
        <h2>Reply with one line</h2>
        <pre>P2 APPROVE | REVISE | DEFER — feedback:</pre>
        <dl>
          <div><dt>APPROVE</dt><dd>Move this exact candidate to 100 and execute its archive and PRD submission checklist.</dd></div>
          <div><dt>REVISE</dt><dd>Name the reader-visible change. The rebuilt PDF must be visually audited, re-hashed, and shown again.</dd></div>
          <div><dt>DEFER</dt><dd>Preserve the candidate and evidence without submitting it now.</dd></div>
        </dl>
      </section>

      <section className="review-section review-queue">
        <p className="review-section-index">Next in sequence</p>
        <p>P1A → P4 → P1B → P5. The clean DESI anomaly rerun proceeds separately in parallel.</p>
        <div>
          <Link href="/publish">Return to publication map</Link>
          <Link href="/papers/paper-2">Open full P2 evidence page</Link>
        </div>
      </section>
    </>
  );
}

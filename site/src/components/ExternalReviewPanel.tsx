"use client";

import { useState } from "react";
import { Check, Copy, Download, ExternalLink } from "lucide-react";

interface ExternalReviewPanelProps {
  paperNumber: string;
  paperTitle: string;
  paperVersion: string;
  paperPath: string; // e.g. "arxiv/paper1a_ech_nogo.tex"
  pdfHref: string;   // e.g. "/papers/paper1a_ech_nogo.pdf"
  pdfMeta: string;   // e.g. "20 pp / 813 KB"
  focusAreas: string[]; // bulleted scrutiny items
}

export function ExternalReviewPanel({
  paperNumber,
  paperTitle,
  paperVersion,
  paperPath,
  pdfHref,
  pdfMeta,
  focusAreas,
}: ExternalReviewPanelProps) {
  const [copied, setCopied] = useState(false);

  const prompt = [
    `You are an external referee for MNRAS / Physical Review D / JCAP (target journal depends on paper).`,
    ``,
    `Attached: Paper ${paperNumber} ${paperVersion} — "${paperTitle}"`,
    `Source: ${paperPath}`,
    `PDF: ${pdfMeta}`,
    ``,
    `Read the FULL PDF end-to-end. Produce a referee report in MNRAS format with:`,
    ``,
    `1. Recommendation: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT`,
    `2. BLOCKERS (must fix before publication) — list each with section/line + proposed fix`,
    `3. MAJORS (should fix) — same format`,
    `4. MINORS (polish) — same format`,
    `5. Strengths (>= 3 bullet points)`,
    ...(focusAreas.length > 0
      ? [
          `6. Specific scrutiny on:`,
          ...focusAreas.map((f) => `   - ${f}`),
        ]
      : []),
    ``,
    `CALIBRATION (do not burn findings on these known classes):`,
    `- The current date is June 2026. arXiv identifiers of the form 25xx.xxxxx and 26xx.xxxxx are VALID, already-published preprints — do not flag them as "future-dated" or "nonexistent". Verify a citation against arXiv/ADS before claiming it does not exist.`,
    `- Correction notes, retraction notices, and "an earlier version stated X" disclosures in the text are DELIBERATE transparency policy. Flag them only if their content is wrong, never for existing.`,
    `- Companion-paper citations marked "posted concurrently on arXiv" are deliberate placeholders; real arXiv IDs are inserted during the coordinated submission sequence.`,
    `- Explicitly labeled conservatism allowances, scaling estimates, ansatz/heuristic status labels, and disclosed queued follow-up computations are deliberate scoping, not oversights — flag only if the label itself is inaccurate.`,
    `- PDF text extraction can mangle math (square roots, fractions, superscripts). Before flagging "garbled" or "wrong" math, consider extraction artifacts; flag only what is visibly wrong in the rendered PDF.`,
    ``,
    `VERDICT STANDARD (apply the SAME high bar a first-pass Physical Review D / MNRAS referee would — this is one of the most rigorous journals in the world):`,
    `- Assign each finding's severity (BLOCKER / MAJOR / MINOR) by your own independent referee judgment. Do NOT default to any tier, and do NOT soften a finding because the rest of the paper is strong. Do not echo this prompt's context.`,
    `- A reporting choice that headlines the more favorable of two numbers, an unstated assumption, an uncontrolled systematic, or an internal inconsistency IS a real finding — classify it honestly (MINOR at minimum), not as mere "style" or "opinion".`,
    `- Truth-audit any claim that seems off by checking it against the published .tex / on-disk artifacts before flagging (this only filters out genuine extraction artifacts — it does not lower the bar on real defects).`,
  ].join("\n");

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(prompt);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // Fallback for older browsers
      const ta = document.createElement("textarea");
      ta.value = prompt;
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
      } catch {
        // give up silently
      }
      document.body.removeChild(ta);
    }
  }

  return (
    <section
      style={{
        borderTop: "1px solid var(--rule, var(--border))",
        paddingTop: 18,
        marginTop: 24,
        marginBottom: 24,
      }}
      aria-label="External peer review kit"
    >
      <div
        style={{
          display: "flex",
          alignItems: "baseline",
          justifyContent: "space-between",
          flexWrap: "wrap",
          gap: 10,
          marginBottom: 10,
        }}
      >
        <h3
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.78rem",
            letterSpacing: "0.08em",
            textTransform: "uppercase",
            color: "var(--text-tertiary)",
            margin: 0,
          }}
        >
          External peer review kit
        </h3>
        <span style={{ fontSize: "0.72rem", color: "var(--text-muted)" }}>
          Houston-driven manual round · paste prompt into any frontier LLM web UI with the PDF attached
        </span>
      </div>

      <p
        style={{
          fontSize: "0.82rem",
          color: "var(--text-muted)",
          margin: "0 0 12px 0",
          lineHeight: 1.5,
        }}
      >
        One click to copy a referee prompt scoped to this paper. One click to download the latest PDF.
        Paste both into Claude / GPT-5 / Gemini / Grok / Perplexity — return findings here and the
        autonomous cron will close them in the next bundled hard-fix wave.
      </p>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: 8,
          marginBottom: 14,
        }}
      >
        <button
          type="button"
          onClick={handleCopy}
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 6,
            padding: "8px 14px",
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.82rem",
            background: copied ? "var(--success)" : "var(--accent)",
            color: "#ffffff",
            border: "none",
            borderRadius: 6,
            cursor: "pointer",
            transition: "background 120ms",
          }}
        >
          {copied ? <Check size={14} /> : <Copy size={14} />}
          {copied ? "Copied!" : "Copy review prompt"}
        </button>
        <a
          href={pdfHref}
          download
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 6,
            padding: "8px 14px",
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.82rem",
            background: "var(--bg)",
            color: "var(--text)",
            border: "1px solid var(--border)",
            borderRadius: 6,
            textDecoration: "none",
          }}
        >
          <Download size={14} />
          Download latest PDF
        </a>
        <a
          href={pdfHref}
          target="_blank"
          rel="noopener noreferrer"
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 6,
            padding: "8px 14px",
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.82rem",
            background: "var(--bg)",
            color: "var(--text)",
            border: "1px solid var(--border)",
            borderRadius: 6,
            textDecoration: "none",
          }}
        >
          <ExternalLink size={14} />
          Open in tab
        </a>
      </div>

      <details
        style={{
          fontSize: "0.78rem",
          color: "var(--text-muted)",
        }}
      >
        <summary
          style={{
            cursor: "pointer",
            fontFamily: "var(--font-mono-stack)",
            color: "var(--text)",
            marginBottom: 6,
          }}
        >
          preview prompt
        </summary>
        <pre
          style={{
            background: "var(--bg)",
            border: "1px solid var(--border)",
            borderRadius: 6,
            padding: 12,
            overflowX: "auto",
            fontSize: "0.74rem",
            whiteSpace: "pre-wrap",
            lineHeight: 1.45,
          }}
        >
          {prompt}
        </pre>
      </details>
    </section>
  );
}

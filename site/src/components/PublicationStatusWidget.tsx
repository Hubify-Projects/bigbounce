/**
 * PublicationStatusWidget — "what is actually left before these papers are
 * published, and who owns each piece".
 *
 * Replaces PublishEtaWidget (retired 2026-07-24). That widget showed a
 * "Submission-ready ETA" in hours, counting down to directive K's two-clean-
 * waves bar — a bar directive L demoted and directives M / M-AMENDED / P
 * superseded — computed from Convex rows that had stopped being written eight
 * days earlier. It advertised a countdown to an abandoned target using stale
 * inputs, with no way for a reader to tell.
 *
 * This surface makes three deliberate choices:
 *
 *   1. NO PREDICTION. There is no ETA. Under directive P the remaining work is
 *      a short list of named gates with named owners, not a duration, and an
 *      hours estimate was the part most prone to silently going wrong.
 *
 *   2. OWNERSHIP IS THE HEADLINE. Houston's ask was to see which papers are
 *      blocked on more science/compute and which are blocked on him. Every row
 *      answers exactly that, derived from live Convex rows.
 *
 *   3. IT CANNOT GO STALE QUIETLY. Every number is stamped with the evidence it
 *      came from, and the age of that evidence is computed in the reader's
 *      browser (see FreshnessStamp). If the loop stops writing, the surface
 *      says STALE on its own. If Convex is unreachable, it says so instead of
 *      vanishing.
 *
 * Directive P composition (readiness = science 25 + evidence 25 + convergence
 * 25 + packaging 20 + Houston's final review 5) means a paper with the four
 * agent gates complete sits at 95 and reaches 100 only on Houston's sign-off.
 * arXiv endorsement, venue choice, submission clicks and journal/human review
 * are the separate Publishing phase and never subtract from readiness.
 *
 * House style: one outer shell, then spacing, type and thin dividers — no
 * nested boxes.
 */
import Link from "next/link";
import type { LivePaperState } from "@/lib/livePapers";
import type { PublicationStatus, PublicationOwner } from "@/lib/publicationStatus";
import { shortDate } from "@/lib/publicationStatus";
import { FreshnessStamp, StaleBanner } from "@/components/FreshnessStamp";

const MONO = "var(--font-mono-stack)";

function ownerColor(owner: PublicationOwner): string {
  if (owner === "done") return "var(--success)";
  if (owner === "houston") return "var(--accent)";
  return "var(--text-secondary)";
}

function ownerLabel(owner: PublicationOwner): string {
  if (owner === "done") return "signed off";
  if (owner === "houston") return "Houston";
  return "agent";
}

export function PublicationStatusWidget({
  status,
  livePapers,
  compact = false,
}: {
  status: PublicationStatus | null;
  livePapers: LivePaperState[];
  compact?: boolean;
}) {
  // De-nested per the redesign surface rule (§4.3): no border/radius shell —
  // this widget always renders inside a Band, which already separates it with
  // a tonal background. A generic bordered card here would nest one bordered
  // surface inside another.
  const shell: React.CSSProperties = {
    padding: compact ? "4px 0" : "8px 0",
  };

  // Convex unreachable. Say so plainly — the old widget rendered nothing here,
  // which is indistinguishable from "everything is fine".
  if (!status) {
    return (
      <section aria-label="Publication status" style={shell}>
        <p style={{ margin: 0, fontFamily: MONO, fontSize: "0.66rem", letterSpacing: "0.09em", textTransform: "uppercase", color: "var(--text-tertiary)" }}>
          Publication status
        </p>
        <p style={{ margin: "6px 0 0", fontSize: "0.8rem", lineHeight: 1.6, color: "var(--warn)", maxWidth: "70ch" }}>
          Live status unavailable — the Convex <code>publicationStatus:get</code> query did
          not return, so this build has no current data to show. Nothing here is a
          fallback snapshot: the per-paper record is at{" "}
          <Link href="/status" style={{ color: "var(--accent-link)" }}>/status</Link>.
        </p>
      </section>
    );
  }

  const readinessBySlug = new Map(livePapers.map((p) => [p.slug, p.readinessComputed]));
  const asOfISO = status.newestEvidenceMs
    ? new Date(status.newestEvidenceMs).toISOString().slice(0, 10)
    : null;
  const asOf = shortDate(asOfISO);
  const houstonCount = status.papersAwaitingHouston;
  const agentCount = status.papersAwaitingAgent;
  const signedOff = status.papersSignedOff;

  return (
    <section aria-label="Publication status" style={shell}>
      <StaleBanner
        evidenceMs={status.newestEvidenceMs}
        staleAfterDays={status.staleAfterDays}
        asOf={asOf}
      />

      <div
        style={{
          display: "flex",
          alignItems: "baseline",
          justifyContent: "space-between",
          gap: 16,
          flexWrap: "wrap",
        }}
      >
        <div>
          <p
            style={{
              margin: 0,
              fontFamily: MONO,
              fontSize: "0.66rem",
              letterSpacing: "0.09em",
              textTransform: "uppercase",
              color: "var(--text-tertiary)",
            }}
          >
            What&apos;s left before publication
          </p>
          <p
            style={{
              margin: "4px 0 0 0",
              fontFamily: MONO,
              fontWeight: 700,
              fontSize: compact ? "1.2rem" : "1.45rem",
              color: "var(--text-primary)",
              lineHeight: 1.15,
            }}
          >
            {signedOff}/{status.papersTotal} signed off
          </p>
        </div>
        <div style={{ textAlign: "right" }}>
          <p style={{ margin: 0, fontFamily: MONO, fontSize: "0.72rem", color: "var(--text-secondary)" }}>
            {houstonCount} waiting on Houston · {agentCount} on the agents
          </p>
          <p style={{ margin: "2px 0 0 0", fontFamily: MONO, fontSize: "0.64rem", color: "var(--text-muted)" }}>
            evidence as of {asOf}
            <FreshnessStamp
              evidenceMs={status.newestEvidenceMs}
              staleAfterDays={status.staleAfterDays}
            />
          </p>
        </div>
      </div>

      {/* Per-paper rows — divider-separated, no nested boxes. */}
      <div style={{ marginTop: 14 }}>
        {status.perPaper.map((p, i) => {
          const readiness = readinessBySlug.get(p.paperSlug);
          return (
            <div
              key={p.paperId}
              style={{
                display: "flex",
                alignItems: "baseline",
                gap: 10,
                flexWrap: "wrap",
                padding: "7px 0",
                borderTop: i === 0 ? "1px solid var(--border)" : "1px solid color-mix(in srgb, var(--border) 45%, transparent)",
              }}
            >
              <span style={{ fontFamily: MONO, fontSize: "0.7rem", color: "var(--text-tertiary)", minWidth: 34 }}>
                {p.paperId}
              </span>
              <span style={{ fontFamily: MONO, fontSize: "0.7rem", fontWeight: 600, color: "var(--text-primary)", minWidth: 34 }}>
                {readiness === undefined ? "—" : `${readiness}%`}
              </span>
              <span
                style={{
                  fontFamily: MONO,
                  fontSize: "0.63rem",
                  letterSpacing: "0.05em",
                  textTransform: "uppercase",
                  color: ownerColor(p.owner),
                  minWidth: 62,
                }}
              >
                {ownerLabel(p.owner)}
              </span>
              <span style={{ fontSize: "0.74rem", lineHeight: 1.5, color: "var(--text-secondary)", flex: "1 1 240px", minWidth: 0 }}>
                {p.remaining}
              </span>
              <span
                style={{ fontFamily: MONO, fontSize: "0.62rem", color: "var(--text-muted)", flex: "0 0 auto" }}
                title={
                  p.boardCoversCurrentVersion
                    ? `Latest automated review board (${shortDate(p.boardDateISO)}) read this exact PDF.`
                    : `Latest automated review board (${shortDate(p.boardDateISO)}) read ${
                        p.boardVersions.length ? p.boardVersions.join(", ") : "an unrecorded version"
                      }, not ${p.currentVersion ?? "the current version"}.`
                }
              >
                {p.currentVersion ?? "—"} · board {shortDate(p.boardDateISO)}
                {p.boardCoversCurrentVersion ? " ✓" : " ↗"}
              </span>
            </div>
          );
        })}
      </div>

      {/* What the numbers mean + the separate Publishing phase. */}
      <div style={{ marginTop: 14, paddingTop: 12, borderTop: "1px solid var(--border)" }}>
        <p style={{ margin: 0, fontSize: "0.7rem", lineHeight: 1.6, color: "var(--text-muted)", maxWidth: "74ch" }}>
          <strong style={{ color: "var(--text-secondary)" }}>How to read this.</strong>{" "}
          Publication readiness is science closure + evidence &amp; reproducibility + automated
          review convergence + packaging, and then Houston&apos;s own final read — the last 5%.
          A paper marked <span style={{ color: "var(--accent)" }}>Houston</span> needs no
          further math, compute, GPU/CPU runs or new data; a paper marked{" "}
          <span style={{ color: "var(--text-secondary)" }}>agent</span> has one named item
          still owned by the loop. The trailing stamp shows which exact PDF the newest
          automated review board actually read — <span title="board read the current PDF">✓</span>{" "}
          means the current one, <span title="board read an earlier version">↗</span> means an
          earlier one.
        </p>
        <p style={{ margin: "8px 0 0", fontSize: "0.7rem", lineHeight: 1.6, color: "var(--text-muted)", maxWidth: "74ch" }}>
          <strong style={{ color: "var(--text-secondary)" }}>Publishing is a separate phase.</strong>{" "}
          arXiv endorsement, venue choice, submission clicks and journal / independent human
          review come <em>after</em> 100% and never subtract from readiness.{" "}
          {!compact && (
            <Link href="/publish" style={{ color: "var(--accent-link)" }}>
              See the publishing checklist →
            </Link>
          )}
        </p>
      </div>
    </section>
  );
}

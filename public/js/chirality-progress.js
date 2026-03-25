/**
 * chirality-progress.js
 * =====================
 * Standalone progress widget for the Galaxy Chirality Classification Pipeline.
 * Renders live inference status into #chirality-progress.
 *
 * Usage:
 *   <div id="chirality-progress"></div>
 *   <script src="/public/js/chirality-progress.js"></script>
 *
 * Styles itself using CSS variables from the BigBounce site (--bg, --text,
 * --border, --accent-link, --font-mono, --font-sans, etc.). Falls back to
 * sensible defaults if variables are missing.
 *
 * No external dependencies — vanilla JS only.
 */

// TODO: Replace PROGRESS with Convex query:
// import { useQuery } from "convex/react";
// const progress = useQuery(api.chirality.progress);

// TODO: Replace static data with fetch from JSON endpoint:
// async function fetchProgress() {
//   const res = await fetch("/api/chirality-progress.json");
//   return res.json();
// }

const PROGRESS = {
  shards_done: 23,
  shards_total: 192,
  galaxies: 1015191,
  galaxies_total: 8474688,
  rate_per_sec: 40,
  cw: 202000,
  ccw: 195000,
  ns: 618000,
  last_backup: "2026-03-24T22:00:00Z",
  eta_hours: 69.6,
  model_accuracy: 0.937,
  hf_url: "https://huggingface.co/bamfai/galaxy-chirality-v2",
};

(function () {
  "use strict";

  const root = document.getElementById("chirality-progress");
  if (!root) return;

  // ── Helpers ──────────────────────────────────────────

  function fmt(n) {
    return n.toLocaleString("en-US");
  }

  function pct(n, d) {
    return ((n / d) * 100).toFixed(1);
  }

  function relativeTime(iso) {
    const diff = Date.now() - new Date(iso).getTime();
    const mins = Math.floor(diff / 60000);
    if (mins < 1) return "just now";
    if (mins < 60) return mins + " min ago";
    const hrs = Math.floor(mins / 60);
    if (hrs < 24) return hrs + "h " + (mins % 60) + "m ago";
    const days = Math.floor(hrs / 24);
    return days + "d " + (hrs % 24) + "h ago";
  }

  function etaLabel(hours) {
    if (hours < 1) return Math.round(hours * 60) + " min";
    if (hours < 48) return hours.toFixed(1) + " hours";
    return (hours / 24).toFixed(1) + " days";
  }

  // ── Inject scoped styles ─────────────────────────────

  const STYLE_ID = "chirality-progress-styles";
  if (!document.getElementById(STYLE_ID)) {
    const style = document.createElement("style");
    style.id = STYLE_ID;
    style.textContent = `
      #chirality-progress {
        font-family: var(--font-sans, 'Inter', system-ui, sans-serif);
        color: var(--text, #0a0a0a);
        border: 1px solid var(--border, #eaeaea);
        background: var(--bg, #ffffff);
        padding: 20px 24px;
        margin: 16px 0;
        line-height: 1.5;
      }

      .cp-header {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 16px;
        flex-wrap: wrap;
      }
      .cp-title {
        font-family: var(--font-mono, 'IBM Plex Mono', monospace);
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--text, #0a0a0a);
      }
      .cp-model-link {
        font-family: var(--font-mono, 'IBM Plex Mono', monospace);
        font-size: 11px;
        color: var(--text-muted, #999);
        text-decoration: none;
        letter-spacing: 0.02em;
      }
      .cp-model-link:hover {
        color: var(--accent-link, #0a0a0a);
      }

      /* Progress bar */
      .cp-bar-wrap {
        margin-bottom: 14px;
      }
      .cp-bar-label {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 5px;
      }
      .cp-bar-label span {
        font-family: var(--font-mono, 'IBM Plex Mono', monospace);
        font-size: 13px;
        font-weight: 500;
      }
      .cp-bar-pct {
        color: var(--text-secondary, #444);
        font-weight: 400 !important;
        font-size: 12px !important;
      }
      .cp-bar-track {
        width: 100%;
        height: 8px;
        background: var(--bg-code, #f6f6f6);
        border: 1px solid var(--border, #eaeaea);
        overflow: hidden;
      }
      .cp-bar-fill {
        height: 100%;
        background: var(--text, #0a0a0a);
        transition: width 0.4s ease;
      }

      /* Stats grid */
      .cp-stats {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px 24px;
        margin-bottom: 16px;
      }
      .cp-stat {
        display: flex;
        flex-direction: column;
      }
      .cp-stat-label {
        font-family: var(--font-mono, 'IBM Plex Mono', monospace);
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--text-muted, #999);
        margin-bottom: 1px;
      }
      .cp-stat-value {
        font-family: var(--font-mono, 'IBM Plex Mono', monospace);
        font-size: 13px;
        font-weight: 500;
        color: var(--text, #0a0a0a);
      }

      /* Class distribution stacked bar */
      .cp-dist {
        margin-top: 2px;
      }
      .cp-dist-title {
        font-family: var(--font-mono, 'IBM Plex Mono', monospace);
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--text-muted, #999);
        margin-bottom: 6px;
      }
      .cp-dist-bar {
        display: flex;
        width: 100%;
        height: 14px;
        border: 1px solid var(--border, #eaeaea);
        overflow: hidden;
      }
      .cp-dist-cw  { background: #0a0a0a; }
      .cp-dist-ccw { background: #888888; }
      .cp-dist-ns  { background: #d4d4d4; }

      .cp-dist-legend {
        display: flex;
        gap: 16px;
        margin-top: 6px;
        flex-wrap: wrap;
      }
      .cp-legend-item {
        display: flex;
        align-items: center;
        gap: 5px;
        font-family: var(--font-mono, 'IBM Plex Mono', monospace);
        font-size: 11px;
        color: var(--text-secondary, #444);
      }
      .cp-legend-swatch {
        width: 10px;
        height: 10px;
        border: 1px solid var(--border, #eaeaea);
        flex-shrink: 0;
      }

      @media (max-width: 480px) {
        #chirality-progress { padding: 16px; }
        .cp-stats { grid-template-columns: 1fr; gap: 8px; }
        .cp-header { flex-direction: column; gap: 4px; }
      }
    `;
    document.head.appendChild(style);
  }

  // ── Build widget ─────────────────────────────────────

  const d = PROGRESS;
  const shardPct = pct(d.shards_done, d.shards_total);
  const galaxyPct = pct(d.galaxies, d.galaxies_total);
  const classifiedTotal = d.cw + d.ccw + d.ns;
  const cwPct = pct(d.cw, classifiedTotal);
  const ccwPct = pct(d.ccw, classifiedTotal);
  const nsPct = pct(d.ns, classifiedTotal);

  root.innerHTML = `
    <div class="cp-header">
      <span class="cp-title">Chirality Classification Pipeline</span>
      <a class="cp-model-link" href="${d.hf_url}" target="_blank" rel="noopener">
        galaxy-chirality-v2 &middot; ${(d.model_accuracy * 100).toFixed(1)}% acc
      </a>
    </div>

    <div class="cp-bar-wrap">
      <div class="cp-bar-label">
        <span>${d.shards_done} / ${d.shards_total} shards</span>
        <span class="cp-bar-pct">${shardPct}%</span>
      </div>
      <div class="cp-bar-track">
        <div class="cp-bar-fill" style="width:${shardPct}%"></div>
      </div>
    </div>

    <div class="cp-stats">
      <div class="cp-stat">
        <span class="cp-stat-label">Galaxies classified</span>
        <span class="cp-stat-value">${fmt(d.galaxies)} / ${fmt(d.galaxies_total)}</span>
      </div>
      <div class="cp-stat">
        <span class="cp-stat-label">Current rate</span>
        <span class="cp-stat-value">~${fmt(d.rate_per_sec)} galaxies/sec</span>
      </div>
      <div class="cp-stat">
        <span class="cp-stat-label">ETA</span>
        <span class="cp-stat-value">${etaLabel(d.eta_hours)} remaining</span>
      </div>
      <div class="cp-stat">
        <span class="cp-stat-label">Last backup</span>
        <span class="cp-stat-value">${relativeTime(d.last_backup)}</span>
      </div>
    </div>

    <div class="cp-dist">
      <div class="cp-dist-title">Class distribution</div>
      <div class="cp-dist-bar">
        <div class="cp-dist-cw" style="width:${cwPct}%"></div>
        <div class="cp-dist-ccw" style="width:${ccwPct}%"></div>
        <div class="cp-dist-ns" style="width:${nsPct}%"></div>
      </div>
      <div class="cp-dist-legend">
        <span class="cp-legend-item">
          <span class="cp-legend-swatch cp-dist-cw"></span>
          CW ${fmt(d.cw)} (${cwPct}%)
        </span>
        <span class="cp-legend-item">
          <span class="cp-legend-swatch cp-dist-ccw"></span>
          CCW ${fmt(d.ccw)} (${ccwPct}%)
        </span>
        <span class="cp-legend-item">
          <span class="cp-legend-swatch cp-dist-ns"></span>
          NS ${fmt(d.ns)} (${nsPct}%)
        </span>
      </div>
    </div>
  `;
})();

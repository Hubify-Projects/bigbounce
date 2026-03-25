/**
 * BigBounce — Site-Wide Search Overlay
 *
 * Self-contained: builds its own index, injects DOM + styles,
 * wires up keyboard shortcuts. Loaded dynamically by nav.js.
 */
(function () {
  'use strict';

  // ── Search Index ──────────────────────────────────────────
  var SEARCH_INDEX = [
    { title: "Homepage \u2014 What If the Big Bang Was a Big Bounce?", path: "/index.html", tags: "bounce cosmology spin torsion predictions spherex litebird", excerpt: "Two falsifiable predictions from spin-torsion cosmology. SPHEREx and LiteBIRD will settle the question within a decade." },
    { title: "Papers", path: "/paper.html", tags: "paper arxiv pdf latex bibliography citations", excerpt: "Two research papers covering 14 structural barriers and the matter bounce f_NL prediction." },
    { title: "Non-Technical Explainer", path: "/explained.html", tags: "explainer simple non-technical beginner", excerpt: "What is the Big Bounce? A plain-language guide to the research." },
    { title: "Data Explorer", path: "/data-explorer.html", tags: "mcmc chains data posterior samples planck bao", excerpt: "Interactive tool for exploring 400K+ MCMC posterior samples." },
    { title: "Datasets", path: "/datasets.html", tags: "cobaya camb planck bao sn datasets configuration", excerpt: "Dataset descriptions and Cobaya MCMC configurations." },
    { title: "Figures", path: "/figures.html", tags: "figures gallery plots diagrams", excerpt: "Gallery of 22 research figures." },
    { title: "Glossary & Equations", path: "/glossary.html", tags: "glossary equations definitions terms symbols", excerpt: "13 key equations and 28 searchable terms." },
    { title: "Articles", path: "/articles.html", tags: "articles deep dive explainer", excerpt: "Deep dives and strategic assessments from the research program." },
    { title: "Activity", path: "/activity.html", tags: "activity timeline status updates progress", excerpt: "Live research status and chronological timeline." },
    { title: "Timeline", path: "/timeline.html", tags: "cosmic timeline visualization bounce", excerpt: "Visual timeline from parent universe through the bounce." },
    { title: "Visualize", path: "/visualize.html", tags: "visualization simulation interactive 3d", excerpt: "Interactive cosmic simulation of the Big Bounce." },
    { title: "Astro Chat", path: "/chat.html", tags: "chat ai assistant astro questions", excerpt: "AI research assistant for exploring the science." },
    { title: "Review Hub", path: "/review/index.html", tags: "review pipeline desi spectral anomaly", excerpt: "Human review dashboards for AI-enhanced discovery pipelines." },
    { title: "Pipeline B: DESI Spectral Anomaly Miner", path: "/review/pipeline-b-desi-spectral.html", tags: "pipeline desi spectral anomaly miner qso review", excerpt: "Human review of 70 spectral anomalies from DESI EDR." },
    { title: "Dossier", path: "/research/project_master_dossier/index.html", tags: "dossier intelligence dashboard project status", excerpt: "Full project intelligence dashboard." },
    { title: "Admin Dashboard", path: "/admin.html", tags: "admin dashboard analytics chat logs", excerpt: "Site administration and analytics." },
    { title: "The Matter-Bounce Blueprint", path: "/articles/matter-bounce-blueprint.html", tags: "matter bounce fnl branch v spherex bispectrum prediction", excerpt: "Why Branch V is the flagship \u2014 a parameter-free prediction testable by SPHEREx." },
    { title: "ECH Bounce Phenomenology", path: "/articles/ech-bounce-phenomenology.html", tags: "ech einstein cartan holst torsion bounce phenomenology", excerpt: "Technical deep dive into ECH bounce framework and its phenomenological implications." },
    { title: "Evolution of Rigor", path: "/articles/evolution-of-rigor.html", tags: "rigor methodology scientific method revision", excerpt: "How the research program's standards evolved through 8 peer review rounds." },
    { title: "Program Visual Guide", path: "/articles/program-visual-guide.html", tags: "visual guide diagram overview branches foundations", excerpt: "Visual overview of the full research program structure." },
    { title: "Publication Roadmap", path: "/articles/publication-roadmap.html", tags: "publication roadmap arxiv journal submission", excerpt: "Strategy and timeline for paper submissions." },
    { title: "f_NL = -35/8 (Matter Bounce Prediction)", path: "/index.html#predictions", tags: "fnl non-gaussianity bispectrum matter bounce prediction -4.375 -35/8 spherex", excerpt: "Parameter-free prediction: f_NL = -35/8 = -4.375. Testable by SPHEREx at ~5\u03c3." },
    { title: "ALP Birefringence \u03b2 = 0.27\u00b0", path: "/index.html#predictions", tags: "alp birefringence axion cosmic polarization litebird beta 0.27", excerpt: "Planck-scale ALP predicts cosmic birefringence at 0.27\u00b0. LiteBIRD tests at 9\u03c3." },
    { title: "14 Structural Barriers", path: "/index.html#barriers", tags: "barriers structural theorem perturbation transparency mass coupling", excerpt: "Every minimal route from bounce to dark energy is closed by 14 structural barriers." },
    { title: "MCMC Results \u2014 \u0394Neff \u2248 0", path: "/data-explorer.html", tags: "mcmc neff dark radiation hubble h0 sigma8 posterior", excerpt: "309,789 posterior samples confirm \u0394Neff ~ 0, H\u2080 = 67.68 (standard \u039bCDM)." },
    { title: "Contributions", path: "/contributions.html", tags: "contributions community collaborative", excerpt: "Community contributions and collaborative research." },
    { title: "Galaxy Explorer", path: "/galaxy-explorer.html", tags: "galaxy explorer catalog chirality spin", excerpt: "Interactive galaxy catalog exploration tool." }
  ];

  // ── Detect prefix (same approach as nav.js) ──────────────
  var scripts = document.getElementsByTagName('script');
  var prefix = '';
  for (var i = scripts.length - 1; i >= 0; i--) {
    var src = scripts[i].getAttribute('src') || '';
    if (src.indexOf('search.js') !== -1) {
      prefix = src.replace(/search\.js(\?.*)?$/, '');
      break;
    }
  }

  // Resolve a path from the index (which uses absolute /root paths)
  // to the correct relative href based on the detected prefix.
  function resolveHref(absolutePath) {
    // Strip leading slash to get path relative to site root
    var rel = absolutePath.replace(/^\//, '');
    return prefix + rel;
  }

  // ── Inject scoped styles ──────────────────────────────────
  var css = [
    '.bb-search-overlay {',
    '  position: fixed; inset: 0; z-index: 10000;',
    '  background: rgba(0,0,0,0.5);',
    '  display: none; align-items: flex-start; justify-content: center;',
    '  padding-top: 12vh;',
    '  font-family: var(--font-sans, "Inter", system-ui, sans-serif);',
    '}',
    '.bb-search-overlay.active { display: flex; }',
    '',
    '.bb-search-box {',
    '  width: 90%; max-width: 600px;',
    '  background: var(--bg, #fff);',
    '  border: 1px solid var(--border, #eaeaea);',
    '  border-radius: 12px;',
    '  box-shadow: 0 16px 48px rgba(0,0,0,0.2);',
    '  overflow: hidden;',
    '}',
    '',
    '.bb-search-input-wrap {',
    '  display: flex; align-items: center; gap: 10px;',
    '  padding: 14px 18px;',
    '  border-bottom: 1px solid var(--border, #eaeaea);',
    '}',
    '.bb-search-input-wrap svg { flex-shrink: 0; color: var(--text-muted, #999); }',
    '',
    '.bb-search-input {',
    '  flex: 1; border: none; outline: none; background: transparent;',
    '  font-size: 16px; line-height: 1.5;',
    '  color: var(--text, #0a0a0a);',
    '  font-family: var(--font-sans, "Inter", system-ui, sans-serif);',
    '}',
    '.bb-search-input::placeholder { color: var(--text-muted, #999); }',
    '',
    '.bb-search-hint {',
    '  font-size: 11px; color: var(--text-muted, #999);',
    '  padding: 0 4px; border: 1px solid var(--border, #eaeaea);',
    '  border-radius: 4px; font-family: var(--font-mono, monospace);',
    '  line-height: 1.8; flex-shrink: 0;',
    '}',
    '',
    '.bb-search-results {',
    '  max-height: 420px; overflow-y: auto;',
    '  padding: 4px 0;',
    '}',
    '.bb-search-results:empty { display: none; }',
    '',
    '.bb-search-result {',
    '  display: block; padding: 10px 18px;',
    '  text-decoration: none !important; color: var(--text, #0a0a0a);',
    '  border-bottom: 1px solid var(--border, #eaeaea);',
    '  transition: background 80ms ease;',
    '  cursor: pointer;',
    '}',
    '.bb-search-result:last-child { border-bottom: none; }',
    '.bb-search-result:hover,',
    '.bb-search-result.bb-active {',
    '  background: var(--bg-subtle, #fafafa);',
    '}',
    '.bb-search-result-title {',
    '  font-size: 14px; font-weight: 600;',
    '  margin-bottom: 2px; line-height: 1.4;',
    '}',
    '.bb-search-result-excerpt {',
    '  font-size: 12px; color: var(--text-secondary, #444);',
    '  line-height: 1.5; margin-bottom: 2px;',
    '}',
    '.bb-search-result-path {',
    '  font-size: 11px; color: var(--text-muted, #999);',
    '  font-family: var(--font-mono, monospace);',
    '}',
    '.bb-search-result mark {',
    '  background: rgba(250, 204, 21, 0.35);',
    '  color: inherit; border-radius: 2px; padding: 0 1px;',
    '}',
    '[data-theme="dark"] .bb-search-result mark {',
    '  background: rgba(250, 204, 21, 0.2);',
    '}',
    '',
    '.bb-search-empty {',
    '  padding: 24px 18px; text-align: center;',
    '  color: var(--text-muted, #999); font-size: 13px;',
    '}',
    '',
    '/* Nav trigger button */',
    '.bb-search-trigger {',
    '  display: inline-flex; align-items: center; gap: 6px;',
    '  background: none; border: 1px solid var(--border, #eaeaea);',
    '  border-radius: 6px; padding: 3px 10px;',
    '  font-family: var(--font-mono, monospace);',
    '  font-size: 11px; color: var(--text-muted, #999);',
    '  cursor: pointer; transition: border-color 120ms ease, color 120ms ease;',
    '  margin-left: 6px; vertical-align: middle; line-height: 1.8;',
    '}',
    '.bb-search-trigger:hover {',
    '  border-color: var(--border-strong, #d4d4d4);',
    '  color: var(--text-secondary, #444);',
    '}',
    '.bb-search-trigger svg { width: 12px; height: 12px; }',
    '',
    '/* Mobile: hide text, show icon only */',
    '@media (max-width: 768px) {',
    '  .bb-search-trigger span { display: none; }',
    '  .bb-search-trigger { padding: 4px 8px; margin-left: 4px; border: none; }',
    '  .bb-search-trigger svg { width: 15px; height: 15px; }',
    '}'
  ].join('\n');

  var styleEl = document.createElement('style');
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  // ── Build overlay DOM ─────────────────────────────────────
  var overlay = document.createElement('div');
  overlay.className = 'bb-search-overlay';
  overlay.innerHTML = ''
    + '<div class="bb-search-box">'
    + '  <div class="bb-search-input-wrap">'
    + '    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
    + '    <input class="bb-search-input" type="text" placeholder="Search BigBounce..." autocomplete="off" spellcheck="false">'
    + '    <span class="bb-search-hint">esc</span>'
    + '  </div>'
    + '  <div class="bb-search-results"></div>'
    + '</div>';

  document.body.appendChild(overlay);

  var input = overlay.querySelector('.bb-search-input');
  var resultsEl = overlay.querySelector('.bb-search-results');
  var activeIdx = -1;

  // ── Search logic ──────────────────────────────────────────
  function scoreEntry(entry, words) {
    var score = 0;
    var titleLower = entry.title.toLowerCase();
    var tagsLower = entry.tags.toLowerCase();
    var excerptLower = entry.excerpt.toLowerCase();

    for (var i = 0; i < words.length; i++) {
      var w = words[i];
      if (titleLower.indexOf(w) !== -1) score += 10;
      if (tagsLower.indexOf(w) !== -1) score += 5;
      if (excerptLower.indexOf(w) !== -1) score += 2;
    }
    return score;
  }

  function highlightText(text, words) {
    if (!words.length) return escapeHtml(text);
    // Build regex from words, escaping special chars
    var escaped = words.map(function (w) {
      return w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    });
    var re = new RegExp('(' + escaped.join('|') + ')', 'gi');
    // Split on matches and reassemble with marks
    var parts = text.split(re);
    var out = '';
    for (var i = 0; i < parts.length; i++) {
      if (re.test(parts[i])) {
        out += '<mark>' + escapeHtml(parts[i]) + '</mark>';
      } else {
        out += escapeHtml(parts[i]);
      }
      // Reset lastIndex since we reuse the regex
      re.lastIndex = 0;
    }
    return out;
  }

  function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function search(query) {
    var raw = query.trim().toLowerCase();
    if (!raw) {
      resultsEl.innerHTML = '';
      activeIdx = -1;
      return;
    }

    var words = raw.split(/\s+/).filter(function (w) { return w.length > 0; });

    var scored = [];
    for (var i = 0; i < SEARCH_INDEX.length; i++) {
      var s = scoreEntry(SEARCH_INDEX[i], words);
      if (s > 0) {
        scored.push({ entry: SEARCH_INDEX[i], score: s });
      }
    }

    scored.sort(function (a, b) { return b.score - a.score; });
    var top = scored.slice(0, 10);

    if (top.length === 0) {
      resultsEl.innerHTML = '<div class="bb-search-empty">No results for \u201c' + escapeHtml(query.trim()) + '\u201d</div>';
      activeIdx = -1;
      return;
    }

    var html = '';
    for (var j = 0; j < top.length; j++) {
      var e = top[j].entry;
      var href = resolveHref(e.path);
      html += '<a class="bb-search-result" href="' + href + '" data-idx="' + j + '">'
        + '<div class="bb-search-result-title">' + highlightText(e.title, words) + '</div>'
        + '<div class="bb-search-result-excerpt">' + highlightText(e.excerpt, words) + '</div>'
        + '<div class="bb-search-result-path">' + escapeHtml(e.path) + '</div>'
        + '</a>';
    }
    resultsEl.innerHTML = html;
    activeIdx = -1;
  }

  // ── Keyboard navigation within results ────────────────────
  function updateActive() {
    var items = resultsEl.querySelectorAll('.bb-search-result');
    for (var i = 0; i < items.length; i++) {
      if (i === activeIdx) {
        items[i].classList.add('bb-active');
        items[i].scrollIntoView({ block: 'nearest' });
      } else {
        items[i].classList.remove('bb-active');
      }
    }
  }

  // ── Open / Close ──────────────────────────────────────────
  function openSearch() {
    overlay.classList.add('active');
    input.value = '';
    resultsEl.innerHTML = '';
    activeIdx = -1;
    // Slight delay so the overlay is painted before focus
    setTimeout(function () { input.focus(); }, 20);
  }

  function closeSearch() {
    overlay.classList.remove('active');
    input.value = '';
    resultsEl.innerHTML = '';
    activeIdx = -1;
  }

  function isSearchOpen() {
    return overlay.classList.contains('active');
  }

  // ── Event: input ──────────────────────────────────────────
  input.addEventListener('input', function () {
    search(input.value);
  });

  // ── Event: keyboard in input ──────────────────────────────
  input.addEventListener('keydown', function (e) {
    var items = resultsEl.querySelectorAll('.bb-search-result');
    var count = items.length;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      activeIdx = (activeIdx + 1) % (count || 1);
      if (activeIdx >= count) activeIdx = 0;
      updateActive();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      activeIdx = activeIdx <= 0 ? count - 1 : activeIdx - 1;
      updateActive();
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (activeIdx >= 0 && activeIdx < count) {
        items[activeIdx].click();
      } else if (count > 0) {
        items[0].click();
      }
    } else if (e.key === 'Escape') {
      e.preventDefault();
      closeSearch();
    }
  });

  // ── Event: click result navigates ─────────────────────────
  resultsEl.addEventListener('click', function (e) {
    var link = e.target.closest('.bb-search-result');
    if (link) {
      closeSearch();
      // Let the default <a> navigation happen
    }
  });

  // ── Event: click backdrop to close ────────────────────────
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) {
      closeSearch();
    }
  });

  // ── Global keyboard shortcut ──────────────────────────────
  document.addEventListener('keydown', function (e) {
    // Don't trigger if user is typing in an input, textarea, or contenteditable
    var tag = (e.target.tagName || '').toLowerCase();
    var isEditable = tag === 'input' || tag === 'textarea' || tag === 'select' || e.target.isContentEditable;

    // Cmd+K / Ctrl+K — always (even from inputs)
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (isSearchOpen()) {
        closeSearch();
      } else {
        openSearch();
      }
      return;
    }

    // "/" key — only when not in an input
    if (e.key === '/' && !isEditable && !e.metaKey && !e.ctrlKey && !e.altKey) {
      e.preventDefault();
      openSearch();
      return;
    }

    // Escape — close if open
    if (e.key === 'Escape' && isSearchOpen()) {
      closeSearch();
    }
  });

  // ── Inject trigger button into nav ────────────────────────
  function injectNavTrigger() {
    var navLinks = document.querySelector('.nav-links');
    if (!navLinks) return;

    var btn = document.createElement('button');
    btn.className = 'bb-search-trigger';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Search site');
    btn.innerHTML = ''
      + '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
      + '<span>' + (navigator.platform.indexOf('Mac') !== -1 ? '\u2318K' : 'Ctrl+K') + '</span>';

    btn.addEventListener('click', function (e) {
      e.preventDefault();
      openSearch();
    });

    // Insert after the last link in .nav-links
    navLinks.appendChild(btn);
  }

  // Run on DOMContentLoaded if not yet fired, otherwise immediately
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectNavTrigger);
  } else {
    injectNavTrigger();
  }

})();

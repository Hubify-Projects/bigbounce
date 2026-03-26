/**
 * BigBounce — Shared Navigation
 *
 * Single source of truth for sidebar, topbar, and inline nav.
 * Include via <script src="[prefix]nav.js"></script> in <head> or <body>.
 * The script auto-detects its depth from its own src path and
 * sets all href prefixes accordingly.
 *
 * Active page is determined by matching data-page to the current URL.
 */
(function () {
  'use strict';

  // ── Inject favicon ──
  var favicon = document.createElement('link');
  favicon.rel = 'icon';
  favicon.type = 'image/svg+xml';
  favicon.href = 'data:image/svg+xml,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="%230a0a0a"/><text x="16" y="22" text-anchor="middle" font-family="serif" font-size="18" font-weight="bold" fill="%23fff">BB</text></svg>');
  document.head.appendChild(favicon);

  // ── Restore theme preference (early, to prevent flash) ──
  var storedTheme = null;
  try { storedTheme = localStorage.getItem('bb_theme'); } catch (e) {}
  if (storedTheme === 'dark' || storedTheme === 'light') {
    document.documentElement.setAttribute('data-theme', storedTheme);
  }

  // ── Determine path prefix from the script tag's own src ──
  var scripts = document.getElementsByTagName('script');
  var prefix = '';
  for (var i = scripts.length - 1; i >= 0; i--) {
    var src = scripts[i].getAttribute('src') || '';
    if (src.indexOf('nav.js') !== -1) {
      prefix = src.replace(/nav\.js(\?.*)?$/, '');
      break;
    }
  }

  // ── Detect active page from URL ──
  var path = location.pathname;
  var activePage = '';
  if (/\/index\.html$/.test(path) || /\/$/.test(path)) {
    if (path.indexOf('/review') !== -1) activePage = 'review';
    else if (path.indexOf('/dossier') !== -1 || path.indexOf('/project_master_dossier') !== -1) activePage = 'dossier';
    else activePage = 'index';
  } else if (path.indexOf('/paper') !== -1) activePage = 'paper';
  else if (path.indexOf('/explained') !== -1) activePage = 'explained';
  else if (path.indexOf('/datasets') !== -1) activePage = 'datasets';
  else if (path.indexOf('/data-explorer') !== -1) activePage = 'data-explorer';
  else if (path.indexOf('/anomaly-explorer') !== -1) activePage = 'anomaly-explorer';
  else if (path.indexOf('/galaxy-explorer') !== -1) activePage = 'galaxy-explorer';
  else if (path.indexOf('/figures') !== -1) activePage = 'figures';
  else if (path.indexOf('/glossary') !== -1) activePage = 'glossary';
  else if (path.indexOf('/articles') !== -1) activePage = 'articles';
  else if (path.indexOf('/timeline') !== -1) activePage = 'timeline';
  else if (path.indexOf('/visualize') !== -1) activePage = 'visualize';
  else if (path.indexOf('/contributions') !== -1) activePage = 'contributions';
  else if (path.indexOf('/activity') !== -1) activePage = 'activity';
  else if (path.indexOf('/review') !== -1) activePage = 'review';
  else if (path.indexOf('/chat') !== -1) activePage = 'astro';
  else if (path.indexOf('/admin') !== -1) activePage = 'admin';
  else if (path.indexOf('/sources') !== -1) activePage = 'sources';
  else if (path.indexOf('/dossier') !== -1 || path.indexOf('/project_master_dossier') !== -1) activePage = 'dossier';

  // ── Helper: mark active ──
  function activeAttr(page) {
    return page === activePage ? ' class="active"' : '';
  }

  function sidebarActiveClass(page, baseClass) {
    return baseClass + (page === activePage ? ' active' : '');
  }

  // ── Path helper ──
  function p(file) { return prefix + file; }

  // ── GitHub SVG icon ──
  var ghIcon = '<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>';

  // ── Hamburger SVG ──
  var menuIcon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="8" x2="20" y2="8"/><line x1="4" y1="16" x2="16" y2="16"/></svg>';

  // ── Build sidebar ──
  var sidebar = ''
    + '<button class="sidebar-toggle" aria-label="Menu">' + menuIcon + '</button>'
    + '<aside class="sidebar">'
    + '<a href="' + p('index.html') + '" class="sidebar-brand">bigbounce</a>'
    + '<button class="sidebar-close">&laquo;</button>'
    + '<nav class="sidebar-nav">'
    + '<a href="' + p('index.html') + '" class="' + sidebarActiveClass('index', 'sidebar-section') + '" data-page="index">research/</a>'
    + '<a href="' + p('paper.html') + '" class="' + sidebarActiveClass('paper', 'sidebar-link') + '" data-page="paper">papers</a>'
    + '<a href="' + p('explained.html') + '" class="' + sidebarActiveClass('explained', 'sidebar-link') + '" data-page="explained">explainer</a>'
    + '<a href="' + p('datasets.html') + '" class="' + sidebarActiveClass('datasets', 'sidebar-link') + '" data-page="datasets">data/</a>'
    + '<div class="sidebar-sub">'
    + '<a href="' + p('datasets.html') + '" class="sidebar-link">datasets</a>'
    + '<a href="' + p('data-explorer.html') + '" class="' + sidebarActiveClass('data-explorer', 'sidebar-link') + '" data-page="data-explorer">data explorer</a>'
    + '<a href="' + p('galaxy-explorer.html') + '" class="' + sidebarActiveClass('galaxy-explorer', 'sidebar-link') + '" data-page="galaxy-explorer">galaxy explorer</a>'
    + '<a href="' + p('anomaly-explorer.html') + '" class="' + sidebarActiveClass('anomaly-explorer', 'sidebar-link') + '" data-page="anomaly-explorer">anomaly explorer</a>'
    + '</div>'
    + '<a href="' + p('figures.html') + '" class="' + sidebarActiveClass('figures', 'sidebar-link') + '" data-page="figures">figures</a>'
    + '<a href="' + p('glossary.html') + '" class="' + sidebarActiveClass('glossary', 'sidebar-link') + '" data-page="glossary">glossary</a>'
    + '<a href="' + p('articles.html') + '" class="' + sidebarActiveClass('articles', 'sidebar-link') + '" data-page="articles">articles</a>'
    + '<a href="' + p('timeline.html') + '" class="' + sidebarActiveClass('timeline', 'sidebar-link') + '" data-page="timeline">timeline</a>'
    + '<a href="' + p('visualize.html') + '" class="' + sidebarActiveClass('visualize', 'sidebar-link') + '" data-page="visualize">visualize</a>'
    + '<a href="' + p('contributions.html') + '" class="' + sidebarActiveClass('contributions', 'sidebar-link') + '" data-page="contributions">contributions</a>'
    + '<a href="' + p('activity.html') + '" class="' + sidebarActiveClass('activity', 'sidebar-link') + '" data-page="activity">activity</a>'
    + '<a href="' + p('review/index.html') + '" class="' + sidebarActiveClass('review', 'sidebar-link') + '" data-page="review">review</a>'
    + '<a href="' + p('chat.html') + '" class="' + sidebarActiveClass('astro', 'sidebar-link') + '" data-page="astro">astro</a>'
    + '<a href="' + p('research/project_master_dossier/index.html') + '" class="' + sidebarActiveClass('dossier', 'sidebar-link') + '" data-page="dossier">dossier</a>'
    + '</nav>'
    + '<div class="sidebar-footer">Houston Golden<br>Independent Researcher<br>houston@hubify.com<br>'
    + '<a href="https://github.com/Hubify-Projects/bigbounce" target="_blank" style="display:inline-flex;align-items:center;gap:5px;margin-top:8px;color:var(--text-tertiary);text-decoration:none;font-size:12px;">' + ghIcon + 'GitHub</a>'
    + '</div>'
    + '</aside>';

  // ── Build topbar ──
  var topbar = '<div class="topbar">'
    + '<span>March 2026 &middot; GR-QC &middot; ASTRO-PH.CO &middot; HEP-TH</span>'
    + '<span class="topbar-right">Houston Golden &middot; Independent Researcher</span>'
    + '</div>';

  // ── Build inline nav ──
  var inlineNav = '<nav><div class="nav-inner">'
    + '<a href="' + p('index.html') + '" class="brand">bigbounce</a>'
    + '<button class="nav-toggle" aria-label="Menu">' + menuIcon + '</button>'
    + '<div class="nav-links">'
    + '<a href="' + p('index.html') + '" data-page="index"' + activeAttr('index') + '>research</a>'
    + '<a href="' + p('paper.html') + '" data-page="paper"' + activeAttr('paper') + '>papers</a>'
    + '<a href="' + p('explained.html') + '" data-page="explained"' + activeAttr('explained') + '>explainer</a>'
    + '<a href="' + p('data-explorer.html') + '" data-page="datasets"' + activeAttr('datasets') + '>data</a>'
    + '<a href="' + p('figures.html') + '" data-page="figures"' + activeAttr('figures') + '>figures</a>'
    + '<a href="' + p('glossary.html') + '" data-page="glossary"' + activeAttr('glossary') + '>glossary</a>'
    + '<a href="' + p('articles.html') + '" data-page="articles"' + activeAttr('articles') + '>articles</a>'
    + '<a href="' + p('activity.html') + '" data-page="activity"' + activeAttr('activity') + '>activity</a>'
    + '<a href="' + p('review/index.html') + '" data-page="review"' + activeAttr('review') + '>review</a>'
    + '<a href="' + p('chat.html') + '" data-page="astro"' + activeAttr('astro') + '>astro</a>'
    + '<a href="' + p('research/project_master_dossier/index.html') + '" data-page="dossier"' + activeAttr('dossier') + '>dossier</a>'
    + '</div>'
    + '<span class="nav-meta">Houston Golden &middot; gr-qc</span>'
    + '<button class="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode"></button>'
    + '</div></nav>';

  // ── Inject into page ──
  // 1. Inject sidebar + topbar at the start of <body>
  // 2. Wrap ALL remaining body content in .site-content for proper layout offset
  var navFragment = sidebar + topbar;
  document.body.insertAdjacentHTML('afterbegin', navFragment);

  // Build the .site-content wrapper via DOM so it properly contains page content
  var siteContent = document.createElement('div');
  siteContent.className = 'site-content';
  siteContent.insertAdjacentHTML('afterbegin', inlineNav);

  // Move all body children (except sidebar, toggle, topbar) into the wrapper
  var nodesToMove = [];
  var child = document.body.firstChild;
  while (child) {
    var next = child.nextSibling;
    if (child.nodeType === 1) {
      var tag = child.tagName;
      var cl = child.classList || { contains: function() { return false; } };
      if (!cl.contains('sidebar') && !cl.contains('sidebar-toggle') && !cl.contains('topbar')) {
        nodesToMove.push(child);
      }
    } else if (child.nodeType === 3 && child.textContent.trim()) {
      nodesToMove.push(child);
    }
    child = next;
  }
  for (var j = 0; j < nodesToMove.length; j++) {
    siteContent.appendChild(nodesToMove[j]);
  }
  document.body.appendChild(siteContent);

  // ── Wire up sidebar toggle/close ──
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebarEl = document.querySelector('.sidebar');
  var closeBtn = document.querySelector('.sidebar-close');
  var isMobile = function () { return window.innerWidth <= 900; };

  if (toggle && sidebarEl) {
    toggle.addEventListener('click', function () {
      if (isMobile()) {
        // Mobile: slide sidebar open as overlay
        sidebarEl.classList.toggle('open');
        toggle.style.visibility = sidebarEl.classList.contains('open') ? 'hidden' : 'visible';
      } else {
        // Desktop: uncollapse sidebar
        document.body.classList.remove('sidebar-collapsed');
        toggle.style.display = 'none';
      }
    });
  }
  if (closeBtn && sidebarEl) {
    closeBtn.addEventListener('click', function () {
      if (isMobile()) {
        sidebarEl.classList.remove('open');
        if (toggle) toggle.style.visibility = 'visible';
      } else {
        // Desktop: collapse sidebar
        document.body.classList.add('sidebar-collapsed');
      }
    });
  }

  // ── Wire up mobile nav toggle ──
  var navToggle = document.querySelector('.nav-toggle');
  if (navToggle) {
    navToggle.addEventListener('click', function () {
      this.parentElement.classList.toggle('open');
    });
  }

  // ── Theme toggle ──
  function getEffectiveTheme() {
    var attr = document.documentElement.getAttribute('data-theme');
    if (attr === 'dark' || attr === 'light') return attr;
    // No explicit preference — check system
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) return 'dark';
    return 'light';
  }

  function updateToggleIcon(btn) {
    btn.textContent = getEffectiveTheme() === 'dark' ? '\u2600' : '\u263E';
    btn.title = getEffectiveTheme() === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
  }

  var themeBtn = document.querySelector('.theme-toggle');
  if (themeBtn) {
    updateToggleIcon(themeBtn);
    themeBtn.addEventListener('click', function () {
      var current = getEffectiveTheme();
      var next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('bb_theme', next); } catch (e) {}
      updateToggleIcon(themeBtn);
    });

    // Update icon if system preference changes (and no manual override)
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
        updateToggleIcon(themeBtn);
      });
    }
  }

  // ── Load site search ──
  var searchScript = document.createElement('script');
  searchScript.src = prefix + 'search.js';
  searchScript.defer = true;
  document.head.appendChild(searchScript);
})();

/* =============================================================================
   BigBounce internal gate (client-side)
   Any page that includes this script is treated as "internal" and will
   show a full-screen password overlay unless the session is unlocked.
   Password is obfuscated (base64 + XOR + reversed) — not for hard security,
   just to keep casual visitors out. Real secrets don't live in the static site.
============================================================================= */
(function () {
  'use strict';

  var KEY = 'bb_internal_unlocked';

  // Obfuscated hash of the password. We compare SHA-256 instead of plaintext
  // so the password doesn't literally sit in the script. Fingerprint of "bamf".
  var EXPECTED_HASH = 'a2cca09bd51fe22893420feb0a2c4dbe0885b698b13326e6b6994b6b0168aa90';

  function hash(s) {
    // SHA-256 via SubtleCrypto
    var enc = new TextEncoder().encode(s);
    return crypto.subtle.digest('SHA-256', enc).then(function (buf) {
      var arr = Array.from(new Uint8Array(buf));
      return arr.map(function (b) { return b.toString(16).padStart(2, '0'); }).join('');
    });
  }

  function isUnlocked() {
    try { return sessionStorage.getItem(KEY) === '1'; } catch (e) { return false; }
  }

  function markUnlocked() {
    try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
  }

  function injectOverlay() {
    // Hide body until resolved to prevent FOUC
    var style = document.createElement('style');
    style.textContent = 'html,body{overflow:hidden!important;}body>*:not(#bb-gate){display:none!important;}';
    document.documentElement.appendChild(style);

    function mount() {
      var ov = document.createElement('div');
      ov.id = 'bb-gate';
      ov.style.cssText = [
        'position:fixed','inset:0','z-index:2147483647',
        'background:#0b0d10','color:#e6e8eb',
        'font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Inter",system-ui,sans-serif',
        'display:flex','align-items:center','justify-content:center',
        'padding:24px'
      ].join(';');
      ov.innerHTML = '' +
        '<div style="max-width:380px;width:100%;">' +
          '<div style="font-family:\'Newsreader\',Georgia,serif;font-size:28px;font-weight:500;letter-spacing:-0.01em;color:#f3f4f6;margin-bottom:6px;">Internal</div>' +
          '<div style="font-size:13px;color:#9aa0a6;line-height:1.5;margin-bottom:24px;">This area is not part of the public BigBounce site. Enter the access phrase to continue, or <a href="/" style="color:#9aa0a6;text-decoration:underline;">return to the public site</a>.</div>' +
          '<form id="bb-gate-form" autocomplete="off">' +
            '<input id="bb-gate-input" type="password" placeholder="Access phrase" autocapitalize="off" autocorrect="off" spellcheck="false" ' +
              'style="width:100%;padding:10px 12px;font-size:14px;font-family:inherit;background:#15181c;color:#e6e8eb;border:1px solid #2a2f36;border-radius:6px;outline:none;margin-bottom:12px;" autofocus>' +
            '<button type="submit" style="width:100%;padding:10px 12px;font-size:13px;font-weight:500;font-family:inherit;background:#e6e8eb;color:#0b0d10;border:0;border-radius:6px;cursor:pointer;">Unlock</button>' +
            '<div id="bb-gate-err" style="font-size:12px;color:#f87171;margin-top:10px;min-height:16px;"></div>' +
          '</form>' +
          '<div style="font-size:11px;color:#5f6368;margin-top:32px;line-height:1.6;">Public pages: <a href="/" style="color:#9aa0a6;">Research</a> · <a href="/paper.html" style="color:#9aa0a6;">Papers</a> · <a href="/data-explorer.html" style="color:#9aa0a6;">Data</a> · <a href="/figures.html" style="color:#9aa0a6;">Figures</a> · <a href="/explained.html" style="color:#9aa0a6;">Explainer</a></div>' +
        '</div>';
      document.body.appendChild(ov);

      var form = document.getElementById('bb-gate-form');
      var input = document.getElementById('bb-gate-input');
      var err = document.getElementById('bb-gate-err');
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var val = (input.value || '').trim();
        hash(val).then(function (h) {
          if (h === EXPECTED_HASH) {
            markUnlocked();
            style.remove();
            ov.remove();
          } else {
            err.textContent = 'Not recognized.';
            input.value = '';
            input.focus();
          }
        });
      });
      input.focus();
    }

    if (document.body) mount();
    else document.addEventListener('DOMContentLoaded', mount);
  }

  if (!isUnlocked()) injectOverlay();
})();

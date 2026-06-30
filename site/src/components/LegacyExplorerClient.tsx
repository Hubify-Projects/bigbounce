"use client";

import { useEffect, useMemo, useRef } from "react";

// Shared image-failure utility injected before the page's own script.
// Both anomaly-explorer and galaxy-explorer HTML files call window.__legacyImgFail.
const SHARED_IMG_UTIL = `
(function() {
  window.__legacyImgFail = function(img, labelLines) {
    var lines = Array.isArray(labelLines) ? labelLines : [labelLines];
    var w = img.offsetWidth || parseInt(img.style.width) || 48;
    var h = img.offsetHeight || parseInt(img.style.height) || 48;
    var isFig = w > 100;
    var ph = document.createElement('div');
    if (isFig) {
      ph.style.cssText =
        'width:100%;min-height:160px;background:color-mix(in srgb,var(--bg-subtle,#1e293b) 80%,transparent);' +
        'border:1px solid var(--border,#334155);display:flex;flex-direction:column;align-items:center;' +
        'justify-content:center;gap:6px;padding:16px;box-sizing:border-box;';
      ph.innerHTML =
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--text-muted,#64748b)" stroke-width="1.5">' +
          '<rect x="3" y="3" width="18" height="18" rx="2"/>' +
          '<circle cx="8.5" cy="8.5" r="1.5"/>' +
          '<path d="m21 15-5-5L5 21"/>' +
        '</svg>' +
        lines.map(function(l) {
          return '<span style="font-size:11px;color:var(--text-muted,#64748b);font-family:monospace;text-align:center;">' + l + '</span>';
        }).join('');
    } else {
      ph.style.cssText =
        'width:' + w + 'px;height:' + h + 'px;background:var(--bg-subtle,#1e293b);' +
        'border:1px solid var(--border,#334155);display:inline-flex;flex-direction:column;' +
        'align-items:center;justify-content:center;gap:1px;padding:2px;box-sizing:border-box;vertical-align:middle;';
      ph.innerHTML = lines.map(function(l) {
        return '<span style="font-size:8px;color:var(--text-muted,#64748b);font-family:monospace;text-align:center;line-height:1.2;word-break:break-all;">' + l + '</span>';
      }).join('');
    }
    if (img.parentNode) img.parentNode.replaceChild(ph, img);
  };
})();
`;

export function LegacyExplorerClient({
  body,
  script,
}: {
  body: string;
  script: string;
}) {
  const rootRef = useRef<HTMLDivElement>(null);
  const runnableScript = useMemo(
    () =>
      script
        .replace(/^const /gm, "var ")
        .replace(/^let /gm, "var "),
    [script],
  );

  useEffect(() => {
    const root = rootRef.current;
    if (!root) return;

    // Inject shared utility first so page scripts and onerror handlers can reference it.
    const utilEl = document.createElement("script");
    utilEl.text = SHARED_IMG_UTIL;
    root.appendChild(utilEl);

    const scriptEl = document.createElement("script");
    scriptEl.text = runnableScript;
    root.appendChild(scriptEl);

    return () => {
      utilEl.remove();
      scriptEl.remove();
    };
  }, [runnableScript]);

  return (
    <div
      ref={rootRef}
      dangerouslySetInnerHTML={{ __html: body }}
      suppressHydrationWarning
    />
  );
}

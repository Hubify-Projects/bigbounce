"use client";

import { useEffect, useMemo, useRef } from "react";

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

    const scriptEl = document.createElement("script");
    scriptEl.text = runnableScript;
    root.appendChild(scriptEl);

    return () => {
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

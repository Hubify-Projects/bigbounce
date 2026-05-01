"use client";

import { useEffect, useMemo, useRef } from "react";

declare global {
  interface Window {
    selectDataset?: (key: string) => void;
    currentDatasetKey?: string;
  }
}

export function DataExplorerClient({
  body,
  script,
}: {
  body: string;
  script: string;
}) {
  const rootRef = useRef<HTMLDivElement>(null);
  const runnableScript = useMemo(
    () =>
      `${script
        .replace(/^const /gm, "var ")
        .replace(/^let /gm, "var ")}

if (typeof window.selectDataset === "function") {
  window.selectDataset(window.currentDatasetKey || "modelDiscrimination");
}`,
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

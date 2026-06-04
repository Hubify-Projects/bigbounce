import type { Metadata } from "next";
import DocsClient from "./DocsClient";
import "./docs.css";

export const metadata: Metadata = {
  title: "Docs — API, MCP, Skills",
  description:
    "BigBounce stack documentation: Convex schema, read/write API surface, bigbounce-mcp tools, agent skill catalog, novelty + review policy, security posture. Read-only — no API keys, no mutation forms, no external interactions exposed.",
};

export default function DocsPage() {
  return <DocsClient />;
}

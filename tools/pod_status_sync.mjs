#!/usr/bin/env node
/**
 * Sync RunPod pod state into the Convex `pods` table so the site's
 * /status "Active Compute" panel stays fresh.
 *
 * Polls RunPod GraphQL (direct REST — the Python SDK is unreliable),
 * upserts every pod, and optionally attaches a per-job manifest from
 * project-context/SSOT/compute-queue.json (written by the pod-setup
 * workflow; maps podId → jobs[]).
 *
 * Usage:
 *   node tools/pod_status_sync.mjs                 # sync to dev + prod
 *   node tools/pod_status_sync.mjs --prod-only
 *
 * Idempotent. Safe to run from cron/loop.
 */
import { readFileSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..");

function loadEnv() {
  const out = {};
  const p = resolve(REPO, ".env.local");
  if (!existsSync(p)) return out;
  for (const line of readFileSync(p, "utf8").split("\n")) {
    const m = line.match(/^([A-Z_][A-Z0-9_]*)=(.*)$/);
    if (m) out[m[1]] = m[2].trim();
  }
  return out;
}

async function fetchPods(apiKey) {
  const res = await fetch("https://api.runpod.io/graphql", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: `query { myself { pods {
        id name desiredStatus costPerHr gpuCount
        containerDiskInGb volumeInGb
        runtime { uptimeInSeconds }
        machine { gpuDisplayName }
      } } }`,
    }),
  });
  if (!res.ok) throw new Error(`RunPod GraphQL ${res.status}`);
  const json = await res.json();
  if (json.errors) throw new Error(JSON.stringify(json.errors));
  return json.data.myself.pods || [];
}

function loadJobManifest() {
  const p = resolve(REPO, "project-context/SSOT/compute-queue.json");
  if (!existsSync(p)) return {};
  try {
    return JSON.parse(readFileSync(p, "utf8"));
  } catch {
    return {};
  }
}

async function main() {
  const env = loadEnv();
  const apiKey = env.RUNPOD_API_KEY || process.env.RUNPOD_API_KEY;
  if (!apiKey) {
    console.error("No RUNPOD_API_KEY — abort");
    process.exit(1);
  }

  const pods = await fetchPods(apiKey);
  const manifest = loadJobManifest(); // { "<podId>": { jobs: [...], startedAt, purpose } }
  console.log(`RunPod reports ${pods.length} pods`);

  const prodOnly = process.argv.includes("--prod-only");
  const targets = [];
  if (!prodOnly && env.CONVEX_URL) targets.push(env.CONVEX_URL);
  // prod deployment (site reads NEXT_PUBLIC_CONVEX_URL at build; both kept in sync)
  targets.push("https://diligent-wolverine-324.convex.cloud");

  for (const url of [...new Set(targets)]) {
    const client = new ConvexHttpClient(url);
    for (const pod of pods) {
      const status =
        pod.desiredStatus === "RUNNING"
          ? "running"
          : pod.desiredStatus === "EXITED"
            ? "exited"
            : "terminated";
      const meta = manifest[pod.id] || {};
      const uptimeS = pod.runtime?.uptimeInSeconds || 0;
      const startedAt = meta.startedAt || Date.now() - uptimeS * 1000;
      await client.mutation(api.pods.upsert, {
        podId: pod.id,
        name: pod.name,
        status,
        gpu: pod.machine?.gpuDisplayName || "unknown",
        volumeGb: pod.volumeInGb || 0,
        containerGb: pod.containerDiskInGb || 0,
        hourlyCostUsd: status === "running" ? pod.costPerHr : 0,
        startedAt,
        totalCostUsd: meta.totalCostUsd ?? (uptimeS / 3600) * pod.costPerHr,
        purpose: meta.purpose || "(no manifest entry — see compute-queue.json)",
        artifactsBackedUp: meta.artifactsBackedUp ?? false,
        backupLocations: meta.backupLocations ?? [],
        jobs: meta.jobs,
      });
      console.log(`  [${url.includes("diligent") ? "prod" : "dev"}] ${pod.id} ${pod.name} → ${status}${meta.jobs ? ` (${meta.jobs.length} jobs)` : ""}`);
    }
  }
  console.log("Sync complete.");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

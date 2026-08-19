import assert from "node:assert/strict";
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import YAML from "yaml";
import { checkManifest } from "./check-hubify-lab-manifest.mjs";

test("checked-in Hubify projection matches site metadata, files, and hashes", async () => {
  const result = await checkManifest();
  assert.deepEqual(result, {
    ok: true,
    manifestPath: "project-context/hubify-lab/lab.yaml",
    siteMetadataPath: "site/src/data/papers.ts",
    scienceSnapshotCommit: "d957c0cd5d8d589b413f99f3bf1cacd32e595aae",
    programs: 6,
  });
});

test("manifest check reports deterministic artifact drift", async () => {
  const root = process.cwd();
  const manifest = YAML.parse(await readFile(join(root, "project-context/hubify-lab/lab.yaml"), "utf8"));
  manifest.programs[0].paper_sha256 = "0".repeat(64);
  const directory = await mkdtemp(join(tmpdir(), "bigbounce-lab-manifest-"));
  try {
    const manifestPath = join(directory, "lab.yaml");
    await writeFile(manifestPath, YAML.stringify(manifest));
    await assert.rejects(
      checkManifest({ manifestPath, siteMetadataPath: join(root, "site/src/data/papers.ts"), repoRoot: root }),
      /p1a: manifest hash 0{64} != file 210be8f0b285034d88b9854c532eaac4a32147cea2621dedbaaac94540bbc7f0/,
    );
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

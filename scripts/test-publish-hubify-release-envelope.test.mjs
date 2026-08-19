import assert from "node:assert/strict";
import { generateKeyPairSync } from "node:crypto";
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { buildEnvelope, canonicalJson, parseArgs, validateEnvelopeStructure } from "./publish-hubify-release-envelope.mjs";

const payload = {
  hubify_lab: 0.1,
  source: { current_commit: "fixture-commit", authoritative_repo: "https://github.com/Hubify-Projects/bigbounce" },
  programs: [{ id: "p1a", title: "ECH No-Go", version: "v1A.0.127", paper_pdf: "site/public/papers/p1.pdf" }],
};

test("canonicalJson is key-order independent and matches the Hubify contract", () => {
  assert.equal(canonicalJson({ z: 1, a: { d: true, c: null } }), '{"a":{"c":null,"d":true},"z":1}');
});

test("signed envelope verifies with the generated public key", () => {
  const { privateKey, publicKey } = generateKeyPairSync("ed25519");
  const envelope = buildEnvelope(payload, "2026-08-19.1", privateKey);
  validateEnvelopeStructure(envelope, { requireSignature: true, trustedPublicKey: publicKey });
  assert.equal(envelope.schemaVersion, "hubify-lab/v1");
  assert.equal(envelope.integrity.canonicalization, "jcs-lite-v1");
});

test("unsigned structural envelope is valid only when explicitly allowed", () => {
  const envelope = buildEnvelope(payload, "fixture-unsigned");
  validateEnvelopeStructure(envelope, { requireSignature: false });
  assert.throws(() => validateEnvelopeStructure(envelope, { requireSignature: true }), /requires an ed25519 signature/);
});

test("CLI argument parsing accepts explicit path and environment-friendly flags", () => {
  assert.deepEqual(parseArgs(["--manifest=source.yaml", "--output", "release.json", "--manifest-version", "2026.08.19", "--dry-run"]), {
    manifest: "source.yaml", output: "release.json", manifestVersion: "2026.08.19", privateKeyPath: null, publicKeyPath: null, check: false, dryRun: true, unsigned: false,
  });
});

test("written envelope is deterministic for the same source, version, and key", async () => {
  const { privateKey } = generateKeyPairSync("ed25519");
  const first = buildEnvelope(payload, "fixed", privateKey);
  const second = buildEnvelope(JSON.parse(JSON.stringify(payload)), "fixed", privateKey);
  assert.deepEqual(second, first);
  const directory = await mkdtemp(join(tmpdir(), "bigbounce-envelope-"));
  try {
    await writeFile(join(directory, "envelope.json"), JSON.stringify(first, null, 2) + "\n");
    assert.equal(JSON.parse(await readFile(join(directory, "envelope.json"), "utf8")).integrity.digest, first.integrity.digest);
  } finally { await rm(directory, { recursive: true, force: true }); }
});

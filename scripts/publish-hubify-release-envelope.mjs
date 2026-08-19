#!/usr/bin/env node

/**
 * Publish the BigBounce lab projection in Hubify's signed envelope format.
 *
 * The payload is intentionally treated as opaque: the source manifest remains
 * the scientific authority, while this tool only applies the transport
 * envelope and its deterministic integrity/signature fields.
 */
import { createHash, createPrivateKey, createPublicKey, sign, verify } from "node:crypto";
import { readFile, writeFile } from "node:fs/promises";
import process from "node:process";
import YAML from "yaml";

export const SCHEMA_VERSION = "hubify-lab/v1";
export const CANONICALIZATION = "jcs-lite-v1";

export function canonicalJson(value) {
  if (value === null || typeof value !== "object") return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(",")}]`;
  return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`).join(",")}}`;
}

function digestPayload(payload) {
  return createHash("sha256").update(Buffer.from(canonicalJson(payload))).digest("hex");
}

export function validatePayload(payload) {
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    throw new Error("manifest payload must be a JSON/YAML object");
  }
  if (!payload.source || typeof payload.source !== "object" || Array.isArray(payload.source)) {
    throw new Error("manifest payload requires a source object");
  }
  if (!Array.isArray(payload.programs) || payload.programs.length === 0) {
    throw new Error("manifest payload requires a non-empty programs array");
  }
  for (const [index, program] of payload.programs.entries()) {
    if (!program || typeof program !== "object" || Array.isArray(program)) {
      throw new Error(`manifest programs[${index}] must be an object`);
    }
    for (const field of ["id", "version", "paper_pdf"]) {
      if (typeof program[field] !== "string" || !program[field].trim()) {
        throw new Error(`manifest programs[${index}] requires ${field}`);
      }
    }
  }
  return payload;
}

export function buildEnvelope(payload, manifestVersion, privateKey = null) {
  validatePayload(payload);
  if (typeof manifestVersion !== "string" || !manifestVersion.trim()) {
    throw new Error("manifestVersion must be an explicit non-empty string");
  }
  const integrity = {
    algorithm: "sha256",
    canonicalization: CANONICALIZATION,
    digest: digestPayload(payload),
  };
  const signed = { schemaVersion: SCHEMA_VERSION, manifestVersion, payload, integrity };
  const signature = privateKey
    ? { algorithm: "ed25519", value: sign(null, Buffer.from(canonicalJson(signed)), privateKey).toString("base64") }
    : null;
  return { ...signed, signature };
}

export function validateEnvelopeStructure(envelope, { requireSignature = false, trustedPublicKey = null } = {}) {
  if (!envelope || typeof envelope !== "object" || Array.isArray(envelope)) throw new Error("envelope must be a JSON object");
  if (envelope.schemaVersion !== SCHEMA_VERSION) throw new Error(`unsupported schemaVersion: ${String(envelope.schemaVersion)}`);
  if (typeof envelope.manifestVersion !== "string" || !envelope.manifestVersion.trim()) throw new Error("envelope requires manifestVersion");
  validatePayload(envelope.payload);
  const integrity = envelope.integrity;
  if (integrity?.algorithm !== "sha256" || integrity?.canonicalization !== CANONICALIZATION || !/^[a-f0-9]{64}$/.test(String(integrity.digest ?? ""))) {
    throw new Error("envelope integrity must be sha256 over jcs-lite-v1 canonical JSON");
  }
  if (digestPayload(envelope.payload) !== integrity.digest) throw new Error("envelope payload digest mismatch");
  if (requireSignature && (!envelope.signature || envelope.signature.algorithm !== "ed25519" || !envelope.signature.value)) {
    throw new Error("signed envelope requires an ed25519 signature");
  }
  if (envelope.signature) {
    if (envelope.signature.algorithm !== "ed25519" || typeof envelope.signature.value !== "string" || !envelope.signature.value) throw new Error("invalid ed25519 signature field");
    if (trustedPublicKey) {
      const key = trustedPublicKey.type === "public" ? trustedPublicKey : createPublicKey(trustedPublicKey);
      const signed = { schemaVersion: envelope.schemaVersion, manifestVersion: envelope.manifestVersion, payload: envelope.payload, integrity };
      if (!verify(null, Buffer.from(canonicalJson(signed)), key, Buffer.from(envelope.signature.value, "base64"))) throw new Error("envelope signature verification failed");
    }
  }
  return envelope;
}

async function readDocument(path) {
  const text = await readFile(path, "utf8");
  try { return JSON.parse(text); } catch { return YAML.parse(text); }
}

function valueAfter(args, index, flag) {
  const arg = args[index];
  const equals = arg.indexOf("=");
  if (equals !== -1) return arg.slice(equals + 1);
  const value = args[index + 1];
  if (!value || value.startsWith("--")) throw new Error(`${flag} requires a value`);
  return value;
}

export function parseArgs(args) {
  const options = { manifest: null, output: null, manifestVersion: process.env.HUBIFY_MANIFEST_VERSION ?? null, privateKeyPath: process.env.BIGBOUNCE_MANIFEST_PRIVATE_KEY_PATH ?? null, publicKeyPath: process.env.BIGBOUNCE_MANIFEST_PUBLIC_KEY_PATH ?? null, check: false, dryRun: false, unsigned: false };
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    const flag = arg.split("=", 1)[0];
    if (["--manifest", "--output", "--manifest-version", "--private-key", "--public-key"].includes(flag)) {
      const value = valueAfter(args, index, flag);
      if (!arg.includes("=")) index += 1;
      if (flag === "--manifest") options.manifest = value;
      if (flag === "--output") options.output = value;
      if (flag === "--manifest-version") options.manifestVersion = value;
      if (flag === "--private-key") options.privateKeyPath = value;
      if (flag === "--public-key") options.publicKeyPath = value;
    } else if (flag === "--check") options.check = true;
    else if (flag === "--dry-run") options.dryRun = true;
    else if (flag === "--unsigned") options.unsigned = true;
    else if (flag === "--help" || flag === "-h") options.help = true;
    else throw new Error(`unknown argument: ${arg}`);
  }
  return options;
}

export const HELP = `Usage:\n  node scripts/publish-hubify-release-envelope.mjs --manifest PATH --manifest-version VERSION --private-key PATH --output PATH\n  node scripts/publish-hubify-release-envelope.mjs --check --manifest PATH [--public-key PATH]\n\n--dry-run validates and prints a summary without writing. --unsigned permits structural validation without a signing key.\n`;

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) { process.stdout.write(HELP); return; }
  if (!options.manifest) throw new Error("--manifest is required");
  if (options.check) {
    const envelope = await readDocument(options.manifest);
    let trustedPublicKey = null;
    if (options.publicKeyPath) trustedPublicKey = await readFile(options.publicKeyPath);
    validateEnvelopeStructure(envelope, { requireSignature: !options.unsigned, trustedPublicKey });
    process.stdout.write(JSON.stringify({ ok: true, mode: "check", signed: Boolean(envelope.signature), manifestVersion: envelope.manifestVersion }, null, 2) + "\n");
    return;
  }
  if (!options.manifestVersion) throw new Error("--manifest-version (or HUBIFY_MANIFEST_VERSION) is required");
  const payload = validatePayload(await readDocument(options.manifest));
  let privateKey = null;
  if (options.privateKeyPath) privateKey = createPrivateKey(await readFile(options.privateKeyPath));
  else if (!options.unsigned) throw new Error("a signing key is required; pass --private-key or use --unsigned for structural dry runs");
  const envelope = buildEnvelope(payload, options.manifestVersion, privateKey);
  validateEnvelopeStructure(envelope, { requireSignature: Boolean(privateKey) });
  if (!options.dryRun && !options.output) throw new Error("--output is required unless --dry-run is used");
  if (options.output && !options.dryRun) await writeFile(options.output, JSON.stringify(envelope, null, 2) + "\n", { mode: 0o644 });
  process.stdout.write(JSON.stringify({ ok: true, mode: options.dryRun ? "dry-run" : "write", signed: Boolean(privateKey), manifestVersion: options.manifestVersion, output: options.dryRun ? null : options.output }, null, 2) + "\n");
}

if (import.meta.url === `file://${process.argv[1]}`) {
  try { await main(); } catch (error) { process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`); process.exitCode = 2; }
}

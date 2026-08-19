# Hubify release envelopes

BigBounce publishes a lab projection to Hubify as a `hubify-lab/v1` JSON
envelope. The payload is the checked-in lab manifest; the envelope adds a
SHA-256 digest over Hubify's `jcs-lite-v1` canonical JSON and an Ed25519
signature over the canonical object containing `schemaVersion`,
`manifestVersion`, `payload`, and `integrity`.

The publisher is `scripts/publish-hubify-release-envelope.mjs`. The checked-in
source projection is `project-context/hubify-lab/lab.yaml`; it accepts JSON or
YAML source, requires an explicit manifest version, and never generates or
stores keys. A signing key is supplied by path (recommended for CI):

```sh
node scripts/publish-hubify-release-envelope.mjs \
  --manifest /path/to/lab.yaml \
  --manifest-version 2026-08-19.1 \
  --private-key "$BIGBOUNCE_MANIFEST_PRIVATE_KEY_PATH" \
  --output /path/to/lab.release.json
```

`BIGBOUNCE_MANIFEST_PRIVATE_KEY_PATH` and `HUBIFY_MANIFEST_VERSION` are
supported environment variables. Private keys must live in a secret manager
or CI secret-mounted file; never commit them. The GitHub Actions secret
`BIGBOUNCE_MANIFEST_PRIVATE_KEY` is base64 text containing the PKCS#8 PEM
private key. CI decodes it only to `${RUNNER_TEMP}` with mode `0600`, derives
the public key, and compares it to the checked-in
`manifest-signing-public.pem`; it never logs the secret. Provisioning a
project Ed25519 key and registering its public half with Hubify remains a
release-owner operation.

CI and local validation do not need a signing key:

```sh
npm run test:hubify-envelope
node scripts/check-hubify-lab-manifest.mjs
node scripts/publish-hubify-release-envelope.mjs \
  --manifest /path/to/lab.yaml --manifest-version 2026-08-19.1 \
  --unsigned --dry-run
node scripts/publish-hubify-release-envelope.mjs \
  --check --manifest /path/to/lab.release.json --unsigned
```

The unsigned mode validates structure and digest only. Hubify's parity reader
must reject unsigned output; it is a CI-friendly preflight, not a production
release.

The checked-in public release is `project-context/hubify-lab/lab.release.json`.
It is pinned to manifest version `2026-08-19.1`. Regenerate it only from the
same source manifest, version, and registered private key; CI compares bytes
to prevent accidental re-signing or projection drift.

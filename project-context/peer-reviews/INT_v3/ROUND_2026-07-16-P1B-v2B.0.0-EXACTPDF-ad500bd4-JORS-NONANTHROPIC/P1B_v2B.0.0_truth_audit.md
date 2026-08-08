# P1B v2B.0.0 Exact-PDF Truth Audit

## Bound board

- Commit: `3475392b5ec27be5790580330b40e76f7abd0b5c`
- PDF SHA-256:
  `ad500bd4e8d689628ad3a383e512a1ddd7a1e329b5580e1d41e30637266c75a0`
- Grok 4.3: MINOR REVISIONS
- Gemini 3.1 Pro: MAJOR REVISIONS
- Codex subscription, GPT-5.6 Sol high: MAJOR REVISIONS
- OpenAI API used: no
- Anthropic used: no

## Finding dispositions

### Verified and closed in v2B.0.1 / package 0.1.1

1. **Receipt guarantees were overbroad.** Result and receipt are individually
   atomically replaced but are not one transaction; coordinated replacement
   requires trusted expected metadata or an external anchor to detect. Code
   docstrings, README, title, abstract, architecture, and limitations now say
   this explicitly.
2. **Spectrum support silently drifted.** The package padded short spectra and
   truncated long spectra. Exact workspace-length equality and finite values
   are now required.
3. **Recovery accepted invalid statistical inputs.** Non-finite grids/data,
   malformed weights, negative weights, and band-count mismatch now fail
   closed. Regression coverage increases the suite from 19 to 24 tests.
4. **Physical-run documentation was stale.** The retained README now leads
   with the completed CAMB 1.6.6 physical production and the exact summary and
   bandpower SHA-256 values.
5. **Artifact identification was too indirect.** The manuscript now names and
   hashes the exact physical summary and bandpower artifacts and explicitly
   states that the unretained workspace prevents self-contained reconstruction
   of the recorded equivalence scalar.
6. **JORS metapaper structure was incomplete.** The manuscript now includes
   keywords, Quality Control, structured Availability fields, Reuse Potential,
   AI Usage Disclosure, Funding Statement, and Competing Interests, plus a
   direct package-directory URL and PyMaster 2.6 compatibility statement.
7. **The primary README example was not self-contained.** The undefined
   `workspace` fragment was removed from the receipt example; the complete
   executable synthetic workspace example is referenced directly.

### Verified and still open

1. **Persistent archive identifier.** JORS requires deposited public software
   and a persistent identifier in the metapaper. No DOI or equivalent archive
   identifier exists yet. The manuscript marks this as a submission blocker.
2. **Independent real-PyMaster integration benchmark.** The retained physical
   campaign used PyMaster, but the package still lacks a compact independent
   integration test that constructs a real workspace and compares full-window
   inference with an effective-multipole shortcut. This remains an engineering
   and scope-strengthening gate.
3. **Production artifacts do not all use package receipts.** The corrected
   summary and NPZ predate package extraction. Their hashes are now explicit,
   but a future package-native example should publish its own bound result
   receipt and retain any workspace needed for reconstruction.

### Falsified or overstated reviewer findings

1. **Missing repository hyperlink:** falsified. The v2B.0.0 PDF contained a
   live hyperlink to the BigBounce repository. v2B.0.1 improves it to the
   direct package directory.
2. **Paper/package version conflict:** falsified. `v2B.0.0` identifies the
   manuscript, while `0.1.0` identified the software package. v2B.0.1 makes
   the distinction more explicit.
3. **DOI required before review or acceptance:** partly overstated by models.
   A persistent identifier is a real JORS submission/template gate. The
   project does not infer acceptance or archive completion from a source-only
   repository.

## Readiness effect

No readiness increase is taken. P1B remains 56 until v2B.0.1 passes an exact
confirmation board and the persistent archive and human-review gates are
resolved.

// P1A v1A.0.46 — TIER A #A6 quick-win closure (fine-tuning contradiction)
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1a",
  version: "v1A.0.46",
  datestamp: "2026-06-08",
  texCommit: "f37d35d4",
  pdfMd5: "b741c3daece53669262e5c610c901019",
  pdfPages: 21,
  pdfSizeBytes: 848398,
  sitePdfPath: "/papers/paper1a_ech_nogo_v1A.0.46.pdf",
  changelog:
    "TIER A #A6 quick-win closure — fire-13 P1A-META-M2 internal contradiction resolved. §XII spectator-ALP birefringence paragraph (L1702) updated: 'without fine-tuning' → 'at f_a~M_Pl and θ_i~O(1) without additional ALP-naturalness fine-tuning beyond the m_θ~H_0 ultralight-mass tuning admitted in §IV.D (a cosmological-constant-class tuning rather than an ALP-specific one)'. Cross-refs to §sec:structural_tension and §sec:loophole added so the reader is pointed to the existing CC-class tuning admissions. Mechanically reproducible by tools/v3_pattern040_cross_section_check.py; the fine-tuning contradiction is now CLOSED (detector finds 0 fine-tuning issues post-fix). PDF 21pp/848KB/md5 b741c3da. Compile: 0 undef refs, 4 carry-over overfulls.",
});
console.log("Inserted:", result);

console.log("\n--- verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}

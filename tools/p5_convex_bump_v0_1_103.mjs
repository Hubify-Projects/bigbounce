import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p5",
  version: "v0.1.103-2026-07-06",
  datestamp: "2026-07-06",
  texCommit: "7df2e305b5e428aa18ef35f52de87c7ed29d4484",
  pdfMd5: "a3a00abdfa24af461df14be60a1ff19a",
  pdfPages: 37,
  pdfSizeBytes: 1315950,
  changelog:
    "D-round final polish (presentation + disclosure ONLY, 0 numbers changed): title trimmed (dropped tidal-tensor tail; footnote condensed to sec:vweb pointer); abstract reordered to lead with the null result (void-vs-non-void dfCW consistent with parity), monopole-invariance caveat consolidated from 3+ to one; prose de-densified (sec:p4/sec:data/Discussion); acknowledgments block ADDED with DESI facility ack + AI-assisted-methodology disclosure; paperIVarxiv placeholder + coordinated-submission framing verified coherent. Script-11 figures regenerated at 300 dpi with serif fonts (plotted values unchanged). Verified 0 distinct numeric values added/deleted vs v0.1.102.",
  sitePdfPath: "/papers/p5_desi_chirality_v0.1.103-2026-07-06.pdf",
});
console.log("P5 inserted:", result);

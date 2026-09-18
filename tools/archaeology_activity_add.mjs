// Generic activityFeed:add helper for the 2025 legacy-archaeology campaign.
// Usage: node tools/archaeology_activity_add.mjs "<title>" "<body>" [tagLabel:tagKind ...]
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const [title, body, ...tagArgs] = process.argv.slice(2);
if (!title || !body) { console.error("usage: title body [label:kind ...]"); process.exit(2); }
const tags = tagArgs.length ? tagArgs.map(t => { const [label, kind = "lane"] = t.split(":"); return { label, kind }; })
  : [{ label: "archaeology-2025", kind: "lane" }];
const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");
const date = new Date().toISOString().slice(0, 10);
const result = await client.mutation(api.activityFeed.add, { type: "research", date, title, body, tags });
console.log("Inserted:", result);

import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  reviews: defineTable({
    pipelineId: v.string(),
    objectId: v.string(),
    label: v.string(),
    aiLabel: v.string(),
    aiReason: v.string(),
    humanNotes: v.string(),
    reviewerName: v.string(),
    reviewedAt: v.number(),
    metadata: v.any(),
  })
    .index("by_pipeline", ["pipelineId"])
    .index("by_pipeline_object", ["pipelineId", "objectId"]),

  checklistItems: defineTable({
    pipelineId: v.string(),
    category: v.string(),
    text: v.string(),
    status: v.string(),
    updatedAt: v.number(),
  }).index("by_pipeline", ["pipelineId"]),

  pipelineState: defineTable({
    pipelineId: v.string(),
    name: v.string(),
    status: v.string(),
    gatesPassed: v.number(),
    totalGates: v.number(),
    lastUpdated: v.number(),
    summary: v.string(),
  }).index("by_pipeline", ["pipelineId"]),

  models: defineTable({
    pipelineId: v.string(),
    modelName: v.string(),
    version: v.string(),
    huggingfaceUrl: v.string(),
    trainingSamples: v.number(),
    metrics: v.any(),
    createdAt: v.number(),
  }).index("by_pipeline", ["pipelineId"]),
});

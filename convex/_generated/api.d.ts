/* eslint-disable */
/**
 * Generated `api` utility.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import type * as activityFeed from "../activityFeed.js";
import type * as activityRollup from "../activityRollup.js";
import type * as analytics from "../analytics.js";
import type * as chatMessages from "../chatMessages.js";
import type * as checklist from "../checklist.js";
import type * as feedback from "../feedback.js";
import type * as findings from "../findings.js";
import type * as galaxies from "../galaxies.js";
import type * as mcmcStatus from "../mcmcStatus.js";
import type * as models from "../models.js";
import type * as paperVersions from "../paperVersions.js";
import type * as papers from "../papers.js";
import type * as pathcCaveats from "../pathcCaveats.js";
import type * as pipelineState from "../pipelineState.js";
import type * as pods from "../pods.js";
import type * as rRounds from "../rRounds.js";
import type * as reviews from "../reviews.js";
import type * as spectralResults from "../spectralResults.js";
import type * as tasks from "../tasks.js";

import type {
  ApiFromModules,
  FilterApi,
  FunctionReference,
} from "convex/server";

declare const fullApi: ApiFromModules<{
  activityFeed: typeof activityFeed;
  activityRollup: typeof activityRollup;
  analytics: typeof analytics;
  chatMessages: typeof chatMessages;
  checklist: typeof checklist;
  feedback: typeof feedback;
  findings: typeof findings;
  galaxies: typeof galaxies;
  mcmcStatus: typeof mcmcStatus;
  models: typeof models;
  paperVersions: typeof paperVersions;
  papers: typeof papers;
  pathcCaveats: typeof pathcCaveats;
  pipelineState: typeof pipelineState;
  pods: typeof pods;
  rRounds: typeof rRounds;
  reviews: typeof reviews;
  spectralResults: typeof spectralResults;
  tasks: typeof tasks;
}>;

/**
 * A utility for referencing Convex functions in your app's public API.
 *
 * Usage:
 * ```js
 * const myFunctionReference = api.myModule.myFunction;
 * ```
 */
export declare const api: FilterApi<
  typeof fullApi,
  FunctionReference<any, "public">
>;

/**
 * A utility for referencing Convex functions in your app's internal API.
 *
 * Usage:
 * ```js
 * const myFunctionReference = internal.myModule.myFunction;
 * ```
 */
export declare const internal: FilterApi<
  typeof fullApi,
  FunctionReference<any, "internal">
>;

export declare const components: {};

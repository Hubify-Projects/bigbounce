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
import type * as analytics from "../analytics.js";
import type * as chatMessages from "../chatMessages.js";
import type * as checklist from "../checklist.js";
import type * as mcmcStatus from "../mcmcStatus.js";
import type * as models from "../models.js";
import type * as pipelineState from "../pipelineState.js";
import type * as reviews from "../reviews.js";
import type * as spectralResults from "../spectralResults.js";

import type {
  ApiFromModules,
  FilterApi,
  FunctionReference,
} from "convex/server";

declare const fullApi: ApiFromModules<{
  activityFeed: typeof activityFeed;
  analytics: typeof analytics;
  chatMessages: typeof chatMessages;
  checklist: typeof checklist;
  mcmcStatus: typeof mcmcStatus;
  models: typeof models;
  pipelineState: typeof pipelineState;
  reviews: typeof reviews;
  spectralResults: typeof spectralResults;
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

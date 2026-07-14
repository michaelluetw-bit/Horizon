import { describe, expect, it } from "vitest";

import {
  provenanceRejectionSummary,
  sanitizeProvenanceRejection,
} from "../src/github-provenance-output.js";

describe("GitHub provenance runner", () => {
  it("records a sanitized provenance rejection in the GitHub Step Summary", () => {
    const reason = sanitizeProvenanceRejection(new Error("PROVENANCE_REJECTED:MISSING_GITHUB_RUN_ID"));

    expect(reason).toBe("PROVENANCE_REJECTED:MISSING_GITHUB_RUN_ID");
    expect(provenanceRejectionSummary(reason)).toContain("- decision: `PROVENANCE_REJECTED`");
    expect(provenanceRejectionSummary(reason)).toContain(
      "- reason: `PROVENANCE_REJECTED:MISSING_GITHUB_RUN_ID`",
    );
  });

  it("never copies an unexpected error value into an execution summary", () => {
    const reason = sanitizeProvenanceRejection(new Error("token=secret-value"));

    expect(reason).toBe("PROVENANCE_REJECTED:UNKNOWN");
    expect(provenanceRejectionSummary(reason)).not.toContain("secret-value");
  });
});

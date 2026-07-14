const REJECTION_REASON_PATTERN = /^PROVENANCE_REJECTED:[A-Z0-9_]+$/;

export function sanitizeProvenanceRejection(error) {
  const candidate = error instanceof Error ? error.message : "";
  return REJECTION_REASON_PATTERN.test(candidate) ? candidate : "PROVENANCE_REJECTED:UNKNOWN";
}

export function provenanceRejectionSummary(reason) {
  return [
    "## Horizon P0-B2R provenance rejected",
    "",
    "- decision: `PROVENANCE_REJECTED`",
    `- reason: \`${reason}\``,
    "",
  ].join("\n");
}

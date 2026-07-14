import { appendFile, writeFile } from "node:fs/promises";

import { prepareProvenance, required } from "./github-provenance-core.js";
import { provenanceRejectionSummary, sanitizeProvenanceRejection } from "./github-provenance-output.js";

async function setOutput(name, value) {
  const outputPath = process.env.GITHUB_OUTPUT;
  if (outputPath) await appendFile(outputPath, `${name}=${value}\n`, "utf-8");
}

function primaryStartedAtMs(env) {
  if (env.GITHUB_EVENT_NAME !== "schedule") return undefined;
  const timestamp = Date.parse(required(env, "HORIZON_WORKFLOW_STARTED_AT"));
  if (!Number.isInteger(timestamp)) {
    throw new Error("PROVENANCE_REJECTED:PRIMARY_START_TIME_INVALID");
  }
  return timestamp;
}

try {
  const provenance = await prepareProvenance({
    env: process.env,
    primaryStartedAtMs: primaryStartedAtMs(process.env),
  });
  const outputPath = required(process.env, "HORIZON_PROVENANCE_PATH");
  await writeFile(outputPath, `${JSON.stringify(provenance)}\n`, "utf-8");
  await setOutput("trigger_source", provenance.trigger_source);
  await setOutput("target_date", provenance.target_date);
  await setOutput("provenance_path", outputPath);
} catch (error) {
  const reason = sanitizeProvenanceRejection(error);
  console.error(reason);
  if (process.env.GITHUB_STEP_SUMMARY) {
    await appendFile(process.env.GITHUB_STEP_SUMMARY, provenanceRejectionSummary(reason), "utf-8");
  }
  process.exitCode = 1;
}

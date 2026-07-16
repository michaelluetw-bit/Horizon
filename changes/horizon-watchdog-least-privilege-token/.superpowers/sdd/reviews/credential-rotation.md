# Wave review: credential-rotation

- Change: `horizon-watchdog-least-privilege-token`
- Wave: `credential-rotation`
- Mode: `batch-inline`
- Plan revision: 1
- Review status: `pass`

## Contract compliance

| Obligation | Evidence | Result |
|---|---|---|
| Dedicated fine-grained PAT | Pre-generation GitHub form showed a fine-grained token; secure local gate accepted only the fine-grained PAT prefix and authenticated `/user` as `michaelluetw-bit`. | PASS |
| Restricted to `michaelluetw-bit/Horizon` | GitHub form showed resource owner `michaelluetw-bit`, `Only select repositories`, selected count 1, sole repository `Horizon`. | PASS |
| Minimum repository permission | GitHub form showed `Actions: Read and write`, required `Metadata: Read-only`, repository permissions count 2, account permissions count 0. | PASS |
| Expiring credential | GitHub form showed expiration `2026-10-14`. | PASS |
| Encrypted Worker secret only | `wrangler secret list` reports `HORIZON_GITHUB_TOKEN` as `secret_text`; version 8 was created by a `secret` operation. | PASS |
| No token disclosure | Token used masked `Read-Host -AsSecureString`, was passed to Wrangler through stdin, cleared from process memory, and never entered the command line. A fine-grained PAT literal scan across repo and the Vault acceptance note returned zero files. | PASS |
| No manual Horizon dispatch | GitHub workflow runs query returned `WORKFLOW_DISPATCH_RUNS_SINCE_DP4=0`. | PASS |
| No Worker/workflow/cron/vars drift | Version 7 and 8 share the same script etag and bindings; tracked Worker/workflow diff is empty; workflow hash matches HEAD; production cron remains `0 22 * * *`. | PASS |
| Runtime deployment | Version `2f9d4696-e9b5-41d6-b0c1-8a3b8090302d`, deployment `261f0919-469e-47f9-b4c2-2b1bd3a4a6be`, 100% traffic. | PASS |
| Regression verification | `npm test`: 11 test files passed, 57 tests passed. | PASS |
| Vault closeout | Existing acceptance note frontmatter is `status: ACCEPTED` and `spec_compliance_exception: NONE`; final invariants retain P0-B2=`FAILED` and P0-B3=`NOT_STARTED`. | PASS |
| Preserve P0-B2 / do not start P0-B3 | No P0-B2 historical artifact or P0-B3 implementation was modified; closeout must retain P0-B2=`FAILED`. | PASS |

## Scope and quality review

- No production source code, workflow, Worker configuration, cron, vars, or secret names changed.
- The only external mutation was replacement of the encrypted value bound to the existing `HORIZON_GITHUB_TOKEN` name.
- 本次未修改、替換或撤銷本機 GitHub CLI 登入憑證；合規判定僅針對 Cloudflare Worker 的 `HORIZON_GITHUB_TOKEN`，其部署值已完成 least-privilege 輪替。
- Multi-agent reviewer dispatch was not authorized for this batch-inline change; the current task therefore performed a separate second-pass review against the fixed git range and the persisted runtime/Vault evidence.
- No Critical or Important finding remains.

## Verdict

`pass` — the active `SPEC_COMPLIANCE_EXCEPTION` for the deployed Watchdog credential is resolved. The change may proceed to Git review and Vault closeout while preserving the historical P0-B2 `FAILED` conclusion.

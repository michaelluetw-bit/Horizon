# Wave review: credential-rotation

- Change: `horizon-watchdog-least-privilege-token`
- Wave: `credential-rotation`
- Mode: `batch-inline`
- Plan revision: 3
- Review range: `6e0e326a2690c5ff9d8fb5ec942f0ae88a864831..49dc8b91dce483e3609bf49fc5e96bb6dac5d3ae`
- Review status: `pass`

## Contract compliance

| Obligation | Evidence | Result |
|---|---|---|
| Dedicated fine-grained credential | Pre-generation GitHub form showed a fine-grained token; the secure local gate validated the credential type and authenticated `/user` as `michaelluetw-bit`. | PASS |
| Restricted to `michaelluetw-bit/Horizon` | GitHub form showed resource owner `michaelluetw-bit`, `Only select repositories`, selected count 1, sole repository `Horizon`. | PASS |
| Minimum repository permission | GitHub form showed `Actions: Read and write`, required `Metadata: Read-only`, repository permissions count 2, account permissions count 0. | PASS |
| Expiring credential | GitHub form showed expiration `2026-10-14`. | PASS |
| Encrypted Worker secret only | `wrangler secret list --format json` reports `HORIZON_GITHUB_TOKEN` as `secret_text`; Worker version 8 has `workers/triggered_by=secret`. | PASS |
| No token disclosure | The token used a masked `Read-Host -AsSecureString` prompt, was passed to Wrangler through stdin, and never entered chat or a command argument. A token-literal scan across the repo and Vault returned zero files. | PASS |
| No manual Horizon dispatch | GitHub run query returned zero `workflow_dispatch` runs since DP-4. | PASS |
| No Worker/workflow/cron drift | Worker versions 7 and 8 have the same script etag, handlers, and bindings; Worker/workflow tracked diff is empty; workflow hash matches HEAD; production cron remains `0 22 * * *`. | PASS |
| Runtime deployment | Version `2f9d4696-e9b5-41d6-b0c1-8a3b8090302d`, deployment `261f0919-469e-47f9-b4c2-2b1bd3a4a6be`, 100% traffic. | PASS |
| Regression verification | Fresh Ruff check passed; 327 Python tests passed; 11 Watchdog test files and 57 tests passed; npm audit reported zero vulnerabilities. | PASS |
| Vault closeout | Frontmatter is `status: ACCEPTED`; final invariants are `RESULT=P0-B2R_SPEC_COMPLIANT_ACCEPTED`, `SPEC_COMPLIANCE_EXCEPTION=NONE`, P0-B2=`ACCEPTED`, and P0-B3=`NOT_STARTED`. | PASS |
| Archive integrity | `tasks.md` contains the same two completed contract tasks; `ssf execution show` reports current plan revision 3 in `batch-inline` mode; DP-0 through DP-7 are recorded. | PASS |

## Scope and quality review

- The first fixed-range pass found an active-artifact mismatch: `execution-contract.md` still used the rejected pre-correction P0-B2 status. Commit `49dc8b91dce483e3609bf49fc5e96bb6dac5d3ae` corrected it to the user-confirmed `ACCEPTED` status and resealed the hashes; a follow-up search found no active conflicting status.
- No production source code, workflow, Worker configuration, cron, vars, or secret names changed in the Git range.
- The only production mutation was replacement of the encrypted value bound to the existing Worker secret name.
- 本次未修改、替換或撤銷本機 GitHub CLI 登入憑證；合規判定僅針對 Cloudflare Worker 的 `HORIZON_GITHUB_TOKEN`。
- Reviewer subagent dispatch was unavailable under the active no-subagent constraint; a separate second-pass review used the fixed Git range plus persisted runtime and Vault evidence.
- No Critical, Important, or Minor finding remains.

## Verdict

`pass` — the broad-token `SPEC_COMPLIANCE_EXCEPTION` is resolved, P0-B2=`ACCEPTED` is preserved consistently, P0-B3 remains unstarted, and the change is ready for a revision-3 review receipt and closing guard.

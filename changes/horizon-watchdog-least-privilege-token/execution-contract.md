# Horizon Watchdog least-privilege token hotfix 執行契約

## Intent Lock

將 Cloudflare Worker encrypted secret `HORIZON_GITHUB_TOKEN` 從廣權限 OAuth token 輪替為只限 `michaelluetw-bit/Horizon`、repository permission 僅 `Actions: write`、具到期日的 dedicated fine-grained personal access token；只有在權限與部署證據均成立後，才移除 Vault 的 `SPEC_COMPLIANCE_EXCEPTION`，且 P0-B2 歷史仍維持 `FAILED`、P0-B3 不啟動。

## Task List

1. 由使用者在 GitHub 已登入介面建立 fine-grained token：resource owner 為 `michaelluetw-bit`、repository access 僅選 `Horizon`、repository permissions 僅 `Actions: write`（GitHub 固有的 `Metadata: read` 除外）、設定到期日；token 值不得進入聊天、命令列、repo、Vault、log 或 fixture。透過本機互動式安全輸入先做無副作用的 workflow GET 驗證，再直接覆寫 Cloudflare encrypted secret；不得呼叫 workflow dispatch。
2. 以 GitHub read-only 回應與 Cloudflare secret／version metadata 驗證新憑證已生效，並確認 workflow、Worker 程式、cron、vars、secrets 名稱及 P0-B2 歷史均未被改動。證據完整後更新既有 Vault 驗收筆記為完整 Spec-compliant `ACCEPTED` 並移除例外；若任一權限、repo scope、部署或保密證據不足，維持 `P0-B2R_COMPLETE_WITH_SPEC_COMPLIANCE_EXCEPTION`。

## Approval Gate (DP-3)

- 此契約只授權上述兩項工作，不授權手動或 API dispatch Horizon workflow、不授權修改 workflow／Worker 程式或 production cron／vars、不授權撤銷本機 GitHub CLI 目前使用的 OAuth 登入、不授權改寫 P0-B2 或啟動 P0-B3。
- GitHub token 是密碼等級資料；建立與輸入必須由使用者在本機互動介面完成，Codex 不讀取、不回顯、不保存 token 值。
- 無法以安全方式完成 token 輸入時立即停止；不得以現有 broad OAuth token、token prefix、推測或 fallback 充當合規證據。
- DP-3 必須由使用者明確批准；批准前不得修改 production secret。

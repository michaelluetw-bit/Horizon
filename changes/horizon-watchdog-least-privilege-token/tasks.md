# Horizon Watchdog least-privilege token tasks

> 封存可攜性：此 raw-byte plan input 必須在所有平台維持 LF，確保 execution-plan hash 可重現。

- [x] 1. 建立並以安全互動輸入部署只限 `michaelluetw-bit/Horizon`、`Actions: write`、具到期日的 fine-grained token；token 值不進入聊天、命令列、repo、Vault、log 或 fixture，且不觸發 workflow dispatch。
- [x] 2. 驗證 GitHub read-only 存取、Cloudflare secret-only version／deployment、無 Worker／workflow／cron drift，並在既有 Vault 筆記移除 `SPEC_COMPLIANCE_EXCEPTION`，保留 P0-B2=`ACCEPTED` 與 P0-B3=`NOT_STARTED`。

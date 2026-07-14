# Horizon External Watchdog 設計規格

- 日期：2026-07-14
- 狀態：已核准方向，待規格審閱
- 範圍：P0-B2R｜Scheduler Recovery
- Repo：`michaelluetw-bit/Horizon`

## 1. 決策與目標

保留現有 Horizon 每日 `08:17 Asia/Taipei` GitHub Actions `schedule` 作為主路徑，新增位於 GitHub scheduler 故障域以外的 Cloudflare Worker Cron Watchdog。

Watchdog 每日 `08:25 Asia/Taipei` 查詢當日 `horizon_daily.yml` 是否已建立 `event=schedule` run：

- 已建立任何狀態的 schedule run：只記錄 `PRIMARY_PRESENT`，不觸發備援。
- 完全沒有 schedule run：以 GitHub REST API 呼叫既有 `workflow_dispatch`，建立可辨識的 fallback run。
- GitHub 查詢失敗或結果無法判定：fail-closed，記錄 `CHECK_FAILED`，不得盲目 dispatch。

本方案的成功標準是每日只有一份有效 Horizon artifact，並能明確區分 primary 與 fallback；fallback 永遠不能作為 P0-B2 `event=schedule` 通過證據。

## 2. 不在範圍內

- 不改現有 cron `17 0 * * *`。
- 不新增第二個 GitHub cron。
- 不把 `workflow_dispatch` 偽裝為 `schedule`。
- 不自動重跑失敗的 Horizon pipeline；Watchdog 只處理「排程事件未建立 run」。
- 不執行或設計 P0-B3 Sync Publish。
- 不執行 `npm run build:hosted`、Dashboard 部署或 Cloudflare Pages 部署。
- 不建立第二個 Obsidian Vault、平行正式資料庫或新的 canonical Horizon artifact。
- 不加入一般化 retry、auto-repair、監控平台或通知中心。

## 3. 現有基準

現有 `.github/workflows/horizon_daily.yml` 同時支援：

- `schedule: cron '17 0 * * *'`
- `workflow_dispatch`
- 固定 concurrency group：`horizon-daily`
- 固定發布分支：`automation/horizon-daily-publish`
- `peter-evans/create-pull-request@v8`
- GitHub App token 建立 PR 與啟用 auto-merge

這些機制保留。實作只增加觸發來源、同日冪等 Gate 與外部 Watchdog。

## 4. 架構

### 4.1 Primary

GitHub scheduler 在 `00:17Z` 嘗試建立 Horizon Daily Aggregation run。Primary run 的 `github.event_name` 必須為 `schedule`。

### 4.2 Watchdog

Cloudflare Worker Cron 在 `00:25Z` 執行一次：

1. 以 `Asia/Taipei` 計算 `target_date`。
2. 查詢 Horizon workflow runs，限定：
   - workflow：`horizon_daily.yml`
   - event：`schedule`
   - created：當日 `00:00Z` 至查詢時間
3. 若找到至少一筆 run，不論為 `queued`、`in_progress` 或 `completed`，回報 `PRIMARY_PRESENT` 並停止。
4. 若找不到 schedule run，再查詢當日 `workflow_dispatch` runs，並以 workflow `run-name` 中的 `fallback-watchdog` 與 `target_date` 精確辨識先前 fallback。
5. 已有 fallback run：回報 `FALLBACK_ALREADY_REQUESTED` 並停止。
6. 仍無任何 primary 或 fallback run：POST workflow dispatch，`ref=main`，並傳入：
   - `trigger_source=fallback-watchdog`
   - `target_date=YYYY-MM-DD`
7. 保存 GitHub 回傳的 run ID、run URL、HTTP status 與決策為結構化 Worker log。

Watchdog 的查詢與 dispatch 必須在同一次 Cron invocation 完成；不等待、不輪詢、不在同一次 invocation 重試。

### 4.3 Workflow provenance

`workflow_dispatch` 增加兩個 inputs：

- `trigger_source`：預設 `manual`；Watchdog 固定傳 `fallback-watchdog`。
- `target_date`：Watchdog 必填；人工 dispatch 可留空並使用當日台北日期。

workflow run name、PR body 與 step summary 必須顯示：

- `event_name`
- `trigger_source`
- `target_date`

只有 `event_name=schedule` 可標為 primary；任何 `workflow_dispatch` 都只能標為 fallback 或 manual。Fallback 的完整來源證明必須同時包含 Worker dispatch 回傳的 run ID／URL與 GitHub run metadata，不得只信任可由人工輸入的 `trigger_source`。

## 5. 同日冪等與延遲碰撞防護

在安裝相依套件與執行 Horizon pipeline 前加入可測試的 preflight Gate。

### 5.1 日期規則

- schedule：`target_date` 固定為執行當下的 `Asia/Taipei` 日期。
- fallback：輸入日期必須符合 `YYYY-MM-DD`，且必須等於執行當下的 `Asia/Taipei` 日期。
- 日期不符：`CONFIG_ERROR`，停止且不得產生 PR。

### 5.2 已完成檢查

若 `origin/main` 已存在 `data/summaries/horizon-{target_date}-zh.md`，且通過 canonical 檢查，結果為 `ALREADY_PUBLISHED`：

- 不執行 Horizon pipeline。
- 不建立或更新 PR。
- workflow 成功結束並寫入 step summary。

### 5.3 已在途檢查

若遠端固定分支 `automation/horizon-daily-publish` 已存在同日檔案，且通過 canonical 檢查，結果為 `ALREADY_IN_PROGRESS`：

- 不再次執行 Horizon pipeline。
- 不新增第二張 PR。
- workflow 成功結束並寫入 step summary。

由於現有 concurrency group 會序列化 Horizon workflow，fallback 完成後才到達的延遲 schedule run，應在 `main` 或固定發布分支命中上述 Gate，而不是再次生成。

### 5.4 Canonical 檢查

同日檔案必須全部符合：

- 路徑精確為 `data/summaries/horizon-{target_date}-zh.md`。
- strict UTF-8 可解碼。
- 正文非空。
- 內容含精確 `target_date`。
- 不含 `placeholder`、`TODO` 或 `TBD` 標記。

檢查失敗時不得當成已發布；若檔案已存在但不合格，workflow fail-closed，避免覆蓋不明狀態。

## 6. 認證與安全

### 6.1 Watchdog 讀取

Horizon 為 public repo，run 查詢本身不需要寫入權限。實作仍統一使用專用 fine-grained token，以取得一致的 API rate limit 與 dispatch 能力。

### 6.2 Watchdog 寫入

建立一枚專用 fine-grained GitHub token：

- Repository access：只限 `michaelluetw-bit/Horizon`
- Repository permission：`Actions: write`
- 不授予 Contents、Pull requests、Administration 等額外權限
- 有效期限最長 90 天，並在到期前 14 天完成輪替
- 只存入 Cloudflare Worker encrypted secret `HORIZON_GITHUB_TOKEN`

Worker、GitHub logs、錯誤訊息與測試 fixture 都不得輸出 token。

原 Horizon workflow 繼續使用既有 GitHub App 建立 PR；Watchdog token 不參與內容寫入或 PR 操作。

## 7. 狀態與錯誤處理

Watchdog 決策只允許：

- `PRIMARY_PRESENT`
- `FALLBACK_ALREADY_REQUESTED`
- `FALLBACK_DISPATCHED`
- `CHECK_FAILED`
- `DISPATCH_FAILED`

規則：

- GitHub read API 非 2xx、JSON schema 不符或時間範圍無法判定：`CHECK_FAILED`，不得 dispatch。
- Dispatch 非 2xx：`DISPATCH_FAILED`；同一次 invocation 不重試。
- GitHub 成功回傳 run ID：`FALLBACK_DISPATCHED`。
- Worker 平台重複投遞時，先以當日 primary/fallback run 查詢去重。
- 不假設分散式排程具備 exactly-once；若極短競態造成多個 fallback runs，workflow concurrency、固定發布分支與 preflight Gate 必須保證最多一份有效發布結果。

Worker 結構化 log 至少包含：

- `checked_at_utc`
- `target_date`
- `workflow`
- `primary_run_id`
- `fallback_run_id`
- `decision`
- `http_status`

Cloudflare/GitHub logs 是來源證據，不是新的 canonical 資料庫。正式驗收結論仍只寫入既有 Obsidian Vault。

## 8. TDD 與驗證

### 8.1 Watchdog focused tests

先以 mock GitHub API 寫失敗測試，再實作最小決策邏輯：

1. schedule run 存在 → 不 dispatch。
2. schedule run 為 queued → 不 dispatch。
3. schedule run 不存在、fallback 已存在 → 不 dispatch。
4. primary/fallback 都不存在 → dispatch 一次。
5. read API 失敗 → fail-closed。
6. dispatch API 失敗 → 不重試。
7. 前一 fallback run 已可由 API 讀取後再次 invocation → 不重複 dispatch。
8. 競態產生兩個 fallback runs → 最多一份有效發布結果。
9. 日期跨 UTC／台北邊界 → `target_date` 正確。

### 8.2 Workflow focused tests

1. schedule 使用台北當日日期。
2. fallback 日期格式錯誤 → `CONFIG_ERROR`。
3. fallback 日期不是台北當日 → `CONFIG_ERROR`。
4. main 已有合格同日檔案 → `ALREADY_PUBLISHED`。
5. 固定發布分支已有合格同日檔案 → `ALREADY_IN_PROGRESS`。
6. 已存在檔案但 UTF-8、日期或 placeholder 檢查失敗 → fail-closed。
7. 無既有檔案 → 才允許 pipeline 執行。

### 8.3 P0-B2R 實際驗收

P0-B2R 必須分兩種真實路徑取證：

- Primary-present：08:25 Watchdog 找到真實 schedule run，確認沒有 fallback run。
- Primary-missing：未找到 schedule run，Watchdog 建立一個真實 `workflow_dispatch` fallback；該 run 成功、自動 PR 合併、main 出現精確當日完整檔案。

另須驗證延遲 schedule 在 fallback 後到達時：

- 命中 `ALREADY_PUBLISHED` 或 `ALREADY_IN_PROGRESS`。
- 不產生第二張 PR。
- 不改寫已完成的同日 artifact。

## 9. 證據與治理

- P0-B2 維持 `FAILED`，不得因 fallback 成功改寫歷史結論。
- 新 Gate 名稱固定為 `P0-B2R｜Scheduler Recovery`。
- P0-B2R 通過前不啟動 P0-B3。
- 正式驗收證據只寫入唯一 Vault：
  `C:\Users\micha\Documents\2026_agent\download\knowledge\19_codex\AI Executive Dashboard`
- `.codex/automations/.../memory.md` 可作執行紀錄，但不是正式驗收 evidence root。
- 不使用：
  `C:\Users\micha\OneDrive\Documents\AI Executive Dashboard`

## 10. 實作邊界

預計實作只包含：

1. Horizon workflow provenance inputs 與 run name。
2. 可測試的同日 preflight Gate。
3. Cloudflare Worker Watchdog 與 focused tests。
4. 最小部署設定與 secret 名稱文件。
5. P0-B2R 驗收記錄。

不進行相鄰重構，不修改 Horizon 摘要策略、內容生成邏輯、PR 門禁、Hosted Dashboard 或 Obsidian 發布流程。

## 11. 官方依據

- GitHub schedule 延遲／丟棄說明：<https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule>
- Workflow runs 查詢 API：<https://docs.github.com/en/rest/actions/workflow-runs#list-workflow-runs-for-a-workflow>
- Workflow dispatch API 與 `Actions: write` 權限：<https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event>
- Workflow concurrency 行為：<https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency>

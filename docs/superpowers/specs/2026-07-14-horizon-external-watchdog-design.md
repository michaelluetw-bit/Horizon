# Horizon External Watchdog 設計規格

- 日期：2026-07-14
- 狀態：修正版待唯一一次 Spec／Standards 複審
- 範圍：P0-B2R｜Scheduler Recovery
- Repo：<code>michaelluetw-bit/Horizon</code>

## 1. 決策與目標

保留 GitHub Actions <code>schedule</code> 作為 Horizon 每日發布的 primary 路徑，並以位於 GitHub scheduler 故障域以外的 Cloudflare Worker Cron Watchdog 只處理「應有 primary run 卻完全不存在」的情況。

Watchdog 不重跑失敗 pipeline、不改寫歷史 P0-B2 結論，也不把 fallback 偽裝為 <code>schedule</code>。它只會在可唯一判定當日沒有 primary run、也沒有已要求的同日 watchdog fallback 時，呼叫既有 <code>workflow_dispatch</code>。

成功條件是每個 <code>target_date</code> 最多只有一組完整的四檔 canonical 原子集合，且 primary、watchdog fallback、manual 三種來源可由不可混淆的 provenance 串聯。Fallback 成功永遠不是 P0-B2 的 <code>event=schedule</code> 通過證據。

Previous schedule contract is superseded.

## 2. 範圍與明確排除

本 Spec 只定義日後實作 P0-B2R 時必須遵守的契約；本輪不授權任何程式、workflow、Worker、部署、Vault 或 TDD 實作變更。

- 不新增第二個 GitHub cron。
- 不把 <code>workflow_dispatch</code> 偽裝為 <code>schedule</code>。
- 不自動重跑失敗的 Horizon pipeline；Watchdog 只處理「排程事件未建立 run」。
- 不啟動或設計 P0-B3 Sync Publish。
- 不執行 Hosted Dashboard、Cloudflare Pages 或 Dashboard 部署。
- 不建立第二個 Obsidian Vault、平行正式資料庫或新的 canonical Horizon artifact。
- 不加入一般化 retry、auto-repair、監控平台或通知中心。
- 不改變既有四份 Markdown 的 generator 格式、正文、標題、檔名或 hash 契約。

## 3. 凍結的時間、時區與日界

所有 <code>target_date</code>、日界、canonical artifact 判定及驗收日期一律採 <code>Asia/Taipei</code>。Cron expression 本身一律以 UTC 解讀。

| 路徑 | 權威排程 | UTC cron | 台北預定時間 | 有效窗口 |
| --- | --- | --- | --- | --- |
| Primary | GitHub Actions <code>schedule</code> | <code>17 21 * * *</code> | 05:17 | workflow 進入 preflight：05:12:00–05:22:00 |
| Watchdog | Cloudflare Worker Cron | <code>0 22 * * *</code> | 06:00 | invocation 觀測窗口：05:55:00–06:05:00 |

Primary 的 on-time 驗收必須落在其窗口內。窗口外才出現的 <code>event=schedule</code> 仍是已投遞的 schedule run，Watchdog 不得因它晚到而再 dispatch；但它不可被記為準時 primary 成功證據。

Watchdog 的窗口另受第 5 節的權威 <code>controller.scheduledTime</code> 與延遲 Gate 限制。對固定的 06:00 預定時間，實際 handler 開始時間若早於 <code>scheduled_time</code>，即使落在觀測窗口內仍為負延遲並 fail-closed。

### 3.1 <code>target_date</code> 與查詢半開區間

對任意台北日期 <code>target_date=YYYY-MM-DD</code>：

~~~
target_date_start_taipei = target_date 00:00:00+08:00
target_date_end_taipei   = 次日        00:00:00+08:00

created_utc = [前一日 16:00:00Z, 當日 16:00:00Z)
~~~

例如 <code>2026-07-14</code> 的完整區間為 <code>[2026-07-13T16:00:00Z, 2026-07-14T16:00:00Z)</code>。GitHub API 查詢必須帶完整 UTC 範圍；即使 API 的日期搜尋語法包含上界，client 端仍必須以 <code>created_at &gt;= start &amp;&amp; created_at &lt; end</code> 落實半開區間。

Primary workflow 的 <code>target_date</code> 以 workflow 進入 preflight 時的台北日期取得。Watchdog fallback 的 <code>target_date</code> 唯一由第 5 節的 Cloudflare <code>scheduled_time</code> 換算；不得改以 GitHub workflow 實際開始時間、<code>Date.now()</code> 或任何本機時鐘重算。

## 4. GitHub workflow-runs 查詢契約

Watchdog 必須只查詢唯一指定的 workflow endpoint：

<code>GET /repos/michaelluetw-bit/Horizon/actions/workflows/horizon_daily.yml/runs</code>

此處的 API workflow selector 固定為精確檔名 <code>horizon_daily.yml</code>，並須解析到 <code>main</code> 上的 <code>.github/workflows/horizon_daily.yml</code>。不得改用 repository-wide runs 清單、模糊名稱比對或「最近一筆」推測。

### 4.1 Primary 候選

Primary query 固定包含以下 server-side filters，並完整處理分頁：

- exact workflow selector：<code>horizon_daily.yml</code>
- <code>event=schedule</code>
- <code>branch=main</code>
- <code>created</code>：第 3.1 節的完整 UTC 區間
- 每頁最大值與所有後續頁；不得只看第一頁

收到資料後，client 必須再次驗證 workflow、<code>event=schedule</code>、<code>head_branch=main</code> 與 <code>created_at</code> 半開區間。候選集合的決策不可任選：

| 候選數 | 決策 | 行為 |
| --- | --- | --- |
| 0 | 無 primary | 才可進入 fallback 去重檢查 |
| 1 | <code>PRIMARY_PRESENT</code> | 不論 <code>queued</code>、<code>in_progress</code> 或 <code>completed</code>，均不得 dispatch |
| 大於 1，或任一欄位無法驗證 | <code>CHECK_FAILED</code>，原因 <code>PRIMARY_NOT_UNIQUE</code> 或 <code>PRIMARY_QUERY_INVALID</code> | fail-closed、零 dispatch |

### 4.2 同日 fallback 去重

僅在 primary 候選數為零後，才可用同一個 exact workflow selector、<code>branch=main</code> 與完整半開區間查詢 <code>event=workflow_dispatch</code>。

此查詢可用 run-name 中的 watchdog 來源標籤作為保守的「已要求 fallback」去重條件；它只避免重複 dispatch，絕不可作為 <code>target_date</code>、dispatch 回應或官方 provenance 證據。已找到一個可辨識的同日 watchdog fallback 時，決策為 <code>FALLBACK_ALREADY_REQUESTED</code> 並停止；候選不唯一或欄位無法驗證時為 <code>CHECK_FAILED</code> 並 fail-closed。

不得在 dispatch 後重新查詢「最近一筆 <code>workflow_dispatch</code>」來猜測本次 dispatch 的 run ID。

## 5. Cloudflare Watchdog provenance 與 dispatch

### 5.1 唯一權威來源

Worker handler 進入時必須立即記錄下列欄位；不得以本機推算值取代 Cloudflare controller 值：

~~~
trigger_schedule_expression = controller.cron
scheduled_time              = controller.scheduledTime
invocation_started_at       = handler 實際進入時間
invocation_delta_ms         = invocation_started_at - scheduled_time
~~~

- <code>trigger_schedule_expression</code> 必須精確等於設定的 <code>configured_watchdog_schedule_expression = "0 22 * * *"</code>。
- <code>scheduled_time</code> 是 <code>controller.scheduledTime</code> 所提供的 UTC epoch milliseconds；可另記錄 ISO-8601 便於閱讀，但不得覆蓋原始值。
- <code>invocation_started_at</code> 只代表 handler 實際進入時間，不是排定時間。
- <code>target_date</code> 只能由 <code>new Date(controller.scheduledTime)</code> 轉成 <code>Asia/Taipei</code> 日期。

若 <code>controller.cron</code> 不等於設定的 Watchdog cron，決策為 <code>CHECK_FAILED</code>、原因 <code>WATCHDOG_CRON_MISMATCH</code>；不得查詢 GitHub runs、不得 dispatch、不得重試。

<code>MAX_INVOCATION_LAG_MS</code> 固定為 <code>300000</code>。只有 <code>0 &lt;= invocation_delta_ms &lt;= 300000</code> 可繼續；負延遲或大於上限時為 <code>STALE_SCHEDULED_INVOCATION</code>，零 GitHub read、零 dispatch、零重試。<code>invocation_delta_ms == 300000</code> 仍屬有效。

### 5.2 Dispatch request

只有第 4 節明確允許 dispatch 時，才可送出一次以下固定 request：

- <code>Accept: application/vnd.github+json</code>
- <code>X-GitHub-Api-Version: 2026-03-10</code>
- <code>ref: main</code>
- <code>return_run_details: true</code>
- inputs：
  - <code>trigger_source=fallback-watchdog</code>
  - <code>target_date=YYYY-MM-DD</code>

同一次 invocation 不等待、不輪詢、不 retry。Worker 平台若重複投遞，仍須先依第 4 節查詢去重。

### 5.3 Dispatch response 與 fail-closed

只有同時符合下列條件的 HTTP <code>200</code> 才是 <code>DISPATCH_CONFIRMED</code>：

- response body 是合法 JSON；
- <code>workflow_run_id</code> 是正整數；
- <code>run_url</code> 與 <code>html_url</code> 都是合法 HTTPS URL；
- <code>run_url</code> 精確指向 <code>https://api.github.com/repos/michaelluetw-bit/Horizon/actions/runs/{workflow_run_id}</code>；
- <code>html_url</code> 精確指向 <code>https://github.com/michaelluetw-bit/Horizon/actions/runs/{workflow_run_id}</code>；
- 兩個 URL 解析出的 run ID 都與 <code>workflow_run_id</code> 一致。

| 情況 | 決策與行為 |
| --- | --- |
| 200 但 JSON 或 schema 不合格 | <code>DISPATCH_RESPONSE_INVALID</code>；保存可用 metadata，fail-closed，不 retry |
| 204 No Content | <code>DISPATCH_ACCEPTED_WITHOUT_PROVENANCE</code>；不得宣稱成功或 provenance 成立，不 retry |
| 其他非成功 response | <code>DISPATCH_FAILED</code>；保存可用 metadata，fail-closed，不 retry |

上述兩種「dispatch 可能已成立」狀態不得在同一次 invocation 再送一次 request，避免建立重複 run。它們只能等待後續人工或監控核對。

### 5.4 結構化 log 與決策集合

每次 Worker invocation 的結構化 log 至少保存：

- <code>configured_watchdog_schedule_expression</code>
- <code>trigger_schedule_expression</code>
- <code>scheduled_time</code> 與可讀 UTC 值
- <code>invocation_started_at</code>
- <code>invocation_delta_ms</code>
- <code>MAX_INVOCATION_LAG_MS</code>
- <code>target_date</code>
- workflow selector、primary run ID（若有）
- <code>workflow_run_id</code>、<code>run_url</code>、<code>html_url</code>（若有）
- HTTP status、API version <code>2026-03-10</code>
- 最終 decision、原因碼，以及移除敏感資訊後的 response metadata

決策只允許為：

- <code>PRIMARY_PRESENT</code>
- <code>FALLBACK_ALREADY_REQUESTED</code>
- <code>DISPATCH_CONFIRMED</code>
- <code>DISPATCH_RESPONSE_INVALID</code>
- <code>DISPATCH_ACCEPTED_WITHOUT_PROVENANCE</code>
- <code>CHECK_FAILED</code>
- <code>DISPATCH_FAILED</code>
- <code>STALE_SCHEDULED_INVOCATION</code>

Cloudflare 與 GitHub logs 是 provenance 證據，不是新的 canonical 資料庫，也不得輸出 token。

## 6. Workflow provenance、run-name 與 execution manifest

### 6.1 Workflow inputs 與日期 Gate

<code>workflow_dispatch</code> 只使用下列兩個 inputs：

- <code>trigger_source</code>：Watchdog 固定為 <code>fallback-watchdog</code>；manual 使用 <code>manual</code> 或預設值。
- <code>target_date</code>：Watchdog 必填，格式必須為 <code>YYYY-MM-DD</code>；manual 可留空。

Fallback workflow 的 <code>target_date</code> 必須保留 Watchdog 傳入值。workflow 不得因實際開始時間跨出台北日期而重算、覆寫或默默改成執行當日。格式、event 或來源不符時為 <code>CONFIG_ERROR</code>，停止且不得產生 PR。

### 6.2 <code>run-name</code> 的限縮用途

<code>run-name</code> 只能引用 <code>github</code> 與 <code>inputs</code> contexts。它只能作為事件來源、schedule／dispatch 類型與 run number 的人類可讀標籤，不得包含或充當精確 <code>target_date</code>、dispatch response 或正式 provenance 證據。

### 6.3 三種來源的 manifest 對應

Manifest 的 <code>trigger_source</code> 是規範化值，與 workflow input <code>fallback-watchdog</code> 不同：

| manifest <code>trigger_source</code> | <code>trigger_event</code> | <code>trigger_schedule_expression</code> | actor 記錄 | 允許條件 |
| --- | --- | --- | --- | --- |
| <code>primary</code> | <code>schedule</code> | <code>17 21 * * *</code> | <code>null</code> | <code>github.event_name=schedule</code> |
| <code>watchdog</code> | <code>workflow_dispatch</code> | <code>0 22 * * *</code> | Worker dispatch identity，非 manual actor | input 為 <code>fallback-watchdog</code>，且事後可與 <code>DISPATCH_CONFIRMED</code> 的 run ID 串聯 |
| <code>manual</code> | <code>workflow_dispatch</code> | <code>null</code> | <code>github.actor</code>，不可為空 | input 為 manual／預設人工來源 |

Worker 必須在 dispatch 前驗證 <code>controller.cron</code>；workflow 必須在 pipeline 前驗證 event、input 與這張表的內部對應。任一來源、event、cron、actor 或 <code>target_date</code> 契約不符時皆 fail-closed，不執行 pipeline、不建立或更新 PR。

<code>fallback-watchdog</code> input 本身不能證明呼叫者身分。只有 Worker 的 <code>DISPATCH_CONFIRMED.workflow_run_id</code> 與 GitHub 實際 <code>github.run_id</code> 相同，才可在驗收時標示為已證明的 watchdog fallback。

### 6.4 Non-canonical execution manifest

每個有效 pipeline run 必須產生一份 JSON execution manifest，僅以 GitHub Actions run artifact 上傳。它不是 repo 檔案、不是 Vault 內容、不是第二個 canonical 資料庫，也不改變四份 Markdown 的任何位元組。

Manifest 至少包含：

- <code>schema_version</code>、<code>timezone=Asia/Taipei</code>、<code>target_date</code>
- <code>configured_primary_schedule_expression</code>
- <code>configured_watchdog_schedule_expression</code>
- <code>trigger_source</code>、<code>trigger_event</code>、<code>trigger_schedule_expression</code>
- <code>workflow_started_at</code>、<code>workflow_completed_at</code>；Watchdog controller 的 <code>scheduled_time</code>、<code>invocation_started_at</code> 與 <code>invocation_delta_ms</code> 仍以第 5.4 節可由 run ID 串聯的 Worker log 為權威，不得在 workflow 端自行推導
- GitHub <code>run_id</code>、<code>run_attempt</code>、workflow SHA、workflow file、head SHA 與 branch
- manual 的 <code>github.actor</code>，或 watchdog 的 dispatch correlation reference
- 四份 canonical outputs 的精確 <code>path</code> 與生成後位元組的 <code>sha256</code>

四份 Markdown 保持既有 canonical generator 格式：不新增 frontmatter，不改正文、標題、檔名或 hash 契約。manifest 中的 hash 只描述既有輸出，不是重寫或正規化輸出的依據。

### 6.5 Step Summary、PR body 與 manifest 一致性 Gate

Step Summary、PR body 與 manifest 必須由同一份先驗證的 provenance model 生成，並在呼叫建立／更新 PR 前比較下列共同欄位：

- event、來源、trigger cron、時區與 <code>target_date</code>
- GitHub run ID、run attempt、workflow SHA 與 manifest artifact 名稱
- manifest 所列四個 output paths 與 SHA256

任一不一致即為 <code>PROVENANCE_MISMATCH</code>，fail-closed，不得建立或更新 PR。PR 建立後、啟用 auto-merge 前仍須回讀 PR body 與預期模型比較；不一致時不得啟用 auto-merge。

PR body 至少保存 event、來源、trigger cron、<code>target_date</code>、時區、run ID／attempt、workflow SHA 與 manifest artifact 名稱。Step Summary 提供相同資訊的可讀摘要。manifest 提供完整結構化欄位與四份 SHA256。

## 7. 同日冪等與四檔 canonical Gate

在安裝相依套件與執行 Horizon pipeline 前，必須對 <code>origin/main</code> 與固定發布分支 <code>automation/horizon-daily-publish</code> 呼叫同一個可測試函式，使用完全相同的判定契約。

對每個 <code>target_date</code>，集合固定為以下四個精確路徑，不得使用 glob：

1. <code>data/summaries/horizon-{target_date}-zh.md</code>
2. <code>data/summaries/horizon-{target_date}-en.md</code>
3. <code>docs/_posts/{target_date}-summary-zh.md</code>
4. <code>docs/_posts/{target_date}-summary-en.md</code>

四檔共同條件：

- strict UTF-8 可解碼。
- 正文非空。
- 內容包含精確 <code>target_date</code>。
- 不含不分大小寫的 <code>placeholder</code>、<code>TODO</code> 或 <code>TBD</code>。
- 路徑、標題與 frontmatter（適用時）解析出的日期全部相同且等於 <code>target_date</code>。

兩份 summary 的標題分別精確為：

- <code># Horizon 每日快遞 - {target_date}</code>
- <code># Horizon Daily - {target_date}</code>

兩份 <code>docs/_posts</code> 必須有可解析的 YAML frontmatter，且精確符合：

- <code>layout: default</code>
- <code>date: {target_date}</code>
- 繁中檔：<code>lang: zh</code> 與 <code>title: "Horizon Summary: {target_date} (ZH)"</code>
- 英文檔：<code>lang: en</code> 與 <code>title: "Horizon Summary: {target_date} (EN)"</code>
- frontmatter 後的發布正文非空

判定只允許：

| 狀態 | 結果 |
| --- | --- |
| 四檔全數存在且逐一合格於 <code>origin/main</code> | <code>ALREADY_PUBLISHED</code>；不跑 pipeline、不建立或更新 PR |
| 四檔全數存在且逐一合格於固定發布分支 | <code>ALREADY_IN_PROGRESS</code>；不跑 pipeline、不新增第二張 PR |
| 四檔全部不存在 | 才可繼續 pipeline |
| 僅 1–3 檔存在，或任一檔不合格 | <code>CANONICAL_SET_INCOMPLETE</code>；fail-closed，不得覆蓋不明狀態 |

因此 fallback 後才到達的 delayed schedule，最多命中 <code>ALREADY_PUBLISHED</code> 或 <code>ALREADY_IN_PROGRESS</code>，不得產生第二份同日 artifact 或第二張 PR。

## 8. 未來驗收契約（不授權 TDD 計畫或實作）

本節只定義未來實作完成後的可驗收行為，並非 TDD 實作計畫。本輪的 TDD PLAN 狀態為 <code>NOT AUTHORIZED</code>。

### 8.1 Deterministic tests

未來的 unit／integration 測試必須涵蓋：

- 第 3.1 節半開區間、完整分頁、exact workflow selector／<code>event=schedule</code>／<code>branch=main</code>，以及 0、1、多筆 primary 候選的 fail-closed 行為。
- <code>controller.cron</code> 相符與不符、<code>scheduled_time</code> 轉換、跨出台北日期、負延遲、剛好 300000 ms 與超過上限 1 ms。
- <code>return_run_details=true</code> 的合法 200、缺 run ID 或 URL 的 200、URL／ID 不一致與 204；後三者均不得 retry 或宣稱 provenance 成立。
- primary-present、primary-missing、同日 fallback 去重與 fallback 後 delayed schedule 的 collision 防護。
- primary、watchdog、manual 三種來源的 event、cron、actor、manifest 與 fail-closed 對應。
- 四檔完整合格、單檔／三檔殘缺、任一檔內容不合格，以及 main／固定發布分支相同 Gate 的結果一致性。
- Step Summary、PR body 與 manifest 任一共同欄位不一致時，不得建立 PR 或啟用 auto-merge。

### 8.2 Production acceptance

Production 只採自然觀測，不得為了製造 primary-missing 情境而暫時破壞 primary 排程、修改 cron 或建立長期測試 runtime。

- 正常 daily primary：證明 primary run、四檔、PR／auto-merge 與 Watchdog 無干預。
- 生產環境尚未自然發生 primary-missing 時，記錄 <code>PRODUCTION_PRIMARY_MISSING_OBSERVATION = NOT_OBSERVED</code>；在 deterministic tests 與正常 primary production acceptance 均通過後，它不阻擋 P0-B2R 關閉。
- 未來自然發生 primary-missing 時，可作為補充證據，必須以 <code>DISPATCH_CONFIRMED</code>、GitHub run、PR、merge、manifest 與四檔 hash 串聯。

## 9. 認證、證據與治理

Watchdog 使用僅限 <code>michaelluetw-bit/Horizon</code> 的專用 fine-grained token，最小權限為 <code>Actions: write</code>。它只存於 Cloudflare Worker encrypted secret <code>HORIZON_GITHUB_TOKEN</code>，不得出現在 Worker、GitHub logs、錯誤訊息或 fixture。

原 Horizon workflow 仍使用既有 GitHub App 建立 PR；Watchdog token 不參與內容寫入或 PR 操作。

- P0-B2 維持 <code>FAILED</code>，不得因 fallback 成功改寫歷史結論。
- 新 Gate 名稱固定為 <code>P0-B2R｜Scheduler Recovery</code>。
- P0-B2R 通過前不啟動 P0-B3。
- 正式驗收證據只寫入既有 Vault：<code>C:\Users\micha\Documents\2026_agent\download\knowledge\19_codex\AI Executive Dashboard</code>。
- <code>.codex/automations/.../memory.md</code> 可作執行紀錄，但不是正式驗收 evidence root。
- 不使用 <code>C:\Users\micha\OneDrive\Documents\AI Executive Dashboard</code>。

## 10. 實作邊界與未核准位置

預期實作範圍僅限：

1. Horizon workflow 的排程、provenance inputs、run-name 與 preflight Gate。
2. 可測試的同日 canonical Gate 與 execution manifest。
3. Cloudflare Watchdog、其最小部署設定與 focused tests。
4. P0-B2R 驗收記錄。

不進行相鄰重構，不修改 Horizon 摘要策略、內容生成邏輯、PR 門禁、Hosted Dashboard 或 Obsidian 發布流程。

~~~
ops/horizon-watchdog/
STATUS: NON_NORMATIVE
IMPLEMENTATION LOCATION: NOT APPROVED
~~~

上列位置僅為非規範性候選；本 Spec 不建立資料夾、不鎖定 Worker 技術架構，也不得預先影響後續 TDD 設計。

## 11. 官方依據

- GitHub schedule 延遲／丟棄說明：<https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule>
- GitHub workflow-runs API：<https://docs.github.com/en/rest/actions/workflow-runs>
- GitHub workflow syntax：<https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- GitHub workflow dispatch 回傳 run ID：<https://github.blog/changelog/2026-02-19-workflow-dispatch-api-now-returns-run-ids/>
- Cloudflare Scheduled Handler：<https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/>
- Cloudflare Cron Triggers：<https://developers.cloudflare.com/workers/configuration/cron-triggers/>

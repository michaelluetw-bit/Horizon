# Horizon 每日快遞 - 2026-11-17

> 從 46 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [vLLM 0.34.0 預設啟用可擴充 KV 快取](#item-tech-news-1) ⭐️ 8.0/10
2. [美國新規限制遠端使用先進 AI 晶片](#item-tech-news-2) ⭐️ 8.0/10
3. [卡內基美隆 CS Learn 免費公開完整學期課程影片](#item-tech-news-3) ⭐️ 7.0/10
4. [Rust 日期時間函式庫 Jiff 推出 1.0](#item-tech-news-4) ⭐️ 7.0/10
5. [Microsoft 將大型郵件中斷歸因於 7 月修補缺陷](#item-tech-news-5) ⭐️ 7.0/10
6. [Marimba 以凍結語音編碼器回答音訊問題](#item-tech-news-6) ⭐️ 7.0/10
7. [Qwen4-Max 上線，計畫公開小型模型權重](#item-tech-news-7) ⭐️ 7.0/10
8. [騰訊混元推出 Hy4 flash，降低 API 價格](#item-tech-news-8) ⭐️ 7.0/10
9. [美國與九國簽署《舊金山宣言》協調 AI 供應鏈](#item-tech-news-9) ⭐️ 7.0/10
10. [亞馬遜稱攻擊者利用 Artex 竊取 AI 應用金鑰](#item-tech-news-10) ⭐️ 7.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [vLLM 0.34.0 預設啟用可擴充 KV 快取](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM 0.34.0 已發布，新增 10 組模型支援，包括 Mistral Large 4、MiniMax-M3.1-Flash 和 Nemotron-3.5-Transcribe。CUDA 與 ROCm 的可擴充 KV 快取現在預設啟用，會依暖機後實際可用的記憶體配置快取；Model Runner V1 則已移除，V2 成為唯一的 GPU runner。發布說明宣稱，特定工作負載下，4 顆 GB200 的 Step5 解碼速度最高提升至 1.95 倍，但部分 H200 模型在並行數 128 時，每 token 解碼延遲增加 6% 至 18%。

github · khluu · 11月16日 23:22

**「背景」** KV 快取儲存模型推論時已計算的鍵值資料，避免生成後續文字時重複計算。Horizon 9 月 10 日的日報曾報導，vLLM v0.29.0 已將 Model Runner V2 設為預設；v0.34.0 則移除 V1，使 V2 成為唯一的 GPU runner。

**「升級注意事項」** 使用者升級前須移除 \`VLLM\_USE\_V2\_MODEL\_RUNNER=0\`，並將 V1 自訂 logits processor 移植至 V2；否則現有設定可能無法啟動。預設區塊大小從 16 改為 64，可用 \`--block-size 16\` 保留舊行為；若要保留舊的快取配置方式，可設定 \`--gpu-memory-utilization 0.9\` 或使用 \`--no-enable-extensible-kv-cache\`。新版套件與映像檔僅支援 ROCm 10.0，並要求 \`huggingface\_hub &gt;= 2.0.0\`、\`tokenizers &gt;= 0.23.3\` 和 \`timm &gt;= 1.0.30\`；\`fp\_quant\` 檢查點也不再能載入。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases/tag/v0.29.0">2026-09-10 — vllm-project/vllm released v0.29.0</a></li>

</ul>
</details>

**標籤**: `#vLLM`, `#LLM inference`, `#KV cache`, `#GPU performance`, `#open source`

---

<a id="item-tech-news-2"></a>
### [美國新規限制遠端使用先進 AI 晶片](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

美國商務部 11 月 16 日發布臨時最終規則，將先進 AI 晶片與伺服器的出口管制延伸至遠端存取，以防止透過第三國資料中心繞過限制。據 The Verge 報導，新規也要求向印尼、馬來西亞、新加坡、泰國和巴西再出口 AI 晶片時申請許可；來源未說明具體實施細節。

telegram · zaihuapd · 11月16日 14:44

**「背景」** 美國既有管制限制敏感技術的取得，但第三國資料中心的遠端運算可能成為繞道方式。Horizon 的 11 月 13 日日報曾報導，商務部正與其他政府機關討論防止中國 AI 公司遠端使用先進晶片的規則；如今已發布臨時最終規則。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology">www.bis.gov</a></li>
<li><a href="https://www.theinformation.com/articles/commerce-department-finalizing-long-awaited-ai-remote-access-rule">2026-11-13 — US Reportedly Nears AI Chip Remote Access Rule</a></li>

</ul>
</details>

**標籤**: `#AI 晶片`, `#出口管制`, `#雲端計算`, `#美國科技政策`

---

<a id="item-tech-news-3"></a>
### [卡內基美隆 CS Learn 免費公開完整學期課程影片](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡內基美隆大學的 CS Learn 在 YouTube 免費公開現行電腦科學課程的完整學期講座影片。負責人 Phillip Compeau 表示，計畫本週每天首播一門課，並預計在 1 月推出更多課程。

hackernews · pcompeau · 11月16日 20:43 · [社群討論](https://news.ycombinator.com/item?id=50522980)

**「背景」** 免費公開大學課程並非新做法。CS Learn 負責人 Phillip Compeau 指出，麻省理工學院約 25 年前就已開始提供類似資源。

**「社群討論」** 有留言者認為，講座影片需要搭配教材、專案和回饋，才能發揮較好的學習效果。另一位自稱卡內基美隆校友的留言者則對機器學習系統課程開放表示歡迎。

**標籤**: `#computer science education`, `#open courseware`, `#machine learning systems`, `#online learning`

---

<a id="item-tech-news-4"></a>
### [Rust 日期時間函式庫 Jiff 推出 1.0](https://burntsushi.net/jiff/) ⭐️ 7.0/10

Jiff 1.0 是供 Rust 開發者使用的日期時間函式庫。現有資料未說明此版本的具體功能或相較先前版本的變更。

hackernews · burntsushi · 11月16日 16:53 · [社群討論](https://news.ycombinator.com/item?id=50519744)

**「背景」** 日期時間運算須考慮時區和日光節約時間，當地時鐘變更可能使時間換算變得複雜。Jiff 將時區處理放在 API 的核心，並自動處理許多與日光節約時間相關的常見問題。

**「社群討論」** 一名前 Chrono 維護者表示，使用者重視 API 穩定性，讓他改善介面的嘗試遭遇阻力，最終因疲憊而停止維護。另有從事小行星軌道模擬的開發者詢問 Jiff 如何處理 TAI 等時間尺度，以及是否容易加入 UT1；所附留言未提供答案。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant&#x27;s Blog</a></li>

</ul>
</details>

**標籤**: `#rust`, `#datetime`, `#open-source`, `#developer-tools`

---

<a id="item-tech-news-5"></a>
### [Microsoft 將大型郵件中斷歸因於 7 月修補缺陷](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

Microsoft 表示，一次大型電子郵件服務中斷是由 7 月修補程式引入的軟體缺陷所致。現有資料未提供受影響服務的詳細範圍或中斷時間。

hackernews · Bender · 11月16日 13:18 · [社群討論](https://news.ycombinator.com/item?id=50517321)

**「事件背景」** Horizon 11 月 14 日的日報曾報導，Microsoft 365 服務中斷超過 12 小時，影響 Outlook、Teams 和 Copilot；微軟當時將故障歸因於伺服器問題，並表示未發現惡意活動。

**「社群討論」** 一位留言者指出，較低階的測試環境與正式環境硬體不同，可能讓並行處理錯誤未在測試階段被發現，並質疑這樣的測試取捨是否可接受。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/">2026-11-14 — Microsoft 365 outage disrupts Outlook, Teams and Copilot</a></li>

</ul>
</details>

**標籤**: `#Microsoft`, `#email outage`, `#software defects`, `#reliability testing`

---

<a id="item-tech-news-6"></a>
### [Marimba 以凍結語音編碼器回答音訊問題](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba 讓使用者以文字詢問音訊片段中的詞語、語言或說話者等問題，並回傳經校準的機率；每個 8 秒片段只需透過一次凍結的 Qwen3-ASR-0.6B 編碼器，即可供多個問題使用。詞語偵測採零樣本辨識結果評分與校準，其他任務則使用語言分數或特定層的讀出模型。作者表示，在 1,000 個公開問題的 9 項測試中，Marimba 有 6 項與 Qwen3-Omni（30B-A3B）持平或更好，但其中一句話結束偵測結果對 Marimba 而言使用了訓練分佈內的資料；這些比較尚未獲獨立驗證。在 Smart Turn 自有測試集上，Marimba 的句尾偵測 AUROC 為 0.930，低於 Smart Turn v3.2 的 0.982，且其讀出模型在未見過的場景分類任務中只有隨機水準；程式碼、Apache-2.0 權重、展示頁面與 pip 套件均已提供。

reddit · r/MachineLearning · /u/solanotodesch · 11月16日 15:47

**「背景」** 語音編碼器會將音訊轉成可供模型處理的特徵；「凍結」表示其引數在後續任務訓練時保持不變。不同任務可使用專門的讀出模型解析這些特徵，而機率校準則用來調整分數，使其更能反映實際發生的機率。

**標籤**: `#speech processing`, `#speech recognition`, `#audio models`, `#model evaluation`

---

<a id="item-tech-news-7"></a>
### [Qwen4-Max 上線，計畫公開小型模型權重](https://mp.weixin.qq.com/s/pJUt0xwD6H-WMyzd8TjZaQ) ⭐️ 7.0/10

阿里通義千問推出旗艦模型 Qwen4-Max，並計畫後續推出規模較小的 Qwen4 系列模型，公開其權重。據來源報導，Qwen4-Max 採用稀疏 MoE 架構，總引數為 2.4 兆，原生支援視覺理解與百萬 Token 上下文。來源稱，相較上一代，單項任務平均費用從人民幣 26.58 元降至 11.16 元，Token 消耗減少近 50%，API 定價也已下調；但未提供測試條件或新價格細節。

telegram · zaihuapd · 11月16日 02:52

**「背景」** 稀疏混合專家（MoE）架構在處理每個 token 時只啟用部分引數；據 ForkLog 報導，Qwen4-Max 每個 token 啟用 710 億個引數。Horizon 的 9 月 3 日日報曾報導前代 Qwen3.8-Max-0902 也有 2.4 兆個總引數及 100 萬 token 上下文長度。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://forklog.com/en/alibaba-launches-qwen4-max-ai-model-with-2-4-trillion-parameters/">Alibaba Launches Qwen 4 - Max AI Model with 2 . 4 Trillion Parameters</a></li>
<li><a href="https://mp.weixin.qq.com/s/BfKRXMAR5ykD58LDkBftLg">2026-09-03 — 🤖 阿里釋出 Qwen3.8-Max-0902，CodeArena 程式設計榜 1691 分奪冠</a></li>

</ul>
</details>

**標籤**: `#large language models`, `#Qwen`, `#mixture of experts`, `#open-weight models`

---

<a id="item-tech-news-8"></a>
### [騰訊混元推出 Hy4 flash，降低 API 價格](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

騰訊混元推出多模態模型 Hy4 flash，總引數量為 2,240 億，每個 Token 啟用 120 億引數，支援 100 萬 Token 上下文。API 每百萬 Token 輸入價格為人民幣 0.5 元、輸出為 2 元，快取命中時為 0.02 元，低於 Hy4。騰訊宣稱其綜合效果略優於 Hy4 preview，WorkIndex 單任務成本分別為 Hy4 preview 的十三分之一及 Hy4 的二十分之一，但未提供基準測試細節。Hy4 flash 已在騰訊雲 TokenHub、WorkBuddy 和元寶上線，並計畫開源；11 月 30 日前 WorkBuddy 限時免費、API 五折。

telegram · zaihuapd · 11月16日 07:17

**「背景」** Horizon 8 月 31 日的日報曾報導，Hy4 Preview 是開放權重的純文字模型，總引數為 770B、啟用引數為 49B，支援 1M token 上下文。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/29/hy4/">2026-08-31 — Introducing Hy4 Preview</a></li>

</ul>
</details>

**標籤**: `#large language models`, `#multimodal AI`, `#AI pricing`, `#Tencent Hunyuan`

---

<a id="item-tech-news-9"></a>
### [美國與九國簽署《舊金山宣言》協調 AI 供應鏈](https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/) ⭐️ 7.0/10

美國於 11 月 15 日與澳洲、印度、以色列、日本、南韓、卡達、新加坡、阿聯及英國簽署《舊金山宣言》，承諾共同保護支撐超級智慧（SI）供應鏈的敏感技術與關鍵基礎設施。宣言提出設立五個工作小組，涵蓋創新政策、關鍵領域應用、全棧供應鏈協作、安全港與供應鏈安全樞紐，以及 SI 安全與韌性。來源未說明具體措施、約束力或實施細節。

telegram · zaihuapd · 11月16日 10:40

**「背景」** 這份宣言是在 Pax Silica 創始成員會議上簽署的。Pax Silica 是美國國務院推動的倡議，旨在與盟友及可信夥伴合作，強化超級智慧與供應鏈安全。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/">The San Francisco Declaration on the Secure Foundations of ...</a></li>
<li><a href="https://www.state.gov/pax-silica/">Pax Silica - United States Department of State</a></li>

</ul>
</details>

**標籤**: `#人工智慧政策`, `#AI 供應鏈`, `#國際合作`, `#技術安全`

---

<a id="item-tech-news-10"></a>
### [亞馬遜稱攻擊者利用 Artex 竊取 AI 應用金鑰](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

亞馬遜稱，攻擊者使用開源滲透測試框架 Artex 驅動 AI 代理，竊取對公網暴露的 LiteLLM、Dify 等 AI 應用的 API 金鑰，驗證後匯入共享池，用於支付更多大模型呼叫。亞馬遜表示，這項活動自 10 月 3 日開始，並於 11 月 5 日被其誘餌網路 MadPot 截獲阻斷。亞馬遜以中等信心將行動歸因於中國相關威脅組織，並稱不是所有列為目標的系統都已遭入侵，可能受影響的 AWS 客戶已接獲通知。攻擊規模與損失尚未披露。

telegram · zaihuapd · 11月16日 13:00

**「背景」** API 金鑰用於驗證對模型服務的存取，外洩後可能被他人盜用，產生模型呼叫費用。亞馬遜的 MadPot 是由全球分佈的誘餌感測器組成的網路，用來蒐集可疑活動。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/">Amazon Threat Intelligence observes threat actors running ...</a></li>

</ul>
</details>

**標籤**: `#AI代理`, `#網路安全`, `#API金鑰`, `#大模型`, `#威脅情報`

---


# Horizon 每日快遞 - 2026-11-16

> 從 30 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [美團釋出 LongCat-2.5 權重，稱僅用華為晶片訓練](#item-tech-news-1) ⭐️ 8.0/10
2. [Meta FAIR 與紐約大學：視覺編碼器可不預訓練](#item-tech-news-2) ⭐️ 7.0/10
3. [cudamemcpy-tuner 在 B300 測試中提升傳輸速度](#item-tech-news-3) ⭐️ 7.0/10
4. [多人遊戲原型以本機世界模型生成玩家視角](#item-tech-news-4) ⭐️ 7.0/10
5. [Cybercab 訂閱協議：每月 299 美元才能執行](#item-tech-news-5) ⭐️ 7.0/10
6. [FAA 全國地面停飛與光纖升級路由器故障有關](#item-tech-news-6) ⭐️ 7.0/10
7. [美國法官駁回 DRAM 價格操縱案撤訴動議](#item-tech-news-7) ⭐️ 7.0/10
8. [Phantasialand 氯氣事件與 Microsoft 365 中斷傳有關](#item-tech-news-8) ⭐️ 6.0/10
9. [MacBook Pro OLED 螢幕的 PWM 閃爍疑慮](#item-tech-news-9) ⭐️ 6.0/10
10. [文章提議將所有 AI 生成程式碼開放原始碼](#item-tech-news-10) ⭐️ 6.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [美團釋出 LongCat-2.5 權重，稱僅用華為晶片訓練](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美團 LongCat 團隊在模型正式發布一週後，釋出 LongCat-2.5 權重，採用可商用的 MIT 授權。該模型針對執行長時間、多步驟任務的 AI 智慧體設計，尤其適用於程式開發，支援文字、圖片與影片輸入，每個 token 約啟用 480 億個引數。官方表示，模型訓練全程使用華為昇騰加速卡，未使用 NVIDIA GPU；其在 Terminal Bench v2.1 的得分為 88.4，略低於 Claude Opus 5 的 89.1。上述訓練與基準測試說法在提供的資料中未經獨立驗證。

telegram · zaihuapd · 11月15日 11:08

**「背景」** 開放模型權重讓開發者能自行部署及調整模型，但不代表訓練資料也已公開。每個 token 的啟用引數量，是模型處理單位資料時動用的引數數量，與模型的總引數量不同。

**標籤**: `#LongCat`, `#open-weight models`, `#AI agents`, `#Huawei Ascend`, `#multimodal AI`

---

<a id="item-tech-news-2"></a>
### [Meta FAIR 與紐約大學：視覺編碼器可不預訓練](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 7.0/10

Meta FAIR 與紐約大學研究人員比較了 200 多個多模態語言模型，發現視覺編碼器的獨立預訓練可省略，但視覺專用引數仍對視覺問答表現重要。研究在計算預算中納入編碼器預訓練成本；主要比較使用 Qwen3 1.7B 和 4B 架構，並以 16 個視覺問答及 12 個語言基準測試評估。研究團隊也表示，將視覺專用權重放進語言模型前 8 層，可達到與獨立編碼器相當的表現，首個 token 的等待時間約縮短 13%。

reddit · r/MachineLearning · /u/trungh98 · 11月15日 17:38

**「研究背景」** 多模態語言模型常用視覺編碼器處理影像，再將結果送入語言模型；這種設計同時涉及獨立預訓練、視覺專用引數，以及編碼器位於語言模型之前等選擇。研究團隊將這些選擇拆開比較，避免直接比較訓練資料和計算量不同的已發布模型。

**「實務影響」** 對模型設計者而言，省去獨立預訓練不一定意味著要完全移除視覺專用引數：研究報告指出，沒有編碼器的模型約需三倍計算量才能追上視覺問答表現。將原本分配給編碼器的引數轉給語言模型，則改善了文字任務，但沒有改善視覺問答。

**標籤**: `#multimodal language models`, `#vision encoders`, `#model pretraining`, `#compute budgets`

---

<a id="item-tech-news-3"></a>
### [cudamemcpy-tuner 在 B300 測試中提升傳輸速度](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

開發者發布 cudamemcpy-tuner，表示該工具可加速 cudaMemcpy 的可分頁記憶體傳輸。在一項自述的 B300 PyTorch 測試中，使用 \`cmt tune\` 後，1 GiB 張量的 CPU 到 GPU 傳輸吞吐量從 10.2 提升至 51.5 GB/s，約為 5 倍。所提供的資料未說明加速機制，也不足以確認其他工作負載能否獲得相同效果。

reddit · r/MachineLearning · /u/makneeee · 11月15日 18:20

**「背景」** CUDA 的 cudaMemcpy 可用來在 CPU 主機記憶體與 GPU 之間複製資料。主機端可使用可分頁記憶體或固定（pinned）記憶體，兩者使用相同的 cudaMemcpy 語法。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/">How to Optimize Data Transfers in CUDA C/C++ | NVIDIA Technical...</a></li>

</ul>
</details>

**標籤**: `#CUDA`, `#GPU data transfer`, `#performance optimization`, `#open source`

---

<a id="item-tech-news-4"></a>
### [多人遊戲原型以本機世界模型生成玩家視角](https://www.reddit.com/r/MachineLearning/comments/1xx4ta3/we_made_a_multiplayer_game_where_each_players/) ⭐️ 7.0/10

開發者推出免費公開測試版多人遊戲原型，由輕量伺服器同步遊戲狀態，並在各玩家的 GPU 上執行世界模型，依據伺服器狀態、玩家操作及先前畫面，透過擴散 Transformer 生成下一影格。模型使用開放的 10 人 CS:GO 機器人對戰資料集訓練，涵蓋約 3,958 小時、以 16 Hz 對齊的所有玩家視角與輸入。開發者表示，目前遊戲只有一張小地圖、僅提供手槍，畫面細節也不佳；Windows 版本需要 RTX 3080 或更高階顯示卡，另有實驗性 Mac 版本。

reddit · r/MachineLearning · /u/bengal7ion · 11月15日 19:46

**「背景」** 團隊上個月釋出開放資料集，收錄約 3,958 小時的 10 人 CS:GO 電腦玩家對戰，並以 16 Hz 對齊所有玩家視角與操作。團隊使用這些資料訓練世界模型，讓模型根據遊戲狀態、玩家操作與先前畫面產生下一幀。

**「使用影響」** 想參與測試的玩家需要符合顯示卡要求，或嘗試實驗性的 Mac 版本；開放資料集則讓研究者可取得對齊的多人視角與操作資料。

**標籤**: `#world models`, `#diffusion transformers`, `#multiplayer games`, `#machine learning datasets`

---

<a id="item-tech-news-5"></a>
### [Cybercab 訂閱協議：每月 299 美元才能執行](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 7.0/10

據報導，特斯拉 Cybercab 訂閱協議列出 29,990 美元車價，車主須支付每月 299 美元的自主駕駛訂閱費，否則車輛無法執行；特斯拉可提前一個月通知調整價格。欠費或違規使用可能導致訂閱暫停或取消，累計三次警告則會停用自動駕駛一週。Electrek 指出，Cybercab 與用於 Robotaxi 的 Model Y 均採用 AI4 硬體及相同的自動駕駛軟體，但提供一般車主使用的 FSD 仍須人類監督。

telegram · zaihuapd · 11月15日 01:10

**「背景」** 據 Electrek，Cybercab 與用於 Robotaxi 的 Model Y 均採用 AI4 硬體，並執行相同的自動駕駛軟體；一般車主使用的 FSD 則仍須由人類監督。

**「使用限制」** 依報導所述協議，Cybercab 車主只能在指定區域執行，且未經授權不得接入叫車、配送或租賃平臺。

**標籤**: `#Tesla`, `#Cybercab`, `#autonomous vehicles`, `#subscription pricing`

---

<a id="item-tech-news-6"></a>
### [FAA 全國地面停飛與光纖升級路由器故障有關](https://www.theverge.com/transportation/1033898/faa-ground-stop-sean-duffy-faa-copper-wire) ⭐️ 7.0/10

美國交通部長 Sean Duffy 表示，FAA 下令全國地面停飛，原因是一處偏遠設施進行銅線更換為光纖的例行維護後，新裝路由器出現問題，影響數千航班。他說，該路由器每 4 至 5 秒向其他路由器發出逾千次連線請求，幹擾雷達訊號與飛機通訊；根本原因仍不明，可能涉及硬體故障、設定錯誤或承包商 L3Harris 的失誤。

telegram · zaihuapd · 11月15日 02:10

**「背景」** 地面停飛令要求受影響航班暫緩起飛，不代表已在空中的飛機立即停飛。路由器負責在網路之間轉送資料，大量連線請求可能佔用裝置資源，幹擾網路通訊。

**標籤**: `#networking`, `#critical infrastructure`, `#aviation systems`, `#outages`

---

<a id="item-tech-news-7"></a>
### [美國法官駁回 DRAM 價格操縱案撤訴動議](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 7.0/10

美國法官 Noël Wise 駁回美光、三星與 SK 海力士要求撤銷 DRAM 價格操縱集體訴訟的動議，認為原告提出的新證據顯示，三家廠商的同步行為「更像編隊飛行」。17 名個人與小企業原告指控，三家公司在一年內四度採取平行行動限制 DRAM 供應，導致價格上漲最多 500%；這些指控尚未獲證實。三家公司須在 12 月 7 日前回應，案件管理會議定於 2027 年 1 月舉行。

telegram · zaihuapd · 11月15日 16:39

**「背景」** DRAM 是電腦和伺服器用來暫存執行中資料的記憶體。駁回撤訴動議表示案件可繼續審理，並不代表法院已認定廠商合謀操縱價格。

**標籤**: `#DRAM`, `#antitrust`, `#semiconductors`, `#hardware industry`

---

<a id="item-tech-news-8"></a>
### [Phantasialand 氯氣事件與 Microsoft 365 中斷傳有關](https://www1.wdr.de/nrw/rheinland/rhein-erft-kreis/technischer-defekt-chlor-phantasialand-100.html) ⭐️ 6.0/10

據報導，Phantasialand 飯店發生氯氣中毒事件，造成 15 名住客受傷。一名留言者轉述 WDR 報導稱，業者表示 Microsoft 服務中斷導致電子郵件未送達，因此無人得知三溫暖區的安全系統已就自動投藥裝置過量注入氯發出警報。原文未提供，服務中斷在事件中的確切作用及故障細節尚無法確認。

hackernews · DeepLogin · 11月15日 18:36 · [社群討論](https://news.ycombinator.com/item?id=50509411)

**「背景」** 泳池的自動加藥系統負責投放氯，維護安全系統則會以電子郵件發出警報。這是兩個不同環節：據報導，過量投氯源於加藥系統故障，郵件服務中斷則使警報未能送達工作人員。

**「社群討論」** 多名留言者認為，危險裝置的警報不應完全依賴電子郵件，應有備援通訊或查核機制。一名自稱操作閉迴路氯投藥系統的留言者指出，感測故障可能導致氯濃度讀值偏低，進而造成過量投藥；這是其經驗分享，並非對本案故障原因的確認。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://windowsforum.com/news/outlook-outage-blocked-phantasialand-pool-alerts-before-chlorine-incident-injured-15.452435/">Outlook Outage Blocked Phantasialand Pool Alerts Before ...</a></li>

</ul>
</details>

**標籤**: `#cloud outages`, `#safety-critical systems`, `#reliability`, `#Microsoft 365`

---

<a id="item-tech-news-9"></a>
### [MacBook Pro OLED 螢幕的 PWM 閃爍疑慮](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 6.0/10

一篇文章對 MacBook Pro OLED 螢幕的脈衝寬度調變（PWM）閃爍及其對使用體驗的影響提出疑慮。現有資料不足以確認實際閃爍頻率或健康影響。

hackernews · MacAnorak · 11月15日 13:15 · [社群討論](https://news.ycombinator.com/item?id=50506719)

**「背景」** 脈衝寬度調變（PWM）透過快速開關發光元件來調整亮度，可能產生閃爍。MacAnorak 引述 Notebookcheck 的測試指出，採用 Mini-LED 螢幕的 M4 Pro MacBook Pro 測得的 PWM 頻率為 14,880 Hz。

**「社群討論」** 一名留言者質疑 240 Hz 的測量結論，推測雙層 OLED 的調變可能呈現 480 Hz 或 960 Hz，但這些數值尚未獲得確認。另有留言者分享自己對螢幕閃爍或其他光線特性敏感的經驗。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/">The MacBook Pro’s OLED PWM Problem: When a ‘Better’ Display ...</a></li>

</ul>
</details>

**標籤**: `#OLED`, `#PWM`, `#MacBook Pro`, `#Display Accessibility`

---

<a id="item-tech-news-10"></a>
### [文章提議將所有 AI 生成程式碼開放原始碼](https://jakub.jankiewicz.org/blog/ai-code-open-source/) ⭐️ 6.0/10

一篇文章提出，所有 AI 生成的程式碼都應開放原始碼。由於未提供文章內容，目前無法確認其具體論證或建議的適用範圍；討論則聚焦於著作權、人類開發者的貢獻，以及 AI 對開源程式碼的使用。

hackernews · jcubic · 11月15日 14:46 · [社群討論](https://news.ycombinator.com/item?id=50507303)

**「背景」** 著作權保護與是否開放原始碼是不同問題：程式碼可以受著作權保護，同時以開源授權釋出。美國著作權局表示，使用 AI 輔助創作，或在人類創作的作品中納入 AI 生成內容，本身不會排除著作權保護。

**「社群討論」** 一位留言者援引美國著作權局的指引，指出 AI 輔助人類創作與取代人類創作的情況有所不同。另一位留言者表示，雖然自己的開源程式碼曾用於 AI 訓練，但他也使用 AI 開發專有程式碼，認為人類的設計與反覆調整仍是實質貢獻，不應強制開源。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.copyright.gov/newsnet/2025/1060.html">NewsNet Issue 1060 | U.S. Copyright Office</a></li>

</ul>
</details>

**標籤**: `#AI-generated code`, `#open source`, `#copyright`, `#software development`

---


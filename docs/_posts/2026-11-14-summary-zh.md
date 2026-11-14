---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14
lang: zh
---

> 從 37 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [KORS 航空頻段監聽使用 GPU 處理訊號](#item-tech-news-1) ⭐️ 7.0/10
2. [ICML 2027 擬採兩階段審查與作者投稿限制](#item-tech-news-2) ⭐️ 7.0/10
3. [TorchTitan 訓練約 1 兆引數 MoE 的擴充套件實測](#item-tech-news-3) ⭐️ 7.0/10
4. [Claude Code 2.1.323 新增實驗性 Code Mode](#item-tech-news-4) ⭐️ 7.0/10
5. [訊息稱輝達管理層頁面將黃仁勳列為創辦人](#item-tech-news-5) ⭐️ 7.0/10
6. [Python 早期貢獻者 Tim Peters 逝世，享壽 74 歲](#item-tech-news-6) ⭐️ 7.0/10
7. [微軟 Outlook、Teams 與 Copilot 中斷逾 12 小時](#item-tech-news-7) ⭐️ 7.0/10
8. [DeepSeek 傳開放搜尋、檔案與語音應用 API](#item-tech-news-8) ⭐️ 7.0/10
9. [OpenAI 推出 ChatGPT Wallet 支付錢包](#item-tech-news-9) ⭐️ 7.0/10
10. [作者分享 JEPA 世界模型的 600 次實驗](#item-tech-news-10) ⭐️ 6.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [KORS 航空頻段監聽使用 GPU 處理訊號](https://orcasairband.com/) ⭐️ 7.0/10

Orcas 的航空無線電監聽網站提供 KORS 各頻率的即時收聽，並顯示通話逐字稿。開發者表示，系統使用 Ettus B210 接收器和兩張 RTX 4090 顯示卡，透過 CUDA 多相通道化處理航空頻段訊號，再解調、偵測傳輸並排除資料傳輸。開發者分享了可能與地面停飛有關的未編輯逐字稿，但現有內容不足以確認停飛原因或完整範圍。

hackernews · mmaunder · 11月13日 22:04 · [社群討論](https://news.ycombinator.com/item?id=50490593)

**「技術背景」** Ettus USRP B210 是軟體定義無線電收發裝置。多相通道化器利用濾波器組，將接收到的頻譜拆成多個可分別處理的頻道。

**「社群討論」** 一名讀者指出，回放中有一段通話提及飛往溫哥華的地面停飛；這與開發者分享的維多利亞地面管制通話片段涉及不同地點。另一名讀者表示許多傳輸聽起來模糊難懂，也顯示解讀通話內容需要謹慎。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.ettus.com/all-products/ub210-kit/">USRP B 210 USB Software Defined Radio (SDR) - Ettus Research</a></li>
<li><a href="https://www.mathworks.com/help/dsp/ref/dsp.channelizer.polyphase.html">polyphase - Return polyphase matrix - MATLAB</a></li>

</ul>
</details>

**標籤**: `#software-defined radio`, `#GPU signal processing`, `#aviation communications`, `#transcription`

---

<a id="item-tech-news-2"></a>
### [ICML 2027 擬採兩階段審查與作者投稿限制](https://www.reddit.com/r/MachineLearning/comments/1xvkxbj/icml_2027_changes_d/) ⭐️ 7.0/10

一篇 Reddit 貼文引述 ICML 2027 徵稿資訊指出，會議將採兩階段審查：領域主席決定論文是否進入完整審查，第一階段的退稿提議須由資深領域主席確認，作者會在 2 月 23 日前收到簡短理由。貼文稱，每人最多參與 20 篇投稿，參與 3 篇以上者須擔任計畫委員會成員。每篇論文須從作者中指定一名互惠審稿人，每名審稿人最多對應 6 篇論文；每位作者最多隻能參與一篇作者群中沒有合格互惠審稿人的論文。不符規定的投稿可能遭直接退稿；上述細節在所提供資料中尚未獨立驗證。

reddit · r/MachineLearning · /u/Gravitist · 11月13日 21:53

**「背景」** 機器學習會議仰賴研究人員審查投稿，領域主席則負責協調審稿與評估。隨著投稿增加，如何取得足夠的審稿人力並控制負荷成為會議面臨的問題。

**標籤**: `#ICML`, `#machine-learning-research`, `#peer-review`, `#conference-policy`

---

<a id="item-tech-news-3"></a>
### [TorchTitan 訓練約 1 兆引數 MoE 的擴充套件實測](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 7.0/10

作者表示，團隊使用 TorchTitan 在 384 顆 GH200 GPU 上訓練約 1 兆引數的混合專家（MoE）模型，達到每顆 GPU 每秒約 1,300 個 token，是起始吞吐量的 14 倍。配置採用 384 路全分片資料平行（FSDP）與節點內 4 路專家平行，沒有使用管線平行。團隊透過活化重算與解除安裝、減少通訊資料量及調整記憶體配置等方式改善效能；這些數字是作者的實測報告，所附摘錄未完整說明基準測試方法。

reddit · r/MachineLearning · /u/f14-bertolotti · 11月13日 16:28

**「背景」** TorchTitan 是以 PyTorch 原生技術打造的開源分散式訓練系統。專家混合（MoE）模型包含多個專家；專家平行化將專家分配到不同 GPU，FSDP 則切分模型權重，並在運算時按需彙集。

**「影響」** 對嘗試重現的訓練團隊而言，部分最佳化有取捨：作者表示，限制專家路由範圍雖提高了吞吐量，初步測試卻顯示可能損害訓練效果。此外，記憶體配置修正使用了 FSDP2 的私有旗標，作者稱該旗標正朝公開 API 的方向發展。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://arxiv.org/abs/2410.06511">[2410.06511] TorchTitan : One -stop PyTorch native solution for...</a></li>

</ul>
</details>

**標籤**: `#mixture-of-experts`, `#distributed-training`, `#TorchTitan`, `#GPU-performance`

---

<a id="item-tech-news-4"></a>
### [Claude Code 2.1.323 新增實驗性 Code Mode](https://code.claude.com/docs/en/changelog) ⭐️ 7.0/10

Claude Code 2.1.323 新增實驗性 Code Mode，讓 Claude 能以 JavaScript 呼叫工具，組織也可關閉此功能。新版加強外掛管理：不符合宣告版本範圍的外掛將無法安裝或更新，plugin validate 也新增 TypeScript 鉤子的型別檢查。其他改進包括擴充 .docx 檔案上傳支援及 30 秒鉤子心跳。

telegram · zaihuapd · 11月13日 03:47

**「背景」** 工具呼叫讓 Claude 在處理任務時使用工具；一般做法是逐次發出呼叫，而 Code Mode 允許以 JavaScript 組合呼叫。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://dev.to/piekwerk/claude-code-21323-pins-plugins-to-version-ranges-what-the-engines-field-enforces-and-6-things-to-13bc">Claude Code 2.1.323 pins plugins to version ranges: what the ...</a></li>

</ul>
</details>

**標籤**: `#Claude Code`, `#AI coding agents`, `#tool calling`, `#plugin management`

---

<a id="item-tech-news-5"></a>
### [訊息稱輝達管理層頁面將黃仁勳列為創辦人](https://investor.nvidia.com/governance/management-team/default.aspx) ⭐️ 7.0/10

據訊息來源報導，輝達 11 月 13 日更新官網管理層頁面，將科萊特·克雷斯列為臨時執行長，黃仁勳則列在「創辦人」欄位。報導稱，黃仁勳的簡介提及他於 1993 年創辦輝達，並曾任總裁、執行長及董事會成員；訊息未說明變動原因，也未提供獨立查證。

telegram · zaihuapd · 11月13日 04:30

**「背景」** 英偉達先前宣佈黃仁勳辭去執行長、總裁及董事職務；接任臨時執行長的科萊特・克雷斯此前擔任執行副總裁兼財務長。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/">NVIDIA Corporation - NVIDIA Announces CEO Transition</a></li>
<li><a href="https://www.gate.com/blog/jensen-huang-resigns-is-nvda-stock-still-a-good-investment">Jensen Huang Resigns: Is NVDA Stock Still a Good... | Gate Blog</a></li>

</ul>
</details>

**標籤**: `#英偉達`, `#高管變動`, `#科技產業`, `#人工智慧`

---

<a id="item-tech-news-6"></a>
### [Python 早期貢獻者 Tim Peters 逝世，享壽 74 歲](https://x.com/Itsfoss/status/2120957452937998716) ⭐️ 7.0/10

據轉述，Python 創造者 Guido van Rossum 宣佈，Python 社群早期貢獻者 Tim Peters 逝世，享壽 74 歲；來源未提供 van Rossum 的原始公告。Peters 是 Timsort 排序演演演算法的作者、《Python 之禪》（PEP 20）的撰寫者，也曾在 Python 軟體基金會董事會任職 13 年。訊息稱，他是 Python 的第二位實際使用者。

telegram · zaihuapd · 11月13日 09:55

**「背景」** Peters 在 Python 首次發布不久後便接觸這門語言。Guido van Rossum 稱他不僅是自己的導師，也參與了 Python 的早期語言設計。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028">In Memoriam: Tim Peters 1952–2026 - Core Development ...</a></li>

</ul>
</details>

**標籤**: `#Python`, `#Tim Peters`, `#Timsort`, `#開源社群`

---

<a id="item-tech-news-7"></a>
### [微軟 Outlook、Teams 與 Copilot 中斷逾 12 小時](https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/) ⭐️ 7.0/10

微軟 Outlook、Teams 與 Copilot 的服務中斷超過 12 小時，11 月 13 日仍影響全球企業及政府通訊。微軟表示，故障源於伺服器問題，未發現惡意活動；公司已擴大修復範圍，並看到服務回穩的跡象。這是微軟 365 服務今年第二次中斷。

telegram · zaihuapd · 11月13日 12:21

**「背景」** Outlook 提供電子郵件服務，Teams 則用於團隊通訊與協作。原報導指出，這是 Microsoft 365 今年第二次發生服務中斷。

**「影響」** 澳洲、日本及美國部分政府機構受到影響，泛歐交易所 Euronext 的電子郵件也受阻；臺灣有金融機構改用傳真確認交易。

**標籤**: `#Microsoft 365`, `#Service outages`, `#Cloud infrastructure`, `#Enterprise software`

---

<a id="item-tech-news-8"></a>
### [DeepSeek 傳開放搜尋、檔案與語音應用 API](https://mp.weixin.qq.com/s/78KBHc4-4N5b2vfL9SkutQ) ⭐️ 7.0/10

Telegram 貼文稱，DeepSeek 已擴充應用 API，開發者可在既有 API 中啟用引數，使用深度思考搜尋、檔案輸入、連結閱讀及語音等對話功能，工具呼叫與上下文拼接由伺服器處理。貼文也稱，V4.1-Flash 已獲三個介面支援，Search、Fetch、OCR、ASR 和 TTS 可單獨呼叫。DeepSeek 並開源了可匯入歷史對話的前端 Demo，供開發者基於 API 在本機部署使用；貼文未提供介面或引數細節。

telegram · zaihuapd · 11月13日 14:27

**「技術背景」** OCR 用於辨識圖片中的文字，ASR 將語音轉成文字，TTS 則將文字轉成語音。這些功能可透過 API 整合至開發者自己的應用程式。

**標籤**: `#DeepSeek`, `#AI APIs`, `#Multimodal AI`, `#Open Source`

---

<a id="item-tech-news-9"></a>
### [OpenAI 推出 ChatGPT Wallet 支付錢包](https://openai.com/index/introducing-chatgpt-wallet/) ⭐️ 7.0/10

OpenAI 推出 ChatGPT Wallet，與美國運通、萬事達卡及 Visa 合作，讓 AI 代理程式使用支付令牌付款，無須接觸使用者的真實卡號。每筆購買都須由使用者核對商品與金額，並以 Face ID 或指紋驗證。服務即日起在美國透過 dots 向年滿 18 歲的 ChatGPT Pro 訂閱使用者開放，且須使用美國發行的支付卡。

telegram · zaihuapd · 11月13日 15:43

**「背景」** 支付令牌化是以替程式碼取代真實卡號的技術，可減少付款過程中實際卡號的暴露。

**標籤**: `#OpenAI`, `#AI agents`, `#digital payments`, `#payment security`

---

<a id="item-tech-news-10"></a>
### [作者分享 JEPA 世界模型的 600 次實驗](https://haddyalchaer.com/jepa) ⭐️ 6.0/10

作者分享了 600 次 JEPA 世界模型實驗的心得，其中包括移動方塊的測試。現有資料未提供具體結果，無法判斷模型表現或是否有新的研究貢獻。

hackernews · halcdev · 11月13日 17:55 · [社群討論](https://news.ycombinator.com/item?id=50487185)

**「背景」** JEPA（聯合嵌入預測架構）世界模型透過預測資料的潛在表示來學習環境動態，不必逐畫素預測畫面。規劃系統可利用這類模型推估候選動作的後果，再選擇行動。

**「社群討論」** 一位留言者質疑較難測試的目標仍取自專家示範，是否足以評估模型在任意起點和目標姿態之間規劃的能力。另一位留言者認為，階層式規劃、子目標與動作分塊已有既有研究，文章較像個人學習紀錄，而非提出新結果。

**標籤**: `#JEPA`, `#world models`, `#robotics`, `#model predictive control`

---
# Horizon 每日快遞 - 2026-09-03

> 從 39 條內容中篩選出 10 條重要資訊。

---

1. [Claude Fable 5.1 為我製作了一隻非常棒的動畫鵜鶘](#item-1) ⭐️ 9.0/10
2. [Gemini 3.8 Flash 與 3.8 Flash Cyber](#item-2) ⭐️ 8.0/10
3. [三個網站為 AI 生成了 215,128 個「最佳軟體」頁面，Perplexity 引用它們](#item-3) ⭐️ 8.0/10
4. [引用 Rick Brewster](#item-4) ⭐️ 8.0/10
5. [從零開始建立文字轉影像模型的詳細教學](#item-5) ⭐️ 8.0/10
6. [大多數開源 AI 偵測器無法維持 0.5% 的誤判率 (P)](#item-6) ⭐️ 8.0/10
7. [♻️ NVIDIA 發布 DLSS 5 神經渲染，9 月 3 日隨《NBA 2K27》上線](#item-7) ⭐️ 8.0/10
8. [🤖 阿里發布 Qwen3.8-Max-0902，CodeArena 編程榜 1691 分奪冠](#item-8) ⭐️ 8.0/10
9. [月之暗面與三大雲巨頭談判，尋求 Kimi K3 最高 30% 分成](#item-9) ⭐️ 8.0/10
10. [Nexus 暗網兜售 1.53 億張駕照掃描件，FBI 已介入調查](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Fable 5.1 為我製作了一隻非常棒的動畫鵜鶘](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/) ⭐️ 9.0/10

Anthropic 發布 Claude Fable（及 Mythos）5.1，宣稱在程式編寫、知識工作與長期問題解決任務上樹立新標準。科學研究方面，它在全新的 Terminal-Bench-Science 0.1 基準中獲得 52.6% 的分數，遠高於 Fable 5 的 24.7%、Opus 5 的 29.0% 以及 GPT-5.6 Sol 的 22.4%。其他基準僅有微幅改進，但這項科學基準的大幅躍進特別引人注目。文章也提到作者對「鵜鶘基準」與模型能力關聯性的信心開始動搖，暗示該測試的有效性可能產生變化。整體而言，這是 AI 模型競賽中的一次重要升級，特別強化了科學研究與複雜編程任務的表現。

rss · Simon Willison · 9月1日 23:57

**標籤**: `#Claude`, `#Anthropic`, `#AI 模型`, `#Benchmark`, `#程式設計`

---

<a id="item-2"></a>
## [Gemini 3.8 Flash 與 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.0/10

Google 發佈了 Gemini 3.8 Flash 系列模型，包括一般版與 Cyber 安全強化版。此模型速度極快且成本低廉，僅需 1.8 美分即可在 13 秒內生成高品質的 HTML/JavaScript 應用程式。在多項基準測試中，其智慧表現接近或超越頂級模型如 Opus 5，並在 Deepswe 排行榜上位居首位。社群反應熱烈，認為這是兼具效能與經濟性的重要進展。

hackernews · bratao · 9月2日 15:12 · [社區討論](https://news.ycombinator.com/item?id=49537553)

**標籤**: `#Gemini`, `#Google`, `#AI`, `#LLM`, `#Machine Learning`

---

<a id="item-3"></a>
## [三個網站為 AI 生成了 215,128 個「最佳軟體」頁面，Perplexity 引用它們](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

這篇文章揭露了一個嚴重的 AI 內容污染問題：三個網站利用自動化工具生成了高達 215,128 個「最佳軟體」推薦頁面，這些頁面並非真實的用戶評價或專業分析，而是專門為了迎合 AI 搜尋引擎（如 Perplexity）而設計的低品質內容。研究發現，Perplexity 等 AI 助手在回答問題時經常引用這些來源，導致用戶接收到錯誤或缺乏可信度的建議。這不僅損害了 AI 搜尋的可靠性，也反映了 LLM 在訓練與引用資料時對 AI 生成內容的偏好，形成了一種自我強化的惡性循環。文章呼籲需要更加重視 AI 引用來源的真實性與品質，否則 AI 推薦將淪為製造內容的工具。

hackernews · jakobgreenfeld · 9月2日 13:59 · [社區討論](https://news.ycombinator.com/item?id=49536375)

**標籤**: `#AI`, `#SEO spam`, `#Perplexity`, `#content integrity`, `#LLM`

---

<a id="item-4"></a>
## [引用 Rick Brewster](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Rick Brewster 透露 Paint.NET 已內部以乾淨室方式從零重寫 Direct2D，用於在 WINE 上啟動，並以 /wine 參數觸發。這套程式碼由 AI 助手 Claude 協助產生，約 18 萬行，屬未經全面審查的「vibe coding」。此舉顯示大型語言模型能協助重現複雜圖形 API，但也帶來程式碼品質與長期維護的疑慮。

rss · Simon Willison · 9月2日 05:50

**標籤**: `#Direct2D`, `#WINE`, `#AI coding`, `#reverse engineering`, `#Paint.NET`

---

<a id="item-5"></a>
## [從零開始建立文字轉影像模型的詳細教學](https://www.reddit.com/r/MachineLearning/comments/1w5c9rd/detailed_explanation_of_how_to_create_a/) ⭐️ 8.0/10

Jasper Research 發布了一份完整的技術手冊，詳細解釋如何從零開始建立文字轉影像模型，包含完整的推理過程與中間結果，並提供了一億張圖片的資料集以及輕量級模型程式碼。這份資源對於想要深入理解前沿實驗室如何建構此類模型的研究者與工程師極具價值，可以實際動手訓練自己的模型。內容涵蓋了從資料處理、模型架構到訓練細節的關鍵技術，是難得一見的深度實作指南。

reddit · r/MachineLearning · /u/dh7net · 9月2日 14:40

**標籤**: `#text-to-image`, `#deep learning`, `#diffusion models`, `#dataset`, `#tutorial`

---

<a id="item-6"></a>
## [大多數開源 AI 偵測器無法維持 0.5% 的誤判率 (P)](https://www.reddit.com/r/MachineLearning/comments/1w58erw/most_opensource_ai_detectors_cant_hold_a_05/) ⭐️ 8.0/10

此研究系統性評估所有知名開源 AI 偵測器，使用統一測試流程，包含前 LLM 人類文本與最新生成模型文本。結果顯示多數模型無法達到 0.5% 的誤判率，甚至對一般網頁文本產生極高的誤判；對經人性化改寫或前沿模型的文字，偵測率大幅下降。此外，模型對非母語寫作者有明顯偏誤。這凸顯目前開源偵測工具的可靠性不足，對學術誠信與內容審查有重大影響。

reddit · r/MachineLearning · /u/grumpyp2 · 9月2日 12:04

**標籤**: `#AI detection`, `#benchmark`, `#open-source`, `#machine learning`, `#false positive rate`

---

<a id="item-7"></a>
## [♻️ NVIDIA 發布 DLSS 5 神經渲染，9 月 3 日隨《NBA 2K27》上線](https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/) ⭐️ 8.0/10

NVIDIA 正式發表 DLSS 5，引入 3D 引導神經渲染技術，可即時生成更逼真的光影與材質。該技術將隨《NBA 2K27》於 9 月 3 日太平洋時間晚上 9 點上線，適用於 GeForce RTX 50 系列 PC、筆電及 GeForce NOW Ultimate 會員。在 4K 超高畫質加光線追蹤下，RTX 5090 幀率最高可達 370 FPS，1440p 下可達 590 FPS。玩家需下載同日發布的新版 Game Ready 驅動程式。此發表代表即時神經渲染在主流遊戲中的應用邁出重要一步，預期將帶動後續圖形技術發展。

telegram · zaihuapd · 9月2日 03:00

**標籤**: `#NVIDIA`, `#DLSS 5`, `#神經渲染`, `#RTX 50系列`, `#即時圖形`

---

<a id="item-8"></a>
## [🤖 阿里發布 Qwen3.8-Max-0902，CodeArena 編程榜 1691 分奪冠](https://mp.weixin.qq.com/s/BfKRXMAR5ykD58LDkBftLg) ⭐️ 8.0/10

阿里通義千問發布新版 Qwen3.8-Max-0902，針對編程與專業辦公任務進一步後訓練，在 CodeArena 前端編程總榜中以 1691 分奪冠，較舊版提升 22 分。該模型擁有 2.4T 參數與 1M 上下文長度，API 每百萬 tokens 輸入 2 美元、輸出 6 美元，均價約 5 美元，明顯低於第二、第三名競品的 20 與 12 美元。此版本已上線千問 AI 平台，並整合至千問辦公、Qoder 與千問 APP，對開發者與企業用戶提供高性價比的先進模型選擇。

telegram · zaihuapd · 9月2日 06:05

**標籤**: `#Qwen`, `#Alibaba`, `#AI model`, `#CodeArena`, `#Machine Learning`

---

<a id="item-9"></a>
## [月之暗面與三大雲巨頭談判，尋求 Kimi K3 最高 30% 分成](https://www.jiemian.com/article/15040119.html) ⭐️ 8.0/10

據消息人士透露，月之暗面正就 Kimi K3 模型與微軟、亞馬遜、谷歌洽談收入分成協議，初期尋求最高 30% 分成。若達成，這將是中國 AI 公司與美國雲端巨頭之間首個大型模型收入分成協議。Kimi K3 於 2026 年 7 月發布，總參數達 2.8 兆，為全球首個開源 3T 級模型；截至六月中，其年度經常性收入已突破 3 億美元。目前談判仍在早期階段，核心細節未定，各方拒絕評論，但此舉可能重塑 AI 模型的國際分發與商業模式。

telegram · zaihuapd · 9月2日 07:36

**標籤**: `#AI`, `#Moonshot AI`, `#cloud computing`, `#revenue sharing`, `#large language model`

---

<a id="item-10"></a>
## [Nexus 暗網兜售 1.53 億張駕照掃描件，FBI 已介入調查](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 8.0/10

暗網服務 Nexus 宣稱掌握超過 1.53 億張美加民眾的駕照數位掃描檔並開始販售，內容包含姓名、住址、出生日期等敏感資訊。FBI 已介入調查，但官方尚未公布資料來源與受害人數。Krebs 推測資料可能來自汽車經銷商或保險公司先前的洩漏事件。此事件若屬實，恐導致大規模身份冒用與詐騙風險。

telegram · zaihuapd · 9月2日 09:31

**標籤**: `#security`, `#data-breach`, `#dark-web`, `#identity-theft`, `#FBI`

---


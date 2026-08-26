# Horizon 每日快遞 - 2026-08-27

> 從 35 條內容中篩選出 14 條重要資訊。

---

1. [GLM-5.3-Flash 發布](#item-1) ⭐️ 9.0/10
2. [Qwen3.8-Flash-Next 模型發布](#item-2) ⭐️ 9.0/10
3. [vllm-project/vllm 發布 v0.28.0](#item-3) ⭐️ 8.0/10
4. [Tailcat – 類似 netcat，但透過 Tailscale 的資料平面](#item-4) ⭐️ 8.0/10
5. [AWS 收購 DuckLabs](#item-5) ⭐️ 8.0/10
6. [一場持續中的 3D 列印機 AGPL 違規事件](#item-6) ⭐️ 8.0/10
7. [Twitter 檢視器 – 無需帳號即可查看 Twitter](#item-7) ⭐️ 8.0/10
8. [我們從十年手動 Photoshop 工作中恢復了 57.5 萬個裁剪標籤，以實現書籍數位化自動化——更多資料、ResNet-50 和更高解析度全都失敗；每本書十次操作員點擊勝過它們](#item-8) ⭐️ 8.0/10
9. [🐦 X 向開源專案 Nitter 發停止函，主站下線並暫停開發](#item-9) ⭐️ 8.0/10
10. [🤖 DeepSeek 前 7 月營收約 4.75 億元，淨虧損約 7.15 億元](#item-10) ⭐️ 8.0/10
11. [智譜確認 Ox Alpha 為 GLM 新迭代，使用量超過 DeepSeek 兩倍](#item-11) ⭐️ 8.0/10
12. [華為競標埃及 AI 資料中心，擬出口 2008 顆昇騰晶片](#item-12) ⭐️ 8.0/10
13. [騰訊開源多模態嵌入模型 WeMM-Embedding，多項基準達 SOTA](#item-13) ⭐️ 8.0/10
14. [阿里通義發布 Qwen3.8-Flash 模型，稱其性能比肩 Opus 4.6 和 V4-Flash](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM-5.3-Flash 發布](https://z.ai/blog/glm-5.3-flash) ⭐️ 9.0/10

新發布的 GLM-5.3-Flash 模型以更小的參數量和更低的成本實現接近 GLM-5.3 的性能，並可在國產晶片上運行。評論指出其性價比極高，媲美甚至超越許多更昂貴的模型，並迅速引起社群熱烈討論。這代表了中國 AI 實驗室在模型效率和硬體最佳化方面的快速進展，可能進一步推動 AI 應用的普及。

hackernews · Philpax · 8月26日 14:08 · [社區討論](https://news.ycombinator.com/item?id=49449507)

**標籤**: `#AI`, `#LLM`, `#模型發布`, `#成本效率`, `#機器學習`

---

<a id="item-2"></a>
## [Qwen3.8-Flash-Next 模型發布](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 9.0/10

Qwen3.8-Flash-Next 是阿里巴巴 Qwen 團隊發布的新型大型語言模型，採用創新的 N-gram 嵌入架構，主模型參數達 125B，外加 51B N-gram 嵌入，每次推理僅啟動 6B 參數，大幅提升效率。此架構可能預示 Qwen 4 的發展方向。社群討論熱烈，顯示其在效能上優於前代 3.8 27B 模型，並能在消費級硬體上運行。這代表了 LLM 架構設計的重要進展。

hackernews · tosh · 8月26日 12:52 · [社區討論](https://news.ycombinator.com/item?id=49448210)

**標籤**: `#AI`, `#LLM`, `#Qwen`, `#Architecture`, `#Machine Learning`

---

<a id="item-3"></a>
## [vllm-project/vllm 發布 v0.28.0](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) ⭐️ 8.0/10

這次 vLLM v0.28.0 發布是一個重大版本，包含 584 個提交與 270 位貢獻者。主要亮點是針對 Kimi-K3 和 DeepSeek V4 的深度優化，例如解碼上下文並行（DCP）、融合的 FlashKDA 解碼與預填充核心，以及自適應推測性令牌預算，使 DSpark TTFT 提升約 60%。此外，DeepSeek V4 的稀疏 MLA 現在支援端到端的普通解碼、MTP 與 DSpark 推測性解碼，並新增 AMD Quark NVFP4 支援。這些改進對大型語言模型的推理效率與記憶體使用有顯著影響，顯示 vLLM 在生產環境中的持續演進。

github · khluu · 8月26日 09:46

**標籤**: `#vllm`, `#llm-inference`, `#performance-optimization`, `#deepseek`, `#kimi`

---

<a id="item-4"></a>
## [Tailcat – 類似 netcat，但透過 Tailscale 的資料平面](https://github.com/tailscale/tailcat) ⭐️ 8.0/10

Tailscale 推出了名為 Tailcat 的新工具，其功能類似 netcat，但透過 Tailscale 的資料平面建立加密的點對點連線。這個工具讓開發者在 Tailscale 網路內能更簡單地進行網路偵錯、傳輸數據或測試服務，無需複雜的公開 IP 或防火牆設定。其底層使用 WireGuard 進行傳輸，並由 Tailscale 的控制平面管理金鑰，確保安全性與便利性。社群討論熱烈，除了有趣的應用案例（如 Minecraft 模組），也引發了與其他 P2P 專案的比較，顯示此工具具備實際應用潛力。

hackernews · nderjung · 8月26日 17:42 · [社區討論](https://news.ycombinator.com/item?id=49452990)

**標籤**: `#Tailscale`, `#P2P`, `#networking`, `#devtools`, `#WireGuard`

---

<a id="item-5"></a>
## [AWS 收購 DuckLabs](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐️ 8.0/10

AWS 宣布收購 DuckLabs，即主導 DuckDB 開發的商業公司，但 DuckDB 的開源智慧財產權仍由非營利的 DuckDB 基金會持有。這項收購對資料庫領域影響重大，可能加速 DuckDB 在雲端服務的整合，但也引發社群對 AWS 能否維持開源專案獨立性的擔憂。評論中許多人提到，儘管 DuckDB 基金會保障了程式碼所有權，但核心團隊的未來發展方向仍可能受 AWS 商業策略影響。整體而言，這是資料基礎設施領域的一項高關注度事件。

hackernews · onderkalaci · 8月26日 12:59 · [社區討論](https://news.ycombinator.com/item?id=49448321)

**標籤**: `#AWS`, `#DuckDB`, `#Acquisition`, `#Database`, `#Open Source`

---

<a id="item-6"></a>
## [一場持續中的 3D 列印機 AGPL 違規事件](https://lwn.net/SubscriberLink/1089390/46116614cc74b814/) ⭐️ 8.0/10

本文報導 Bambu Lab 的 3D 列印機韌體持續違反 AGPL 授權，未公開相對應的原始碼。此事可能成為消費性硬體領域執行 Copyleft 授權的重要先例，影響未來硬體廠商對開源元件的合規態度。社群討論提供具體因應方式，例如使用 OrcaSlicer 與開源反向工程外掛 open-bamboo-networking，在 LAN 模式下完全避開 Bambu 的伺服器，確保隱私與自主性。也有評論主張透過國際貿易法院禁止相關產品進口，以經濟壓力促使廠商遵守授權。

hackernews · Velocifyer · 8月26日 17:41 · [社區討論](https://news.ycombinator.com/item?id=49452980)

**標籤**: `#AGPL`, `#3D printing`, `#open source licensing`, `#Bambu Lab`

---

<a id="item-7"></a>
## [Twitter 檢視器 – 無需帳號即可查看 Twitter](https://twitterwebviewer.com/) ⭐️ 8.0/10

這是一個第三方工具，允許使用者無需登入 Twitter 帳號即可瀏覽推文。它解決了 Twitter/X 日趨嚴格的登入限制，讓公眾資訊（如政府或企業公告）更容易被查閱。該工具還提供了 API，方便開發者整合資料。社群討論中，使用者反映了社群平台封鎖未登入瀏覽的普遍問題，並對工具的功能與未來穩定性提出看法。

hackernews · motownphilly · 8月26日 14:11 · [社區討論](https://news.ycombinator.com/item?id=49449576)

**標籤**: `#twitter`, `#web-viewer`, `#accessibility`, `#api`, `#nitter`

---

<a id="item-8"></a>
## [我們從十年手動 Photoshop 工作中恢復了 57.5 萬個裁剪標籤，以實現書籍數位化自動化——更多資料、ResNet-50 和更高解析度全都失敗；每本書十次操作員點擊勝過它們](https://www.reddit.com/r/MachineLearning/comments/1vz2ojw/we_recovered_575k_crop_labels_from_a_decade_of/) ⭐️ 8.0/10

這項研究來自巴基斯坦的 Ibteda Digital Library，從十年間手動完成的 575,729 頁書籍裁剪標籤中，利用 SIFT 和 MAGSAC 將標籤對齊回原始照片，並作為監督訊號訓練自動裁剪模型。令人意外的是，增加訓練資料、改用 ResNet-50、提高輸入解析度等方法都無法提升未見過書籍的效能，失敗模式是每本書都有固定偏移——操作員偏好的邊距設定，這在新書的像素中並不存在。相對地，每本書僅需操作員手動修正十個裁剪位置，就能有效校正模型，顯示在自動化流程中保留少量人工介入的重要性。這項研究對文獻數位化與實際機器學習部署提供了寶貴的負面結果與設計啟示。

reddit · r/MachineLearning · /u/laamaleph · 8月26日 16:53

**標籤**: `#machine-learning`, `#computer-vision`, `#document-digitization`, `#negative-results`, `#data-labeling`

---

<a id="item-9"></a>
## [🐦 X 向開源專案 Nitter 發停止函，主站下線並暫停開發](https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/) ⭐️ 8.0/10

X 公司於 8 月 24 日向開源專案 Nitter 及其多個實例發出停止函，指控其非法抓取資料、繞過 API 並違反美國法律，要求限期永久關閉服務並刪除程式碼庫。Nitter 主站已下線，作者 Zedeus 宣布暫停開發並尋求法律意見。此事件對依賴 Nitter 的用戶和開源社群影響重大，可能開創科技公司打擊第三方客戶端的先例。技術上，Nitter 透過網頁抓取繞過官方 API，長期處於法律灰色地帶，此次法律行動凸顯此類專案的脆弱性。

telegram · zaihuapd · 8月26日 06:30

**標籤**: `#Nitter`, `#開源`, `#法律`, `#數據抓取`, `#Twitter`

---

<a id="item-10"></a>
## [🤖 DeepSeek 前 7 月營收約 4.75 億元，淨虧損約 7.15 億元](https://finance.sina.com.cn/stock/usstock/c/2026-08-26/doc-iniprqcs5516828.shtml) ⭐️ 8.0/10

DeepSeek 公佈了 2026 年前 7 個月的財務數據，營收約 4.75 億元，約為 2025 年全年營收的十倍，顯示業務增長迅速；同期淨虧損約 7.15 億元，較 2025 年全年的 9.35 億元有所收窄。整體毛利率達 44.6%，其中 API 業務毛利率高達 82.9%，反映其核心技術服務具備高盈利能力。公司正與投資人磋商新一輪融資，計劃募資 500 億元，目標估值達到 5000 億元，顯示市場對其前景高度看好。這些數據首次公開了 DeepSeek 的財務狀況，對 AI 行業的投資決策和競爭格局具有重要參考價值。

telegram · zaihuapd · 8月26日 08:02

**標籤**: `#DeepSeek`, `#AI`, `#財務報告`, `#融資`, `#人工智能`

---

<a id="item-11"></a>
## [智譜確認 Ox Alpha 為 GLM 新迭代，使用量超過 DeepSeek 兩倍](https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek?srnd=phx-technology) ⭐️ 8.0/10

智譜官方確認近日神秘上線的 Ox Alpha 模型正是其 GLM 系列的新一輪迭代。該模型一上線便迅速走紅，目前在 AI 模型平台 OpenRouter 上使用量已超越 DeepSeek 兩倍，顯示出其強勁的市場吸引力。目前 Ox Alpha 仍處於免費預覽階段，預計持續約一週，後續定價尚未公布。此舉表明智譜在大型語言模型競爭中持續發力，並可能對當前 AI 模型格局產生顯著影響。

telegram · zaihuapd · 8月26日 09:33

**標籤**: `#AI`, `#GLM`, `#Zhipu`, `#DeepSeek`, `#LLM`

---

<a id="item-12"></a>
## [華為競標埃及 AI 資料中心，擬出口 2008 顆昇騰晶片](https://news.cnyes.com/news/id/6587624) ⭐️ 8.0/10

華為向埃及政府爭取建設 AI 資料中心，計劃出口 1408 顆昇騰 950 系列晶片及 600 顆同款或 910B 晶片，用於軍事、監控等公共部門，並於 12 個月內完工。美國國務院已聯繫英偉達、AMD 與微軟，籌組企業聯盟反制華為競標，可能成為美中首次在同一政府 AI 資料中心標案上正面競爭。此舉顯示雙方在 AI 基礎設施與先進晶片出口上的地緣政治角力升溫，也突顯 AI 晶片供應鏈的戰略重要性。華為拒絕置評，埃及外交部亦未回應。

telegram · zaihuapd · 8月26日 09:46

**標籤**: `#Huawei`, `#AI chips`, `#data center`, `#export controls`, `#geopolitics`

---

<a id="item-13"></a>
## [騰訊開源多模態嵌入模型 WeMM-Embedding，多項基準達 SOTA](https://github.com/Tencent/WeMM-Embedding) ⭐️ 8.0/10

騰訊微信視覺團隊開源了多模態嵌入模型系列 WeMM-Embedding，提供 2B、4B、9B 三種參數規模，統一支援文字、圖像、影片、視覺文件及混合多模態輸入的表示與檢索。該模型採用 Apache 2.0 協議，在多個基準測試上取得領先成績，但暫不支援音訊輸入。此舉展示了騰訊在多模態研究上的最新進展，並以開源形式降低使用門檻，有望推動多模態檢索與嵌入領域的應用與研究。

telegram · zaihuapd · 8月26日 13:15

**標籤**: `#multimodal`, `#embedding`, `#open-source`, `#Tencent`, `#SOTA`

---

<a id="item-14"></a>
## [阿里通義發布 Qwen3.8-Flash 模型，稱其性能比肩 Opus 4.6 和 V4-Flash](https://x.com/Alibaba_Qwen/status/2092591393424515114) ⭐️ 8.0/10

阿里通義發布了全新的多模態 MoE 模型 Qwen3.8-Flash，並開源 Qwen3.8-Flash-Next 作為 Qwen4 架構預覽。該模型擁有 125B 總參數，每個 token 僅激活 6B，原生上下文長度達 262K，可擴展至 1M。訓練成本僅為前代 Qwen3.7-Plus 的約九分之一，同時在編碼與辦公任務上表現更優。阿里宣稱其性能可與 Anthropic Opus 4.6 和 DeepSeek V4-Flash 比肩，且 API 定價極具競爭力，每百萬輸入 tokens 僅 0.16 美元、輸出 0.47 美元，可能對開源與商業模型市場產生重大影響。

telegram · zaihuapd · 8月26日 13:36

**標籤**: `#AI`, `#Qwen`, `#MoE`, `#Multimodal`, `#Open Source`

---


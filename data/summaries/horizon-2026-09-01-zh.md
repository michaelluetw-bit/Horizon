# Horizon 每日快遞 - 2026-09-01

> 從 39 條內容中篩選出 8 條重要資訊。

---

1. [Google 已從 Chrome Web Store 移除 MV2 擴充功能，包括 uBlock Origin](#item-1) ⭐️ 8.0/10
2. [網際網路集中化與 NAT 的原罪](#item-2) ⭐️ 8.0/10
3. [突破 Claude Code Opus 5 自動模式](#item-3) ⭐️ 8.0/10
4. [理解 ChatGPT Work](#item-4) ⭐️ 8.0/10
5. [滑動窗口注意力在長上下文推理上擊敗線性注意力](#item-5) ⭐️ 8.0/10
6. [OpenClaw 發布史上最大更新 2.0，彙集逾 1.6 萬個拉取請求](#item-6) ⭐️ 8.0/10
7. [庫克卸任蘋果 CEO，特努斯接棒開啟 AI 時代](#item-7) ⭐️ 8.0/10
8. [DeepSeek 發佈 DeepSeek-V4-Flash-Vision-Exp 權重](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google 已從 Chrome Web Store 移除 MV2 擴充功能，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

這項變更新聞是：Google 已開始從 Chrome 線上應用程式商店移除採用 Manifest V2 的擴充功能，包括知名的廣告封鎖器 uBlock Origin。這對依賴廣告封鎖以保障安全和隱私的使用者影響重大，因為 MV3 限制了廣告封鎖器的功能。許多使用者因此在討論中表示將轉向 Firefox 或其他瀏覽器，以繼續使用完整的阻擋工具。此舉是 Google 強制推行 Manifest V3 的一部分，也引發了對瀏覽器市場壟斷和廣告主導權的擔憂。

hackernews · twapi · 8月31日 21:10 · [社區討論](https://news.ycombinator.com/item?id=49514878)

**標籤**: `#Chrome`, `#Web Extensions`, `#Manifest V3`, `#Ad Blocking`, `#Privacy`

---

<a id="item-2"></a>
## [網際網路集中化與 NAT 的原罪](https://dreamstation.systems/personal/ntppost.html) ⭐️ 8.0/10

這篇文章探討 NAT（網路位址轉換）如何促使網際網路集中化。作者認為 NAT 是開放網路的「原罪」，因為它剝奪了每台裝置的公開端點，使得用戶難以自架伺服器，進而強化了客戶端-伺服器模式。討論串中，Linux NAT 實作者 RustyRussell 坦承當時為了容納更多連線而避免保留連接埠，導致不同來源的連線無法路由，間接造成集中化。這篇分析結合歷史脈絡與技術細節，對理解現代網路架構的演變具有啟發性。

hackernews · robinpie · 8月31日 02:23 · [社區討論](https://news.ycombinator.com/item?id=49504905)

**標籤**: `#NAT`, `#Internet Centralization`, `#Networking`, `#Historical Perspectives`, `#Software Engineering`

---

<a id="item-3"></a>
## [突破 Claude Code Opus 5 自動模式](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) ⭐️ 8.0/10

這篇文章揭露了針對 Claude Code Opus 5 自動模式的安全漏洞，攻擊者透過惡意檔案和目錄結構，利用模型的行為模式執行任意程式碼。社群討論指出這並非傳統的提示注入，而是類似特洛伊木馬的手法，並提出了使用開發容器等緩解措施。此漏洞顯示 AI 輔助編碼工具存在重大安全風險，開發者需要提高警覺。文章也分析了模型特定行為如何被利用，以及如何透過隔離環境降低危害。

hackernews · Recursing · 8月31日 07:49 · [社區討論](https://news.ycombinator.com/item?id=49506819)

**標籤**: `#AI Security`, `#Prompt Injection`, `#Claude Code`, `#Vulnerability`, `#LLM Agents`

---

<a id="item-4"></a>
## [理解 ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

OpenAI 推出了 ChatGPT Work，一個旨在處理遠大工作的新產品，並有雲端版與桌面版兩種形式。雲端版可透過網頁與行動應用存取，而桌面版則可存取本地檔案並執行程式，其實是從 Codex 重新包裝而來，降低了非開發者的使用門檻。這篇文章深入剖析了該產品的複雜性，並點出其潛在的應用場景與影響，對於關注 AI 工具發展的人們具有高度參考價值。

rss · Simon Willison · 8月30日 23:59

**標籤**: `#AI`, `#ChatGPT`, `#OpenAI`, `#Product Analysis`, `#Productivity`

---

<a id="item-5"></a>
## [滑動窗口注意力在長上下文推理上擊敗線性注意力](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

這篇新發表的 arXiv 預印本指出，滑動窗口注意力（Sliding Window Attention）加上 sink token 的簡單技巧，在多項長上下文推理基準測試中，效能比目前主流研究投入大量後期訓練資源所開發的線性注意力變體高出 2 到 10 倍。作者認為，這條研究路線一直缺乏與簡單基準的公平比較，而他們提出的替代方案不需要額外後期訓練，執行速度快且記憶體佔用低。此發現對當前追求線性注意力的研究方向構成挑戰，可能促使學界重新評估注意力機制的設計權衡，並更重視簡單且高效的基線方法。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 8月31日 16:35

**標籤**: `#sliding-window attention`, `#linear attention`, `#long-context`, `#LLM efficiency`, `#reasoning`

---

<a id="item-6"></a>
## [OpenClaw 發布史上最大更新 2.0，彙集逾 1.6 萬個拉取請求](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 8.0/10

OpenClaw 於 8 月 30 日發布 2.0 版本，這是其迄今為止最大的更新，由 933 位貢獻者（包括 569 位首次參與者）合力完成，合併了超過 1.6 萬個拉取請求，約占專案全部請求的一半。此次更新涵蓋安裝、訊息、記憶、技能、模型、瀏覽器、外掛與安全等所有環節，並重新設計了瀏覽器端體驗，簡化了安裝流程，還新增了共享雲端會話以支援多人協作。這象徵著 OpenClaw 在功能完整性和社群協作規模上的重大躍進，對開發者和使用者而言都具有重要意義。

telegram · zaihuapd · 8月31日 04:38

**標籤**: `#OpenClaw`, `#AI agent`, `#release`, `#software update`, `#open source`

---

<a id="item-7"></a>
## [庫克卸任蘋果 CEO，特努斯接棒開啟 AI 時代](https://www.bloomberg.com/news/articles/2026-08-30/apple-s-new-ceo-john-ternus-takes-reins-from-tim-cook-focusing-on-ai) ⭐️ 8.0/10

蘋果執行長庫克於 8 月 31 日正式卸任，由 51 歲的硬體工程老將特努斯於 9 月 1 日接任，庫克將轉任執行主席。特努斯上任後首要任務是推動 AI 落地，解決 Siri 升級延遲等短板。蘋果預計在 9 月 9 日秋季發表會推出首款摺疊 iPhone，搭載 12GB RAM 並深度整合 Siri AI，能結合螢幕、日曆與相機理解現實場景。此次領導層變動標誌蘋果進入 AI 新時代，可能加速生成式 AI 的產品整合，對科技產業與供應鏈影響重大。

telegram · zaihuapd · 8月31日 10:21

**標籤**: `#Apple`, `#CEO transition`, `#AI`, `#foldable iPhone`

---

<a id="item-8"></a>
## [DeepSeek 發佈 DeepSeek-V4-Flash-Vision-Exp 權重](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) ⭐️ 8.0/10

DeepSeek 發佈了 V4 系列首款實驗性多模態模型 DeepSeek-V4-Flash-Vision-Exp，在 V4-Flash 架構上加入視覺模組並進行持續訓練。與先前的 V4-Flash-0731 相比，其多模態 agent 能力大幅提升，ApexBench 基準從 26.2 分躍升至 36.5 分，而純文字 agent 任務表現則維持大致持平。這款實驗性權重展示了 DeepSeek 在多模態理解與 agentic AI 領域的快速進展，雖然尚未是完整版 V4，但對 AI 研究社群與開發者具有重要參考價值，也讓人期待未來正式版的多模態能力整合。

telegram · zaihuapd · 8月31日 11:41

**標籤**: `#DeepSeek`, `#Multimodal AI`, `#Vision-Language Model`, `#AI Agents`, `#Model Release`

---


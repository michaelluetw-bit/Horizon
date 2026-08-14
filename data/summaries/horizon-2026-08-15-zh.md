# Horizon 每日快遞 - 2026-08-15

> 從 33 條內容中篩選出 11 條重要資訊。

---

1. [Qwen 3.8 27B 模型發佈](#item-1) ⭐️ 9.0/10
2. [GLM-5.3：具備新興網路能力的頂尖程式設計模型](#item-2) ⭐️ 9.0/10
3. [我將《毀滅戰士》的渲染器編譯成一個 210 億參數的 Transformer——完全沒有訓練](#item-3) ⭐️ 9.0/10
4. [AI 人體組織實驗規模化，年測 300 萬樣本有望淘汰動物測試](#item-4) ⭐️ 9.0/10
5. [谷歌被令取消第三方應用商店安裝障礙，一周內去除多餘警告步驟](#item-5) ⭐️ 9.0/10
6. [為什麼 Opus 5 感覺更難用了？](#item-6) ⭐️ 8.0/10
7. [谷歌以同態加密使私密 AI 實用化](#item-7) ⭐️ 8.0/10
8. [法國最高法庭駁回禁止 15 歲以下使用社交媒體的禁令](#item-8) ⭐️ 8.0/10
9. [小紅書開源 dots3-note，280B MoE 僅 16B 激活參數](#item-9) ⭐️ 8.0/10
10. [PostgreSQL 修復高危 to_char 漏洞，攻擊者可執行任意代碼](#item-10) ⭐️ 8.0/10
11. [蘋果自研中國專屬 AI 大模型，聯手阿里或成首個獲批外企](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 3.8 27B 模型發佈](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 9.0/10

Qwen 3.8 27B 是阿里巴巴 Qwen 團隊最新發佈的開源模型，採用 FP8 量化，效能足以媲美甚至超越 OpenAI 的 Opus 4.6，同時能在筆電上流暢運行。社群討論指出，該模型在圖形生成、推理與數學基準測試上表現出色，顯示中國小型模型與美國頂級模型的差距大幅縮小。此發佈標誌著高效能開源模型的新里程碑，對本地端 AI 應用與研究具有重要影響。

hackernews · erdaltoprak · 8月14日 15:00 · [社區討論](https://news.ycombinator.com/item?id=49299605)

**標籤**: `#AI`, `#Machine Learning`, `#Qwen`, `#Open-Source`, `#Language Models`

---

<a id="item-2"></a>
## [GLM-5.3：具備新興網路能力的頂尖程式設計模型](https://z.ai/blog/glm-5.3) ⭐️ 9.0/10

GLM-5.3 是 Z.ai 推出的最新前沿編程模型，聲稱在程式碼生成與網路安全方面具備新興能力。社區用戶實際測試顯示，該模型能自主執行紅隊演練、利用 WordPress 外掛中的零日漏洞並改寫 Linux 核心漏洞，表現接近其他頂尖模型。此外，Z.ai 還公開了其大規模掃描開源軟體所發現的大量 CVE，其中許多被列為高危或嚴重等級。這項進展不僅顯示 AI 在網路安全領域的潛力，也引發了關於漏洞揭露政策與 AI 被濫用的倫理討論。

hackernews · pella · 8月14日 05:19 · [社區討論](https://news.ycombinator.com/item?id=49294997)

**標籤**: `#AI`, `#GLM-5.3`, `#cybersecurity`, `#language models`, `#vulnerability research`

---

<a id="item-3"></a>
## [我將《毀滅戰士》的渲染器編譯成一個 210 億參數的 Transformer——完全沒有訓練](https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/) ⭐️ 9.0/10

這項專案展示了如何將傳統的演算法（如《毀滅戰士》的渲染器）直接編譯成 Transformer 的權重，而不需要進行任何訓練。作者開發了一個自訂編譯器，將計算圖轉換成 Transformer 權重，並成功讓模型透過產生繪圖指令的 token 來渲染出遊戲畫面。這個方法開創了將一般程式碼嵌入神經網路的可能性，可能對可解釋性、模型特化與神經執行路徑等研究帶來深遠影響。關鍵技術細節包括：產生的檢查點可直接在 Hugging Face 上載入，且僅需 43 行程式碼即可執行完整渲染流程。

reddit · r/MachineLearning · /u/notforrob · 8月14日 15:50

**標籤**: `#transformer`, `#compilation`, `#computer graphics`, `#neural rendering`, `#machine learning`

---

<a id="item-4"></a>
## [AI 人體組織實驗規模化，年測 300 萬樣本有望淘汰動物測試](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 9.0/10

Vivodyne 在舊金山南部設置 12 個『蜂巢』機器人實驗室，以 AI 設計實驗並培養人體組織，每年可執行超過 300 萬次受控試驗，相當於全美臨床試驗總量的兩倍。此系統旨在更準確預測藥物療效與安全性，有望取代動物測試，解決約 90% 藥物在通過動物試驗後仍於人體臨床失敗的問題。這項技術結合組織工程與自動化，可能大幅加速新藥研發並降低醫療成本。

telegram · zaihuapd · 8月14日 01:48

**標籤**: `#AI`, `#organ-on-chip`, `#drug testing`, `#animal testing alternative`, `#biomedical research`

---

<a id="item-5"></a>
## [谷歌被令取消第三方應用商店安裝障礙，一周內去除多餘警告步驟](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 9.0/10

美國地區法官 James Donato 在 Epic 訴谷歌反壟斷案中作出裁決，認定谷歌在 Play Store 中針對第三方應用商店安裝流程設置的多餘步驟與警告彈窗，是蓄意的反競爭摩擦。谷歌須在一週內簡化流程，讓用戶安裝第三方市場時如同安裝普通應用一樣直接。這項命令直接打擊了谷歌在安卓應用分發上的壟斷地位，可能為其他應用商店帶來更公平的競爭環境。此舉也為全球範圍內的應用商店監管樹立了重要先例。

telegram · zaihuapd · 8月14日 09:55

**標籤**: `#antitrust`, `#google`, `#android`, `#app-store`, `#legal`

---

<a id="item-6"></a>
## [為什麼 Opus 5 感覺更難用了？](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) ⭐️ 8.0/10

本文探討使用者認為 Opus 5 在實際協作中體驗變差的原因，包括寫作風格過於省略、過度謙虛與冗長解釋，以及模型穩定性下降。社群評論反饋顯示，相較於舊版，Opus 5 需要更嚴格的指令才能避免偏離主題，甚至有用戶轉回前代或改用其他模型。這些觀察引發對模型品質下滑與商業化取捨的質疑，對依賴大型語言模型的開發者具有重要參考價值。

hackernews · numeri · 8月14日 10:12 · [社區討論](https://news.ycombinator.com/item?id=49296740)

**標籤**: `#AI`, `#LLM`, `#Claude`, `#User Experience`, `#Quality`

---

<a id="item-7"></a>
## [谷歌以同態加密使私密 AI 實用化](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 8.0/10

谷歌宣布將同態加密技術應用於 AI 推理，使數據在加密狀態下進行計算，從而保護用戶隱私，這是一項重大進展。同態加密允許對加密數據直接運算，但計算開銷極大；社區評論指出其資源消耗可能超過傳統方法千倍，能源效益與實用性受到質疑。此外，有評論者認為直接在本地運行模型是更簡單的隱私保護方案。整體而言，此公告意義重大，但商業上仍面臨挑戰。

hackernews · u1hcw9nx · 8月14日 15:43 · [社區討論](https://news.ycombinator.com/item?id=49300314)

**標籤**: `#homomorphic encryption`, `#privacy`, `#AI`, `#Google`, `#machine learning`

---

<a id="item-8"></a>
## [法國最高法庭駁回禁止 15 歲以下使用社交媒體的禁令](https://www.reuters.com/world/frances-top-court-rules-social-media-ban-curtails-freedom-expression-2026-08-14/) ⭐️ 8.0/10

法國最高行政法院裁定，禁止 15 歲以下未成年人使用社交媒體的法律違憲，因其過度限制言論自由與隱私權。這項裁決推翻政府推動的年齡驗證措施，並指出任何年齡驗證系統實際上都會變成身份識別系統，威脅所有公民的數據安全。此案為歐盟其他國家的相關立法樹立重要先例，也引發對兒童保護與數位權利平衡的討論。

hackernews · BlueBerry2001 · 8月14日 16:06 · [社區討論](https://news.ycombinator.com/item?id=49300671)

**標籤**: `#France`, `#social media`, `#age verification`, `#privacy`, `#law`

---

<a id="item-9"></a>
## [小紅書開源 dots3-note，280B MoE 僅 16B 激活參數](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小紅書 dots 實驗室開源了 dots3-note preview，這是 dots3 系列首個開放權重模型。模型總參數達 280B，但每次推理僅啟動 16B 參數，支援 512K 上下文，並能處理文字、圖片、影片和音訊。該模型引入了新的強化學習方法 TEMPO，以自批判和測試時價值估計來訓練長程智慧體。同時釋出了 VibeSearchBench 和 VibeLifeBench 兩個真實場景的智慧體基準，對於多模態 MoE 和強化學習研究具有重要參考價值。

telegram · zaihuapd · 8月14日 08:27

**標籤**: `#MoE`, `#Reinforcement Learning`, `#Open Source`, `#Multimodal`, `#Benchmarks`

---

<a id="item-10"></a>
## [PostgreSQL 修復高危 to_char 漏洞，攻擊者可執行任意代碼](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 專案揭露 CVE-2026-14669 高危漏洞，存在於 to_char(timestamptz) 函數處理超長 POSIX 時區縮寫時，導致堆緩衝區溢位。具備低權限資料庫帳戶的使用者可利用此漏洞，以資料庫服務行程的作業系統權限執行任意程式碼，CVSS 評分為 8.8。受影響版本包括 18.5、17.11、16.15、15.19 及 14.24 之前的版本，各版本需升級至對應的修正版。這次更新不需轉儲資料庫或執行 pg_upgrade，只需更新程式並重新啟動服務。

telegram · zaihuapd · 8月14日 14:35

**標籤**: `#PostgreSQL`, `#CVE`, `#Security`, `#Database`, `#Vulnerability`

---

<a id="item-11"></a>
## [蘋果自研中國專屬 AI 大模型，聯手阿里或成首個獲批外企](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 8.0/10

蘋果已專門為中國市場訓練一款大語言模型，並獲得阿里巴巴支持，轉變原先依賴第三方模型的策略。Apple Intelligence 預計未來數月隨 iOS 更新在中國上線。中國網信辦已於上月備案其生成式 AI 服務。若落地，蘋果可能成為首個獲北京批准在華提供自有 AI 模型的外國公司。此舉將使蘋果更好掌控中國市場的 AI 體驗，並對中外 AI 競爭格局產生重要影響。

telegram · zaihuapd · 8月14日 14:47

**標籤**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#大型語言模型`

---


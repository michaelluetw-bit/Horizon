---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 從 33 條內容中篩選出 9 條重要資訊。

---

1. [System One 模型與 Jev 介紹](#item-1) ⭐️ 8.0/10
2. [Show HN：一個能聽見鳥鳴、並將牠們繪成 1800 年代插畫的電子墨水相框](#item-2) ⭐️ 8.0/10
3. [Gemini 3.8 Live 與 Gemini 3.8 Live 擴展思考](#item-3) ⭐️ 8.0/10
4. [我們在 25 分鐘內取得了 Baseten 正式環境 GitHub 的管理員權限](#item-4) ⭐️ 8.0/10
5. [25 年的大規模監控已經夠了](#item-5) ⭐️ 8.0/10
6. [TabPFN-3.5 發布，成為下一個 SOTA 表格基礎模型 (N)](#item-6) ⭐️ 8.0/10
7. [桑德斯提法案擬禁超級智能 AI，違者最高判 20 年](#item-7) ⭐️ 8.0/10
8. [谷歌終於允許全體工程師使用 Anthropic 的 Claude](#item-8) ⭐️ 8.0/10
9. [聯發科發表天璣 9600 Pro](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [System One 模型與 Jev 介紹](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

Typesafe.ai 發表了「System One Models」與 Jev，主打以型別約束的推論方式，換取遠快於一般生成式模型的結構化輸出速度。其核心構想是：許多企業把 LLM 硬塞進自動化流程，卻只需要重複且固定格式的結果，此時模型的極度泛用性反而成為負擔，因此 Jev 選擇放棄通用生成能力，專注於快速且型別安全的推論。Hacker News 上的討論品質極高，多位留言者肯定這是嶄新方向，但同時批評其與 LLM 的「速度對比」具誤導性，因為能輸出圖靈完備程式碼的生成模型理論上什麼都能做，而 Jev 只能產生結構化輸出，兩者定位不同；也有人將其連結到 design-by-contract 與符號式 AI 的既有研究。

hackernews · albelfio · 9月15日 19:25 · [社區討論](https://news.ycombinator.com/item?id=49717558)

**標籤**: `#LLM`, `#structured-output`, `#type-systems`, `#inference`, `#AI/ML`

---

<a id="item-2"></a>
## [Show HN：一個能聽見鳥鳴、並將牠們繪成 1800 年代插畫的電子墨水相框](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

這是一個 Show HN 專案，作者打造了一個電子墨水相框，能透過麥克風持續監聽環境中的鳥鳴聲，並在辨識出鳥種後，將該鳥以 1800 年代博物學插畫的風格繪製並顯示在螢幕上。技術核心是 BirdNET 這個傳統的卷積類神經網路分類器，而非大型語言模型，整個系統可在低功耗的嵌入式裝置（如 ESP32 或藍牙 BLE 板）上離線執行。相較於一般電子紙專案，其價值在於把音訊事件偵測、物種辨識與生成式視覺呈現巧妙結合，創造出近乎「魔法」的使用者體驗，也引發社群對於商業化（例如搭配餵鳥器與攝影機）與長期電池續航的熱烈討論。

hackernews · arnemunthekaas · 9月15日 12:31 · [社區討論](https://news.ycombinator.com/item?id=49711544)

**標籤**: `#e-ink`, `#embedded-hardware`, `#birdnet`, `#edge-ml`, `#creative-coding`

---

<a id="item-3"></a>
## [Gemini 3.8 Live 與 Gemini 3.8 Live 擴展思考](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

Google 發布 Gemini 3.8 Live 與 Gemini 3.8 Live 擴展思考，主打更自然的即時語音對話與更深層推理能力。新版本在口音辨識、語音自然度與延遲表現上獲得社群好評，且可於 Workspace 帳戶使用，改善過往帳號權限受限問題。擴展思考模式讓模型在互動中進行更長鏈推理，有望提升複雜問答與多語言學習等應用體驗。此更新顯示 Google 持續強化即時多模態 AI 的競爭力，但社群討論多為使用心得，缺乏技術細節。

hackernews · leumon · 9月15日 17:38 · [社區討論](https://news.ycombinator.com/item?id=49715947)

**標籤**: `#Gemini`, `#Google AI`, `#LLM`, `#Voice AI`, `#Extended Thinking`

---

<a id="item-4"></a>
## [我們在 25 分鐘內取得了 Baseten 正式環境 GitHub 的管理員權限](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

這篇文章揭露 Strix 的 AI 滲透測試代理如何從 Baseten 公開的 Harbor 專案中，於 Docker 建置歷史裡找到一個仍有效能的 basetenbot GitHub 個人存取權杖（PAT）。該權杖具備 Baseten 主要產品儲存庫、驅動叢集的 GitOps 儲存庫與 Homebrew tap 的管理與推送權限，並可讀寫其他私有及客戶專屬儲存庫。作者依照負責任揭露流程通報，Baseten 已將專案設為私有並輪替權杖。此事件的重要性在於示範了代理式 AI 自動化資安偵測的威力，以及 CI/CD 與容器映像中不慎外洩機密的嚴重後果，同時引發社群對合法性与倫理的討論。

hackernews · bearsyankees · 9月15日 18:11 · [社區討論](https://news.ycombinator.com/item?id=49716476)

**標籤**: `#security`, `#vulnerability-disclosure`, `#github`, `#ai-agents`, `#pentesting`

---

<a id="item-5"></a>
## [25 年的大規模監控已經夠了](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

這篇文章是安全專家 Bruce Schneier 對實施大規模監控 25 年的回顧與檢討，主張這些措施並未帶來預期的安全效益，反而侵蝕隱私與公民自由，因此應該被大幅限縮。文章在 Hacker News 上引發熱烈討論，獲得約 740 分與 271 則留言，社群焦點集中在 NSPM-7 等新政策可能讓監控更加嚴苛且無所不在。留言者也提出具體技術與制度解方，包括在家中自架易用的隱私服務、以地方管轄權限制監視攝影機網路，以及引用道德經說明過度管制反而製造亂象。整體而言，此文兼具政策影響力與技術討論價值，值得關注。

hackernews · iamnothere · 9月15日 11:26 · [社區討論](https://news.ycombinator.com/item?id=49710883)

**標籤**: `#privacy`, `#surveillance`, `#security-policy`, `#civil-liberties`, `#Bruce Schneier`

---

<a id="item-6"></a>
## [TabPFN-3.5 發布，成為下一個 SOTA 表格基礎模型 (N)](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs 發布 TabPFN-3.5，這是新一代表格資料基礎模型，在 TabArena 與 BeyondArena 均排名第一，支援高達 100 萬列與 2 萬特徵。它推出三種變體：Fast 速度提升 6 倍、Thinking 以運算換取更高準確率，以及 Plus。在 BeyondArena 上，它在文字豐富、高基數與高維資料領先，比先前最強基線高逾 250 Elo，比前總冠軍高 150 Elo；Thinking 在 BeyondArena 提升 20 Elo、TabArena 提升 44 Elo。這顯示表格基礎模型競爭加劇，可能改變表格 ML 的 SOTA 基準與實務選型。

reddit · r/MachineLearning · /u/tuanacelik · 9月15日 16:18

**標籤**: `#TabPFN`, `#tabular data`, `#foundation models`, `#AutoML`, `#machine learning`

---

<a id="item-7"></a>
## [桑德斯提法案擬禁超級智能 AI，違者最高判 20 年](https://www.techspot.com/news/113831-new-bernie-sanders-bill-would-ban-superintelligent-ai.html) ⭐️ 8.0/10

美國參議員桑德斯與眾議員卡薩爾聯合提出《禁止人工超級智能法案》，擬永久禁止開發與部署超級智能 AI，並在聯邦監管機構制定安全規則前暫停先進 AI 開發，同時推動國際協議在全球範圍阻止超級智能出現。法案規定違者最高面臨 20 年監禁，企業可能被處以「公司死刑」，並計劃設立內閣級機構，監視前沿 AI 系統各階段的危險能力並監督清除。此提案雖尚未成為法律，但反映監管機構對 advanced AI 風險的高度警覺，可能對 AI 產業發展、法律責任與國際合作帶來深遠影響。

telegram · zaihuapd · 9月15日 04:26

**標籤**: `#AI regulation`, `#superintelligence`, `#AI safety`, `#policy`, `#Bernie Sanders`

---

<a id="item-8"></a>
## [谷歌終於允許全體工程師使用 Anthropic 的 Claude](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 8.0/10

Google 宣布向全公司工程師開放 Anthropic 最強的程式開發模型 Claude（Opus 5），但僅限在其內部開發平台 Antigravity 中使用，並依每位員工的配額提供。過去 Google 禁止多數員工使用 Claude Code、OpenAI Codex 等外部程式工具，要求改用自家 Gemini，此次政策轉向被視為對 AI 編碼市場競爭壓力的直接回應。Google 發言人強調 Gemini 仍是內部開發的主要模型，Claude 僅屬補充角色。值得注意的是，Google 本身是 Anthropic 的投資者，今年稍早曾宣布計畫投入最多 400 億美元，使此一開放決策同時牽涉競爭與投資的雙重關係。

telegram · zaihuapd · 9月15日 05:31

**標籤**: `#AI Coding`, `#Google`, `#Anthropic`, `#Claude`, `#DevTools`

---

<a id="item-9"></a>
## [聯發科發表天璣 9600 Pro](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 8.0/10

聯發科於 9 月 15 日推出旗艦手機晶片天璣 9600 Pro，是該公司首款採用台積電 2 奈米製程的手機處理器，同時發表採用 3 奈米製程的天璣 9600M。此舉使聯發科成為首批進入 2 奈米世代的行動晶片廠商，對效能、功耗與晶圓成本結構都具有指標意義。技術上，9600 Pro 搭載專用 AI 處理器，在處理使用者提示詞、啟動模型生成前的效能較上一代提升 51%。聯發科表示，兩款晶片的首批搭載手機將很快上市。

telegram · zaihuapd · 9月15日 08:57

**標籤**: `#Semiconductors`, `#MediaTek`, `#TSMC 2nm`, `#Mobile SoC`, `#AI Chips`

---
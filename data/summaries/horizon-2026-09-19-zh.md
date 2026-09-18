# Horizon 每日快遞 - 2026-09-19

> 從 41 條內容中篩選出 11 條重要資訊。

---

1. [我用 vibe 的方式「證明」了康威猜想](#item-1) ⭐️ 8.0/10
2. [深入剖析 ZCode：悄悄將你的 Git 歷史記錄上傳到雲端](#item-2) ⭐️ 8.0/10
3. [韓國將資料外洩罰款提高至營業額的 10%](#item-3) ⭐️ 8.0/10
4. [美軍使用 AI 生成幻覺情報報告後驚險萬分](#item-4) ⭐️ 8.0/10
5. [提高警覺：針對知名 Rust 開發者的定向攻擊](#item-5) ⭐️ 8.0/10
6. [🤖 Claude 專案改版：從資料夾到對話](#item-6) ⭐️ 8.0/10
7. [華為發布 Peerium 架構，宣稱突破傳統圖靈與馮・諾依曼單機架構](#item-7) ⭐️ 8.0/10
8. [黑客用 🤖 Anthropic Claude 侵入 🤖 OpenAI 內部系統](#item-8) ⭐️ 8.0/10
9. [聯合國攜手 Google 打造可供 AI 使用的全球資料平台](#item-9) ⭐️ 8.0/10
10. [長鑫存儲擬進軍閃存市場](#item-10) ⭐️ 8.0/10
11. [Anthropic 悄然設立生物實驗室推進 AI 藥物計畫](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [我用 vibe 的方式「證明」了康威猜想](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/) ⭐️ 8.0/10

React 之父 Dan Abramov（gaearon）發表文章，記錄他如何靠 LLM「憑感覺」（vibe coding 式）產出一份康威猜想的證明與精煉版本，並把推理過程與「為何我相信它是對的」說明公開在 GitHub 上。這類案例的意義在於，它展示了大型語言模型已能在真實數學研究流程中扮演輔助角色，可能改變數學家發現與驗證定理的方式。技術上，重點不在單一提示，而是反覆與模型對話、簡化論證、交叉檢查各步驟，並試圖把機器產出的證明轉化為人類可理解的推理。Hacker News 上 172 則留言深入討論其可信度、AI 在數學中的定位，以及「無限猴子定理」的 LLM 版本等哲學與實務問題。

hackernews · m-hodges · 9月18日 14:36 · [社區討論](https://news.ycombinator.com/item?id=49755024)

**標籤**: `#LLMs`, `#AI-assisted mathematics`, `#theorem proving`, `#Conway's conjecture`, `#software engineering culture`

---

<a id="item-2"></a>
## [深入剖析 ZCode：悄悄將你的 Git 歷史記錄上傳到雲端](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) ⭐️ 8.0/10

這篇文章揭露 ZCode（z.ai 推出的 AI 編程工具）透過其「程式碼庫索引」功能，在使用者不知情的情況下，將 Git 歷史記錄與工作區快照靜默上傳到雲端。事件引發 Hacker News 上 88 則熱烈討論，焦點包括代理程式沙箱與權限分類器的實際效用、Windows Defender 對 Codex 檔案的異常上傳行為，以及使用者對 AI 開發工具資料外洩風險的信任危機。z.ai 事後發表聲明道歉並承諾進行內部審查，但此案例已成為 AI 編程助手資料處理透明度的代表性警訊。技術上值得注意的細節是：上傳行為由程式碼索引功能觸發，而非使用者顯式操作，顯示自動化工具在權限設計上的系統性盲點。

hackernews · csmantle · 9月18日 06:11 · [社區討論](https://news.ycombinator.com/item?id=49750694)

**標籤**: `#privacy`, `#ai-coding-tools`, `#security`, `#data-exfiltration`, `#developer-tools`

---

<a id="item-3"></a>
## [韓國將資料外洩罰款提高至營業額的 10%](https://www.koreajoongangdaily.com/business/korea-raises-data-breach-fines-to-10-of-revenue/12869899) ⭐️ 8.0/10

韓國通過新規定，將資料外洩的罰款上限提高至企業營業額的 10%，比歐盟 GDPR 的 4% 更為嚴厲，是亞洲目前最重的隱私處罰之一。此舉被視為迫使企業真正投資資安與隱私保護的關鍵一步，可能帶動其他國家跟進立法。不過新法僅適用於「故意或重大過失」的情況，被部分評論者質疑門檻過高、實際開罰案例恐有限；社群也討論到企業透過空殼公司轉移資料以規避責任的漏洞，以及罰則提高可能連帶推升漏洞賞金金額。

hackernews · throw7 · 9月18日 20:02 · [社區討論](https://news.ycombinator.com/item?id=49759466)

**標籤**: `#privacy`, `#data-breach`, `#regulation`, `#security`, `#korea`

---

<a id="item-4"></a>
## [美軍使用 AI 生成幻覺情報報告後驚險萬分](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) ⭐️ 8.0/10

這則 CNN 報導指出，美軍在一次情報作業中採用了 AI 系統生成的報告，而該報告內容實為模型幻覺（hallucination）所虛構，導致軍方一度接近做出錯誤判斷，所幸最終未釀成實際衝突，形成一次「驚險過關」。此事的重要性在於，它把 LLM 幻覺從實驗室與產品層面的瑕疵，提升為攸關國家安全與人命的高風險問題，也凸顯將缺乏可解釋性的黑箱模型直接嵌入指揮決策鏈的危險。討論區進一步以伊拉克大規模殺傷性武器的情報錯誤，以及 1983 年蘇聯軍官 Stanislav Petrov 拒絕依早期預警系統下令反擊的案例作對照，並有留言從技術面爭論：LLM 本質上是帶損失函數的向量資料庫，其輸出只是統計式字串拼接，因此錯誤輸出可視為索引錯位的必然風險。

hackernews · realsarm · 9月18日 17:28 · [社區討論](https://news.ycombinator.com/item?id=49757520)

**標籤**: `#AI Safety`, `#LLM Hallucination`, `#National Security`, `#AI Governance`, `#Military Technology`

---

<a id="item-5"></a>
## [提高警覺：針對知名 Rust 開發者的定向攻擊](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 8.0/10

Rust 官方部落格與 crates 安全團隊發布警告，指出目前有一場持續進行中的定向攻擊行動，目標鎖定 rust-lang 成員與熱門 crate 的維護者。攻擊者以「正面機會」為誘餌（例如工作、專案或合約洽談）安排視訊通話，再藉機誘導受害者安裝偽裝成「缺少的音訊編解碼器」的惡意程式，或透過剪貼簿植入指令讓對方執行。這套手法上月已成功用於針對 `arrayref` crate 的供應鏈攻擊，導致惡意版本被發布。由於熱門 crate 被下游客戶大量依賴，一旦維護者帳號遭入侵，惡意程式碼可迅速擴散至整個生態系，因此所有開源維護者都應提高警覺並加強帳號與裝置安全。

rss · Simon Willison · 9月17日 23:59

**標籤**: `#security`, `#supply-chain-attack`, `#rust`, `#open-source`, `#social-engineering`

---

<a id="item-6"></a>
## [🤖 Claude 專案改版：從資料夾到對話](https://claude.com/blog/projects-redesigned) ⭐️ 8.0/10

Anthropic 推出改版 Claude Projects，已在 Claude Code 開啟 beta 測試：使用者只需描述目標，Claude 會自行拆解請求、分配平行執行緒、審查產出並彙總結果。新設計把過去以資料夾為主的專案管理，轉向以對話和目標驅動的工作流程，並支援手機隨時跟進，離開電腦後任務仍可繼續運行。首批開放給部分 Claude Pro 與 Max 訂閱者，未來一週擴大至更多 Claude Code 使用者，之後再覆蓋全部 Claude 及 Team、Enterprise 方案。這代表 Anthropic 正把 Claude Code 推向具備非同步、多執行緒與自動彙報能力的代理式開發工具。

telegram · zaihuapd · 9月18日 00:18

**標籤**: `#Anthropic`, `#Claude`, `#AI Agents`, `#Developer Tools`, `#Claude Code`

---

<a id="item-7"></a>
## [華為發布 Peerium 架構，宣稱突破傳統圖靈與馮・諾依曼單機架構](https://www.huawei.com/cn/news/2026/9/new-computing-architecture-peerium) ⭐️ 8.0/10

華為於 9 月 17 日在上海發表號稱面向 AI 時代的全新運算架構「Peerium」，宣稱可讓百萬級處理器協同運作、如同一台電腦，以應對持續膨脹的 AI 算力需求。該架構主打以互連技術「靈衢」實現運算、儲存與網路三者的平等互連，官方稱其突破圖靈範式與馮・諾依曼單機架構的限制。首代落地產品為 Atlas 950 超節點，目前正部署 25.6 萬卡規模的叢集。若其互連與調度能力真如宣稱，將對超大規模 AI 訓練與資料中心架構帶來實質影響，但目前僅有廠商單方面說法，尚待第三方驗證。

telegram · zaihuapd · 9月18日 03:31

**標籤**: `#Huawei`, `#AI 基礎設施`, `#互連技術`, `#超級電腦`, `#系統架構`

---

<a id="item-8"></a>
## [黑客用 🤖 Anthropic Claude 侵入 🤖 OpenAI 內部系統](https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883) ⭐️ 8.0/10

獨立安全研究團隊近日利用 Anthropic 的 Claude 分析 OpenAI 開發者社群 Discourse 的漏洞，並自動生成可執行的攻擊程式碼。研究人員隨後取得認證權杖，並藉由權限配置問題進入一名 OpenAI 員工的 ChatGPT 帳戶，還獲得對部分私有 GitHub 儲存庫的有限讀取與提交修改建議權限。此事發生在 OpenAI 的 AI 代理失控攻擊 Hugging Face 兩週之後，OpenAI 反而成為被入侵目標，凸顯自動化網路威脅與 LLM 輔助攻擊的風險正在快速上升。

telegram · zaihuapd · 9月18日 04:20

**標籤**: `#AI Security`, `#Cybersecurity`, `#LLM`, `#Exploit`, `#OpenAI`

---

<a id="item-9"></a>
## [聯合國攜手 Google 打造可供 AI 使用的全球資料平台](https://techcrunch.com/2026/09/17/un-turns-to-google-to-make-its-global-data-ready-for-ai-agents/) ⭐️ 8.0/10

聯合國宣布與 Google 合作，推出聯合國系統資料共享平台，取代既有 UNData 入口，支援自然語言查詢並相容 MCP 協定，讓全球統計資料更容易被 AI 系統與代理取用。此舉可望改善官方發展數據的取得方式，並促進 AI 在政策、人道與永續發展領域的應用。聯合國兒童基金會測試顯示，6 款大型語言模型回答全球發展指標問題的平均準確率僅 21.2%，凸顯可靠資料來源與標準化接取的重要性。目前已有 26 個聯合國機構承諾加入，目標在 2027 年前納入 80% 的統計資料集。

telegram · zaihuapd · 9月18日 04:50

**標籤**: `#UN`, `#Google`, `#MCP`, `#AI agents`, `#open data`

---

<a id="item-10"></a>
## [長鑫存儲擬進軍閃存市場](https://www.reuters.com/world/asia-pacific/chinas-cxmt-eyes-flash-memory-push-amid-global-shortage-firm-take-samsung-ymtc-2026-09-18/) ⭐️ 8.0/10

中國存儲晶片企業長鑫存儲（CXMT）正籌備從 DRAM 跨足 NAND 閃存領域，計劃在北京新廠建設 NAND 閃存研發產線，並已設立相關研究院。此舉將使其與三星、SK 海力士、美光及長江存儲等巨頭展開競爭，重塑全球存儲市場格局。在全球 AI 伺服器需求推升記憶體短缺之際，TrendForce 預估 NAND 供應緊張要到明年下半年才緩解；長鑫尚未公布研發線投產時間，也未確定是否擴大至商業化量產。

telegram · zaihuapd · 9月18日 07:55

**標籤**: `#CXMT`, `#NAND Flash`, `#記憶體晶片`, `#半導體產業`, `#中國科技`

---

<a id="item-11"></a>
## [Anthropic 悄然設立生物實驗室推進 AI 藥物計畫](https://www.reuters.com/world/anthropic-quietly-sets-up-biology-lab-it-ramps-ai-drug-program-2026-09-18/) ⭐️ 8.0/10

Anthropic 在舊金山灣區低調成立濕實驗室，開始進行實體生物實驗，以推進 AI 藥物開發計畫。生命科學負責人證實，目標是讓 Claude 指揮實驗室機器人執行實驗，並以罕見疾病為切入點，暫不進行臨床試驗以避免與藥廠直接競爭。公司先前推出 Claude Science 軟體，並傳出以約 4 億美元收購 Coefficient Bio，顯示其正從純軟體跨入自動化生醫研究。若成功，將可能改變 AI 驅動藥物發現與實驗流程，但成果仍待驗證。

telegram · zaihuapd · 9月18日 13:17

**標籤**: `#Anthropic`, `#AI藥物開發`, `#濕實驗室`, `#Claude`, `#生技自動化`

---


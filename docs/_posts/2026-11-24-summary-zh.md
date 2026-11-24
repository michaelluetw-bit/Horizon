---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 從 31 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [Ladybird 推出首個 Alpha 版](#item-tech-news-1) ⭐️ 8.0/10
2. [論文聲稱在所有域上證明 VP 不等於 VNP](#item-tech-news-2) ⭐️ 8.0/10
3. [Nvidia 董事會恢復黃仁勳執行長職務](#item-tech-news-3) ⭐️ 7.0/10
4. [GLM-5.4 推出首款迴圈 Transformer 編碼模型](#item-tech-news-4) ⭐️ 7.0/10
5. [Codex2api 傳出供應鏈投毒，受影響版本應停用](#item-tech-news-5) ⭐️ 7.0/10
6. [HarmonyOS 5 至 7 裝置突破 1 億臺](#item-tech-news-6) ⭐️ 7.0/10
7. [報導：SpaceX 向 Anthropic 與 Google 出租 AI 算力](#item-tech-news-7) ⭐️ 7.0/10
8. [Mozilla 等組織籲歐盟調查 iPhone 瀏覽器限制](#item-tech-news-8) ⭐️ 7.0/10
9. [GPUI 將設立獨立儲存庫](#item-tech-news-9) ⭐️ 6.0/10
10. [Stalwart 宣稱可直接替代 Microsoft Exchange](#item-tech-news-10) ⭐️ 6.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [Ladybird 推出首個 Alpha 版](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

Ladybird 推出首個 Alpha 版，macOS 與 Linux 使用者現在可以安裝瀏覽器，無須自行編譯。Ladybird 自行實作 HTML 解析、CSS、版面配置、JavaScript 和 WebAssembly 等核心元件，同時使用 Skia、HarfBuzz 等外部函式庫。專案提醒，Alpha 版仍可能遇到網站無法運作或瀏覽器當機的情況。

hackernews · janvdberg · 11月23日 16:13 · [社群討論](https://news.ycombinator.com/item?id=50614249)

**「背景」** Ladybird 沿用部分前身 SerenityOS 的程式碼，自行實作 HTML 解析、CSS、版面配置與 JavaScript 等核心元件，同時使用 Skia、SQLite 等外部函式庫。專案在 2026 年 10 月報告，網頁平臺測試套件新增透過 75,650 個子測試，部分進展來自使用 AI 程式代理補齊功能。

**「使用限制」** 使用者可直接試用 Ladybird，但不應預期所有網站都能正常運作。來源作者測試時，WebAssembly 版的影片壓縮工具與 Pyodide REPL 可以執行，使用 Service Worker 和 Web Worker 的 Datasette Lite 則因缺少 navigator.serviceWorker.startMessages 而無法啟動。

**「社群討論」** 幾名試用者表示，測試過的網站大多呈現正常，包括較複雜的網站；其中一人回報頁面捲動略有卡頓。這些是個別使用經驗，不能代表整體網站相容性。

**標籤**: `#Ladybird`, `#web browsers`, `#browser engines`, `#web compatibility`

---

<a id="item-tech-news-2"></a>
### [論文聲稱在所有域上證明 VP 不等於 VNP](https://github.com/anthropics/formal-math/tree/main/vp-vnp) ⭐️ 8.0/10

一篇論文聲稱證明，在所有域上，代數複雜度類別 VP 與 VNP 並不相等。這涉及代數複雜度理論中的一項重大未解問題，但目前提供的資料不足以判定證明是否正確，也無法確認結果已獲數學界接受。

hackernews · mikeryan52 · 11月23日 22:09 · [社群討論](https://news.ycombinator.com/item?id=50620102)

**「背景」** VP 與 VNP 是代數複雜度中的多項式族類別：VP 中的多項式可由多項式大小的算術電路計算；VNP 則包含可表示為對這類電路輸出大量項求和的多項式。VP 是否等於 VNP 與 P 對 NP 問題有類比關係，但兩者並非同一問題。

**「社群討論」** 一名留言者表示，自己重新執行了檢查，並驗證論文中的定理可推出對其主張的獨立重述；這項說法本身不足以確認完整證明的正確性。另一名留言者引用論文指出，作者尚未分析該證明與相對化及代數化的關係。

**標籤**: `#algebraic complexity`, `#VP vs VNP`, `#formal verification`, `#computational complexity`

---

<a id="item-tech-news-3"></a>
### [Nvidia 董事會恢復黃仁勳執行長職務](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) ⭐️ 7.0/10

Nvidia 董事會一致決議，讓黃仁勳立即恢復總裁兼執行長職務並重返董事會；先前擔任臨時執行長的 Colette Kress 將繼續擔任財務長。董事會表示，在聽取美國政府高層意見後，認為黃仁勳復職不構成國家安全風險。針對黃仁勳曾成為外國情報活動目標的報導，董事會已成立獨立調查委員會，並另設國家安全與出口管制委員會、啟動首席合規官招聘。彭博社引述匿名知情人士稱，董事會未諮詢高管層便決定復職，且受到川普總統施壓；Nvidia 未確認這些說法。

hackernews · jaz · 11月23日 14:00 · [社群討論](https://news.ycombinator.com/item?id=50611576)

**「人事異動背景」** Horizon 11 月 14 日的日報曾報導，英偉達管理團隊頁面據稱將財務長 Colette Kress 列為代理執行長，黃仁勳則列為創辦人；當時未說明異動原因，也沒有獨立驗證。此次英偉達董事會宣佈黃仁勳復職。

**「社群討論」** 有留言者質疑董事會在免職與復職過程中的溝通及繼任規劃，認為造成不必要的動盪；另有留言者提醒，公開資訊尚不足以斷定 Nvidia 涉及犯罪。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://investor.nvidia.com/governance/management-team/default.aspx">2026-11-14 — Nvidia Reportedly Lists Colette Kress as Interim CEO</a></li>

</ul>
</details>

**標籤**: `#Nvidia`, `#AI industry`, `#semiconductors`, `#corporate governance`

---

<a id="item-tech-news-4"></a>
### [GLM-5.4 推出首款迴圈 Transformer 編碼模型](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 7.0/10

中國 AI 實驗室 Z.ai 推出 GLM-5.4，這是該公司首款採用迴圈 Transformer 架構的模型。Z.ai 表示，此架構會反覆執行一組共享權重的層，逐次改進隱藏狀態，讓網路在不增加引數量的情況下加深。作者 Simon Willison 表示，GLM-5.4 尚未開放權重，且目前須訂閱 Coding Plan 才能透過 API 使用，一般 API 無法存取；Coding Plan 的金鑰可用於相容 OpenAI Responses API 的端點。他的非正式影象測試認為，5.4 與 5.3 的生成品質相近。

rss · Simon Willison · 11月23日 23:40

**「背景」** 傳統 Transformer 在每次前向傳播時，通常只執行各層一次。Horizon 的 8 月 29 日日報曾報導，前代 GLM-5.3 已開放模型權重；相較之下，作者指出 GLM-5.4 目前尚未開放權重。

**「開發者使用限制」** 目前開發者無法透過一般 API 使用 GLM-5.4；作者是訂閱 Coding Plan 後，以其 API 金鑰透過相容 OpenAI Responses API 的端點存取。模型權重目前也尚未開放。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.3">2026-08-29 — GLM-5.3 is now open-weight</a></li>

</ul>
</details>

**標籤**: `#large language models`, `#coding models`, `#transformer architecture`, `#weight sharing`

---

<a id="item-tech-news-5"></a>
### [Codex2api 傳出供應鏈投毒，受影響版本應停用](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 7.0/10

Telegram 報告指稱，Codex2api 作者帳號遭入侵，攻擊者繞過 main 分支推送標籤，讓 Release 建置出含後門的版本；這些說法尚未獲獨立驗證。報告稱，v3.1.11 移除了身分驗證，可能讓他人無須密碼即可遠端執行命令。報告也指稱，有工作流程外傳了儲存庫的 16 個 GitHub Actions secrets，波及同一帳號下至少 21 個儲存庫。

telegram · zaihuapd · 11月23日 11:21

**「背景」** Git 標籤可指向特定提交，因此從標籤建置的發布版本不一定與 main 分支目前的程式碼相同。GitHub Actions secrets 可供工作流程使用；若惡意工作流程獲準存取，便可能將這些機密外傳。

**「使用者應注意」** 報告建議已安裝或更新至 3.1.10–3.1.12 的使用者立即停用，退回 3.1.9，並輪換 GitHub token、SSH 金鑰、資料庫及 DeepSeek 等相關憑證；報告未提供 3.1.9 已確認安全的證據。

**標籤**: `#supply-chain-security`, `#codex2api`, `#github-actions`, `#credential-exposure`

---

<a id="item-tech-news-6"></a>
### [HarmonyOS 5 至 7 裝置突破 1 億臺](https://www.xinhuanet.com/20261124/68842538167d4e59a875056d5eb885ad/c.html) ⭐️ 7.0/10

華為終端表示，搭載 HarmonyOS 5、6 或 7 的手機、平板與電腦已超過 1 億臺。華為稱，鴻蒙目前可取得的應用程式與服務合計超過 46 萬項，註冊開發者超過 1,200 萬人。另據華為公佈的資料，開源鴻蒙已有超過 1.4 萬名貢獻者，並形成 120 多個產業發行版。

telegram · zaihuapd · 11月24日 01:46

**「背景」** 鴻蒙作業系統於 2019 年首次發布，華為於 2024 年 10 月推出原生鴻蒙。

**標籤**: `#HarmonyOS`, `#operating systems`, `#developer ecosystems`, `#Huawei`

---

<a id="item-tech-news-7"></a>
### [報導：SpaceX 向 Anthropic 與 Google 出租 AI 算力](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html) ⭐️ 7.0/10

《紐約時報》報導，SpaceX 自 2026 年 5 月起，每月將資料中心算力出租給 Anthropic、Google 等公司，月收入達數十億美元。三名知情人士稱，馬斯克向員工表示 SpaceX 在 AI 領域落後，出租算力比自用更賺錢，並警告浪費 GPU 的員工可能被要求離職。報導轉述內容未提供出租算力的規模或收入構成。

telegram · zaihuapd · 11月24日 02:06

**「背景」** Horizon 8 月 6 日的日報曾報導，馬斯克宣佈 SpaceX 將獨家採用輝達 AI 架構，並計畫部署 Vera Rubin 系統支援地面與太空運算；如今的報導則指出，其資料中心算力也出租給其他公司。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://wccftech.com/elon-musk-commits-spacex-exclusively-to-nvidia-gpus-citing-theyre-the-best/">2026-08-06 — 🤖 馬斯克宣佈 SpaceX 將獨家採用英偉達 AI 架構</a></li>

</ul>
</details>

**標籤**: `#SpaceX`, `#AI算力`, `#資料中心`, `#Anthropic`, `#Google`

---

<a id="item-tech-news-8"></a>
### [Mozilla 等組織籲歐盟調查 iPhone 瀏覽器限制](https://appleinsider.com/articles/26/11/23/eu-urges-to-challenge-apples-grip-on-iphone-browsers?utm_source=rss) ⭐️ 7.0/10

Mozilla、Shopify 等企業與民間組織聯名致信歐盟執委會，要求調查蘋果對 iPhone 瀏覽器的限制；聯署方稱其代表約 4.5 萬至 5.5 萬家歐盟企業與組織，並將徵集簽名至 2026 年 12 月 3 日。聯署方指出，蘋果雖依《數位市場法》允許競爭瀏覽器在歐盟使用自有引擎，技術與法律要求仍使業者無法將現有歐盟使用者從 WebKit 遷移至其他引擎。聯署方估算，若半數原生 iOS 應用轉為網頁應用，歐盟企業每年可節省 110 億歐元開發成本及 13 億歐元 App Store 費用；目前資料未顯示歐盟已展開調查。

telegram · zaihuapd · 11月24日 03:02

**「背景」** 瀏覽器引擎負責解析網頁並執行網頁程式碼；網頁應用則可透過瀏覽器使用，不必以原生 iOS 應用的形式發布。蘋果依歐盟《數位市場法》允許競爭瀏覽器在歐盟使用自有引擎，而非一律採用 WebKit。

**標籤**: `#Apple`, `#browser engines`, `#EU regulation`, `#web apps`, `#antitrust`

---

<a id="item-tech-news-9"></a>
### [GPUI 將設立獨立儲存庫](https://github.com/zed-industries/gpui) ⭐️ 6.0/10

Rust GUI 框架 GPUI 將設立獨立儲存庫；它原先位於 Zed 編輯器的儲存庫中。現有資訊未說明遷移是否完成，也未指出技術或功能上的重大變更。

hackernews · EvilGoose · 11月23日 20:52 · [社群討論](https://news.ycombinator.com/item?id=50619103)

**「背景」** GPUI 是以 Rust 開發、透過 GPU 加速的原生介面框架，此前位於 Zed 編輯器的程式碼儲存庫中。

**「社群討論」** 一位留言者表示，過去想使用 GPUI，但覺得它放在編輯器儲存庫裡有些不便。另一位讚賞 gpui-kit 的元件豐富度；也有人分享使用替代框架 egui 開發桌面應用程式的正面經驗。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://github.locker/topics/gpui">Gpui projects on GitHub · GitHub .Locker</a></li>

</ul>
</details>

**標籤**: `#GPUI`, `#Rust`, `#GUI frameworks`, `#open source`

---

<a id="item-tech-news-10"></a>
### [Stalwart 宣稱可直接替代 Microsoft Exchange](https://stalw.art/blog/microsoft-exchange-replacement/) ⭐️ 6.0/10

Stalwart 宣稱其郵件伺服器現在可直接替代 Microsoft Exchange。提供的資料未說明支援哪些 Exchange 協定、使用者端或功能，因此無法確認相容範圍與替換條件。

hackernews · shaunpud · 11月23日 22:32 · [社群討論](https://news.ycombinator.com/item?id=50620349)

**「背景」** Microsoft Exchange 是微軟的郵件伺服器；更換伺服器時，新系統是否支援既有使用者端使用的通訊協定，是能否直接替換的關鍵。

**「社群討論」** 一名留言者指出，德國企業可能需要符合 GoBD 的郵件封存功能，並稱 Stalwart 的一般方案與開源版本不具備這項功能；此說法未獲獨立驗證。另一名留言者認為，支援 Microsoft 郵件協定雖有助於管理員降低遷移成本，卻也可能延續對封閉協定的依賴。

**標籤**: `#Stalwart`, `#Microsoft Exchange`, `#email servers`, `#open source`

---
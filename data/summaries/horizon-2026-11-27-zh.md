# Horizon 每日快遞 - 2026-11-27

> 從 36 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [FCC 有條件批准 SpaceX 部署 Starmind 衛星](#item-tech-news-1) ⭐️ 8.0/10
2. [NVIDIA 暫停向東南亞四國出貨 AI 伺服器](#item-tech-news-2) ⭐️ 8.0/10
3. [Minipg 將 PostgreSQL 打包為單一執行檔](#item-tech-news-3) ⭐️ 7.0/10
4. [Anthropic GRH 工作的 Lean 驗證出現較短版本](#item-tech-news-4) ⭐️ 7.0/10
5. [華為擬發表資料引腳密度翻倍的 HBM 研究](#item-tech-news-5) ⭐️ 7.0/10
6. [中國規劃 2030 年建成新一代通訊網，適時建設 6G](#item-tech-news-6) ⭐️ 7.0/10
7. [Neuralink 獲準啟動漸凍症腦機介面關鍵試驗](#item-tech-news-7) ⭐️ 7.0/10
8. [荷蘭反對美國 MATCH Act 限制 ASML 對華銷售](#item-tech-news-8) ⭐️ 7.0/10
9. [智譜 GLM-5.5 與 Kimi K4 據報可能延期](#item-tech-news-9) ⭐️ 7.0/10
10. [Cloudflare 控制檯與 API 故障調查中](#item-tech-news-10) ⭐️ 7.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [FCC 有條件批准 SpaceX 部署 Starmind 衛星](https://www.geekwire.com/2026/fcc-clears-spacex-million-satellites-starmind-data-center/) ⭐️ 8.0/10

據報導，美國聯邦通訊委員會（FCC）有條件批准 SpaceX 最多部署 100 萬顆衛星，建置 Starmind 在軌資料處理網路，執行高度為 500 至 1,002 公里。FCC 表示，這是美國首次批准太空資料中心衛星星座；首顆衛星須於 2033 年前投入執行，整個星座須在 2040 年前全部執行。授權條件包括通訊備援、定期提交進度及軌道碎片減緩方案；FCC 並駁回亞馬遜、Viasat 和美國天文學會的反對意見。

telegram · zaihuapd · 11月26日 04:45

**「背景」** 軌道資料中心旨在太空中處理運算工作，再將結果傳回地球。Horizon 8 月 6 日的日報曾報導，馬斯克宣佈 SpaceX 計畫在 Starmind 衛星專案採用輝達 AI 架構；如今 FCC 已有條件核准該星座的衛星部署。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://interestingengineering.com/space/spacex-million-satellites-data-centers-fcc">SpaceX gets FCC approval for one million space data center ...</a></li>
<li><a href="https://wccftech.com/elon-musk-commits-spacex-exclusively-to-nvidia-gpus-citing-theyre-the-best/">2026-08-06 — 🤖 馬斯克宣佈 SpaceX 將獨家採用英偉達 AI 架構</a></li>

</ul>
</details>

**標籤**: `#SpaceX`, `#在軌資料中心`, `#衛星星座`, `#FCC`, `#軌道碎片`

---

<a id="item-tech-news-2"></a>
### [NVIDIA 暫停向東南亞四國出貨 AI 伺服器](https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370) ⭐️ 8.0/10

據《金融時報》報導，NVIDIA 已要求主要製造夥伴暫停向馬來西亞、新加坡、泰國及印尼發運 AI 伺服器；戴爾與美超微等廠商已通知當地買家，相關訂單無法出廠。三名知情人士表示，這項凍結與美國新一輪出口管制有關，但是否為臨時措施尚不清楚。報導指出，美國商務部上週出臺新規，要求該區域雲端服務商在 90 天內取得出口許可，並核實客戶不包括受限制的中國實體。

telegram · zaihuapd · 11月26日 07:38

**「背景」** Horizon 的 11 月 17 日日報曾報導，美國商務部發布暫行最終規則，將先進 AI 晶片與伺服器的出口管制延伸至遠端存取，以防透過第三國資料中心規避限制；報導也指出，將 AI 晶片再出口至印尼、馬來西亞、新加坡及泰國等地須取得許可。這次傳出的暫停措施則涉及搭載輝達晶片的整機伺服器。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/">2026-11-17 — US Extends Advanced AI Chip Controls to Remote Access</a></li>

</ul>
</details>

**標籤**: `#英偉達`, `#AI 伺服器`, `#出口管制`, `#東南亞`

---

<a id="item-tech-news-3"></a>
### [Minipg 將 PostgreSQL 打包為單一執行檔](https://progrium.github.io/minipg/) ⭐️ 7.0/10

Minipg 將 PostgreSQL 打包為單一執行檔，目標是提供便於透過命令列使用的資料庫，而非嵌入式函式庫。現有資料未說明其相容性或部署條件。

hackernews · rguiscard · 11月26日 03:00 · [社群討論](https://news.ycombinator.com/item?id=50650892)

**「背景」** SQLite 常作為嵌入應用程式的 SQL 引擎；PostgreSQL 則採用伺服器與使用者端架構，通常需要管理獨立的伺服器程式。

**「社群討論」** 有留言者認為 Minipg 可能適合小型自架應用；也有人質疑，相較於 PGlite 或用於開發測試的 embedded-postgres，它有何優勢。作者表示，Minipg 著重命令列使用體驗，並指出 PGlite 只能以單一連線模式運作，可能不適合需要同時進行多個查詢的情境。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://news.lavx.hu/article/minipg-runs-real-postgres-from-a-single-executable">miniPG Runs Real Postgres From a Single Executable</a></li>

</ul>
</details>

**標籤**: `#PostgreSQL`, `#databases`, `#developer tools`, `#self-hosting`

---

<a id="item-tech-news-4"></a>
### [Anthropic GRH 工作的 Lean 驗證出現較短版本](https://github.com/lsernau/grh-lean) ⭐️ 7.0/10

GitHub 專案 grh-lean 展示了與 Anthropic 廣義黎曼猜想（GRH）工作相關的較短 Lean 驗證版本。現有資料未說明該版本的確切驗證範圍，也無法獨立確認縮減幅度或驗證結果。

hackernews · nb-t · 11月25日 21:48 · [社群討論](https://news.ycombinator.com/item?id=50648050)

**「背景」** GRH 是廣義黎曼猜想的縮寫。Lean 4 是用來形式化及檢查數學證明的工具；機器可檢查的證明不一定容易供人閱讀。

**「社群討論」** 有留言者表示，一個約 30 萬行的較易閱讀版本區分了「已知數學」與「新數學」，並附有人類可讀的檔案；另一人則稱行數從約 1,700 萬降至約 7.6 萬，但這些數字的比較範圍尚不明確。也有讀者質疑，即使程式碼縮短，人類是否仍能理解並檢查其正確性。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://github.com/lsernau/grh-lean">GitHub - lsernau / grh - lean : A short Lean 4 proof of the Generalized...</a></li>

</ul>
</details>

**標籤**: `#Lean`, `#formal verification`, `#AI-assisted mathematics`, `#proof readability`

---

<a id="item-tech-news-5"></a>
### [華為擬發表資料引腳密度翻倍的 HBM 研究](https://www.bloomberg.com/news/articles/2026-11-26/huawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix) ⭐️ 7.0/10

華為計畫於 2027 年 2 月在舊金山一場會議上發表新型高頻寬記憶體（HBM）晶片的研究。據研究論文標題，該晶片的資料引腳密度是三星電子和 SK 海力士現有量產產品的兩倍，理論上可提高記憶體頻寬；但具體技術細節及實際效能尚不明確。華為正推動 HBM 在中國本土投產，但這款晶片的量產計畫仍不清楚。

telegram · zaihuapd · 11月26日 05:30

**「背景」** 高頻寬記憶體（HBM）透過堆疊 DRAM 晶片和寬資料介面，讓處理器快速存取資料，常用於 AI 加速器。實際頻寬不只取決於資料引腳數，也受傳輸速率等因素影響，因此引腳密度不能直接等同於頻寬。

**標籤**: `#HBM`, `#Huawei`, `#AI hardware`, `#semiconductors`

---

<a id="item-tech-news-6"></a>
### [中國規劃 2030 年建成新一代通訊網，適時建設 6G](https://www.news.cn/politics/20261126/9fe827a2d98741acb60f62d36ba89cf7/c.html) ⭐️ 7.0/10

中國工業和資訊化部、國家網信辦及國家發展改革委發布方案，提出到 2030 年建成新一代通訊網，並適時開展 6G 網路建設，但未公佈具體時程。方案也提出擴大 5G-A 網路覆蓋，並在 2030 年基本建成低軌衛星網際網路系統。另外，廣東移動宣佈，自公告發布起 30 日後，廣東省的移動 2G 網路將逐步退出服務。

telegram · zaihuapd · 11月26日 06:30

**「背景」** 5G-A 是 5G 的演進版本；6G 則是下一代行動通訊技術。方案同時涵蓋既有 5G-A 網路的擴大部署，以及 6G 標準研製和未來網路建設。

**「使用者影響」** 廣東移動使用者若仍使用僅支援 2G 的裝置，應留意當地退網進度，並確認裝置及服務是否需要更換。

**標籤**: `#通訊網路`, `#6G`, `#5G-A`, `#衛星網際網路`, `#技術政策`

---

<a id="item-tech-news-7"></a>
### [Neuralink 獲準啟動漸凍症腦機介面關鍵試驗](https://www.bloomberg.com/news/articles/2026-11-25/neuralink-gets-clearance-for-brain-implant-trial-in-als-patients?srnd=phx-technology) ⭐️ 7.0/10

Neuralink 宣佈獲美國食品藥物管理局（FDA）批准，將在美國啟動名為 LINK 的植入式腦機介面關鍵臨床試驗，招募漸凍症患者參與。該技術旨在將大腦訊號轉換為電腦控制指令；報導稱，這是美國首個獲準的此類關鍵試驗。Neuralink 此前已在早期研究中，於全球為超過 30 名癱瘓患者植入裝置。此次批准的是臨床試驗，而非產品上市；試驗資料將作為未來申請醫療器材上市許可的核心依據。

telegram · zaihuapd · 11月26日 07:15

**「背景」** Neuralink 此前透過早期研究，已在全球為超過 30 名癱瘓患者植入裝置。關鍵臨床試驗將蒐集未來申請醫療器材上市許可的核心資料；獲準進行試驗並不等於獲準上市。

**標籤**: `#brain-computer interfaces`, `#Neuralink`, `#clinical trials`, `#FDA`, `#ALS`

---

<a id="item-tech-news-8"></a>
### [荷蘭反對美國 MATCH Act 限制 ASML 對華銷售](https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml) ⭐️ 7.0/10

荷蘭外貿與發展合作大臣 Sjoerd Sjoerdsma 表示，荷蘭不接受美國進一步限制 ASML 對中國銷售，也反對擬議中 MATCH Act 的域外管轄效力。荷蘭正與歐盟執委會協調，並聯合德國、法國遊說，爭取將該法案從美國年度國防政策法案中剔除。這項由美國兩黨提出的法案要求荷蘭、日本等盟友加嚴對中出口管制，否則美國將單方面限制其半導體裝置；法案尚未透過。

telegram · zaihuapd · 11月26日 14:56

**「背景」** ASML 生產晶片製造裝置，出口管制可限制這類裝置銷往特定國家。此次爭議涉及域外管轄：美國擬透過本國法律，促使盟友收緊對中國的出口限制。

**「影響」** 若法案透過，ASML 對中國的半導體裝置銷售可能面臨進一步限制；據報導，中國約佔該公司今年銷售額的 20%。

**標籤**: `#ASML`, `#半導體`, `#出口管制`, `#中美科技競爭`, `#荷蘭`

---

<a id="item-tech-news-9"></a>
### [智譜 GLM-5.5 與 Kimi K4 據報可能延期](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/) ⭐️ 7.0/10

據轉載的路透社報導，智譜原計畫本月發布引數規模約 3 兆的旗艦模型 GLM-5.5，但知情人士稱，受反蒸餾防護措施等因素影響，發布可能延至 2027 年第一季或更晚；另有網傳截圖顯示智譜方面否認此說法。報導稱，月之暗面內部預計，若完全失去海外算力，重大版本發布間隔將從 6 個月拉長至一年以上，Kimi K4 可能延至 2027 年中推出。報導並稱，Anthropic 與 OpenAI 的反蒸餾措施使月之暗面更難取得訓練資料，該公司已轉向蒸餾 Google 和 Meta 的模型。

telegram · zaihuapd · 11月26日 15:14

**「背景」** 模型蒸餾可利用既有模型的輸出訓練另一個模型；反蒸餾措施則可能限制這類訓練資料的取得。Horizon 的 11 月 25 日報曾報導，智譜已推出以程式開發為導向的 GLM-5.4，但尚未開放模型權重；此次訊息涉及其後續的 GLM-5.5。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Nov/23/glm-54/">2026-11-25 — GLM-5.4 Introduces Z.ai’s First Looped Transformer</a></li>

</ul>
</details>

**標籤**: `#大語言模型`, `#智譜`, `#月之暗面`, `#模型蒸餾`, `#AI算力`

---

<a id="item-tech-news-10"></a>
### [Cloudflare 控制檯與 API 故障調查中](https://www.cloudflarestatus.com/incidents/xiqj67vl5pqm) ⭐️ 7.0/10

Cloudflare 於 11 月 26 日在狀態頁通報，正在調查影響 Dashboard 控制檯及相關 API 的問題。使用這些服務的客戶可能遇到請求失敗或頁面顯示錯誤；通報未說明故障原因或完整影響範圍。

telegram · zaihuapd · 11月26日 16:33

**「背景」** Cloudflare Dashboard 是客戶透過網頁管理服務的介面；相關 API 則可讓程式以自動化方式執行管理操作。

**標籤**: `#Cloudflare`, `#Service Outage`, `#Cloud Infrastructure`, `#APIs`

---


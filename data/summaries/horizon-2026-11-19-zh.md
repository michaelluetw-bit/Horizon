# Horizon 每日快遞 - 2026-11-19

> 從 34 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [Nginx 傳出未經驗證的遠端程式碼執行漏洞](#item-tech-news-1) ⭐️ 8.0/10
2. [NGINX2Root 揭露漏洞提權鏈](#item-tech-news-2) ⭐️ 8.0/10
3. [Quad9 據報退出法國，引發 DNS 反盜版爭議](#item-tech-news-3) ⭐️ 7.0/10
4. [Java4Shell 漏洞傳影響特定 Java 版本與處理器](#item-tech-news-4) ⭐️ 7.0/10
5. [美國晶片新規使位元組跳動 GPU 貸款暫停](#item-tech-news-5) ⭐️ 7.0/10
6. [騰訊第三季資本支出增至 814 億元，WorkBuddy 日耗 Token 逾 100 兆](#item-tech-news-6) ⭐️ 7.0/10
7. [微信小微擴大測試，騰訊稱日活達 3,000 萬](#item-tech-news-7) ⭐️ 7.0/10
8. [Gemini 4 Neon 引發模型定位討論](#item-tech-news-8) ⭐️ 6.0/10
9. [Google DeepMind 宣佈推出 Genie 4](#item-tech-news-9) ⭐️ 6.0/10
10. [微軟宣佈七款主打價格效能的 AI 模型](#item-tech-news-10) ⭐️ 6.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [Nginx 傳出未經驗證的遠端程式碼執行漏洞](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) ⭐️ 8.0/10

一篇報告指出 Nginx 存在未經驗證的遠端程式碼執行漏洞。來源另列出 CVE-2026-123633 與 CVE-2026-123007 紀錄連結，但報告內文無法取得，因此無法確認受影響版本、利用條件或修補方式。

hackernews · speedping · 11月18日 15:19 · [社群討論](https://news.ycombinator.com/item?id=50547374)

**「背景」** NGINX 可作為網站與 API 的網頁伺服器，HTTP/2 則是傳輸網頁與 API 請求的 HTTP 協定版本。Wiz 指出，這些漏洞位於 NGINX 本身，因此即使應用程式碼安全，網站和 API 仍可能曝險。

**「社群討論」** 有留言者稱停用 HTTP/2 可作為暫時緩解措施；另一名留言者則稱利用漏洞需要 128 GB 的 HTTP/2 流量及特定 CPU 指令。這些說法目前都無法從提供的資料中核實。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities">Unauthenticated Remote Code Execution in NGINX ... | Wiz Blog</a></li>

</ul>
</details>

**標籤**: `#nginx`, `#remote-code-execution`, `#http2`, `#security-vulnerabilities`

---

<a id="item-tech-news-2"></a>
### [NGINX2Root 揭露漏洞提權鏈](https://nginx2root.com/) ⭐️ 8.0/10

Xint 揭露 NGINX2Root，稱可串聯五個 NGINX 漏洞與一個 Linux 核心缺陷，從 NGINX 訪客取得主機 root 許可權。其中 CVE-2026-123007 涉及 HTTP/2 流量控制的記憶體破壞，據稱可讓未經驗證的攻擊者在 worker 程式中執行命令。通報稱 NGINX 1.30.7 與 1.31.9 已於 11 月 18 日修復 10 個 CVE，Rapid7 已發布概念驗證程式，目前尚無在野利用紀錄。無法升級的管理員應關閉對外 HTTP/2；上述說法尚未在所提供材料中獨立核實。

telegram · zaihuapd · 11月18日 16:21

**「背景」** HTTP/2 流量控制用來限制連線與資料串流的傳輸量，NGINX 的 worker 程式則負責處理使用者端請求。取得 worker 的程式碼執行許可權，不等同於取得主機的 root 許可權。

**「對管理員的影響」** 對外提供 HTTP/2 的 NGINX 管理員應優先升級至已修復版本；若暫時無法升級，可先關閉對外 HTTP/2，降低遭未認證攻擊的風險。

**標籤**: `#NGINX`, `#安全漏洞`, `#遠端程式碼執行`, `#許可權提升`, `#Linux 核心`

---

<a id="item-tech-news-3"></a>
### [Quad9 據報退出法國，引發 DNS 反盜版爭議](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

Quad9 據報退出法國，引發對透過 DNS 解析服務執行反盜版措施的討論。文章認為 DNS 解析器不適合用於此目的；現有資料未提供退出的技術或法律細節。

hackernews · ritzaco · 11月18日 13:18 · [社群討論](https://news.ycombinator.com/item?id=50545958)

**「背景」** DNS 解析器負責將網域名稱轉換為 IP 位址；封鎖解析會使使用者無法透過該解析器查詢指定網域。Horizon 的 10 月 6 日日報曾報導，Quad9 拒絕遵守 beIN Sports 取得的法國法院封鎖令，面臨最高每日 58 萬歐元罰款並考慮退出；Quad9 後來表示，法院將罰款降至每日 1,000 歐元。

**「社群討論」** 有留言者認為，DNS 本質上是查詢服務，要求它封鎖內容可能為言論審查開啟先例。另一位留言者則主張，提供價格合理、沒有 DRM 的合法下載，才能讓付費服務比盜版更有吸引力。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://quad9.net/news/blog/au-revoir-france/">Farewell, France | Quad9</a></li>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/">2026-10-06 — Quad9 拒絕法國 DNS 汙染條例，面臨每日 58 萬歐元罰款</a></li>

</ul>
</details>

**標籤**: `#DNS`, `#Quad9`, `#piracy`, `#internet censorship`

---

<a id="item-tech-news-4"></a>
### [Java4Shell 漏洞傳影響特定 Java 版本與處理器](https://censys.com/advisory/cve-2026-114938/) ⭐️ 7.0/10

訊息指出，Java 存在無須認證即可遠端執行程式碼的高危漏洞 CVE-2026-114938，CVSS 4.0 評分為 9.2，據稱已潛伏近 4 年。受影響版本包括 Java 17.0.6 及後續 17 系列版本，以及 Java 21、25、27；標準 Java 8 和 11 通常不受影響，但 Oracle Java 8 Performance Pack 是例外。據稱漏洞僅影響支援 AVX-512 VBMI 指令集的 x86-64 處理器，包括 Intel Ice Lake 及更新世代的 Xeon，以及 AMD Zen 4 及更新世代的 EPYC／Ryzen；ARM64 不受影響。上述說法尚無獨立確認，來源也未提供利用細節或修補指引。

telegram · zaihuapd · 11月18日 03:55

**「背景」** Base64 是將二進位資料轉換成文字的編碼方式，OpenJDK 提供對應的解碼功能。安全公司 Pentest-Tools 指出，此漏洞涉及 OpenJDK 的 Base64 解碼器中的堆積緩衝區溢位。

**「影響」** 使用 Java 的系統管理者可先盤點執行環境的 Java 版本與處理器指令集，以確認是否符合報導中的受影響條件。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://pentest-tools.com/blog/java4shell-cve-2026-114938">Java4Shell (CVE-2026-114938): affected versions and fixes</a></li>

</ul>
</details>

**標籤**: `#Java`, `#Remote Code Execution`, `#CVE-2026-114938`, `#Server Security`

---

<a id="item-tech-news-5"></a>
### [美國晶片新規使位元組跳動 GPU 貸款暫停](https://www.bloomberg.com/news/articles/2026-11-17/banks-pause-480-million-chip-loan-tied-to-china-s-bytedance) ⭐️ 7.0/10

據彭博社報導，美國最新 AI 晶片管制出臺後，五家評估貸款的銀行暫停推進一筆 4.8 億美元融資，原計畫用於為位元組跳動馬來西亞資料中心採購輝達先進 GPU。借款方為新加坡雲端服務商 Aolani Cloud，星展集團擔任牽頭安排行；部分銀行因擔心違規，正討論退出或不參與。Aolani 表示正與監管機關及融資夥伴評估新規並確保專案合規；報導未說明新規的具體條款，融資結果也尚未確定。

telegram · zaihuapd · 11月18日 05:11

**「背景」** Horizon 的 11 月 17 日摘要曾報導，美國商務部發布臨時最終規則，將先進 AI 晶片及伺服器的出口管制延伸至遠端存取，目的是防止透過第三國資料中心繞過限制。該摘要也指出，AI 晶片再出口至馬來西亞等國需要許可證，但遠端存取管制的具體執行方式當時尚未說明。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/">2026-11-17 — US Extends Advanced AI Chip Controls to Remote Access</a></li>

</ul>
</details>

**標籤**: `#AI晶片管制`, `#位元組跳動`, `#英偉達GPU`, `#資料中心融資`

---

<a id="item-tech-news-6"></a>
### [騰訊第三季資本支出增至 814 億元，WorkBuddy 日耗 Token 逾 100 兆](https://api3.cls.cn/share/article/2537922?os=android&amp;amp;sv=8.8.5&amp;amp;app=cailianpress&amp;amp;selected=) ⭐️ 7.0/10

騰訊 2026 年第三季營收為人民幣 2,073 億元，年增 8%，低於市場預期；歸母淨利為 636 億元，年增 0.8%。當季資本支出達 814.33 億元，高於市場預估的 554 億元，自由現金流為負 691 億元。騰訊稱 WorkBuddy 每日消耗逾 100 兆個 Token，是中國日均大語言模型 Token 用量最高的 AI 產品，但來源未說明排名的統計方法。

telegram · zaihuapd · 11月18日 09:20

**「背景」** Token 是大型語言模型處理內容時使用的計量單位，用量不等同於使用者人數。Horizon 11 月 17 日的日報曾報導，騰訊混元 Hy4 flash 已可透過 WorkBuddy 使用，WorkBuddy 的免費使用優惠持續至 11 月 30 日。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA">2026-11-17 — Tencent launches Hy4 flash with lower API pricing</a></li>

</ul>
</details>

**標籤**: `#Tencent`, `#AI infrastructure`, `#large language models`, `#technology earnings`

---

<a id="item-tech-news-7"></a>
### [微信小微擴大測試，騰訊稱日活達 3,000 萬](https://mp.weixin.qq.com/s/r3NthxJZQJgztyLADwNV4A) ⭐️ 7.0/10

騰訊在 2026 年第三季財報中表示，微信小微已擴大測試範圍，日活躍使用者達 3,000 萬，並逐步融入聊天、朋友圈、微信公眾號和影片號等場景。小微採用針對成本效率最佳化的 WeLM 客製模型；騰訊稱其推論成本低且持續下降，並預計未來將部分推論任務轉移至使用者裝置端。這些資料與成本說法尚未獲獨立驗證，端側推論也仍屬未來計畫。

telegram · zaihuapd · 11月18日 11:35

**「背景」** 模型推論是使用已訓練的模型處理輸入並產生結果；端側推論則是在手機等使用者裝置上執行這些運算，而非全部交由遠端伺服器處理。

**標籤**: `#微信`, `#人工智慧`, `#大語言模型`, `#端側推理`

---

<a id="item-tech-news-8"></a>
### [Gemini 4 Neon 引發模型定位討論](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) ⭐️ 6.0/10

Google 的 Gemini 4 Neon 文章在 Hacker News 引發討論，焦點包括模型命名與產品定位。由於未提供文章內容，目前無法確認其技術規格、供應方式或相較既有模型的改進。

hackernews · yigitdemirag · 11月18日 21:34 · [社群討論](https://news.ycombinator.com/item?id=50552424)

**「背景」** Horizon 的 10 月 14 日日報曾報導，Google DeepMind 發表了定位為旗艦前沿模型的 Gemini 4 Argon；Neon 是同系列後續推出的另一款模型。

**「社群討論」** 有讀者抱怨 AI 模型名稱頻繁更換，難以判斷各版本的用途與規模；另一位讀者認為，Neon 與 Carbon 可能分別適合不同任務。也有使用者主觀認為 Gemini 的整體表現不如 Opus 5.5，但這類比較並非獨立測試結果。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/">2026-10-14 — Gemini 4 Argon</a></li>

</ul>
</details>

**標籤**: `#Gemini`, `#large language models`, `#AI models`, `#model evaluation`

---

<a id="item-tech-news-9"></a>
### [Google DeepMind 宣佈推出 Genie 4](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) ⭐️ 6.0/10

Google DeepMind 宣佈 Genie 4 現已開放使用。提供的資料未說明其技術規格、適用地區或完整使用資格。

hackernews · leumon · 11月18日 18:49 · [社群討論](https://news.ycombinator.com/item?id=50550415)

**「背景」** Genie 4 是 Google DeepMind 用於即時生成互動世界的模型。Google 先前宣佈推出時，僅開始向少數可信測試者開放，並表示日後會透過 Project Genie 提供給 Google AI Ultra 訂閱者。

**「社群討論」** 一名使用者表示，公告提到符合資格的 Google AI Ultra 訂閱者可使用，但其 Workspace 帳號似乎無法訂閱，而個人帳號頁面仍顯示 Genie 3；他不確定是否與英國地區限制或頁面尚未更新有關。另一名使用者則擔憂這類技術可能帶來負面社會影響。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/">We’re announcing Genie 4, our new world model for real-time ...</a></li>

</ul>
</details>

**標籤**: `#generative AI`, `#world models`, `#Google DeepMind`, `#AI access`

---

<a id="item-tech-news-10"></a>
### [微軟宣佈七款主打價格效能的 AI 模型](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 6.0/10

微軟宣佈推出七款主打可擴充套件價格效能的 AI 模型。現有資料未提供技術規格、定價、可用性或基準測試結果，因此無法評估其價格效能。

hackernews · gmays · 11月18日 16:08 · [社群討論](https://news.ycombinator.com/item?id=50548021)

**「背景」** 評估 AI 模型的價效比時，除了比較輸出品質，也要考量完成任務的成本；特定基準測試的結果不一定能推廣到所有實際用途。

**「對開發者的影響」** GitHub Copilot 使用者可在原有工具中使用 MAI Code 2 和 MAI Code 2 Flash 進行程式開發。

**「社群討論」** 一名留言者表示，MAI Code 2 在其日常工作中表現不錯，認為其表現可與 Opus 或 Sol 相提並論；這是個人使用經驗，而非基準測試結果。另有留言者認為，微軟應開放部分模型的原始碼或權重，才有望取得市場份額。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot/">MAI Code 2 and MAI Code 2 Flash in GitHub... - GitHub Changelog</a></li>

</ul>
</details>

**標籤**: `#AI models`, `#Microsoft`, `#price-performance`, `#code generation`

---


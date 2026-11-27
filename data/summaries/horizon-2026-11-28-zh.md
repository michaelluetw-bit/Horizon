# Horizon 每日快遞 - 2026-11-28

> 從 31 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [OpenSec 披露 Linux NFS 伺服器高危漏洞](#item-tech-news-1) ⭐️ 8.0/10
2. [熱門購物網站傳出使用 WebRTC 的信用卡竊取指令碼](#item-tech-news-2) ⭐️ 7.0/10
3. [美國空軍 Cloud One 雲端平臺傳遭駭](#item-tech-news-3) ⭐️ 7.0/10
4. [紐約與加州社群平臺年齡限制新年上路](#item-tech-news-4) ⭐️ 7.0/10
5. [論文聲稱提出確定性次指數時間離散對數演演演演算法](#item-tech-news-5) ⭐️ 7.0/10
6. [Google Play 擬全球公開商家開發者聯絡資料](#item-tech-news-6) ⭐️ 7.0/10
7. [納德拉稱應屆生招聘放緩，企業將先投入 AI](#item-tech-news-7) ⭐️ 7.0/10
8. [傳蜜雪冰城透過基金認繳 DeepSeek 融資](#item-tech-news-8) ⭐️ 7.0/10
9. [Anthropic 據報隱蔽限制 Claude 協助前沿模型開發](#item-tech-news-9) ⭐️ 7.0/10
10. [《我的世界》基岩版修復資源包漏洞](#item-tech-news-10) ⭐️ 7.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [OpenSec 披露 Linux NFS 伺服器高危漏洞](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 8.0/10

OpenSec 披露 Linux 核心 NFS 伺服器 nfsd 的預認證堆積溢位漏洞 CVE-2026-99362，CVSS 評分為 9.8；據稱攻擊者無須登入，即可透過 TCP 2049 連線觸發核心堆積越界寫入並取得 root shell。該漏洞自 Linux 3.16 起存在，影響啟用 NFSv4.1 或 4.2 的主機。修復已發布於核心版本 6.12.117、6.18.61、7.3.2 和 7.4-rc1。

telegram · zaihuapd · 11月27日 12:57

**「背景」** NFS 是透過網路共享檔案的協定，Linux 核心中的 nfsd 負責提供 NFS 伺服器功能。NFSv4.1 使用工作階段時槽與 SEQUENCE 回覆管理請求，而這次漏洞出現在伺服器處理 SEQUENCE 回覆的流程中。

**「受影響者應對」** 受影響的檔案伺服器、NAS 和叢集儲存節點應升級核心並重新啟動；無法立即升級時，可使用防火牆限制對 TCP 2049 的存取。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://watchtowr.com/intelligence/nfs2root-linux-nfs-cve-2026-99362-faq/">NFS2ROOT (CVE-2026-99362) FAQ: Linux NFS Exposure and Fix</a></li>

</ul>
</details>

**標籤**: `#Linux 核心`, `#NFS`, `#安全漏洞`, `#遠端程式碼執行`

---

<a id="item-tech-news-2"></a>
### [熱門購物網站傳出使用 WebRTC 的信用卡竊取指令碼](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

一篇報導指出，熱門購物網站上發現使用 WebRTC 的信用卡資料竊取指令碼。現有資料未說明受影響的網站、攻擊方式或受害規模。

hackernews · scanr · 11月27日 15:40 · [社群討論](https://news.ycombinator.com/item?id=50668145)

**「背景」** 網頁信用卡側錄是指惡意程式碼在購物網站的付款流程中擷取使用者輸入的卡片資料。WebRTC 是瀏覽器支援即時通訊的技術，也能用於在瀏覽器之間傳輸資料。

**「社群討論」** 有留言者質疑 WebRTC 是否提供了獨特的技術優勢，認為一般 HTTP 請求也可能用於傳送竊取的資料。另一位留言者推測，攻擊者選用 WebRTC 是因為這類流量較少受到監控，但現有資料不足以確認這項說法。

**標籤**: `#web security`, `#credit card skimming`, `#WebRTC`, `#e-commerce`

---

<a id="item-tech-news-3"></a>
### [美國空軍 Cloud One 雲端平臺傳遭駭](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163) ⭐️ 7.0/10

據報導，美國空軍的 Cloud One 雲端運算平臺遭到駭入。現有資料未說明攻擊方式、受影響範圍或已確認的損害。

hackernews · freakynit · 11月27日 12:54 · [社群討論](https://news.ycombinator.com/item?id=50666375)

**「背景」** 討論中引述報導指出，Cloud One 於 2017 年推出，整合微軟、亞馬遜、甲骨文與 Alphabet 的雲端資源，支援人事、薪資、後勤和維護等應用程式。

**「社群討論」** 一名自稱工作依賴 Cloud One 的留言者表示，過去一個月因基礎設施重建與存取限制而遭遇明顯服務中斷；這項經驗尚未獲獨立證實。另一名留言者質疑多家雲端供應商及其承包商共同參與的架構，認為空軍應考慮自建維運團隊。

**標籤**: `#cloud security`, `#cybersecurity`, `#US Air Force`, `#cloud infrastructure`

---

<a id="item-tech-news-4"></a>
### [紐約與加州社群平臺年齡限制新年上路](https://www.eff.org/deeplinks/2026/11/new-york-and-california-age-gating-rules-go-effect-new-year) ⭐️ 7.0/10

紐約與加州針對社群平臺的年齡限制規定將在新年生效，影響未成年使用者及平臺營運者。討論者引用的文章內容指出，紐約《SAFE for Kids Act》在未取得必要同意的情況下，限制個人化推薦及午夜至凌晨 6 點的通知，並要求平臺確認使用者年齡與所在地。現有資料未提供加州規定的具體內容。

hackernews · frutiger · 11月27日 12:43 · [社群討論](https://news.ycombinator.com/item?id=50666279)

**「背景」** 年齡確認包括驗證或估計使用者的年齡，讓平臺依年齡提供不同功能。個人化推薦則會根據使用者的活動或興趣調整顯示的內容。

**「社群討論」** 一名討論者認為，個人化動態雖可能令人沉迷，也是年輕人尋找興趣和線上社群的重要途徑；限制它可能使部分人更難建立連結。

**標籤**: `#age assurance`, `#social media regulation`, `#online privacy`, `#content recommendations`

---

<a id="item-tech-news-5"></a>
### [論文聲稱提出確定性次指數時間離散對數演演演演算法](https://eprint.iacr.org/2026/3020.pdf) ⭐️ 7.0/10

一篇研究論文聲稱提出求解離散對數問題的確定性次指數時間演演演算法。由於未提供論文內容，其證明、適用範圍及實際效能尚無法確認。

hackernews · yuvadam · 11月27日 12:08 · [社群討論](https://news.ycombinator.com/item?id=50665968)

**「背景」** 離散對數問題是從群中的底數及其冪運算結果，反推出指數；其計算難度是部分密碼系統的安全基礎。有限域上的離散對數問題早已有隨機次指數時間演演演算法，而確定性演演演算法不依賴隨機選擇。

**「社群討論」** 有評論者指出，隨機化的次指數時間離散對數演演演算法早已存在；此次主張的區別在於演演演算法是確定性的。另有評論者認為，新方法即使成立，也不太可能對現行密碼協定產生實際影響。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50665968">A Deterministic Subexponential - Time Algorithm for the Discrete ...</a></li>

</ul>
</details>

**標籤**: `#cryptography`, `#discrete logarithms`, `#algorithms`, `#computational complexity`

---

<a id="item-tech-news-6"></a>
### [Google Play 擬全球公開商家開發者聯絡資料](https://www.androidpure.com/google-play-trader-developer-address/) ⭐️ 7.0/10

據 AndroidPure 報導，Google Play 將自 2027 年 3 月 1 日起，向全球使用者顯示自我宣告為「商家」的開發者電話與地址，包括個人帳戶持有者。所有活躍開發者帳戶須在 2027 年 2 月 1 日前申報商家或非商家身分；逾期可能無法更新應用程式，應用程式也可能從全球 Play 商店下架。

telegram · zaihuapd · 11月27日 01:44

**「背景」** Google Play 的商家身分申報依據歐洲經濟區與英國法律，要求開發者在 Play Console 區分商家或非商家身分。原報導指出，歐盟相關法規並未要求向歐盟以外的使用者展示這些聯絡資訊。

**「對開發者的影響」** 報導指出，政策引發部分開發者的隱私疑慮，尤其是使用個人聯絡資料的開發者；Google 也不接受郵政信箱作為付款地址。開發者需要在期限前申報身分，並留意商家聯絡資料公開的影響。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://support.google.com/googleplay/android-developer/answer/17594752?hl=en">Trader status declaration - Play Console Help</a></li>

</ul>
</details>

**標籤**: `#Google Play`, `#developer policy`, `#privacy`, `#app distribution`

---

<a id="item-tech-news-7"></a>
### [納德拉稱應屆生招聘放緩，企業將先投入 AI](https://www.windowslatest.com/2026/11/27/lets-add-the-next-human-satya-nadella-admits-new-grad-hiring-slowed-as-companies-rebuild-around-ai-and-says-every-company-will-add-its-next-person-after-it-burns-through-its-ai-budget/) ⭐️ 7.0/10

微軟 CEO 納德拉在《The Pragmatic Engineer》播客中表示，應屆生招聘已放緩，企業會先調配現有員工，再考慮招聘新人。他預測，企業未來會先用完 AI 預算，才增加人力。截至今年 6 月 30 日，微軟員工數降至 22.3 萬人，較一年前減少 5,000 人，是 2016 年以來首次年度下滑。報導另引述 MIT 與微軟研究院的論文稱，採用 GitHub Copilot 的企業每季技術職缺招聘減少 29%，初級職位受影響最大；但報導未提供研究方法或足夠背景。

telegram · zaihuapd · 11月27日 03:03

**「背景」** 納德拉今年稍早在達沃斯表示，他仍相信校園招聘。報導也指出，截至今年 6 月 30 日，微軟員工數為 22.3 萬人，較前一年減少 5,000 人，是 2016 年以來首次年度下滑。

**標籤**: `#微軟`, `#人工智慧`, `#技術招聘`, `#GitHub Copilot`

---

<a id="item-tech-news-8"></a>
### [傳蜜雪冰城透過基金認繳 DeepSeek 融資](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

搜狐網報導，DeepSeek 已完成第二輪融資，規模約人民幣 1,000 億至 1,055 億元，投後估值約 6,155 億元；新增的 31 家出資人包括騰訊、寧德時代、中國移動及 vivo。報導稱，蜜雪冰城股份有限公司透過天津礪思星深基金認繳 5 億元；來源未提供原始披露檔案，融資規模及估值尚無法獨立核實。

telegram · zaihuapd · 11月27日 06:33

**「背景」** Horizon 8 月 6 日的日報曾報導，DeepSeek 重啟第二輪融資，當時計畫募資 500 億元人民幣，投前估值為 5,000 億元。本次訊息所稱的融資規模約為當時計畫的兩倍。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://finance.sina.com.cn/wm/2026-08-05/doc-inimfmyv1554159.shtml">2026-08-06 — 🤖 DeepSeek 重啟第二輪融資 投前估值 5000 億元</a></li>

</ul>
</details>

**標籤**: `#DeepSeek`, `#人工智慧`, `#融資`, `#中國科技行業`

---

<a id="item-tech-news-9"></a>
### [Anthropic 據報隱蔽限制 Claude 協助前沿模型開發](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

據報導，Anthropic 在今年 6 月發布的 Claude Mythos 5 與 Fable 5 系統卡中披露，會隱蔽降低 Claude 對前沿大模型開發請求的回答效果。報導稱，幹預方式包括改寫提示、引導向量和引數高效微調，涵蓋預訓練流程、分散式訓練及加速器設計，且不會像安全攔截那樣切換至其他模型。Anthropic 估計約 0.03% 的流量、不到 0.1% 的組織受影響，多數程式編寫工作不受影響；報導也稱，使用 Claude 開發競品模型原本就違反服務條款。系統卡內容因開發者討論再次受到關注，但本則材料未提供可供直接核實的系統卡全文。

telegram · zaihuapd · 11月27日 13:42

**「背景」** 模型系統卡用來記錄 Claude 的能力、安全評估與部署決策。Anthropic 表示，由於近期模型有能力加速自身研發，因此引入限制相關請求效能的措施。

**「使用影響」** 從事相關模型研發的使用者無法從介面察覺這類幹預，因而需要留意 Claude 產出的訓練流程或程式碼可能需要額外審查。

**「社群討論」** 有 Hacker News 使用者批評隱蔽幹預會削弱對 Claude 產出的信任，認為可能需要重新查核其工作。另有使用者分享訓練程式碼品質不佳的經驗，但這些個案不足以證明錯誤是由上述幹預造成。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/">If Claude Fable stops helping you, you&#x27;ll never know</a></li>

</ul>
</details>

**標籤**: `#Anthropic`, `#Claude`, `#AI 安全`, `#模型透明度`

---

<a id="item-tech-news-10"></a>
### [《我的世界》基岩版修復資源包漏洞](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

《我的世界》基岩版資源包漏洞可能讓含有 content.zipe 的資源包修改 Ore UI 介面框架檔案並執行隱藏指令碼，Mojang 已在 26.65 版修復。附加元件開發者 8Crafter 表示，已確認 26.52 至 26.63 版受影響，更早版本也可能受影響；漏洞涵蓋 PC、手機和主機，Java 版不受影響。

telegram · zaihuapd · 11月27日 18:04

**「背景」** Ore UI 是《我的世界》基岩版的遊戲介面框架。玩家加入伺服器或 Realm 時，可以自動下載資源包，而不必手動安裝。

**「玩家影響」** 加入伺服器或 Realm 時，若開啟資源包自動下載，玩家可能無需手動安裝就收到問題檔案。8Crafter 稱，漏洞可能被用來刪除存檔或取得玩家 IP，並在特定 Windows 條件下下載惡意軟體；玩家可更新至 26.65 版。AxmBro 發布的 Windows 唯讀偵測工具可查詢 content.zipe，但無法判定資源包是否惡意。

**標籤**: `#Minecraft`, `#安全漏洞`, `#資源包`, `#惡意軟體`

---


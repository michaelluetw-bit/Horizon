# Horizon 每日快遞 - 2026-11-26

> 從 30 條內容中篩選出 10 條重要資訊。

---

**科技新聞**
1. [1Password 發布 2026 年 11 月資安事件更新](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 預印本聲稱矩陣乘法指數為 9/4](#item-tech-news-2) ⭐️ 8.0/10
3. [Minecraft Java 版傳出字型遠端程式碼執行漏洞](#item-tech-news-3) ⭐️ 8.0/10
4. [文章探討繞過 iOS Safari 60 FPS 限制](#item-tech-news-4) ⭐️ 7.0/10
5. [文章稱沙箱內模型可透過推論伺服器側通道通訊](#item-tech-news-5) ⭐️ 7.0/10
6. [SpaceX 與特斯拉傳商談 3.5 兆美元全股票合併](#item-tech-news-6) ⭐️ 7.0/10
7. [騰訊釋出 Hy4 Flash 量化權重](#item-tech-news-7) ⭐️ 7.0/10
8. [英特爾據報遭美商務部施壓交出約 10% 股權](#item-tech-news-8) ⭐️ 7.0/10
9. [報導：三星與 SK 海力士將採用部分 Xtacking 技術](#item-tech-news-9) ⭐️ 7.0/10
10. [Google 公開 Cogentic 整數分解與離散對數研究論文](#item-tech-news-10) ⭐️ 6.0/10

---

## 科技新聞

<a id="item-tech-news-1"></a>
### [1Password 發布 2026 年 11 月資安事件更新](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

密碼管理服務 1Password 針對 2026 年 11 月的一起資安事件發布更新。由於未提供更新全文，目前無法確認事件範圍或客戶密碼庫是否受到影響。

hackernews · lxhrstn · 11月25日 17:18 · [社群討論](https://news.ycombinator.com/item?id=50644817)

**「事件背景」** 1Password 表示，於 2026 年 11 月 19 日開始調查攻擊者取得一名員工公司 GitHub 帳號存取權的跡象；攻擊者利用該帳號存取原始碼，並向後端服務推送惡意程式碼。

**「社群討論」** 評論者關注惡意程式碼進入後端服務的風險，並質疑公告是否充分說明程式碼分支保護措施。另有使用者希望 1Password 明確說明加密密碼庫是否曾遭下載；這些疑慮不能作為事件影響已獲證實的依據。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving... | 1 Password</a></li>

</ul>
</details>

**標籤**: `#1Password`, `#security incident`, `#password managers`, `#software supply chain`

---

<a id="item-tech-news-2"></a>
### [OpenAI 預印本聲稱矩陣乘法指數為 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 8.0/10

OpenAI 一篇預印本聲稱，矩陣乘法指數恰為 9/4，也就是 2.25。這個指數描述大型方陣相乘所需運算量的最佳漸近增長速率；若聲稱成立，將否定指數為 2 的猜想。提供的資料未包含證明內容或獨立驗證，結果仍待確認。

hackernews · E-Reverance · 11月25日 01:19 · [社群討論](https://news.ycombinator.com/item?id=50637220)

**「背景」** 矩陣乘法指數描述兩個 n × n 矩陣相乘所需運算次數的最佳漸近次方；傳統演演演算法的運算量為 n³。長期以來，研究者一直探討該指數是否為 2，也就是能否以接近平方次的運算量完成乘法。

**「社群討論」** 一位留言者聲稱，這篇論文還解決了強多項式時間線性規劃問題，並為平均收益賽局和奇偶賽局提供多項式時間演演演算法。這些額外聲稱同樣無法從提供的資料中核實。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://xenospectrum.com/en/matrix-multiplication-nine-fourths-lower-bound/">OpenAI Preprint Claims the Matrix Multiplication Exponent Is ...</a></li>

</ul>
</details>

**標籤**: `#matrix multiplication`, `#computational complexity`, `#algorithms`, `#mathematical research`

---

<a id="item-tech-news-3"></a>
### [Minecraft Java 版傳出字型遠端程式碼執行漏洞](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

minecraft2shell 專案聲稱，Minecraft Java 版伺服器資源包中的特製 TrueType 字型，可觸發 FreeType 2.14.3 及更早版本的原生越界寫入，並在 Java 版 26.3 的 Windows 使用者端執行任意程式碼。報導稱受影響版本包括 1.20.5 至 1.21.10、26.1 至 26.4 快照，1.20.4 及更早版本和基岩版不受影響；這些範圍與利用條件尚未經獨立驗證。報導稱 Mojang 尚未發布修補程式，社群的 m2sfix 1.0.0 則可透過 Java agent 或模組關閉字型 hinting 以暫時緩解；玩家也可避免新增資源包，並將多人遊戲伺服器資源包許可權設為「停用」。

telegram · zaihuapd · 11月25日 12:46

**「背景」** Minecraft 資源包可包含 TrueType 字型，而 Java 版 26.3 Windows 客戶端內含用於處理字型的 FreeType 2.14.3。FreeType 是原生函式庫，因此處理字型時的記憶體錯誤可能影響遊戲程式本身。

**「玩家應對措施」** 在官方修補前，受影響版本的玩家可將多人伺服器資源包設為「停用」，並避免安裝不受信任的資源包。社群工具 m2sfix 也提供 Java agent 或 mod，透過停用字型 hinting 暫時降低風險。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://github.com/bikini/minecraft2shell">GitHub - bikini / minecraft 2 shell : Minecraft to native RCE · GitHub</a></li>
<li><a href="https://github.com/sunrisemc-tw/minecraft2shell-fix">GitHub - sunrisemc-tw/minecraft2shell-fix: Client-side ...</a></li>
<li><a href="https://wurst.wiki/minecraft2shell">Minecraft2Shell Vulnerability [Wurst.Wiki]</a></li>

</ul>
</details>

**標籤**: `#Minecraft`, `#遠端程式碼執行`, `#FreeType`, `#軟體安全`

---

<a id="item-tech-news-4"></a>
### [文章探討繞過 iOS Safari 60 FPS 限制](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit) ⭐️ 7.0/10

一篇文章描述如何繞過 iOS Safari 的 60 FPS 限制，讓網頁應用程式的動畫更接近原生體驗。由於未提供文章內文，目前無法確認繞過方式、相容條件或實測效能。

hackernews · vinhnx · 11月25日 03:04 · [社群討論](https://news.ycombinator.com/item?id=50637890)

**「背景」** 觸控輸入的取樣頻率與網頁畫面的更新頻率是兩回事。文章指出，即使取得高頻輸入，DOM 仍可能每秒只更新 60 次，因此單純更頻繁地更新數值，不會增加實際顯示的畫面數。

**「使用條件」** 想以 120 Hz 觀看示範的使用者，需要配備 ProMotion 螢幕，並關閉低耗電模式及「限制影格速率」設定。

**「社群討論」** 有讀者對展示效果印象深刻，也有人表示在第一個範例中只看到細微差異。另有留言者推測，持續以 120 Hz 運作可能增加耗電，但未提供實測資料。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://rida.dev/blog/bypassing-ios-safari-60-fps-limit">Bypassing iOS Safari ’s 60 FPS Limit to Build Web Applications That...</a></li>
<li><a href="https://rida.dev/blog/bypassing-ios-safari-60-fps-limit">Bypassing iOS Safari ’s 60 FPS Limit to Build Web Applications That...</a></li>

</ul>
</details>

**標籤**: `#iOS Safari`, `#WebKit`, `#Web Performance`, `#Animation`

---

<a id="item-tech-news-5"></a>
### [文章稱沙箱內模型可透過推論伺服器側通道通訊](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) ⭐️ 7.0/10

一篇文章聲稱，受沙箱隔離的模型仍可能透過共用推論伺服器的側通道彼此通訊。現有資料未說明攻擊的完整條件或實際效果，因此無法判定其可行性。

hackernews · gmays · 11月25日 02:34 · [社群討論](https://news.ycombinator.com/item?id=50637686)

**「背景」** 沙箱可以限制代理程式直接交換訊息或存取共用檔案系統；側通道則可能利用共用基礎設施中可觀察的間接影響來傳遞資訊，而不依賴一般通訊管道。

**「社群討論」** 一名留言者建議推論伺服器依安全上下文隔離快取，避免不同上下文互相探測；另一名留言者則認為攻擊需要雙方事先知情，並掌握硬體與軟體細節等不太可能同時成立的條件。一名留言者認為，比起合作式通訊，跨租戶非合作式資訊洩漏更值得關注。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being">Models Can Communicate via Inference Servers Despite Being ...</a></li>

</ul>
</details>

**標籤**: `#AI security`, `#inference servers`, `#side channels`, `#cache isolation`

---

<a id="item-tech-news-6"></a>
### [SpaceX 與特斯拉傳商談 3.5 兆美元全股票合併](https://thenextweb.com/news/spacex-tesla-merger-five-directors-special-committees) ⭐️ 7.0/10

報導稱，SpaceX 與特斯拉已選定五名董事，在兩家公司分別組成特別委員會，商談一項規模據稱達 3.5 兆美元的全股票合併，並力爭在年底前完成。知情人士表示，雙方目前尚未接近達成協議，委員會仍需確定換股比例、爭取股東支援，並防範投資者訴訟。

telegram · zaihuapd · 11月25日 00:41

**「背景」** 全股票合併以股份交換而非現金支付，換股比例會影響雙方股東在合併後的持股比例。特別委員會可負責評估交易條件，並協助處理潛在利益衝突。

**標籤**: `#SpaceX`, `#特斯拉`, `#併購`, `#科技產業`

---

<a id="item-tech-news-7"></a>
### [騰訊釋出 Hy4 Flash 量化權重](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 7.0/10

騰訊混元透過 AngelSlim 開源 2240 億引數模型 Hy4 Flash 的 GGUF 量化權重；最小的 IQ2-AH 版本為 125.73 GiB，原始權重約為 410.27 GiB。據稱，搭配 Strata offload 框架，可在 64 GB 記憶體的 Mac mini 上執行。發布資料顯示，48 GB 顯示記憶體裝置在 10K 上下文下每秒生成 89 個 token；M5 Max 128 GB 執行 Q3\_K 版本時，在 32K 上下文下每秒生成 47 個 token。資料也稱 Q3\_K 在 DeepSWE v1.1 等評測中與原模型的分數差距不超過 0.4 分，但未提供完整測試細節。

telegram · zaihuapd · 11月25日 09:29

**「背景」** 模型量化以較低精度表示權重，減少模型佔用空間，但可能影響輸出品質。解除安裝技術則可將部分模型資料存放在記憶體以外，於推論時按需載入，代價可能是額外的資料搬移時間。

**標籤**: `#large language models`, `#quantization`, `#model offloading`, `#open weights`

---

<a id="item-tech-news-8"></a>
### [英特爾據報遭美商務部施壓交出約 10% 股權](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 7.0/10

據 WIRED 引述的法庭檔案，2025 年 8 月，美國商務部律師在與英特爾財務長通話時表示，總統希望在週五宣佈協議，並警告董事會若拒絕，可能面臨無法預測的後果。幾天後，英特爾董事會同意交出美方要求的股份。特朗普隨後聲稱，美國政府完全擁有並控制英特爾 10% 的股份，且未為此付錢；報導稱這批股份目前價值約 110 億美元。

telegram · zaihuapd · 11月25日 13:25

**「背景」** 相關說法出自英特爾股東訴訟中解除遮蔽的法庭檔案，揭露了美國政府與英特爾協商持股的過程。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/wired-commerce-lawyer-warned-intel-cfo-rejecting-us-10-stake-would-carry">Wired: Commerce Lawyer Warned Intel CFO Rejecting US 10% ...</a></li>

</ul>
</details>

**標籤**: `#英特爾`, `#半導體產業`, `#美國政府`, `#企業治理`

---

<a id="item-tech-news-9"></a>
### [報導：三星與 SK 海力士將採用部分 Xtacking 技術](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

報導稱，三星電子與 SK 海力士已透過交叉授權協議，同意在 3D NAND 快閃記憶體中採用長江儲存 Xtacking 的部分技術。Xtacking 將記憶單元與控制電路分別製作於兩片晶圓，再以鍵合工藝結合，讓兩部分能獨立生產與最佳化。三家公司均拒絕置評，協議細節與實際匯入時間尚不明確。

telegram · zaihuapd · 11月25日 14:33

**「技術背景」** 長江儲存於 2018 年推出 Xtacking 架構，將記憶單元陣列與周邊 CMOS 控制電路分別製作在兩片晶圓上，再以晶圓鍵合連線，讓兩者能獨立製造與最佳化。

**「可能影響」** Omdia 分析師指出，這種設計讓廠商可以自行生產記憶體陣列，並將邏輯電路交由晶圓代工廠製造，以採用更先進的製程；報導未說明三星或 SK 海力士是否會採取這種分工。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**標籤**: `#3D NAND`, `#Xtacking`, `#晶圓鍵合`, `#半導體產業`

---

<a id="item-tech-news-10"></a>
### [Google 公開 Cogentic 整數分解與離散對數研究論文](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 6.0/10

Google 公開了 Cogentic 研究論文，涵蓋整數分解、離散對數等主題。現有資料未說明論文的方法或研究結果，因此無法評估其新穎性或對密碼學的影響。

hackernews · rgwohlbold · 11月25日 13:33 · [社群討論](https://news.ycombinator.com/item?id=50642086)

**「背景」** 整數分解是將整數拆解成質因數的問題，RSA 加密的安全性與大整數分解的困難度有關。離散對數問題則是在有限群中，從已知的冪運算結果反求指數；部分密碼系統的安全性依賴這類問題的困難度。

**標籤**: `#integer-factorization`, `#discrete-logarithms`, `#cryptography`, `#research-papers`

---


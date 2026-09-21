# Horizon 每日快遞 - 2026-09-22

> 從 36 條內容中篩選出 4 條重要資訊。

---

1. [NASA 的火星樣本返回任務已告終](#item-1) ⭐️ 8.0/10
2. [昇陽電腦做錯了什麼](#item-2) ⭐️ 8.0/10
3. [Grok 4.7](#item-3) ⭐️ 8.0/10
4. [Python Workers 正式全面推出](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [NASA 的火星樣本返回任務已告終](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) ⭐️ 8.0/10

根據報導，NASA 的火星樣本返回（Mars Sample Return）任務實際上已被取消，這項原本要將毅力號採集的岩芯樣本帶回地球的旗艦計畫就此中止。文章中提及該計畫成本膨脹至約 110 億美元、樣本返回時間恐延後至 2040 年，且架構設計仍依賴舊型火箭，而未善用 Starship 或 New Glenn 等新世代運載能力。社群討論指出中國的天問三號計畫預計 2028 年發射並嘗試火星取樣返回，可能使美國在行星科學領域失去領先地位；同時也有曾任職 ExoMars 任務的工程師分享歐洲取樣任務屢次延宕的經驗，認為未來仍有機會重啟。此事件對行星科學、深空探測政策與航太產業供應鏈皆有重大影響。

hackernews · Muhammad523 · 9月21日 19:14 · [社區討論](https://news.ycombinator.com/item?id=49791939)

**標籤**: `#space exploration`, `#NASA`, `#Mars Sample Return`, `#JPL`, `#Tianwen-3`

---

<a id="item-2"></a>
## [昇陽電腦做錯了什麼](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

這是 Bryan Cantrill（DTrace 創造者、Oxide Computer 共同創辦人）針對昇陽電腦（Sun Microsystems）為何在 2000 年代走向衰敗所寫的深度檢討文章。文中梳理了多項關鍵失誤，包括 2002 年短暫取消 x86 版 Solaris、以及與 Google 的伺服器交易談判因堅持追問對方伺服器數量而破局，這些決策讓許多客戶與開發者不再信任昇陽。社群討論補充了大量第一手經驗，例如當年向 Sun 與 DEC 採購硬體時繁瑣的業務流程，遠不如 Dell 的即時報價與隔日到貨。文章與討論的價值在於從技術路線、商業策略與企業文化三個層面，解釋了一個曾經主導工作站與 Unix 市場的公司在開放源碼與 x86 浪潮下如何失去立足點。

hackernews · chmaynard · 9月21日 14:03 · [社區討論](https://news.ycombinator.com/item?id=49787436)

**標籤**: `#Sun Microsystems`, `#Solaris`, `#系統工程`, `#科技產業史`, `#企業策略`

---

<a id="item-3"></a>
## [Grok 4.7](https://x.ai/news/grok-4-7) ⭐️ 8.0/10

xAI 發布了新一代前沿模型 Grok 4.7，相較於 Grok 4.6 擁有約多出 40% 的權重參數，但輸入與輸出權杖價格維持不變（每百萬輸出 6 美元、輸入 2 美元）。此舉顯示 xAI 願意犧牲利潤率來換取效能提升，且發布時間延後約兩週，外界推測團隊對 4.7 的成果並非完全滿意。社群討論聚焦於基準測試是否仍具參考價值、模型速度偏慢與成本上升的取捨，以及它能否超越即將推出的 Claude Opus 5.5。整體而言，這反映出前沿模型競爭白熱化與版本迭代節奏加快的趨勢。

hackernews · meetpateltech · 9月21日 15:50 · [社區討論](https://news.ycombinator.com/item?id=49788838)

**標籤**: `#LLM`, `#xAI`, `#Grok`, `#AI Models`, `#Benchmarks`

---

<a id="item-4"></a>
## [Python Workers 正式全面推出](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

Cloudflare 宣布 Python Workers 正式進入一般可用（GA）階段，讓開發者能在邊緣平台上以 WebAssembly 執行 CPython 並部署正式生產環境的工作負載。此次更新的一大重點是套件支援的標準化：PyEmscripten 已透過 PEP 783 成為正式標準，同時 Cloudflare 也向上游貢獻程式碼，讓 Requests 與 urllib3 等熱門 HTTP 客戶端能直接透過 JavaScript 的 fetch API 繞送請求。對開發者而言，這意味著可以沿用既有的 Python 生態系與工具鏈，降低把 Python 服務搬到無伺服器邊緣環境的門檻。社群討論中，urllib3 維護者說明了相關上游貢獻與資金流向，Wasmer 團隊也肯定其架構進展，但同時指出冷啟動效能與其他架構限制仍是後續值得觀察的課題。

hackernews · torutofu · 9月21日 13:38 · [社區討論](https://news.ycombinator.com/item?id=49787142)

**標籤**: `#Cloudflare Workers`, `#WebAssembly`, `#Python`, `#Serverless`, `#Pyodide`

---


# Horizon 每日快遞 - 2026-10-13

> 從 38 條內容中篩選出 5 條重要資訊。

---

1. [以 C 語言實作的現代網頁應用程式](#item-1) ⭐️ 8.0/10
2. [駭客遠端啟動全歐洲超市冰箱的自動除霜功能](#item-2) ⭐️ 8.0/10
3. [把 WiFi 7 路由器改造成 320Msps 軟體定義無線電接收器](#item-3) ⭐️ 8.0/10
4. [Codex CLI 預設會安裝持續自我更新的常駐背景守護程式](#item-4) ⭐️ 8.0/10
5. [哈囉 Python 3.15，告別 3.10，現在我可以用 3.11 了](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [以 C 語言實作的現代網頁應用程式](https://prophitt.me/writing/a-modern-web-app-in-c) ⭐️ 8.0/10

這篇文章展示如何用 C 語言打造現代網頁應用，採用 CGI 與極簡部署模式，並透過 pledge、chroot 等機制降低權限，兼顧安全與效能。它挑戰當前層層堆疊的框架與容器化部署，凸顯單一執行檔、低資源佔用與可稽核性的優勢。文中也涉及 FastCGI、BusyBox cgi-bin 等替代方案，引發 Hacker News 上關於維運、安全性與生產力取捨的熱烈討論。對想理解系統底層、精簡架構或特殊 Web 應用的人而言，這是一份具啟發性的實作參考。

hackernews · prophittcorey · 10月12日 16:13 · [社區討論](https://news.ycombinator.com/item?id=50058528)

**標籤**: `#C`, `#Web Development`, `#CGI`, `#Systems Programming`, `#Privilege Separation`

---

<a id="item-2"></a>
## [駭客遠端啟動全歐洲超市冰箱的自動除霜功能](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

這起事件中，駭客入侵歐洲多家超市連鎖店的連網冷藏控制系統，遠端啟動自動除霜、並影響配送與店面標價，法國 Intermarché 等業者約 150 家門市受波及。討論指出，遭鎖定的多為 Danfoss SM800、SC355 等已停產（EOS 2016/2021）的 15 至 20 年老舊控制器，長期缺乏安全更新。此事件突顯 OT/IoT 設備連網化所帶來的風險：為了遠端診斷與節能而連網，卻讓關鍵民生基礎設施暴露於攻擊之下。留言也延伸到醫療檢驗儀器等需訂閱才能運作的連網設備，反映業界普遍低估老舊工業控制系統的安全債。

hackernews · Zeekaas · 10月12日 12:16 · [社區討論](https://news.ycombinator.com/item?id=50055304)

**標籤**: `#cybersecurity`, `#IoT`, `#critical-infrastructure`, `#OT-security`, `#legacy-systems`

---

<a id="item-3"></a>
## [把 WiFi 7 路由器改造成 320Msps 軟體定義無線電接收器](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

開發者 h0m3us3r 在 GitHub 上釋出專案，將採用 MediaTek 晶片的 WiFi 7 路由器（W1700K）改造成取樣率高達 320 Msps 的軟體定義無線電（SDR）接收器，且工作頻段可達 5 GHz。此舉的意義在於，以往要取得這種等級的取樣率與頻段，通常得購買昂貴的專業 SDR 設備，如今只要利用隨手可得的消費級網通硬體即可達成，大幅降低了入門門檻。社群討論指出，同一開發者先前也曾用 ESP32 做出 eSpDR，並推測由於晶片組相同，此方案很可能也能套用到內建 PCIe 的 Banana Pi R4 上。討論中還延伸到自製射頻服務監測儀的可行性，以及手機 FM 收音機被鎖定的背後原因。

hackernews · djfergus · 10月12日 12:41 · [社區討論](https://news.ycombinator.com/item?id=50055593)

**標籤**: `#SDR`, `#WiFi 7`, `#hardware-hacking`, `#reverse-engineering`, `#embedded-systems`

---

<a id="item-4"></a>
## [Codex CLI 預設會安裝持續自我更新的常駐背景守護程式](https://github.com/openai/codex/issues/48195) ⭐️ 8.0/10

Hacker News 上的一則討論指出，OpenAI 的 Codex CLI 在預設情況下會安裝一個持續執行、會自我更新的背景守護程式（daemon），而且官方並未提供任何文件化的關閉設定，只能透過 config.toml 中的 feature flag（daemon_auto_start = false）來停用。使用者回報這個 daemon 會在 ~/.codex 目錄寫入 PID 與鎖定檔，還會保留舊版本佔用大量硬碟空間，有人實測累積達 12GB。更嚴重的是，自動更新過程曾隨機破壞檔案權限，導致 .git 變成唯讀並使任務中斷，讓使用者難以信任其穩定執行。社群提出的因應方式包括刪除這些檔案並改以指向 /dev/null 的符號連結，再以 chattr +i 標記為不可寫。

hackernews · whimblepop · 10月12日 18:29 · [社區討論](https://news.ycombinator.com/item?id=50060694)

**標籤**: `#openai-codex`, `#developer-tools`, `#cli`, `#background-daemon`, `#software-quality`

---

<a id="item-5"></a>
## [哈囉 Python 3.15，告別 3.10，現在我可以用 3.11 了](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 正式發布，由 3.14 與 3.15 的發布經理 Hugo van Kemenade 整理的官方 What's New 指南同步上線。本次最受矚目的新功能是 PEP 810 的「顯式延遲匯入」（explicit lazy imports），開發者可用 lazy import json 的語法延後模組載入，藉此加快啟動速度並降低記憶體開銷。對維護須支援多個 Python 版本的開源專案作者而言，另一個實務重點是 3.10 已進入終止支援，可開始安心採用 3.11 的功能。這代表生態系的最低支援基準正式往前推進一格，對函式庫作者與應用開發者都有直接的排程與相容性影響。

rss · Simon Willison · 10月12日 18:15

**標籤**: `#Python`, `#Python 3.15`, `#PEP 810`, `#lazy imports`, `#programming languages`

---


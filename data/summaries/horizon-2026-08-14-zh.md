# Horizon 每日快遞 - 2026-08-14

> 從 31 條內容中篩選出 9 條重要資訊。

---

1. [DRAM 的義大利麵化](#item-1) ⭐️ 9.0/10
2. [DeepMind 推手語轉文字模型 SL2T，首次落地 Pixel 11 鍵盤與即時字幕](#item-2) ⭐️ 9.0/10
3. [🤖 DeepSeek-V4-Pro 正式版上線，API 將實行峰谷定價](#item-3) ⭐️ 9.0/10
4. [Gemini 3.7 Flash](#item-4) ⭐️ 8.0/10
5. [選擇無聊的技術（2015）](#item-5) ⭐️ 8.0/10
6. [DeepSeek Harness 開發者預覽版](#item-6) ⭐️ 8.0/10
7. [DeepSeek V4 Pro 0813（在 OpenRouter 上）](#item-7) ⭐️ 8.0/10
8. [worldproof：診斷世界模型預測何處失效，以及像素指標何時完全無法對模型排序的測量 (P)](#item-8) ⭐️ 8.0/10
9. [🤖 OpenAI 預覽 Ultrafast 模式，GPT-5.6 Sol 提速 14 倍](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DRAM 的義大利麵化](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

這是一項由知名駭客研究員 Christopher Domas 所開發的硬體安全研究專案，展示了如何透過操縱 DRAM 的物理特性與行為來取得任意程式碼執行能力。該研究特別針對 AMD Jaguar 架構（用於 PS4 和 Xbox One）進行示範，顯示即使在主機系統上獲得核心權限後，攻擊者仍可利用 DRAM 的弱點進一步突破安全防護。與傳統軟體漏洞不同，這種攻擊利用的是記憶體硬體本身的可變異性與瑕疵，難以透過一般修補程式防禦。此技術將在 Black Hat 大會上發表，引發社群對記憶體層面攻擊面的新一輪關注。

hackernews · matt_d · 8月13日 14:17 · [社區討論](https://news.ycombinator.com/item?id=49286341)

**標籤**: `#hardware security`, `#DRAM`, `#exploit`, `#reverse engineering`, `#Black Hat`

---

<a id="item-2"></a>
## [DeepMind 推手語轉文字模型 SL2T，首次落地 Pixel 11 鍵盤與即時字幕](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 9.0/10

DeepMind 發布大規模多語言手語轉文字模型 SL2T，首次將手語 AI 整合至消費產品，率先支援美國手語轉英語，並在 Pixel 11 的 Gboard 和 Live Transcribe 上線。模型使用超過 10 萬小時、50 多種手語資料訓練，在 FLEURS-ASL 基準上零樣本得分 70 BLEURT，遠高於先前紀錄。為保護隱私，僅處理手部與身體姿態關鍵點，不讀取原始影片。這項突破將顯著提升聽障人士的溝通便利性，並可能推動更多設備與語言支援。

telegram · zaihuapd · 8月13日 08:55

**標籤**: `#sign-language`, `#accessibility`, `#DeepMind`, `#AI`, `#translation`

---

<a id="item-3"></a>
## [🤖 DeepSeek-V4-Pro 正式版上線，API 將實行峰谷定價](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 9.0/10

DeepSeek-V4-Pro 正式版已同步上線 APP、網頁端與 API，模型名稱為 deepseek-v4-pro，既有呼叫方式不變。新版模型強化 Agent 能力，並原生支援 Responses API 格式，可直接相容 Codex，對開發者與 AI 應用整合有顯著助益。同時，V4-Pro 與 V4-Flash 的思考模式新增 low、high、max 三種強度選項，讓使用者能依據任務複雜度調整推理資源。API 將自 2026 年 8 月 17 日 0 時起實施峰谷定價，離峰時段價格為高峰時段的一半，這項調整可能影響成本敏感型用戶的呼叫策略，並促進離峰時段的算力使用效率。

telegram · zaihuapd · 8月13日 11:12

**標籤**: `#DeepSeek`, `#AI`, `#API`, `#Pricing`, `#Agent`

---

<a id="item-4"></a>
## [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

Google 推出了新一代高效能模型 Gemini 3.7 Flash，在視覺理解和推理能力上有所提升，同時提供可調節的思考層級以平衡效能與成本。社群討論聚焦於其與 Opus 5、GPT-5.6 Luna 的基準比較，以及特別的「初期定價」——預計在 2026 年底調漲一倍。整體而言，這個模型在價格與效能之間提供了具競爭力的選擇，尤其適合視覺相關任務。

hackernews · thisisauserid · 8月13日 17:23 · [社區討論](https://news.ycombinator.com/item?id=49289112)

**標籤**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#model release`

---

<a id="item-5"></a>
## [選擇無聊的技術（2015）](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

這篇文章提出「創新代幣」（innovation tokens）的概念，每個公司只有少量代幣，應謹慎用於真正需要創新的地方，其餘部分則應選擇成熟、可預測的「無聊技術」。作者認為這樣做能降低風險、減少技術債，並讓團隊專注於產品差異化。此觀點對工程管理和技術選型具有深遠影響，本次 Hacker News 的討論也將此概念延伸至 AI 代理時代的技術選擇，顯示其持續的相關性。

hackernews · tosh · 8月13日 17:48 · [社區討論](https://news.ycombinator.com/item?id=49289512)

**標籤**: `#technology-strategy`, `#engineering-management`, `#innovation`, `#software-design`

---

<a id="item-6"></a>
## [DeepSeek Harness 開發者預覽版](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek Harness 是一款面向 AI 代理的開發工具，本次發布開發者預覽版。其核心特色是完整的可追溯性：所有模型看到的內容（包括系統提示詞、推理過程、工具調用等）都會記錄在僅追加的會話日誌中，方便開發者檢查、重放和分叉。此外，它支援多種模型供應商，無需修改即可整合，提高了靈活性。這項工具對 AI 代理的除錯和透明度有重要意義，也反映了 DeepSeek 在開放性和可觀測性上的努力。社群討論熱烈，特別讚賞其追蹤功能，認為這比美國模型的封閉設計更勝一籌。

hackernews · bjin · 8月13日 12:58 · [社區討論](https://news.ycombinator.com/item?id=49285244)

**標籤**: `#AI Agents`, `#DeepSeek`, `#Developer Tools`, `#Observability`, `#Open Source`

---

<a id="item-7"></a>
## [DeepSeek V4 Pro 0813（在 OpenRouter 上）](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek 推出了最新的 V4 Pro 0813 模型，目前透過 OpenRouter 以 API 方式提供，尚未有官方正式公告頁面。作者推測基於先前四月與七月版本皆開放權重的模式，此次新版本很可能也會開放權重。初步測試發現，模型在低、中、高三種推理等級下輸出的結果（例如生成的鵜鶘圖案）差異極大，這是作者在其他模型上未曾觀察到的現象，顯示推理等級可能對模型行為有顯著影響。此發布對 AI 研究與應用社群具有高度關注價值。

rss · Simon Willison · 8月12日 23:59

**標籤**: `#DeepSeek`, `#AI`, `#LLM`, `#OpenRouter`, `#model release`

---

<a id="item-8"></a>
## [worldproof：診斷世界模型預測何處失效，以及像素指標何時完全無法對模型排序的測量 (P)](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 8.0/10

worldproof 是一個開源工具，用於診斷世界模型在未來幀預測中的失敗情形。作者發現，在真實機器人影片上，像素指標（如 SSIM、PSNR）往往無法區分模型優劣，因為即使是「預測畫面不變」的基線也能獲得極高分數，且誤差不會隨預測時間步長增加而明顯上升。這意味著這類指標對世界模型評估可能嚴重失真。該工具透過比較 rollout 與真實軌跡及物理不變量，來定位並解釋預測失敗的原因，為模型評估提供了更可靠的參考。

reddit · r/MachineLearning · /u/georgia_bucea · 8月13日 19:58

**標籤**: `#世界模型`, `#評估指標`, `#像素指標`, `#機器人影片`, `#開源工具`

---

<a id="item-9"></a>
## [🤖 OpenAI 預覽 Ultrafast 模式，GPT-5.6 Sol 提速 14 倍](https://openai.com/index/previewing-ultrafast/) ⭐️ 8.0/10

OpenAI 首次展示 Ultrafast 模式，讓 GPT-5.6 Sol 比標準處理快至 14 倍，由 Cerebras 驅動，每秒最高輸出 750 個 token，針對故障響應、金融研究、客服與電商等時間敏感場景。目前僅限少數客戶限量預覽，未來將隨算力擴充逐步擴大訪問。這項進展代表 AI 推理速度的重大突破，可能大幅擴展即時應用的可能性，並為高性能 AI 服務樹立新標杆。

telegram · zaihuapd · 8月13日 17:04

**標籤**: `#OpenAI`, `#GPT-5.6`, `#Ultrafast`, `#Cerebras`, `#AI inference`

---


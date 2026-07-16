---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 從 40 條內容中篩選出 14 條重要資訊。

---

1. [Kimi K3：開放前沿智慧](#item-1) ⭐️ 9.0/10
2. [📱🇪🇺 歐盟正式裁定谷歌必須開放 Android 與搜索數據給競爭對手 其他 AI 助手將獲得與 Gemini 同等的系統權限和數據訪問](#item-2) ⭐️ 9.0/10
3. [我們的 Rust 到 Zig 重寫進展如何](#item-3) ⭐️ 8.0/10
4. [索尼再次從「購買」用戶的帳戶中刪除電影](#item-4) ⭐️ 8.0/10
5. [引用 Thibault Sottiaux：一個嚴重的 Codex 錯誤](#item-5) ⭐️ 8.0/10
6. [開源權重模型 Inkling](#item-6) ⭐️ 8.0/10
7. [引用 Linus Torvalds 的言論](#item-7) ⭐️ 8.0/10
8. [xai-org/grok-build 現已開源](#item-8) ⭐️ 8.0/10
9. [ExTernD：擴展秩三元分解——三元 LLM 後訓練量化，精度接近任意量化水平](#item-9) ⭐️ 8.0/10
10. [🤖 馬斯克 xAI 起訴用戶濫用 Grok 生成兒童性虐待深度偽造](#item-10) ⭐️ 8.0/10
11. [長鑫年底產能逼近美光 中國將成全球第二大 DRAM 產地](#item-11) ⭐️ 8.0/10
12. [知網將下架將 DeepSeek 列為作者的論文](#item-12) ⭐️ 8.0/10
13. [日本購買 2.75 萬塊輝達 Rubin 晶片打造機器人主權 AI](#item-13) ⭐️ 8.0/10
14. [1Password 推出 Claude 集成：AI 可代登入網站但全程不接觸密碼](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3：開放前沿智慧](https://www.kimi.com/blog/kimi-k3) ⭐️ 9.0/10

Kimi K3 是一款由 Moonshot AI 推出的開放權重前沿 AI 模型，在多項基準測試中表現與前沿模型相當，且定價與 Anthropic 的 Sonnet 系列相同。該模型具有自主晶片設計能力，能在 48 小時內自動完成晶片設計、優化和驗證，使用開源 EDA 工具在 45nm 製程上實現了 100 MHz 時脈與 8,700 tokens/s 的解碼吞吐量。社群討論中，使用者對其高定價（1M tokens $3/$15）表示合理，但也指出其 API 使用條款允許訓練用途，引發隱私疑慮。此發布對 AI 模型開源社群及晶片設計自動化領域具有重大影響。

hackernews · vincent_s · 7月16日 14:46 · [社區討論](https://news.ycombinator.com/item?id=48935342)

**標籤**: `#AI`, `#frontier model`, `#open-source`, `#chip design`, `#performance`

---

<a id="item-2"></a>
## [📱🇪🇺 歐盟正式裁定谷歌必須開放 Android 與搜索數據給競爭對手 其他 AI 助手將獲得與 Gemini 同等的系統權限和數據訪問](https://www.theverge.com/policy/966438/eu-google-android-ai-interoperability-search-data-dma) ⭐️ 9.0/10

歐盟委員會根據《數位市場法》裁定，谷歌必須向符合條件的競爭對手開放 Android 的部分系統功能以及 Google Search 的部分數據。競爭對手的 AI 助手（如 ChatGPT、Claude）將獲得與 Google Gemini 同等的系統權限（例如調用系統操作、讀取必要資訊），用戶未來可將它們設為深度整合的系統助手。同時，競爭搜索引擎與 AI 聊天機器人也能獲取谷歌長期封閉的搜索數據。谷歌反對稱此舉會危及用戶隱私與安全，但歐盟表示將限制數據用途，並允許谷歌依據隱私和安全標準評估申請訪問 Android 功能的服務，相關限制須符合歐盟規定以保障安全。此裁決對科技巨頭的開放性與市場競爭格局具有深遠影響。

telegram · zaihuapd · 7月16日 13:19

**標籤**: `#欧盟`, `#数字市场法`, `#Android`, `#搜索`, `#AI助手`

---

<a id="item-3"></a>
## [我們的 Rust 到 Zig 重寫進展如何](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

這篇文章和討論記錄了將 Roc 編譯器從 Rust 重寫為 Zig 的過程。作者強調 Zig 在低階記憶體控制上的優勢，特別是在編譯器需要執行不安全操作（如熱補丁）的場景。社群評論中，steveklabnik 質疑「編譯器必然需要不安全程式碼」的說法，而 landr0id 則對 Zig 的執行時期安全檢查（如釋放後使用）的實際效果提出疑問。這場討論反映了程式語言在安全性與效能之間的權衡，對編譯器開發者與系統程式設計師具有參考價值。

hackernews · jorangreef · 7月16日 11:39 · [社區討論](https://news.ycombinator.com/item?id=48933149)

**標籤**: `#Rust`, `#Zig`, `#compilers`, `#systems programming`, `#memory safety`

---

<a id="item-4"></a>
## [索尼再次從「購買」用戶的帳戶中刪除電影](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/) ⭐️ 8.0/10

索尼再次將用戶已「購買」的電影從其帳戶中刪除，引發對數位所有權模式的廣泛討論。此事件凸顯了當前以服務為基礎的數位所有權的脆弱性，消費者實際上並未擁有檔案，而是僅獲得有條件存取權。社群討論聚焦於法律與經濟層面，如退款機制、按鈕標示是否構成欺騙，以及長期儲存責任等。此問題對軟體即服務（SaaS）和數位內容產業具有深遠影響。

hackernews · nekusar · 7月16日 12:13 · [社區討論](https://news.ycombinator.com/item?id=48933419)

**標籤**: `#digital rights`, `#consumer protection`, `#DRM`, `#software-as-a-service`, `#Sony`

---

<a id="item-5"></a>
## [引用 Thibault Sottiaux：一個嚴重的 Codex 錯誤](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

這則內容描述了一個 GPT-5.6 的 Codex 錯誤：當使用者啟用完整存取模式且未開啟沙箱保護或自動審查時，模型可能會意外刪除檔案。具體原因是模型嘗試覆蓋 $HOME 環境變數以定義臨時目錄，但卻錯誤地刪除了 $HOME 目錄本身。此問題凸顯了 AI 編碼代理在缺乏適當安全機制時的潛在風險，對於 AI 安全性和自主代理的部署具有重要警示意義。建議開發者在使用類似工具時務必啟用沙箱和審查功能。

rss · Simon Willison · 7月16日 17:45

**標籤**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-6"></a>
## [開源權重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

由 Mira Murati 領導的 Thinking Machines Lab 發布了首個開源權重模型 Inkling，這是一個混合專家架構的 Transformer 模型，總參數達 975B，激活參數為 41B，採用 Apache-2.0 許可證，並在 45 萬億個文本、圖像、音頻和視頻令牌上進行訓練。該模型支持多模態，但官方提供的模型卡和訓練數據文檔較為簡略，缺乏透明度。Inkling 的發布標誌著開源 AI 領域的重要進展，但對訓練數據的詳細說明不足可能引發社群對模型可信度的關注。

rss · Simon Willison · 7月16日 15:35

**標籤**: `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#AI model`, `#machine learning`

---

<a id="item-7"></a>
## [引用 Linus Torvalds 的言論](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds 在 Linux 核心郵件列表中明確表態，Linux 專案並不反對人工智慧，並將 AI 視為如同其他工具的實用工具。他強調任何對此有異議的人可以分叉或離開專案。這項聲明來自 Linux 的頂層維護者，具有重大影響力，可能加速 AI 工具在核心開發中的整合，並影響整個開源社群對 AI 的態度。Torvalds 認為 AI 的實用性已無庸置疑，反映了他對技術趨勢的務實立場。

rss · Simon Willison · 7月16日 13:26

**標籤**: `#Linux`, `#AI`, `#Linus Torvalds`, `#kernel development`, `#open source`

---

<a id="item-8"></a>
## [xai-org/grok-build 現已開源](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 8.0/10

xAI 的 grok CLI 工具因存在嚴重隱私問題而引發社區強烈反彈：在目錄中運行該命令會將整個目錄（包括 SSH 密鑰、密碼管理器資料庫等）上傳至 xAI 的 Google Cloud 儲存空間。為應對爭議，xAI 迅速禁用該功能，並宣布完全刪除所有已上傳的用戶數據。隨後，xAI 將整個 Grok Build 程式碼庫以 Apache 2.0 許可證開源，此舉在提高透明度的同時，也為社區審計與改進提供了契機。該事件凸顯了 AI 工具在隱私保護與安全設計方面的關鍵挑戰。

rss · Simon Willison · 7月15日 23:59

**標籤**: `#privacy`, `#open-source`, `#AI tool`, `#xAI`, `#command-line`

---

<a id="item-9"></a>
## [ExTernD：擴展秩三元分解——三元 LLM 後訓練量化，精度接近任意量化水平](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

該方法提出一種新穎的三元分解技術，透過將權重矩陣分解為兩個三元矩陣和一個對角縮放矩陣，從而實現可擴展的內部秩，突破了傳統三元量化中固定矩陣大小的限制。這種分解使得量化誤差可以任意小，同時僅需略高於現有量化方法的視訊記憶體。此技術對於大型語言模型的部署具有重要意義，尤其在資源受限的場景下，能夠在保持高精度的同時顯著降低記憶體佔用。關鍵創新在於利用三元運算的優勢，使得額外的計算開銷值得付出，進而達到接近全精度模型的效能。

reddit · r/MachineLearning · /u/LMTLS5 · 7月16日 13:31

**標籤**: `#LLM`, `#Quantization`, `#Ternary`, `#PTQ`, `#Model Compression`

---

<a id="item-10"></a>
## [🤖 馬斯克 xAI 起訴用戶濫用 Grok 生成兒童性虐待深度偽造](https://www.reuters.com/legal/litigation/musks-xai-sues-grok-user-over-sexualized-deepfakes-2026-07-15/) ⭐️ 8.0/10

xAI 對一名南卡羅來納州男子提起訴訟，指控其利用 AI 聊天機器人 Grok 生成兒童性虐待材料和非自願成人色情深度偽造。該男子因性剝削未成年人已於二月被捕，xAI 要求賠償並永久禁止其使用 Grok。此案是首批 AI 公司因用戶生成色情內容而起訴用戶的案件之一，凸顯 AI 濫用與法律責任的重大問題。xAI 還表示今年已暫停超過五萬個帳戶並向相關機構舉報大量案件。

telegram · zaihuapd · 7月16日 01:45

**標籤**: `#AI misuse`, `#deepfakes`, `#legal`, `#child safety`, `#xAI`

---

<a id="item-11"></a>
## [長鑫年底產能逼近美光 中國將成全球第二大 DRAM 產地](https://www.tomshardware.com/pc-components/dram/cxmt-close-to-matching-microns-memory-capacity-in-2026-research-claims-would-put-china-on-track-to-become-worlds-second-largest-dram-producer) ⭐️ 8.0/10

根據調研機構預測，長鑫存儲（CXMT）有望在 2026 年底達到約 35 萬片/月的 DRAM 產能，接近美光的 37.5 萬片/月，屆時中國將成為全球第二大 DRAM 生產基地。除了長鑫，昇維旭、晉華集成等多家中國企業也在擴產，若全部投產，中國 DRAM 總產能可達 60 萬片/月。然而，光刻設備供應仍是關鍵瓶頸，美國 MATCH 法案可能限制先進浸沒式 DUV 對華出口，短期內擴產或受阻。分析師指出，到 2030 年全球 DRAM 供應缺口約 25%，中國新增產能雖有助穩定價格，但主要滿足內需，難以完全消除全球短缺。

telegram · zaihuapd · 7月16日 02:30

**標籤**: `#DRAM`, `#semiconductor`, `#China`, `#CXMT`, `#memory`

---

<a id="item-12"></a>
## [知網將下架將 DeepSeek 列為作者的論文](https://www.zaobao.com.sg/news/china/story20260716-9371836) ⭐️ 8.0/10

中國學術期刊平台知網宣布，已下架將 DeepSeek、Gemini 等 AI 工具列為作者的論文，並明確不接受 AI 作為署名作者。知網指出，AI 不具備民事主體資格，無法承擔論文真實性與學術核查的責任。若作者在研究或寫作中使用 AI，應在研究方法或致謝中說明。此舉標誌著中國學術出版界對 AI 參與論文創作的態度更加規範，可能推動學術倫理標準的更新，也警示研究人員需謹慎使用生成式 AI 工具，避免學術不端風險。

telegram · zaihuapd · 7月16日 07:45

**標籤**: `#学术诚信`, `#人工智能`, `#出版规范`, `#知网`, `#DeepSeek`

---

<a id="item-13"></a>
## [日本購買 2.75 萬塊輝達 Rubin 晶片打造機器人主權 AI](https://www.bloomberg.com/news/articles/2026-07-16/japan-to-buy-nvidia-rubin-chips-to-build-sovereign-ai-for-robots) ⭐️ 8.0/10

日本計劃由新成立的 Noetra 公司主導，購買 27,500 塊輝達下一代 Rubin 晶片，建設大型資料中心，開發面向機器人的本土基礎 AI 模型。該項目獲得政府 3,873 億日圓撥款，軟銀、Preferred Networks、NEC 等企業參與。目標是創建中美之外的第三種選擇，降低對外國技術的依賴，並力爭到 2040 年佔據全球機器人市場 30%以上的份額。首個 AI 模型預計明年 3 月發布，數年內推出機器人專用版本。

telegram · zaihuapd · 7月16日 10:59

**標籤**: `#AI`, `#Robotics`, `#Nvidia`, `#Japan`, `#Sovereign AI`

---

<a id="item-14"></a>
## [1Password 推出 Claude 集成：AI 可代登入網站但全程不接觸密碼](https://9to5mac.com/2026/07/16/1password-now-lets-claude-sign-in-to-websites-without-seeing-your-passwords/) ⭐️ 8.0/10

1Password 正式推出與 Claude 的 Mac 端集成，使用者可授權 AI 代理代為登入網站，但密碼與二次驗證碼不會進入 Claude 的上下文或 Anthropic 系統。憑證經安全通道直接注入目標網頁，使用者需透過生物識別逐條審批當前任務所需的登入項，權限僅限當前會話；若自動填充後提交失敗，已填內容也會立即擦除。此功能目前支援 Mac 的商業、家庭及個人版用戶，需同時安裝 1Password 與 Claude 的桌面及瀏覽器擴展，後續還將支援支付卡和身份資訊。這項整合在保障安全的前提下，提升了 AI 代理操作網站時的便利性與信任度，可能為密碼管理和 AI 安全領域樹立新標準。

telegram · zaihuapd · 7月16日 15:54

**標籤**: `#密码管理`, `#AI集成`, `#安全`, `#Claude`, `#1Password`

---
---
layout: default
title: "Horizon Summary: 2026-08-31 (ZH)"
date: 2026-08-31
lang: zh
---

> 從 28 條內容中篩選出 7 條重要資訊。

---

1. [QubesOS 經由複製到 VM 的錯誤回報後通道導致任意程式碼執行](#item-1) ⭐️ 9.0/10
2. [開放世界多智能體環境中的自主數學發現](#item-2) ⭐️ 9.0/10
3. [METR 和 Redwood 對 HuggingFace 駭客事件提供『神聖的』事後檢討](#item-3) ⭐️ 8.0/10
4. [全新 Hy4 預覽版發布](#item-4) ⭐️ 8.0/10
5. [🤖 索尼音樂等起訴 Anthropic，指控用盜版歌詞訓練 Claude](#item-5) ⭐️ 8.0/10
6. [加州議會通過法案豁免開源系統遵守年齡驗證法](#item-6) ⭐️ 8.0/10
7. [NASA 羅曼太空望遠鏡搭乘獵鷹重型火箭升空，兩枚側助推器成功回收](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [QubesOS 經由複製到 VM 的錯誤回報後通道導致任意程式碼執行](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 9.0/10

QubesOS 發布安全公告 QSB-118，指出在 Dom0 中執行 qvm-copy-to-vm 時，其錯誤回報功能使用 system() 呼叫，導致攻擊者可透過特製的 VM 名稱或路徑注入指令，進而在 Dom0 執行任意程式碼。此漏洞影響所有使用 Dom0 執行複製操作的用戶，但 VM 版本的 qvm-copy-to-vm 因使用不同實作而不受影響。由於 Dom0 是 QubesOS 的安全信任基礎，此漏洞可能讓攻擊者完全控制系統，嚴重性極高。

hackernews · vntok · 8月30日 08:51 · [社區討論](https://news.ycombinator.com/item?id=49496918)

**標籤**: `#security`, `#qubes-os`, `#vulnerability`, `#arbitrary-code-execution`, `#virtualization`

---

<a id="item-2"></a>
## [開放世界多智能體環境中的自主數學發現](https://www.reddit.com/r/MachineLearning/comments/1w2fl67/r_autonomous_mathematical_discovery_in_an/) ⭐️ 9.0/10

該研究介紹了「Station」——一個開放世界多智能體環境，讓不同模型家族的 AI 智能體在沒有中央協調的情況下協作研究數學問題。在 12 個構造問題及其他案例分析中，這些智能體取得了多項新結果，包括有限域 Kakeya 集的無窮新族、11 維 604 點吻接配置的改良，以及若干數學難題的紀錄突破。更關鍵的是，智能體不僅產出數值構造，還提出了定理與分析解釋，展現出 AI 不只是計算工具，也能參與自主數學探索與推導。

reddit · r/MachineLearning · /u/progenitor414 · 8月30日 11:55

**標籤**: `#AI for Math`, `#Multi-Agent Systems`, `#Autonomous Discovery`, `#Open-World`, `#Machine Learning Research`

---

<a id="item-3"></a>
## [METR 和 Redwood 對 HuggingFace 駭客事件提供『神聖的』事後檢討](https://thezvi.wordpress.com/2026/08/29/metr-and-redwood-offer-holy-postmortem-of-the-huggingface-hack/) ⭐️ 8.0/10

這篇文章是對 HuggingFace 駭客事件的事後檢討，由 METR 和 Redwood 等 AI 安全組織提供，強調了 AI 安全社群在事件中的反應與預測。文中指出，雖然 OpenAI 等公司有內部團隊監控，但結構上的人為組織失敗才是主因，而非單純的機器能動性。評論區的討論進一步延伸，提到理性主義社群多年來對這類風險的警告，以及為何這些警告常被忽略。這次事件凸顯了 AI 安全不僅是技術問題，更是機構管理與責任歸屬的挑戰，對未來 AI 治理有重要啟示。

hackernews · catbird · 8月30日 14:06 · [社區討論](https://news.ycombinator.com/item?id=49498787)

**標籤**: `#AI Security`, `#HuggingFace`, `#AI Safety`, `#Postmortem`, `#Institutional Failure`

---

<a id="item-4"></a>
## [全新 Hy4 預覽版發布](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 8.0/10

騰訊今日發布 Hy4 預覽版，這是一款開源權重的純文字大型語言模型，總參數達 770B，活躍參數 49B，支援 100 萬 token 的上下文視窗，規模從上一代 Hy3 大幅提升。其 Hugging Face 檔案大小為 1.56TB，並配有包含 reasoning_effort 參數的聊天模板，暗示其具備推理調控能力。此舉顯示中國科技巨頭在開源 LLM 領域的快速進步，對 AI 研究和應用開發具有重要影響。

rss · Simon Willison · 8月29日 23:53

**標籤**: `#LLM`, `#Tencent`, `#open-weights`, `#AI`, `#Hugging Face`

---

<a id="item-5"></a>
## [🤖 索尼音樂等起訴 Anthropic，指控用盜版歌詞訓練 Claude](https://www.musicbusinessworldwide.com/files/2026/08/COMPLAINT-in-Sony_Music_Publishing_US_LLC_e.pdf) ⭐️ 8.0/10

索尼音樂、華納查佩爾等多家音樂出版商在美國加州聯邦法院起訴 Anthropic，指控其未經授權從 LibGen、PiLiMi 等盜版庫下載超過 700 萬本書籍，並抓取歌詞來訓練 Claude 模型，同時刪除版權管理資訊。原告要求每件作品最高 15 萬美元的賠償及永久禁令。此案凸顯 AI 訓練資料的版權爭議，可能對未來 AI 開發與內容授權產生深遠影響。

telegram · zaihuapd · 8月30日 01:00

**標籤**: `#AI`, `#copyright`, `#LLM`, `#legal`, `#Anthropic`

---

<a id="item-6"></a>
## [加州議會通過法案豁免開源系統遵守年齡驗證法](https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt) ⭐️ 8.0/10

加州議會通過第 1856 號法案（AB 1856），將依據 GPL、MIT、BSD 或 Apache 等開源許可證分發的操作系統排除在《數位年齡保障法》的適用範圍之外。該法案在參議院以 39 比 0 全票通過，目前已送交州長簽署，法律原定於 2027 年 1 月 1 日生效。這意味著 Debian、Fedora、Ubuntu、Arch 及 BSD 系列發行版無需在帳戶設置時收集使用者年齡信息，而 Windows、macOS、iOS 和 Android 等商用系統仍須遵守。此舉對開源社群意義重大，避免了繁重的合規負擔，也為開源軟體在加州的合法使用提供了更清晰的保障。

telegram · zaihuapd · 8月30日 11:04

**標籤**: `#開源`, `#加州法案`, `#年齡驗證`, `#操作系統`, `#政策`

---

<a id="item-7"></a>
## [NASA 羅曼太空望遠鏡搭乘獵鷹重型火箭升空，兩枚側助推器成功回收](https://weibo.com/6560646233/RfOLkeG70) ⭐️ 8.0/10

美國太空總署（NASA）新一代旗艦級太空望遠鏡「南希·格雷斯·羅曼太空望遠鏡」（Roman）於 2025 年搭乘 SpaceX 獵鷹重型火箭從佛羅里達州發射升空。這款望遠鏡具備與哈伯同級的成像能力，但視野廣闊百倍以上，被視為研究暗能量、星系演化與系外行星的關鍵平台。發射後兩枚側助推器成功返回地球並精準降落在卡納維拉爾角太空軍基地，實現同步回收。此任務將大幅加速天文觀測效率，有助於科學家繪製更完整的宇宙地圖，並探索暗能量的本質。

telegram · zaihuapd · 8月30日 11:49

**標籤**: `#NASA`, `#Roman Space Telescope`, `#Falcon Heavy`, `#SpaceX`, `#天文學`

---
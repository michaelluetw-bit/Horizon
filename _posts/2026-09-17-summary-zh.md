---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> 從 33 條內容中篩選出 6 條重要資訊。

---

1. [訓練一個 4B 模型產生比 Postgres 快 81% 的查詢計畫](#item-1) ⭐️ 8.0/10
2. [駭客成功侵入 Flock 攝影機](#item-2) ⭐️ 8.0/10
3. [GoBench：在圍棋對局上評估大型語言模型 (R)](#item-3) ⭐️ 8.0/10
4. [Cloudflare 推出新設定：可保留搜尋收錄並禁止 AI 訓練](#item-4) ⭐️ 8.0/10
5. [🍏 極客灣：蘋果最強 2nm 手機晶片來了](#item-5) ⭐️ 8.0/10
6. [美光稱其展示全球首款 512 GB DDR5 模組，2027 年具備量產條件](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [訓練一個 4B 模型產生比 Postgres 快 81% 的查詢計畫](https://rohanbansal.com/qorl) ⭐️ 8.0/10

這篇文章介紹作者如何訓練一個 40 億參數的語言模型，讓它為 SQL 查詢生成執行計畫，並在自建基準測試中達到比 PostgreSQL 內建查詢規劃器快 81% 的表現。其意義在於展示小模型經蒸餾與強化學習可用於資料庫核心元件，挑戰長久以來依賴成本模型與啟發式規則的傳統做法。不過 Hacker News 上的討論指出，該測試僅使用可完全放入記憶體的 8 GB 資料集、受限的 shared_buffers、預熱過的查詢與唯讀 SELECT，因此結果可能過度擬合，難以推論到真實 OLTP 規模的工作負載。留言也爭論 LLM 是否為合適工具，並期待 AlphaGo 式的學習式啟發法或即時索引等替代方案。

hackernews · polyphilz · 9月16日 18:50 · [社區討論](https://news.ycombinator.com/item?id=49731285)

**標籤**: `#databases`, `#query-optimization`, `#LLM`, `#postgresql`, `#machine-learning`

---

<a id="item-2"></a>
## [駭客成功侵入 Flock 攝影機](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

資安研究人員與記者合作揭露，Flock 車牌辨識（ALPR）監控攝影機存在硬編碼憑證、未加密的裝置內資料，以及安全開機與金鑰管理實作不良等嚴重漏洞。攻擊者只要實際接觸裝置，就能直接讀取甚至取得系統中的敏感資料。評論者批評 Flock 的漏洞揭露政策徒具形式，只為營造負責任的資安形象，實際上卻迴避真正的通報。由於這類攝影機大量部署於公共空間，此事件突顯大規模監控系統在隱私與供應鏈安全上的重大風險，DDoSecrets 亦已公開相關分割區映像檔以供驗證。

hackernews · driverdan · 9月16日 13:18 · [社區討論](https://news.ycombinator.com/item?id=49726586)

**標籤**: `#security`, `#privacy`, `#surveillance`, `#ALPR`, `#vulnerability-disclosure`

---

<a id="item-3"></a>
## [GoBench：在圍棋對局上評估大型語言模型 (R)](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 8.0/10

GoBench 提出一個以 9x9 圍棋評估大型語言模型的新基準，讓模型與從隨機到超人的 KataGo 階梯對手對弈，並持續維護排行榜。此基準旨在測量通用推理能力，且與 ARC-AGI 2 呈高度相關（r=0.83），目前仍未飽和，顯示仍有很大進步空間。技術上，GPT-6 Astra 最高可達 2500 Elo，仍遠低於最佳 KataGo 的 4400 Elo；若允許使用程式工具並在評估前準備兩小時，Codex 搭配 Astra 可提升至 3560 Elo。此工作提供可重現的程式碼、論文與排行榜，對 LLM 推理評測具參考價值。

reddit · r/MachineLearning · /u/Roland31415 · 9月16日 18:54

**標籤**: `#LLM Evaluation`, `#Go`, `#Benchmark`, `#Reasoning`, `#KataGo`

---

<a id="item-4"></a>
## [Cloudflare 推出新設定：可保留搜尋收錄並禁止 AI 訓練](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/) ⭐️ 8.0/10

Cloudflare 於 9 月 15 日宣布推出「禁止 AI 訓練」設定，讓網站站長可以選擇繼續被搜尋引擎收錄，同時阻擋不符合規範的 AI 訓練爬蟲。此設定以網域為單位配置，蘋果、Google 與微軟已符合或承諾遵守相關要求，使這項機制具備實際約束力。需要注意的是，若選擇「阻止」，包含混合型爬蟲在內的所有爬蟲都會被攔截，搜尋收錄也會連帶受到影響。Cloudflare 計畫於明年初進一步讓網站能控制內容被 AI 摘要引用的比例，這可能成為以同意為基礎的 AI 爬取新標準。

telegram · zaihuapd · 9月16日 05:46

**標籤**: `#Cloudflare`, `#AI Crawlers`, `#Web Privacy`, `#Search Indexing`, `#Content Licensing`

---

<a id="item-5"></a>
## [🍏 極客灣：蘋果最強 2nm 手機晶片來了](https://www.bilibili.com/video/BV1oZeA6fERD) ⭐️ 8.0/10

蘋果發表搭載首款 2nm 旗艦晶片 A20 Pro 的 iPhone 18 Pro 系列，A20 Pro 具備 6 核心 CPU（超核提速 20%）、7 核心 GPU（提速 40%）與雙 16 核心神經網路引擎，記憶體頻寬較 A19 Pro 提升 50%。晶片改用借鏡 M 系列的新封裝設計，並疊加 3 倍面積 VC 均熱板，持續效能最多提升 40%。同時推出自研 C2 數據機（上傳提速 50%、功耗降 15%）與首款客製 N1 無線晶片，支援 Wi-Fi 7 與藍牙 6。此舉代表手機晶片正式邁入 2nm 世代，並強化蘋果在通訊與無線領域的自研垂直整合能力。

telegram · zaihuapd · 9月16日 13:24

**標籤**: `#Apple`, `#半導體製程`, `#2nm`, `#行動SoC`, `#晶片封裝`

---

<a id="item-6"></a>
## [美光稱其展示全球首款 512 GB DDR5 模組，2027 年具備量產條件](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 8.0/10

美光宣布展示全球首款 512 GB DDR5 RDIMM 伺服器記憶體模組，最高速率達 9200 MT/s，並正由 AMD 與 Intel 為未來伺服器平台進行驗證，預計 2027 年可量產。該模組採用 3D 堆疊 DRAM 技術，24 根可組成 12 TB 記憶體容量。其單根功耗僅 16W，相較四根 128 GB 模組的 44.2W 降低超過 60%，可望大幅提升資料中心記憶體密度與能源效率。若如期落地，將對雲端、AI 與高效能運算伺服器帶來顯著影響。

telegram · zaihuapd · 9月16日 16:15

**標籤**: `#DDR5`, `#Micron`, `#Server Memory`, `#3D DRAM`, `#Hardware`

---
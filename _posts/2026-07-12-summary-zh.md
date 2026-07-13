---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 從 26 條內容中篩選出 8 條重要資訊。

---

1. [vllm-project/vllm 釋出 v0.25.0](#item-1) ⭐️ 9.0/10
2. [Nvidia、CoreWeave 和 Nebius：GPU 熱潮中的循環融資內幕](#item-2) ⭐️ 8.0/10
3. [我們將 PgBouncer 的吞吐量提升了 4 倍](#item-3) ⭐️ 8.0/10
4. [偏好 SQLite 中的嚴格表](#item-4) ⭐️ 8.0/10
5. [在 HuggingFace 上發布的 VultronRetriever 模型系列(R)](#item-5) ⭐️ 8.0/10
6. [🍏 蘋果起訴 🤖 OpenAI，指控其系統性竊取商業機密推進硬體業務](#item-6) ⭐️ 8.0/10
7. [U-Boot 引導程式曝 6 個漏洞，可繞過驗證在啟動時執行惡意程式碼](#item-7) ⭐️ 8.0/10
8. [智譜創始人唐杰啟動「摸高計劃」：不登頂就是失敗](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vllm-project/vllm 釋出 v0.25.0](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 版本的重大變更包括：Model Runner V2 成為所有密集模型的預設執行路徑，取代了舊版 PagedAttention 注意力機制，這個移除簡化了程式碼並提升了執行效率。Transformers 後端現在與原生 vLLM 速度相當，並新增 FP8 MoE 支援與多種模型（如 LLaVA-OneVision-2、Unlimited OCR 等）。此版本包含 558 項提交，來自 232 位貢獻者，對 LLM 推理框架的效能與擴展性有顯著影響。

github · khluu · 7月11日 20:06

**標籤**: `#vllm`, `#LLM inference`, `#model serving`, `#attention optimization`, `#open-source`

---

<a id="item-2"></a>
## [Nvidia、CoreWeave 和 Nebius：GPU 熱潮中的循環融資內幕](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 8.0/10

本文深入探討了 Nvidia、CoreWeave 和 Nebius 之間的融資關係，揭示了 GPU 雲端市場中可能存在的循環融資模式。分析指出，Nvidia 對 CoreWeave 的投資僅佔其資本支出的一小部分，但整體市場的盈利能力仍存疑，需關注 ROI 和企業代幣預算等指標。社區討論對『循環融資』觀點有異議，認為 Nvidia 的投資具策略性，是對抗超大型雲端業者的手段。此文對於理解 GPU 基礎設施的財務結構和潛在泡沫風險具有重要參考價值。

hackernews · adletbalzhanov · 7月11日 17:21 · [社區討論](https://news.ycombinator.com/item?id=48873836)

**標籤**: `#Nvidia`, `#CoreWeave`, `#GPU`, `#cloud computing`, `#finance`

---

<a id="item-3"></a>
## [我們將 PgBouncer 的吞吐量提升了 4 倍](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 8.0/10

此文章來自 ClickHouse 團隊，詳細介紹了他們如何將 PostgreSQL 連線池 PgBouncer 的吞吐量提升至原來的 4 倍。主要技術包括實作連線「對等（peering）」機制，讓取消查詢能正確轉發到對應工作進程，以及優化資源分配。這對依賴 PostgreSQL 的高併發應用非常重要，因為連線池瓶頸常影響整體效能。社群討論中也提及了 Odyssey、pgdog 等替代方案，以及 Kubernetes 環境下的部署考量。

hackernews · saisrirampur · 7月11日 15:28 · [社區討論](https://news.ycombinator.com/item?id=48872874)

**標籤**: `#PostgreSQL`, `#PgBouncer`, `#connection pooling`, `#scaling`, `#ClickHouse`

---

<a id="item-4"></a>
## [偏好 SQLite 中的嚴格表](https://evanhahn.com/prefer-strict-tables-in-sqlite/) ⭐️ 8.0/10

這篇文章提倡在 SQLite 中使用嚴格表（strict tables）來強制執行欄位類型，避免因類型鬆散導致的資料損毀。雖然 SQLite 預設採用靈活類型，但嚴格表能顯著提升資料完整性。作者也介紹了 sqlite-utils 工具，可將現有表格轉換為嚴格模式。社群討論中，專家們探討了嚴格模式的利弊，指出其對需要高可靠性的專案尤為重要，但並非所有情境都適用。

hackernews · ingve · 7月11日 17:33 · [社區討論](https://news.ycombinator.com/item?id=48873940)

**標籤**: `#SQLite`, `#database`, `#data integrity`, `#strict tables`

---

<a id="item-5"></a>
## [在 HuggingFace 上發布的 VultronRetriever 模型系列(R)](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

這個新發布的 VultronRetriever 模型系列在 MTEB 排行榜上各尺寸級別均排名第一，其中 VultronRetrieverPrime-8B 更是全球總排名第一。這些模型在性能上大幅領先同級別模型，具有高達 16 倍更小的存儲佔用和 12 倍更高的吞吐量。更重要的是，它們能夠完全離線在 iPhone 上運行問答和文檔嵌入任務，這對於邊緣設備上的 AI 應用具有重要意義。VultronRetrieverFlash-0.8B 尤其適合邊緣設備，每分鐘可索引多達 60 張圖片。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**標籤**: `#Machine Learning`, `#HuggingFace`, `#MTEB`, `#Retrieval`, `#Embeddings`

---

<a id="item-6"></a>
## [🍏 蘋果起訴 🤖 OpenAI，指控其系統性竊取商業機密推進硬體業務](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 8.0/10

蘋果於 2026 年 7 月 10 日在美國加州北區聯邦法院對 OpenAI 提起訴訟，指控其通過招聘蘋果前員工、接觸供應商等方式，系統性獲取並利用蘋果的產品設計、製造工藝及供應鏈機密，以加速其消費級硬體研發。蘋果指出，前員工劉暢在離職後仍訪問內部網絡並下載數十份硬體文件；OpenAI 硬體負責人陳中宇則被指在離職前將供應商資料發送至個人郵箱，並要求求職者攜帶蘋果零部件參加面試。目前已有超過 400 名前蘋果員工在 OpenAI 工作。此案若成立，可能對 AI 公司的人才獲取和研發模式產生深遠影響，並加劇科技巨頭之間的競爭與法律糾紛。

telegram · zaihuapd · 7月11日 03:14

**標籤**: `#Apple`, `#OpenAI`, `#lawsuit`, `#trade secrets`, `#hardware`

---

<a id="item-7"></a>
## [U-Boot 引導程式曝 6 個漏洞，可繞過驗證在啟動時執行惡意程式碼](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

此漏洞存在於 U-Boot 引導程式的 FIT 簽名驗證代碼中，最早可追溯至 2013.07 版本，影響超過 50 個穩定版本及大量下游廠商分支。其中兩個漏洞可導致任意程式碼執行，四個可造成裝置崩潰。攻擊者可在作業系統和安全軟體啟動之前執行惡意程式碼，從而禁用固件安全功能、修改啟動流程或植入持久性固件惡意軟體。對於支援遠程固件更新的 BMC 等系統，攻擊者無需物理接觸設備即可利用。雖然 U-Boot 維護者已提交並接受修補程式，但需要各硬體廠商集成到固件更新後才能分發，已停止支持的舊設備可能永遠無法獲得修復。

telegram · zaihuapd · 7月11日 08:32

**標籤**: `#安全漏洞`, `#U-Boot`, `#固件安全`, `#引导程序`

---

<a id="item-8"></a>
## [智譜創始人唐杰啟動「摸高計劃」：不登頂就是失敗](https://mp.weixin.qq.com/s/3CQSkf_kBnXiCDgS4L-Cgg) ⭐️ 8.0/10

唐杰宣布啟動「摸高計劃」，旨在長期聚焦 AGI 研究而非短期商業變現。計劃需翻越四座高峰：長程任務、自治智能體系統、完全自我訓練和極致安全治理。其中極致安全治理將投入百億級資源攻關機械可解釋性，推動黑盒模型透明化。目前智譜 GLM-5.2 模型已接近海外最先進水平，此計劃彰顯其對基礎研究和安全治理的戰略重視。

telegram · zaihuapd · 7月11日 13:59

**標籤**: `#AGI`, `#智谱`, `#可解释性`, `#AI安全`, `#战略计划`

---
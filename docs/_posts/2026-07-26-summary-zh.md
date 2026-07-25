---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 從 23 條內容中篩選出 6 條重要資訊。

---

1. [sgl-project/sglang 发布 v0.5.16 版本](#item-1) ⭐️ 9.0/10
2. [vllm-project/vllm 发布 v0.26.0 版本](#item-2) ⭐️ 8.0/10
3. [Android 可能很快限制裝置端 ADB](#item-3) ⭐️ 8.0/10
4. [開源權重人工智慧正經歷其 Kubernetes 時刻](#item-4) ⭐️ 8.0/10
5. [介紹 Claude Opus 5](#item-5) ⭐️ 8.0/10
6. [兩部門發布離岸信託個稅新規，裝入財產及收益須申報納稅](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [sgl-project/sglang 发布 v0.5.16 版本](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 9.0/10

此版本包含来自 169 位贡献者的 574 个拉取请求，主要亮点包括：新的推测解码算法 DSpark，基于置信度进行半自回归分块生成，并在 DeepSeek-V4-Pro 上达到 383.7 tok/s 的吞吐量；支持 975B 参数的 Inkling 多模态 MoE 模型，该模型结合了滑动窗口、全注意力、Mamba2 线性注意力和 NVFP4 MoE，在 Blackwell 上实现了高达 71.7k tok/s 的输入吞吐量。这些改进显著提升了大型语言模型的推理速度和适用性。

github · Qiaolin-Yu · 7月25日 00:13

**標籤**: `#SGLang`, `#Speculative Decoding`, `#Large Language Models`, `#Inference Optimization`, `#MoE`

---

<a id="item-2"></a>
## [vllm-project/vllm 发布 v0.26.0 版本](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 版本包含了 411 次提交和 212 位贡献者的工作（其中 61 位是新贡献者）。该版本主要亮点包括：引入了全新的 Inkling 模型家族，并提供了从基础建模、CUDA 图支持、注意力机制到推测解码和 LoRA 的完整支持栈；针对 DeepSeek-V4 模型进行了深度性能优化，涉及专有路由内核、融合操作、稀疏解码/预填充优化以及跨厂商的推测解码支持；新增了 fp32 lm_head（通过 head_dtype 参数）以提高生成头的精度，并扩展到 LoRA 路径；此外还改进了灵活的注意力后端。这些更新显著提升了 vLLM 的推理效率和模型支持广度，对大规模语言模型的部署和应用具有重要价值。

github · khluu · 7月25日 10:38

**標籤**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#deep learning`, `#open source`

---

<a id="item-3"></a>
## [Android 可能很快限制裝置端 ADB](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/) ⭐️ 8.0/10

這篇文章討論 Android 可能限制裝置端 ADB（Android 除錯橋）的提案，目的是增強安全性，防止未經授權的存取。此舉將影響開發者和高階使用者，因為他們依賴 ADB 進行應用程式安裝、日誌擷取和除錯。社群評論反映兩極看法：一方認為攻擊向量極少且用戶可自主選擇，另一方則視此為 Google 逐步鎖定裝置的跡象。關鍵技術細節包括限制遠端 ADB 連線和僅允許特定 IP 位址，但引發對開發者自由與便利性的擔憂。

hackernews · shscs911 · 7月25日 06:57 · [社區討論](https://news.ycombinator.com/item?id=49045159)

**標籤**: `#Android`, `#security`, `#ADB`, `#developer tools`, `#privacy`

---

<a id="item-4"></a>
## [開源權重人工智慧正經歷其 Kubernetes 時刻](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

本文將開源權重 AI 模型與 Kubernetes 的崛起類比，指出它們正成為行業標準。作者認為美國實驗室需要釋出前沿級別的開源權重模型，以維持競爭力。討論中用戶探討了禁止中國 AI 模型的技術不可行性，以及開源模型對推理價格的錨定作用。這反映了開源 AI 生態系統的成熟，可能重塑監管和商業模式。

hackernews · tknaup · 7月25日 14:49 · [社區討論](https://news.ycombinator.com/item?id=49048034)

**標籤**: `#open-weight`, `#AI`, `#open-source`, `#Kubernetes`, `#regulation`

---

<a id="item-5"></a>
## [介紹 Claude Opus 5](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 8.0/10

Anthropic 發布了新的語言模型 Claude Opus 5，定價僅為 Claude Fable 5 的一半，但在性能上接近後者，並在 Artificial Analysis 排行榜上領先。它被描述為「深思熟慮且主動的模型」，價格與 Opus 4.8 相同，並提供高速模式。這一發布可能會影響 AI 模型的定價和競爭格局。

rss · Simon Willison · 7月24日 23:48

**標籤**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#model release`

---

<a id="item-6"></a>
## [兩部門發布離岸信託個稅新規，裝入財產及收益須申報納稅](https://liaoning.chinatax.gov.cn/art/2026/7/24/art_5869_7823.html) ⭐️ 8.0/10

中國財政部與稅務總局發布 2026 年第 21 號公告，明確離岸信託的個人所得稅徵管規則。新規要求居民個人將財產裝入離岸信託時，按市場價值扣除原值及合理費用後的增值部分，以「財產轉讓所得」稅率 20%繳稅。信託存續期間產生的收益，無論是否實際分配，居民個人均須按年申報納稅。此舉徹底堵住了過去「信託收益不分配即不納稅」的避稅空間，具有重大合規影響。對於 2023 年至 2025 年期間的歷史稅務問題，提供了 90 天的補繳寬限期且不加收滯納金。

telegram · zaihuapd · 7月25日 00:31

**標籤**: `#税务`, `#离岸信托`, `#中国税法`, `#个人所得税`, `#合规`

---
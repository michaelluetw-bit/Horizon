---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 從 26 條內容中篩選出 3 條重要資訊。

---

1. [阿里 AI 開放權重模型下載量超 30 億，半年內超過 Meta 和谷歌](#item-1) ⭐️ 9.0/10
2. [不要分類，要幻覺！](#item-2) ⭐️ 8.0/10
3. [BDH-CQ：基於循環潛在推理的上下文學習](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [阿里 AI 開放權重模型下載量超 30 億，半年內超過 Meta 和谷歌](https://www.bloomberg.com/news/articles/2026-08-15/alibaba-ai-models-hit-3-billion-downloads-passing-meta-google) ⭐️ 9.0/10

阿里巴巴的開放權重 AI 模型在過去六個月內全球下載量超過 30 億次，根據 Hugging Face 的報告，這一數字超越了 Meta（2.27 億次）和谷歌（4.18 億次）的模型下載量。阿里表示，其 Qwen 系列已開源超過 460 個模型，並衍生出超過 30 萬個版本。此事件標誌著開源 AI 生態系統的重大轉變，顯示中國科技巨頭在全球 AI 開發者社群中的影響力日益增強，可能重新定義開源模型的競爭格局。

telegram · zaihuapd · 8月15日 15:18

**標籤**: `#AI`, `#open-source`, `#Alibaba`, `#Qwen`, `#machine-learning`

---

<a id="item-2"></a>
## [不要分類，要幻覺！](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 8.0/10

此文章介紹 Doug Turnbull 提出的「假想分類」技術：當標籤數量過多而無法一次餵入 LLM 時，先讓模型自由「幻覺」出可能的分類標籤，不受既有詞彙限制；接著利用向量嵌入將這些虛構標籤與既有標籤語料進行比對，找出最接近的真實標籤。這種方法能有效解決大型標籤空間的分類問題，並在搜尋與內容標記上提供新的思路。文章強調示例標籤的形狀能幫助模型產生更實用的猜測，顯示小型提示工程也能帶來顯著效果。

rss · Simon Willison · 8月14日 21:54

**標籤**: `#LLM`, `#vector embeddings`, `#classification`, `#tagging`, `#search`

---

<a id="item-3"></a>
## [BDH-CQ：基於循環潛在推理的上下文學習](https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/) ⭐️ 8.0/10

BDH-CQ 提出了一種新穎的推理系統，將記憶更新與適應整合到統一的計算架構中。該模型在推論時透過高維潛在空間的反覆計算解決查詢，無需將中間步驟解碼為語言。在 ARC-AGI-1 基準上，僅用 150M 參數即達到 29.5% 的 pass@2，每任務成本低至 0.0007 美元，突破了成本與準確率之間的帕累托前緣。這項研究展示了潛在推理與記憶機制的結合，為無需顯式語言中間步驟的高效連續推理提供了新方向。

reddit · r/MachineLearning · /u/moschles · 8月15日 06:18

**標籤**: `#Machine Learning`, `#In-Context Learning`, `#Recurrent Latent Reasoning`, `#ARC-AGI`, `#AI Research`

---
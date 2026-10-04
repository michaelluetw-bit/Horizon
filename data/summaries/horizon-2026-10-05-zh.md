# Horizon 每日快遞 - 2026-10-05

> 從 25 條內容中篩選出 2 條重要資訊。

---

1. [在消費級硬體（RTX 4090）上以 100 T/s 執行 Qwen 3.8 Flash Next（125B）](#item-1) ⭐️ 8.0/10
2. [Kaggle 上 ARC-AGI-3 最高分剛從 7% 躍升至 56%](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [在消費級硬體（RTX 4090）上以 100 T/s 執行 Qwen 3.8 Flash Next（125B）](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

Strata 專案展示了如何於單張消費級 RTX 4090（24GB VRAM）上執行 125B 參數的 Qwen 3.8 Flash Next 模型，並達到每秒超過 100 個 token 的生成速度。其關鍵在於極低位元量化與 MTP 多 token 預測等技術，讓原本需要多張資料中心 GPU 的大模型得以落地於個人工作站，對本地推論社群具有指標性意義。不過討論中也浮現重要疑慮：有使用者以 50 張影像的視覺定位基準測試發現，相同權重下 Strata 的中位誤差為 154.8 像素，遠高於 llama.cpp 的 46.5 像素，顯示低於 4-bit 的量化可能帶來明顯品質衰退；其他人則分享在租用 GPU 上跑 4-bit 量化、兼顧成本與品質的實務經驗。因此這項成果的價值在於速度與可及性，但品質取捨仍需審慎評估。

hackernews · snehesht · 10月4日 12:51 · [社區討論](https://news.ycombinator.com/item?id=49953495)

**標籤**: `#local-llm-inference`, `#quantization`, `#consumer-gpu`, `#Qwen`, `#llm-optimization`

---

<a id="item-2"></a>
## [Kaggle 上 ARC-AGI-3 最高分剛從 7% 躍升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

一篇 Reddit 貼文指出，Kaggle 上 ARC-AGI-3 基準測試的最高分在過去 30 天內從 7% 躍升至 56%。由於 Kaggle 參賽者只能使用較小的本地模型，這意味著模型在特定框架（harness）輔助下，已開始超越平均人類表現。ARC-AGI 原本設計來展示人類在抽象推理上的優勢，因此分數大幅提升被視為重要進展，但也可能需要驗證是否為真正的推理能力或框架技巧。貼文未提供詳細方法與討論內容，因此影響仍待進一步確認。

reddit · r/MachineLearning · /u/we_are_mammals · 10月4日 10:24 · [社區討論](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**標籤**: `#ARC-AGI`, `#Kaggle`, `#LLM reasoning`, `#Benchmarks`, `#Local models`

---


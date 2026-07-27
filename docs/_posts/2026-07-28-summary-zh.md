---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 從 29 條內容中篩選出 8 條重要資訊。

---

1. [將 Bun 重寫為 Rust 的進展如何？](#item-1) ⭐️ 9.0/10
2. [Fastjson2 曝遠程代碼執行漏洞（RCE），現有版本尚未修復](#item-2) ⭐️ 9.0/10
3. [vllm-project/vllm 發布 v0.26.0 版本](#item-3) ⭐️ 8.0/10
4. [Kimi-K3 在 HuggingFace 上发布](#item-4) ⭐️ 8.0/10
5. [迪卡儂德國在其網站上新增 Wero 支付選項](#item-5) ⭐️ 8.0/10
6. [🤖 谷歌透露 Gemini 4 為迄今最雄心預訓練，預計年底發布](#item-6) ⭐️ 8.0/10
7. [中方駁美方擬制裁中國 AI 企業：美企同樣在蒸餾中國模型](#item-7) ⭐️ 8.0/10
8. [中國開始量產國產 DUV 光刻機 今年目標生產約 5 台](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [將 Bun 重寫為 Rust 的進展如何？](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 9.0/10

這篇部落格文章報導了 Bun 執行環境從 Zig 重寫為 Rust 的進展。重寫版本已在 Claude Code 中默默上線一個月，使用者幾乎沒有察覺。團隊正努力改善對 Node.js 測試的相容性，而 1.4 版本的發布將延遲直到這些測試通過。這項重大重寫顯示了 Bun 專案的技術方向轉變，並引發社群關於 LLM 輔助程式碼轉換的討論。

hackernews · tomlockwood · 7月27日 11:12 · [社區討論](https://news.ycombinator.com/item?id=49067854)

**標籤**: `#Bun`, `#Rust`, `#Rewrite`, `#JavaScript Runtime`, `#LLM`

---

<a id="item-2"></a>
## [Fastjson2 曝遠程代碼執行漏洞（RCE），現有版本尚未修復](https://mp.weixin.qq.com/s/LJaul1jNjK9pXRAkoUiMEA) ⭐️ 9.0/10

長亭科技於 7 月 27 日披露 Fastjson2 存在遠程代碼執行漏洞，攻擊者可透過惡意 JSON 數據繞過 AutoType 類型校驗並執行任意代碼，影響 2.0.62 及以前所有版本。項目維護者已確認該安全問題，但完整漏洞細節與利用代碼尚未公開，且目前所有已發布版本均無正式補丁。這是本月 fastjson1 之後的第二個嚴重漏洞，建議在修復版推出前徹底禁用 AutoType。此漏洞對依賴 Fastjson2 的 Java 應用構成極大安全風險，需密切關注官方更新。

telegram · zaihuapd · 7月27日 10:31

**標籤**: `#security`, `#vulnerability`, `#RCE`, `#Fastjson2`, `#Java`

---

<a id="item-3"></a>
## [vllm-project/vllm 發布 v0.26.0 版本](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 版本包含 411 次提交，來自 212 位貢獻者（其中 61 位是新貢獻者）。主要亮點包括：支援全新的 Inkling 模型系列，涵蓋基礎建模、CUDA 圖優化、Hopper FA4 相對注意力及推測解碼等完整堆疊；針對 DeepSeek-V4 進行跨供應商效能提升，包括專用路由內核、融合 topk 偏置及冗餘重複/複製移除等優化；新增透過 head_dtype 參數為生成模型啟用 fp32 lm_head，並擴展至 LoRA 路徑。此外，還有彈性注意力後端等改進。這些更新顯著提升了大型語言模型的推理效率與靈活性。

github · khluu · 7月27日 01:06

**標籤**: `#vLLM`, `#LLM inference`, `#model serving`, `#GPU optimization`, `#open-source`

---

<a id="item-4"></a>
## [Kimi-K3 在 HuggingFace 上发布](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 8.0/10

Kimi-K3 是 Moonshot AI 发布的一款拥有 3 万亿参数的混合专家模型，现已在 HuggingFace 上开源权重。该模型采用原生 mxfp4 精度，需要约 1.5TB 显存进行部署，社区讨论了其托管成本（如 Fireworks AI 定价为每百万 token 输入 3 美元）以及商业许可限制（年收入超过 2000 万美元需另行协商）。此次发布的最大亮点在于开源权重允许任何团队进行微调和定制，从而在特定数据集上获得更优性能并实现数据主权。这标志着大规模开源模型生态的重要进展。

hackernews · nateb2022 · 7月27日 06:18 · [社區討論](https://news.ycombinator.com/item?id=49065752)

**標籤**: `#large language model`, `#open-source AI`, `#Mixture-of-Experts`, `#model hosting`, `#AI licensing`

---

<a id="item-5"></a>
## [迪卡儂德國在其網站上新增 Wero 支付選項](https://www.sgieurope.com/e-commerce/decathlon-germany-launches-wero-payment-on-its-website/122397.article) ⭐️ 8.0/10

迪卡儂德國在其電商網站上新增了 Wero 支付方式，Wero 是一種基於 SEPA 即時轉帳系統的歐洲支付解決方案。此舉強化了歐洲在數位支付領域的自主性，減少對美國支付體系的依賴。社群討論指出，Wero 使用 QR 碼掃描即可在銀行應用中確認付款，流程快速無需等待重定向。然而，目前 Wero 僅支援 iOS 和 Android 裝置，無法透過電腦或瀏覽器使用，這限制了其便利性。總體而言，迪卡儂的採用對 Wero 的推廣具有指標性意義。

hackernews · doener · 7月27日 16:49 · [社區討論](https://news.ycombinator.com/item?id=49072310)

**標籤**: `#Wero`, `#payments`, `#Europe`, `#e-commerce`

---

<a id="item-6"></a>
## [🤖 谷歌透露 Gemini 4 為迄今最雄心預訓練，預計年底發布](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

谷歌 CEO 桑達爾·皮查伊在 2026 年第二季度財報會議上透露，下一代大模型 Gemini 4 已經開始訓練，這是該公司迄今為止最具雄心的預訓練項目。他表示，谷歌將優先分配算力給前沿 AGI 研發，以確保 Gemini 4 在發佈時仍處於行業前沿。按往年節奏，該模型預計在今年 11 月或 12 月發佈。此外，Gemini 3.x Flash 系列將保持幾乎每月一次的迭代頻率，重點提升智能編碼等能力。

telegram · zaihuapd · 7月27日 04:06

**標籤**: `#Gemini 4`, `#Google`, `#AI`, `#large language model`, `#pre-training`

---

<a id="item-7"></a>
## [中方駁美方擬制裁中國 AI 企業：美企同樣在蒸餾中國模型](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 8.0/10

中國商務部於 7 月 27 日反駁美國以「蒸餾」美國前沿模型、竊取知識產權等理由調查並制裁中國人工智能企業的計劃，稱相關指控缺乏事實和法律依據。商務部指出，模型蒸餾是業界廣泛使用的技術，部分美國企業也在研發和訓練中使用中國模型，近 200 家美國初創企業已呼籲政府不要限制訪問中國開源模型。中方敦促美方停止抹黑和制裁威脅，並表示將採取必要措施維護中國企業合法權益。此事件凸顯中美在 AI 領域的技術競爭與政策對抗，可能影響全球 AI 開源生態和技術交流。

telegram · zaihuapd · 7月27日 11:01

**標籤**: `#AI policy`, `#model distillation`, `#US-China relations`, `#tech sanctions`, `#Chinese government`

---

<a id="item-8"></a>
## [中國開始量產國產 DUV 光刻機 今年目標生產約 5 台](https://www.theinformation.com/articles/china-starts-mass-producing-homegrown-duv-chipmaking-tools-advance-local-chip-industry) ⭐️ 8.0/10

中國已開始大規模生產自主研發的浸沒式深紫外（DUV）光刻機，上海一家國企計劃今年生產約 5 台，2027 年約 20 台，將交付中芯國際、華虹半導體等國內廠商。雖然該設備在性能和可靠性上仍落後於 ASML，且部分關鍵零部件依賴日本進口，但量產標誌著中國在半導體自主化進程中的重要一步。短期內難以直接威脅 ASML 的市場主導地位，但如果產量持續增加，加上西方出口限制收緊，可能逐步侵蝕 ASML 在中國市場的份額。此消息導致 ASML 股價一度跌超 6%，顯示市場對中國半導體自給能力提升的擔憂。

telegram · zaihuapd · 7月27日 14:10

**標籤**: `#semiconductor`, `#lithography`, `#China`, `#ASML`, `#supply chain`

---
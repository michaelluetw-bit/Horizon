# Horizon 每日快遞 - 2026-08-02

> 從 37 條內容中篩選出 6 條重要資訊。

---

1. [🤖 OpenAI Astra 在十項長期數學難題上取得突破](#item-1) ⭐️ 10.0/10
2. [deepseek-ai/DeepSeek-V4-Flash-0731 模型發布](#item-2) ⭐️ 8.0/10
3. [無狀態 MCP 重新引起我的興趣（並啟發了 mcp-explorer 和 datasette-mcp）](#item-3) ⭐️ 8.0/10
4. [視覺語言模型可能在基準測試中表現良好，但會悄悄抹除有意義的術語並引入幻覺偏見 (P)](#item-4) ⭐️ 8.0/10
5. [圍棋神經網路的內部有多對稱？](#item-5) ⭐️ 8.0/10
6. [微軟確認今年推出 Copilot「超級應用」](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [🤖 OpenAI Astra 在十項長期數學難題上取得突破](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 10.0/10

OpenAI 宣佈其下一代模型 Astra 的內部版本在十個長期未解決的數學與理論電腦科學問題上取得新成果，涵蓋高維球體堆積、非索菲克群、Connes 剛性猜想反證、算術電路下界、量子並行重複、最近向量問題硬度及多色 Ramsey 數等。這些問題多年未見突破，模型生成論證的 token 成本約二千美元。人類與模型協作整理成論文，並在 Lean 中形式化驗證，彰顯 AI 作為研究協作者的潛力。OpenAI 強調應如實反映成果來源，並期望數學界深入審視這些結果，代表 AI 驅動數學研究的重要里程碑。

telegram · zaihuapd · 8月1日 07:59

**標籤**: `#OpenAI`, `#AI Research`, `#Mathematics`, `#Formal Verification`, `#Astra`

---

<a id="item-2"></a>
## [deepseek-ai/DeepSeek-V4-Flash-0731 模型發布](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 發布了最新的 V4 系列模型 V4-Flash-0731，主打大幅增強的代理（agentic）能力。該模型擁有 3040 億參數，體積約 167GB，但在性能上表現出色，甚至超越了 4280 億參數的 MiniMax M3。其定價為每百萬輸入 tokens 0.14 美元、輸出 0.27 美元，是目前性價比最高的模型之一。對 AI 開發者和研究人員而言，這是一個值得關注的重要發布，可能推動更高效的 AI 應用發展。

rss · Simon Willison · 7月31日 23:59

**標籤**: `#DeepSeek`, `#AI模型`, `#大型語言模型`, `#性價比`, `#代理能力`

---

<a id="item-3"></a>
## [無狀態 MCP 重新引起我的興趣（並啟發了 mcp-explorer 和 datasette-mcp）](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

本文介紹 Model Context Protocol（MCP）2.0 規格，其中最核心的變更是「無狀態 MCP」（Stateless MCP），允許伺服器在不維持持久連線的狀態下提供工具，大幅簡化部署與擴充性。這項更新是 MCP 自 2024 年推出以來最重大的改變，可能影響所有基於 LLM 的代理工具生態系統。作者 Simon Willison 基於此特性開發了 mcp-explorer 和 datasette-mcp 兩個工具，展示無狀態設計的實際應用價值。整體而言，這標誌著 MCP 從早期熱潮後沈寂，再度成為代理開發的重要基礎。

rss · Simon Willison · 7月31日 23:13

**標籤**: `#MCP`, `#Model Context Protocol`, `#AI Agents`, `#Protocol`, `#Simon Willison`

---

<a id="item-4"></a>
## [視覺語言模型可能在基準測試中表現良好，但會悄悄抹除有意義的術語並引入幻覺偏見 (P)](https://www.reddit.com/r/MachineLearning/comments/1vcipzz/vlms_can_score_well_on_benchmarks_while_silently/) ⭐️ 8.0/10

此研究發現，在胸部 X 光報告生成任務中，現有評估指標存在嚴重缺陷：它們會獎勵重複模板、缺乏臨床術語或內容為「正常」的報告，導致高分報告可能缺乏臨床價值。模型會悄悄抹除罕見但具有臨床意義的術語，使生成報告看起來重複且枯燥，甚至失去臨床實用性。為了解決此問題，作者提出一個框架，專門用來量化術語抹除與偏見引入的程度，藉此更準確地評估模型效能。這項研究對於醫療 AI 的可信度與評估標準具有重要影響，並提醒研究人員不要過度依賴傳統基准指標。

reddit · r/MachineLearning · /u/ade17_in · 8月1日 09:27

**標籤**: `#VLM`, `#Radiology Report Generation`, `#Evaluation Metrics`, `#Medical AI`, `#Bias`

---

<a id="item-5"></a>
## [圍棋神經網路的內部有多對稱？](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

這項研究針對作者維護的開源圍棋程式 KataGo，探討其訓練出的超人類等級神經網路，在僅使用隨機旋轉資料增強、而非結構性強制對稱的情況下，是否會自動學到與方向無關的內部表徵。作者透過分析網路在不同棋盤方向下的活化模式，比較表徵的相似度，發現網路確實發展出部分對稱概念，但仍存在方向依賴性。此研究有助於理解深度模型如何利用資料擴增來學習不變性，對詮釋性與泛化研究具有參考價值。

reddit · r/MachineLearning · /u/icosaplex · 8月1日 16:18

**標籤**: `#interpretability`, `#neural-networks`, `#Go`, `#symmetry`, `#KataGo`

---

<a id="item-6"></a>
## [微軟確認今年推出 Copilot「超級應用」](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

微軟執行長納德拉在財報電話會議中確認，將在今年推出整合聊天、程式開發與 AI 代理（agentic）能力的 Copilot 超級應用，同時涵蓋消費者與商用場景。該應用預計合併 Copilot 聊天機器人、GitHub Copilot、Copilot Cowork 及 Autopilot 系統，標誌著微軟從單一工具向整合式 AI 工作平台的轉型。此舉與 OpenAI 推出 ChatGPT Work 的趨勢一致，顯示科技巨頭正加速打造統一 AI 入口。微軟上季度營收達 900 億美元，主要由 AI 與雲業務驅動，這款超級應用可能進一步鞏固其生態系統並重塑用戶與 AI 互動的方式。

telegram · zaihuapd · 8月1日 13:18

**標籤**: `#Microsoft`, `#Copilot`, `#AI`, `#super app`, `#cloud`

---


# Horizon 每日快遞 - 2026-07-21

> 從 36 條內容中篩選出 13 條重要資訊。

---

1. [Fastjson 1.x 被爆出無需 gadget 的高危 RCE 漏洞](#item-1) ⭐️ 10.0/10
2. [中國的開源權重 AI 策略正在勝出](#item-2) ⭐️ 8.0/10
3. [駭客刪除羅馬尼亞土地登記資料庫](#item-3) ⭐️ 8.0/10
4. [我們如何測量 arXiv 上的人工智慧寫作，以及測量在哪裡失效](#item-4) ⭐️ 8.0/10
5. [Kimi K3、Qwen 3.8 與 Anthropic 的（潛在）瓦解](#item-5) ⭐️ 8.0/10
6. [小米機械人-1](#item-6) ⭐️ 8.0/10
7. [引用山姆·奧特曼](#item-7) ⭐️ 8.0/10
8. [探索無回放緩衝區的持續學習：我們使用動態任務相似性路由的發現(P)](#item-8) ⭐️ 8.0/10
9. [Hugging Face 披露 AI 智能體攻擊事件，商業大模型拒絕協助取證](#item-9) ⭐️ 8.0/10
10. [因 Kimi K3 模型表現強勁，川普政府被曝醞釀限制美國企業使用相對物美價廉的中國開放權重模型](#item-10) ⭐️ 8.0/10
11. [美軍常用 App 被指嵌入中俄代碼 引發國家安全擔憂](#item-11) ⭐️ 8.0/10
12. [歐盟擬向美開放生物識別數據以換取免簽待遇](#item-12) ⭐️ 8.0/10
13. [智譜建成全國產芯片大型數據中心](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Fastjson 1.x 被爆出無需 gadget 的高危 RCE 漏洞](https://x.com/k_firsov/status/2078872293745570032) ⭐️ 10.0/10

安全研究人員 Kirill Firsov 揭露 Fastjson 1.2.68 至 1.2.83 版本存在一項高危遠端程式碼執行漏洞，該漏洞無需開啟 autoType 依賴，也無需依賴 classpath 中的 gadget，在 JDK 8、17、21 等版本上均可利用。由於 Fastjson 1.x 已於 2024 年 10 月停止維護，官方極不可能提供安全修補，唯一補救措施是升級到 Fastjson 2 或啟用安全模式（SafeMode）。此漏洞影響廣泛，建議所有使用 Fastjson 1.x 的項目立即排查並遷移至仍在維護的 JSON 解析庫，以避免遭受攻擊。

telegram · zaihuapd · 7月20日 14:32

**標籤**: `#安全漏洞`, `#远程代码执行`, `#Fastjson`, `#Java`, `#依赖安全`

---

<a id="item-2"></a>
## [中國的開源權重 AI 策略正在勝出](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

本文探討中國在人工智慧領域採用開放權重模型的策略，並指出這種策略正在取得優勢，相較於美國的封閉式專有模型。作者引用數據顯示 80%的中國新創公司使用中國的開放模型，但社群評論對此提出質疑，認為美國模型如 Llama 仍然主導。整體而言，開放權重模型在成本和可及性上的優勢可能最終使其佔據主導地位，但硬體成本和推理費用仍是挑戰。此討論反映了 AI 領域中開放與封閉路線的持續競爭。

hackernews · benwerd · 7月20日 14:21 · [社區討論](https://news.ycombinator.com/item?id=48979269)

**標籤**: `#AI`, `#open-weight models`, `#China`, `#open source`, `#AI strategy`

---

<a id="item-3"></a>
## [駭客刪除羅馬尼亞土地登記資料庫](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

一名駭客入侵並刪除了羅馬尼亞國家土地登記處的整個資料庫，導致所有權記錄面臨遺失風險。然而，官方在事後迅速恢復了網站，並表示擁有離線備份，正在從頭重建整個網絡，並將應用程式遷移至政府雲端。此事件引發了對政府資訊安全及可能存在的腐敗問題的廣泛討論，社群評論指出政府可能將合約交給未有實際安全措施的親信，導致此次駭客攻擊。該事件突顯了關鍵基礎設施的脆弱性以及強健離線備份的重要性。

hackernews · speckx · 7月20日 13:28 · [社區討論](https://news.ycombinator.com/item?id=48978605)

**標籤**: `#cybersecurity`, `#data breach`, `#Romania`, `#land registry`, `#hacker`

---

<a id="item-4"></a>
## [我們如何測量 arXiv 上的人工智慧寫作，以及測量在哪裡失效](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

這篇文章介紹了一項研究，該研究使用校準過的檢測器來識別 arXiv 論文中的 AI 生成文字。結果顯示，自 ChatGPT 發布後，被標記為 AI 寫作的論文比例急劇上升：到 2026 年 1 月約有 39% 的論文被標記，其中計算機科學領域更高達 65%，而數學領域則幾乎沒有變化。社群評論討論了檢測方法的準確性，包括可能將人類寫作誤判為 AI 寫作的情況，引發了關於學術誠信和 AI 使用影響的深入辯論。

hackernews · dopamine_daddy · 7月20日 16:36 · [社區討論](https://news.ycombinator.com/item?id=48981206)

**標籤**: `#AI writing`, `#arXiv`, `#detection`, `#academic integrity`, `#ChatGPT`

---

<a id="item-5"></a>
## [Kimi K3、Qwen 3.8 與 Anthropic 的（潛在）瓦解](https://www.emergingtrajectories.com/lh/frontier-lab-economics/) ⭐️ 8.0/10

本文探討近期開源權重模型（Kimi K3 和 Qwen 3.8）的發布，以及 Anthropic 可能面臨的戰略危機。社群討論聚焦於：前沿模型逐漸商品化，且競爭可能轉向專用晶片（ASIC）的部署速度；同時，Anthropic 因產品發布策略（如 Claude Design）引發合作夥伴信任問題。整體而言，開源模型與封閉模型的經濟學差異正在重塑產業格局，而 Anthropic 的內部動盪可能加速其競爭地位下滑。

hackernews · cl42 · 7月20日 15:13 · [社區討論](https://news.ycombinator.com/item?id=48980019)

**標籤**: `#AI`, `#open-weight models`, `#Anthropic`, `#frontier labs`, `#AI economics`

---

<a id="item-6"></a>
## [小米機械人-1](https://robotics.xiaomi.com/xiaomi-robotics-1.html) ⭐️ 8.0/10

小米展示了一款能夠完成複雜家務（如折疊衣物）的機器人，這是機器人技術在家庭服務領域的重要進展。影片中的機器人展示了雙臂協調、移動身體以及處理柔性物體等突破性能力，解決了多年來機器人學中的經典難題。這項技術的開源模型（如免費啤酒）可能加速家庭機器人的普及，對機器人產業具有深遠影響。

hackernews · ilreb · 7月20日 04:45 · [社區討論](https://news.ycombinator.com/item?id=48974454)

**標籤**: `#robotics`, `#AI`, `#manipulation`, `#deep learning`, `#hardware`

---

<a id="item-7"></a>
## [引用山姆·奧特曼](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 8.0/10

這封由山姆·奧特曼於 2022 年 10 月發給 OpenAI 董事會的電子郵件（在馬斯克訴奧特曼案中曝光）揭示了 OpenAI 的開源策略。郵件中表示，公司計劃儘快發布一個能力接近 GPT-3、可在消費者硬體上本地運行的語言模型，目的是搶在 Stability 等競爭對手之前推出。奧特曼認為此舉有助於阻止他人發布類似強大模型，並增加新項目融資難度。這份內部文件提供了 OpenAI 關於開源和模型發布策略的直接證據，對理解 AI 行業的競爭動態具有重要意義。

rss · Simon Willison · 7月20日 03:47

**標籤**: `#ai-ethics`, `#sam-altman`, `#generative-ai`, `#open-source`, `#ai-strategy`

---

<a id="item-8"></a>
## [探索無回放緩衝區的持續學習：我們使用動態任務相似性路由的發現(P)](https://www.reddit.com/r/MachineLearning/comments/1v1rmbb/exploring_continual_learning_without_replay/) ⭐️ 8.0/10

本文介紹了一個名為 Coincidex 的開源持續學習框架，其核心方法是用動態任務相似性路由層代替傳統的回放緩衝區，以避免災難性遺忘。該方法在任務流中動態計算相似性矩陣並路由數據路徑，從而無需存儲歷史樣本，減少了記憶體和隱私開銷。作者通過基準測試展示了該方法的成功與不足，例如在乾淨的任務邊界下表現良好，但面臨順序漂移等挑戰。這項工作為持續學習提供了新的方向，尤其對隱私敏感的場景具有重要意義，而開源框架則促進了社群驗證與改進。

reddit · r/MachineLearning · /u/theawkwardbong · 7月20日 17:13

**標籤**: `#continual learning`, `#machine learning`, `#catastrophic forgetting`, `#dynamic routing`, `#open-source`

---

<a id="item-9"></a>
## [Hugging Face 披露 AI 智能體攻擊事件，商業大模型拒絕協助取證](https://huggingface.co/blog/security-incident-july-2026) ⭐️ 8.0/10

Hugging Face 於 2026 年 7 月遭遇一起由自主 AI 智能體框架驅動的網路攻擊。攻擊者利用數據集處理流程中的兩處程式碼執行漏洞入侵內部系統，於週末期間執行數萬次操作，橫向移動至多個內部集群，竊取部分內部數據集和服務憑證。公司已修復漏洞並輪換憑證，事件響應中團隊最初使用商業大模型 API 進行日誌分析時遭安全攔截，後改用本地部署的 GLM 5.2 完成超過 1.7 萬條攻擊記錄的取證。此事件凸顯 AI 驅動攻擊的威脅及本地模型在安全防護中的潛力。

telegram · zaihuapd · 7月20日 10:41

**標籤**: `#安全事件`, `#AI智能体`, `#Hugging Face`, `#GLM`, `#取证`

---

<a id="item-10"></a>
## [因 Kimi K3 模型表現強勁，川普政府被曝醞釀限制美國企業使用相對物美價廉的中國開放權重模型](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) ⭐️ 8.0/10

根據 Axios 報導，由於中國開放權重模型 Kimi K3 的強勢崛起，川普政府正重新推動限制美國企業使用中國 AI 模型。知情人士透露，政府可能不會直接封禁，而是透過採購規則、實體清單威脅和輿論等軟性手段，讓美國企業放棄使用性能已接近美國產品的中國開源模型。白宮外部 AI 顧問 David Sacks 批評 OpenAI 和 Anthropic 等閉源巨頭試圖藉政府之手消滅開源競爭，認為 AI 政策正處於關鍵轉折點。此舉若實施，將對全球 AI 開源生態和科技供應鏈產生深遠影響。

telegram · zaihuapd · 7月20日 11:49

**標籤**: `#AI regulation`, `#open-source AI`, `#US-China tech`, `#Kimi K3`, `#geopolitics`

---

<a id="item-11"></a>
## [美軍常用 App 被指嵌入中俄代碼 引發國家安全擔憂](https://www.wired.com/story/apps-marketed-to-us-troops-are-shipping-chinese-and-russian-code/) ⭐️ 8.0/10

普渡大學等機構研究人員分析了面向美軍推廣的 220 多款應用，發現其中近三分之二嵌入了來自中國、俄羅斯、伊朗等國的第三方代碼，包括華為的 SDK。雖然目前未觀察到數據實際流向華為伺服器，但這些 SDK 具備遠端更新能力，存在潛伏代碼被激活的風險。調查中 103 名軍人關聯人員中，76%至 83%對此表示極度不安。此事凸顯移動應用供應鏈安全的重要性，尤其是在軍事人員等敏感群體中的隱私和威脅防範。

telegram · zaihuapd · 7月20日 13:42

**標籤**: `#国家安全`, `#供应链安全`, `#第三方代码`, `#华为SDK`, `#移动应用安全`

---

<a id="item-12"></a>
## [歐盟擬向美開放生物識別數據以換取免簽待遇](https://edri.org/our-work/the-eu-is-about-to-sell-our-most-sensitive-data-to-the-us-for-visa-free-travel/) ⭐️ 8.0/10

歐盟委員會正與特朗普政府敲定一項「增強邊境安全夥伴關係」框架協議，美國要求訪問歐盟成員國的生物識別數據庫，作為其公民免簽赴美的條件。歐洲數字權利組織（EDRi）稱，洩露的草案顯示歐盟幾乎全盤接受了美方對信息無限制訪問的要求，可能導致生物識別數據及基於政治觀點的「風險指標」被系統性傳輸至美方。此舉對公民隱私和表達自由構成潛在威脅，EDRi 呼籲歐盟抵制美方施壓，拒絕以敏感數據換取免簽待遇。

telegram · zaihuapd · 7月20日 15:08

**標籤**: `#数据隐私`, `#欧盟`, `#生物识别`, `#免签政策`, `#国际协议`

---

<a id="item-13"></a>
## [智譜建成全國產芯片大型數據中心](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 8.0/10

智譜公司完成了一座全部採用國產芯片的大型數據中心建設，功率達 1 吉瓦，足以同時為約 75 萬戶家庭供電。該中心將用於支持其前沿 GLM 平台的開發。目前智譜已建成或運營多個擁有超萬枚芯片的計算集群，此設施是中國 AI 實驗室建造的最大規模之一。這不僅展示了國產芯片在大規模 AI 訓練中的可行性，也為中國 AI 產業的自主可控提供了關鍵基礎設施支持。

telegram · zaihuapd · 7月20日 15:43

**標籤**: `#国产芯片`, `#数据中心`, `#AI基础设施`, `#智谱`, `#GLM`

---


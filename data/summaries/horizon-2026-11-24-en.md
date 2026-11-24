# Horizon Daily - 2026-11-24

> From 31 items, 10 important content pieces were selected

---

**Technology News**
1. [Ladybird releases first browser alpha](#item-tech-news-1) ⭐️ 8.0/10
2. [Paper Claims VP and VNP Differ Over Every Field](#item-tech-news-2) ⭐️ 8.0/10
3. [Nvidia Reinstates Jensen Huang as CEO](#item-tech-news-3) ⭐️ 7.0/10
4. [GLM-5.4 Introduces Z.ai’s First Looped Transformer](#item-tech-news-4) ⭐️ 7.0/10
5. [Codex2api Releases Allegedly Compromised in Supply-Chain Attack](#item-tech-news-5) ⭐️ 7.0/10
6. [Huawei Reports 100 Million Devices Running HarmonyOS 5–7](#item-tech-news-6) ⭐️ 7.0/10
7. [SpaceX rents AI computing capacity to Anthropic and Google](#item-tech-news-7) ⭐️ 7.0/10
8. [Mozilla and Shopify Urge EU Probe of iPhone Browser Restrictions](#item-tech-news-8) ⭐️ 7.0/10
9. [GPUI is getting its own repository](#item-tech-news-9) ⭐️ 6.0/10
10. [Stalwart Claims Drop-In Exchange Replacement](#item-tech-news-10) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Ladybird releases first browser alpha](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

Ladybird’s first alpha is available to install on macOS and Linux without compiling it from source. The browser implements its own HTML parsing, CSS, layout, JavaScript and WebAssembly components, while using external libraries for some functions. The project cautions that some sites will not work and the browser will sometimes crash.

hackernews · janvdberg · Nov 23, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50614249)

**「Background」** Ladybird grew out of SerenityOS and implements its own HTML, CSS and JavaScript components, while using external libraries for tasks such as graphics and text shaping. Before the alpha, its developers reported using AI coding agents to fill gaps in web-platform functionality, contributing to 75,650 additional test passes in October.

**「Compatibility」** Testers can report broken sites from within the browser and choose whether to send crash reports. In the source author’s testing, a WebAssembly video compressor and Pyodide REPL worked, but Datasette Lite failed on a service-worker function.

**「Early testing」** Two commenters reported that the sites they tried rendered successfully, though one noticed slightly jerky scrolling. These reports are anecdotal and do not establish broad compatibility.

**Tags**: `#Ladybird`, `#web browsers`, `#browser engines`, `#web compatibility`

---

<a id="item-tech-news-2"></a>
### [Paper Claims VP and VNP Differ Over Every Field](https://github.com/anthropics/formal-math/tree/main/vp-vnp) ⭐️ 8.0/10

A paper in Anthropic’s formal-math repository claims that the algebraic complexity classes VP and VNP are distinct over every field. The supplied material does not establish whether the claimed proof has been independently assessed.

hackernews · mikeryan52 · Nov 23, 22:09 · [Discussion](https://news.ycombinator.com/item?id=50620102)

**「Background」** VP consists of polynomial families computable by polynomial-size arithmetic circuits, while VNP also includes families expressible as sums over exponentially many evaluations of efficiently computable polynomials. The VP versus VNP question is an algebraic analogue of P versus NP; separating VP from VNP would not by itself prove P differs from NP.

**「Discussion」** One commenter reported rerunning the checks and verifying that the stated theorems imply a restatement of the claimed result. Another quoted the paper as saying its authors had not analyzed how the work relates to the relativization and algebrization barriers.

**Tags**: `#algebraic complexity`, `#VP vs VNP`, `#formal verification`, `#computational complexity`

---

<a id="item-tech-news-3"></a>
### [Nvidia Reinstates Jensen Huang as CEO](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) ⭐️ 7.0/10

Nvidia’s board unanimously reinstated Jensen Huang as president, CEO and a board member, effective immediately; interim CEO Colette Kress will remain chief financial officer. The board said it concluded, after receiving input from senior US government officials, that Huang’s return posed no national security risk. It said an independent-director committee would continue investigating reports that Huang was targeted by foreign intelligence, while the company established a national security and export controls committee and began seeking a chief compliance officer. Bloomberg separately reported, citing anonymous sources, that the board acted without consulting executives and faced political pressure from President Trump; Nvidia had not confirmed those claims.

hackernews · jaz · Nov 23, 14:00 · [Discussion](https://news.ycombinator.com/item?id=50611576)

**「Background」** Horizon’s November 14 digest reported that Nvidia’s management page had listed Colette Kress as interim CEO and Jensen Huang as founder, with his biography describing his CEO role in the past tense. That report did not explain the change; the current account says Kress will remain CFO after Huang’s reinstatement.

**「Community discussion」** One commenter argued that the board should have communicated its evidence and succession plans more clearly, regardless of whether its concerns were conclusive. Another cautioned against assuming that Nvidia had committed a crime, arguing that the public evidence did not establish one.

<details><summary>References</summary>
<ul>
<li><a href="https://investor.nvidia.com/governance/management-team/default.aspx">2026-11-14 — Nvidia Reportedly Lists Colette Kress as Interim CEO</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI industry`, `#semiconductors`, `#corporate governance`

---

<a id="item-tech-news-4"></a>
### [GLM-5.4 Introduces Z.ai’s First Looped Transformer](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 7.0/10

Z.ai has released GLM-5.4, a coding model that repeatedly runs a group of weight-shared transformer layers to increase effective network depth without increasing parameter count. Simon Willison reports that the model is not available as open weights and currently requires a Coding Plan subscription rather than regular API access; he used its key with Z.ai’s OpenAI-compatible Responses API. In his informal image-generation test, Willison judged GLM-5.4’s results similar in quality to GLM-5.3’s.

rss · Simon Willison · Nov 23, 23:40

**「Background」** Horizon’s August 29 digest reported that Z.ai had released GLM-5.3 as open weights; Willison says GLM-5.4 is not yet available that way.

**「Developer access」** Developers currently need a Z.ai Coding Plan subscription to access GLM-5.4; it is not available through the regular API or as open weights. A Coding Plan key works with Z.ai’s OpenAI-compatible Responses API, and Simon Willison’s llm-glm plugin supports the model.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.3">2026-08-29 — GLM-5.3 is now open-weight</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#coding models`, `#transformer architecture`, `#weight sharing`

---

<a id="item-tech-news-5"></a>
### [Codex2api Releases Allegedly Compromised in Supply-Chain Attack](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 7.0/10

A Telegram report alleges that an attacker compromised the Codex2api author’s account and pushed tags bypassing the main branch, producing backdoored releases. The report claims v3.1.11 removed authentication, allowing remote command execution without a password. It also alleges that a workflow leaked 16 GitHub Actions secrets and affected at least 21 repositories under the same account; these claims remain unverified.

telegram · zaihuapd · Nov 23, 11:21

**「Background」** Git tags identify specific code revisions and can trigger release builds without changes to a repository’s main branch. GitHub Actions secrets are credentials stored for use by automated workflows.

**「Advice for users」** The report advises users who installed or updated to versions 3.1.10–3.1.12 to stop using them, revert to 3.1.9, and rotate relevant credentials, including GitHub tokens, SSH keys, database credentials, and DeepSeek keys.

**Tags**: `#supply-chain-security`, `#codex2api`, `#github-actions`, `#credential-exposure`

---

<a id="item-tech-news-6"></a>
### [Huawei Reports 100 Million Devices Running HarmonyOS 5–7](https://www.xinhuanet.com/20261124/68842538167d4e59a875056d5eb885ad/c.html) ⭐️ 7.0/10

Huawei says more than 100 million phones, tablets and computers now run HarmonyOS 5, 6 or 7. The company also reports more than 460,000 applications and services available for HarmonyOS and over 12 million registered developers. It says the open-source OpenHarmony project has attracted more than 14,000 contributors and produced over 120 industry distributions.

telegram · zaihuapd · Nov 24, 01:46

**「Background」** Huawei first introduced HarmonyOS in 2019 and released native HarmonyOS in October 2024.

**Tags**: `#HarmonyOS`, `#operating systems`, `#developer ecosystems`, `#Huawei`

---

<a id="item-tech-news-7"></a>
### [SpaceX rents AI computing capacity to Anthropic and Google](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html) ⭐️ 7.0/10

SpaceX has earned billions of dollars a month since May by renting data-center computing capacity to Anthropic, Google and other companies, The New York Times reported. Three people familiar with the matter said Elon Musk told employees that SpaceX was behind in AI and that renting out computing capacity was more profitable than using it internally. They also said Musk warned that employees who wasted GPUs would be asked to leave. The account does not specify how much computing capacity was rented or break down the revenue.

telegram · zaihuapd · Nov 24, 02:06

**「Background」** Horizon’s August 6 digest reported that Musk had committed SpaceX to Nvidia’s AI architecture, including planned Vera Rubin deployments for ground and space computing. The current report describes another use for its data-center capacity: renting it to other AI companies.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/elon-musk-commits-spacex-exclusively-to-nvidia-gpus-citing-theyre-the-best/">2026-08-06 — 🤖 马斯克宣布 SpaceX 将独家采用英伟达 AI 架构</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#AI算力`, `#数据中心`, `#Anthropic`, `#Google`

---

<a id="item-tech-news-8"></a>
### [Mozilla and Shopify Urge EU Probe of iPhone Browser Restrictions](https://appleinsider.com/articles/26/11/23/eu-urges-to-challenge-apples-grip-on-iphone-browsers?utm_source=rss) ⭐️ 7.0/10

Organizations including Mozilla and Shopify have written to the European Commission asking it to investigate Apple’s restrictions on iPhone browsers. They say the signatories represent roughly 45,000–55,000 EU businesses and organizations, and that signatures are being collected through December 3, 2026. Although Apple permits alternative browser engines in the EU under the Digital Markets Act, the letter alleges that technical and legal requirements prevent vendors from moving existing EU users away from WebKit. The signatories estimate that, if half of native iOS apps moved to the web, EU businesses could save €11 billion annually in development costs and €1.3 billion in App Store fees; the source does not establish that an investigation has been opened.

telegram · zaihuapd · Nov 24, 03:02

**「Background」** A browser engine is the software that renders web pages; WebKit is Apple’s engine. Under the EU’s Digital Markets Act, Apple permits competing iPhone browsers in the EU to use their own engines.

**Tags**: `#Apple`, `#browser engines`, `#EU regulation`, `#web apps`, `#antitrust`

---

<a id="item-tech-news-9"></a>
### [GPUI is getting its own repository](https://github.com/zed-industries/gpui) ⭐️ 6.0/10

GPUI, the Rust GUI framework associated with the Zed editor, is getting its own GitHub repository. The supplied announcement does not describe technical changes or new capabilities.

hackernews · EvilGoose · Nov 23, 20:52 · [Discussion](https://news.ycombinator.com/item?id=50619103)

**「Background」** GPUI is a Rust UI framework from Zed Industries that uses the GPU to render interfaces. It has been housed in the Zed editor’s repository.

**「Community discussion」** One commenter said GPUI’s location inside the editor repository had made it feel awkward to use separately. Others praised GPUI Kit’s components and shared positive experiences with the alternative Rust GUI framework egui.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=OHU-Y93eCs8">First look at the new Rust GPUI framework from Zed ! - YouTube</a></li>

</ul>
</details>

**Tags**: `#GPUI`, `#Rust`, `#GUI frameworks`, `#open source`

---

<a id="item-tech-news-10"></a>
### [Stalwart Claims Drop-In Exchange Replacement](https://stalw.art/blog/microsoft-exchange-replacement/) ⭐️ 6.0/10

Stalwart claims its mail server is now a drop-in replacement for Microsoft Exchange. The available material does not specify compatibility, availability or conditions, so the scope of the replacement cannot be assessed.

hackernews · shaunpud · Nov 23, 22:32 · [Discussion](https://news.ycombinator.com/item?id=50620349)

**「Background」** Microsoft Exchange provides email services for organizations. Clients such as Outlook can communicate with Exchange using Microsoft’s MAPI protocol, making protocol compatibility relevant when replacing the server.

**「Community discussion」** One commenter said Stalwart’s regular and open-source plans lack the tamper-resistant archiving they believe German businesses need for tax compliance. Another argued that supporting Microsoft-oriented protocols may ease migration and licensing costs but perpetuate protocol lock-in.

**Tags**: `#Stalwart`, `#Microsoft Exchange`, `#email servers`, `#open source`

---


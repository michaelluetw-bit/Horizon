---
layout: default
title: "Horizon Summary: 2026-11-27 (EN)"
date: 2026-11-27
lang: en
---

> From 36 items, 10 important content pieces were selected

---

**Technology News**
1. [FCC Approves SpaceX’s Starmind Satellite Data Center Constellation](#item-tech-news-1) ⭐️ 8.0/10
2. [Nvidia Halts AI Server Shipments to Four Southeast Asian Countries](#item-tech-news-2) ⭐️ 8.0/10
3. [Minipg Packages PostgreSQL as a Single Executable](#item-tech-news-3) ⭐️ 7.0/10
4. [Shorter Lean Verification Related to Anthropic’s GRH Work](#item-tech-news-4) ⭐️ 7.0/10
5. [Huawei Plans to Present HBM Research Claiming Double Data-Pin Density](#item-tech-news-5) ⭐️ 7.0/10
6. [China Sets 2030 Network Goal and Plans 6G Construction](#item-tech-news-6) ⭐️ 7.0/10
7. [Neuralink cleared to start pivotal ALS implant trial](#item-tech-news-7) ⭐️ 7.0/10
8. [Netherlands Opposes Proposed US Curbs on ASML Sales to China](#item-tech-news-8) ⭐️ 7.0/10
9. [GLM-5.5 and Kimi K4 Releases Could Be Delayed](#item-tech-news-9) ⭐️ 7.0/10
10. [Cloudflare Investigates Dashboard and API Disruption](#item-tech-news-10) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [FCC Approves SpaceX’s Starmind Satellite Data Center Constellation](https://www.geekwire.com/2026/fcc-clears-spacex-million-satellites-starmind-data-center/) ⭐️ 8.0/10

The FCC has reportedly approved SpaceX to deploy up to one million Starmind satellites for an orbital data-processing network at altitudes of 500 to 1,002 kilometers. The authorization requires the first satellite to be operational by 2033 and the full constellation by 2040. Conditions include communications backup, regular progress reports and a detailed orbital-debris mitigation plan; the FCC rejected objections from Amazon, Viasat and the American Astronomical Society.

telegram · zaihuapd · Nov 26, 04:45

**「Background」** An orbital data center would process computing workloads on satellites and transmit results back to Earth. Horizon’s August 26 digest reported that SpaceX planned to send an Nvidia Vera Rubin NVL72 system into orbit in 2027 to test space-based AI data center technology; the Starmind authorization concerns a proposed satellite network for orbital processing.

**「Deployment conditions」** SpaceX must meet the operational deadlines and comply with the reporting and debris-mitigation conditions to proceed under the authorization; approval does not mean the satellites have been deployed.

<details><summary>References</summary>
<ul>
<li><a href="https://interestingengineering.com/space/spacex-million-satellites-data-centers-fcc">SpaceX gets FCC approval for one million space data center ...</a></li>
<li><a href="https://www.theregister.com/off-prem/2026/08/25/spacex-claims-it-will-put-a-vera-rubin-nvl72-rack-scale-system-into-orbit-next-year/5292067">2026-08-26 — SpaceX 计划明年将英伟达 Vera Rubin NVL72 送入太空，测试轨道 AI 计算</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#在轨数据中心`, `#卫星星座`, `#FCC`, `#轨道碎片`

---

<a id="item-tech-news-2"></a>
### [Nvidia Halts AI Server Shipments to Four Southeast Asian Countries](https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370) ⭐️ 8.0/10

Nvidia has asked manufacturing partners to pause AI server shipments to Malaysia, Singapore, Thailand and Indonesia, according to a Financial Times report citing three people familiar with the matter. Dell, Supermicro and other manufacturers have told buyers in those countries that affected orders cannot leave their factories. The sources linked the freeze to new US export controls, but it is unclear whether the pause is temporary.

telegram · zaihuapd · Nov 26, 07:38

**「Background」** Horizon’s November 17 digest reported that a US interim rule extended export controls on advanced AI chips and servers to remote access, aiming to prevent circumvention through third-country data centers. The digest also reported that reexports of AI chips to Indonesia, Malaysia, Singapore, Thailand and Brazil require a license.

**「Buyer requirements」** The report says new US rules require regional cloud providers to obtain export licenses within 90 days and verify that their customers do not include restricted Chinese entities. Buyers in the four countries now face delayed server orders while the shipment pause remains in effect.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/">2026-11-17 — US Extends Advanced AI Chip Controls to Remote Access</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#AI 服务器`, `#出口管制`, `#东南亚`

---

<a id="item-tech-news-3"></a>
### [Minipg Packages PostgreSQL as a Single Executable](https://progrium.github.io/minipg/) ⭐️ 7.0/10

Minipg packages PostgreSQL as a single executable for a CLI-friendly database experience, rather than as an embedded library. A commenter reports that it uses PostgreSQL’s Alpine Docker image with the h9 embedded hypervisor, without requiring Docker.

hackernews · rguiscard · Nov 26, 03:00 · [Discussion](https://news.ycombinator.com/item?id=50650892)

**「Background」** PostgreSQL typically runs as a separate server accessed by clients, whereas SQLite is commonly used as an embedded database library. Minipg’s creator says the project targets SQLite’s command-line simplicity rather than its embedded model; the creator also says PGlite’s single-connection mode did not fit the motivating use case.

**「Community discussion」** Commenters debated whether Minipg offers an advantage over PGlite or tools that download native PostgreSQL binaries for development and testing; one suggested small self-hosted applications as a possible use. Minipg’s creator said PGlite was unsuitable for the motivating problem because it supports only a single connection.

**Tags**: `#PostgreSQL`, `#databases`, `#developer tools`, `#self-hosting`

---

<a id="item-tech-news-4"></a>
### [Shorter Lean Verification Related to Anthropic’s GRH Work](https://github.com/lsernau/grh-lean) ⭐️ 7.0/10

A GitHub project presents a shorter Lean verification related to Anthropic’s work on the generalized Riemann hypothesis \(GRH\). The available source material does not establish the verification’s exact scope or independently confirm its size reduction.

hackernews · nb-t · Nov 25, 21:48 · [Discussion](https://news.ycombinator.com/item?id=50648050)

**「Background」** Lean is a proof assistant that checks formal proofs against explicitly stated definitions and assumptions. Evaluating a formalized proof also requires checking that those definitions and assumptions capture the intended mathematical claim.

**「Community discussion」** One commenter reported a reduction from roughly 17 million lines to 76,000, while another praised a 300,000-line readable version for separating known mathematics from new work and providing documentation. Another commenter questioned how realistically a human could understand and check the Lean code; the reported sizes and readability claims are not independently verified.

**Tags**: `#Lean`, `#formal verification`, `#AI-assisted mathematics`, `#proof readability`

---

<a id="item-tech-news-5"></a>
### [Huawei Plans to Present HBM Research Claiming Double Data-Pin Density](https://www.bloomberg.com/news/articles/2026-11-26/huawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix) ⭐️ 7.0/10

Huawei plans to present research on a high-bandwidth memory \(HBM\) chip at a conference in San Francisco in February 2027. The paper’s title indicates that the chip has twice the data-pin density of Samsung and SK hynix’s current mass-produced products, which could theoretically increase memory bandwidth. The source does not provide measured performance results or a production timeline; Huawei is also pursuing domestic HBM production in China, where access to the component is restricted by US sanctions.

telegram · zaihuapd · Nov 26, 05:30

**「Background」** High-bandwidth memory stacks memory chips and uses a wide interface to transfer data to processors, including AI accelerators. Data-pin density describes how closely connections are packed; actual bandwidth also depends on the number of connections and their transfer rate.

**Tags**: `#HBM`, `#Huawei`, `#AI hardware`, `#semiconductors`

---

<a id="item-tech-news-6"></a>
### [China Sets 2030 Network Goal and Plans 6G Construction](https://www.news.cn/politics/20261126/9fe827a2d98741acb60f62d36ba89cf7/c.html) ⭐️ 7.0/10

Three Chinese government bodies have issued a plan to build a new-generation communications network by 2030, including large-scale 5G-A coverage and a substantially completed low-Earth-orbit satellite internet system. The plan calls for 6G network construction at an appropriate time, but gives no specific schedule. Separately, Guangdong Mobile announced that its 2G network will begin a phased withdrawal from service 30 days after its announcement.

telegram · zaihuapd · Nov 26, 06:30

**「Background」** 5G-Advanced, or 5G-A, is an evolution of 5G, while 6G refers to the next generation of mobile communications. 2G is an older mobile standard used for voice calls and basic data services.

**「Who is affected」** Users who rely on Guangdong Mobile’s 2G network will need to account for its phased withdrawal, although the announcement gives no completion date.

**Tags**: `#通信网络`, `#6G`, `#5G-A`, `#卫星互联网`, `#技术政策`

---

<a id="item-tech-news-7"></a>
### [Neuralink cleared to start pivotal ALS implant trial](https://www.bloomberg.com/news/articles/2026-11-25/neuralink-gets-clearance-for-brain-implant-trial-in-als-patients?srnd=phx-technology) ⭐️ 7.0/10

Neuralink says the FDA has cleared it to begin LINK, a pivotal U.S. trial of its implantable brain-computer interface in people with ALS. The device is intended to translate brain signals into computer control commands; the report describes LINK as the first FDA-cleared pivotal trial of its kind in the U.S. Neuralink previously implanted devices in more than 30 people with paralysis worldwide through early studies. The clearance is for a clinical trial, not commercial sale; the trial data are intended to support a future application for device approval.

telegram · zaihuapd · Nov 26, 07:15

**「Background」** Neuralink previously implanted its device in more than 30 people with paralysis worldwide through early studies, according to the report. Data from a pivotal trial can support a future application to market a medical device; clearance to conduct the trial is not marketing approval.

**Tags**: `#brain-computer interfaces`, `#Neuralink`, `#clinical trials`, `#FDA`, `#ALS`

---

<a id="item-tech-news-8"></a>
### [Netherlands Opposes Proposed US Curbs on ASML Sales to China](https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml) ⭐️ 7.0/10

Dutch trade minister Sjoerd Sjoerdsma told parliament that the Netherlands would not accept further US restrictions on ASML’s sales to China under the proposed MATCH Act. The Netherlands is coordinating with the European Commission and lobbying alongside Germany and France to remove the measure from the annual US defense policy bill. The bipartisan proposal would require allies including the Netherlands and Japan to impose tighter export controls on China or face unilateral US restrictions on their semiconductor equipment. A congressional vote is expected in mid-December, but the outcome remains uncertain.

telegram · zaihuapd · Nov 26, 14:56

**「Background」** ASML supplies machines used to manufacture semiconductors. Export controls can restrict where such equipment is sold, including by companies based outside the country imposing the rules.

**「Potential impact」** If enacted, the proposal could further constrain ASML’s sales to China, which accounts for about 20% of the company’s sales this year.

**Tags**: `#ASML`, `#半导体`, `#出口管制`, `#中美科技竞争`, `#荷兰`

---

<a id="item-tech-news-9"></a>
### [GLM-5.5 and Kimi K4 Releases Could Be Delayed](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/) ⭐️ 7.0/10

Reuters reports that Z.AI’s GLM-5.5 and Moonshot AI’s Kimi K4 could be delayed by computing constraints and measures against model distillation. A person familiar with Z.AI’s plans said GLM-5.5, a roughly 3-trillion-parameter model originally planned for November, might arrive in the first quarter of 2027 or later. Moonshot reportedly expects major releases to take more than a year instead of six months if it loses access to overseas computing resources; Kimi K4 could be delayed until mid-2027, and the report says the company has turned to distilling Google and Meta models as OpenAI and Anthropic make training data harder to obtain. A circulated screenshot purports to show Z.AI denying the report, but the denial has not been independently verified.

telegram · zaihuapd · Nov 26, 15:14

**「Background」** Model distillation can use an existing model’s outputs as training data for another model; anti-distillation measures seek to restrict that use. Horizon’s November 25 digest reported that Z.ai had released GLM-5.4, a coding-oriented model whose weights were not yet open.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Nov/23/glm-54/">2026-11-25 — GLM-5.4 Introduces Z.ai’s First Looped Transformer</a></li>

</ul>
</details>

**Tags**: `#大语言模型`, `#智谱`, `#月之暗面`, `#模型蒸馏`, `#AI算力`

---

<a id="item-tech-news-10"></a>
### [Cloudflare Investigates Dashboard and API Disruption](https://www.cloudflarestatus.com/incidents/xiqj67vl5pqm) ⭐️ 7.0/10

Cloudflare is investigating an issue affecting its Dashboard and related APIs, according to a November 26 status notice. Customers may encounter failed API requests or error messages in the Dashboard. The report says the disruption had lasted about half an hour, but does not establish its cause or full scope.

telegram · zaihuapd · Nov 26, 16:33

**「Background」** The Cloudflare Dashboard is a web interface for managing Cloudflare services, while its APIs allow customers to manage them programmatically.

**Tags**: `#Cloudflare`, `#Service Outage`, `#Cloud Infrastructure`, `#APIs`

---
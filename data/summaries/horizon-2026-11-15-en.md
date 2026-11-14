# Horizon Daily - 2026-11-15

> From 28 items, 10 important content pieces were selected

---

**Technology News**
1. [Report Claims Lovable Apps Exposed Passport Details and Private Messages](#item-tech-news-1) ⭐️ 7.0/10
2. [SpaceX reportedly catches Starship after Flight 15](#item-tech-news-2) ⭐️ 7.0/10
3. [Italy fines Meta €805 million over Android photo access](#item-tech-news-3) ⭐️ 7.0/10
4. [Cloudflare Open-Sources Kitesurf Browser for AI Agents](#item-tech-news-4) ⭐️ 7.0/10
5. [PyPI redesign highlights package provenance](#item-tech-news-5) ⭐️ 6.0/10
6. [EFF Raises Concern Over Tech Companies’ Definition of Privacy](#item-tech-news-6) ⭐️ 6.0/10
7. [Starship Flight 15 Reaches Orbit, but Booster Explodes](#item-tech-news-7) ⭐️ 6.0/10
8. [OpenAI Disbands Robotics Team, Citing General-Purpose Models](#item-tech-news-8) ⭐️ 6.0/10
9. [W5000 uncrewed cargo aircraft completes test flight](#item-tech-news-9) ⭐️ 6.0/10
10. [Anthropic IPO orders from China reportedly rejected](#item-tech-news-10) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Report Claims Lovable Apps Exposed Passport Details and Private Messages](https://www.crissyfield.de/research/lovable-en/) ⭐️ 7.0/10

A report claims that apps built with Lovable exposed passport details and more than 200,000 private messages. The report’s contents were not supplied, so the scope and circumstances of the claimed exposure cannot be independently assessed here.

hackernews · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**「Background」** Lovable builds full-stack applications from plain-language prompts. Supabase provides PostgreSQL databases and APIs that applications can use to access data.

**「Community discussion」** Commenters debated responsibility for database security defaults: one argued that Supabase’s defaults contributed to the problem, while another called for deny-by-default databases and automated authorization tests. A commenter also questioned whether accessing data allegedly published through a read-only API key should be described as a breach.

<details><summary>References</summary>
<ul>
<li><a href="https://lovable.dev/">App &amp; Website Builder | Build Software in Minutes | Lovable</a></li>
<li><a href="https://supabase.com/">Supabase | The Postgres Development Platform</a></li>

</ul>
</details>

**Tags**: `#AI app development`, `#data exposure`, `#database security`, `#Supabase`

---

<a id="item-tech-news-2"></a>
### [SpaceX reportedly catches Starship after Flight 15](https://x.com/i/broadcasts/2brajgZlOKRMka) ⭐️ 7.0/10

SpaceX reportedly caught Starship at the end of Flight 15. The supplied account does not describe the catch mechanism or the vehicle’s condition.

hackernews · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**「Background」** Horizon’s September 29 digest reported that Starship had reached orbit and deployed 26 Starlink satellites, but an early engine shutdown shortened the mission and led to a Pacific splashdown. For Flight 15, SpaceX abandoned a separate plan to catch the Super Heavy booster.

**「Discussion」** One commenter suggested that a durable heat shield, repeat catches and re-flights could eventually lower launch costs. That outcome remains speculative in the supplied material.

<details><summary>References</summary>
<ul>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-flight-15-chopsticks-double-catch-super-heavy-ship">SpaceX launches Starship on ambitious 22-hour Flight 15 test , but...</a></li>
<li><a href="https://apnews.com/article/spacex-starship-orbit-262d3c58d56bf7a525b49115d6c5dfe8">2026-09-29 — SpaceX 星舰首次入轨，部署卫星后提前返航</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#Reusable spacecraft`, `#Aerospace engineering`

---

<a id="item-tech-news-3"></a>
### [Italy fines Meta €805 million over Android photo access](https://www.reuters.com/world/italy-fines-meta-887-million-over-android-users-data-access-2026-11-14/) ⭐️ 7.0/10

Italy’s privacy regulator fined Meta €805 million \($887 million\), saying its Facebook Android app accessed photos, videos and metadata belonging to about 20 million Italian users without specific consent. The regulator said the photo recommendation feature, introduced in 2023, was enabled by default and used a generic authorization prompt. Meta must turn it off by default and obtain separate consent within 60 days, or refrain from enabling it for users who have not validly authorized it.

hackernews · giuliomagnifico · Nov 14, 13:48 · [Discussion](https://news.ycombinator.com/item?id=50497009)

**「Background」** Facebook introduced the album recommendation feature in its Android app in 2023. It was enabled by default and used a broadly worded permission prompt rather than requesting specific consent for the feature.

**「Community discussion」** Commenters questioned how the app accessed photos and whether Android’s device-level permission amounted to consent. One argued that users must have granted permission at some point, while another said the technical details were unclear.

**Tags**: `#Meta`, `#data privacy`, `#Android`, `#regulation`

---

<a id="item-tech-news-4"></a>
### [Cloudflare Open-Sources Kitesurf Browser for AI Agents](https://www.phoronix.com/news/Cloudflare-Kitesurf-Open-Source) ⭐️ 7.0/10

Cloudflare has open-sourced Kitesurf, a stateless browser for AI agents, under the Apache 2.0 license. Built on Cloudflare Workers, it parses HTML, processes CSS and executes JavaScript without browser containers. Cloudflare says it aims to use less CPU and memory than Chromium and scale on demand across its global Workers network, but the source provides no benchmarks. The code is available on GitHub.

telegram · zaihuapd · Nov 14, 09:33

**「Background」** AI agents may need a browser engine to process web pages and run JavaScript before extracting or interacting with their content. Kitesurf uses Cloudflare Dynamic Workers to isolate pages; according to the project, that feature is part of the Workers Paid plan.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cloudflare/kitesurf">GitHub - cloudflare / kitesurf : Kitesurf is an experimental browser ...</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#AI agents`, `#browser automation`, `#Cloudflare Workers`, `#open source`

---

<a id="item-tech-news-5"></a>
### [PyPI redesign highlights package provenance](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) ⭐️ 6.0/10

PyPI’s redesigned project pages are now live, with clearer security signals for people browsing Python packages. The new layout gives greater prominence to package provenance information.

hackernews · rbanffy · Nov 14, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50497892)

**「Background」** PyPI is a repository for distributing Python packages, not an auditing service; it does not guarantee the security or suitability of a package.

**「Discussion」** Commenters welcomed more visible provenance but questioned whether trust mechanisms could increase reliance on major cloud or CI providers. One commenter cautioned that provenance signals do not detect projects that are malicious from the outset.

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/">PyPI · The Python Package Index</a></li>
<li><a href="https://pypi.org/project/pip/">pip · PyPI</a></li>

</ul>
</details>

**Tags**: `#PyPI`, `#supply-chain-security`, `#package-provenance`, `#Python`

---

<a id="item-tech-news-6"></a>
### [EFF Raises Concern Over Tech Companies’ Definition of Privacy](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 6.0/10

An Electronic Frontier Foundation article addresses what it describes as technology companies’ attempts to reshape the concept of privacy. The article’s text was not supplied, so its specific arguments cannot be assessed.

hackernews · gslin · Nov 14, 12:45 · [Discussion](https://news.ycombinator.com/item?id=50496602)

**「Background」** AI meeting notetakers can record and transcribe conversations, creating digital records of what participants say.

**「Community discussion」** One commenter said AI notetakers record and upload workplace meetings, including one-on-ones, and asked how employees could opt out without risking their jobs. Another compared the privacy concerns around current recording devices with the backlash against Google Glass.

**Tags**: `#privacy`, `#AI notetakers`, `#workplace surveillance`, `#data protection`

---

<a id="item-tech-news-7"></a>
### [Starship Flight 15 Reaches Orbit, but Booster Explodes](https://www.spacex.com/launches/starship-flight-15) ⭐️ 6.0/10

SpaceX’s 15th Starship test flight launched from Texas on November 13, but its booster aborted a planned return to the launch tower because of a technical problem and exploded after a controlled splashdown in the Gulf of Mexico. The spacecraft reportedly reached orbit and deployed all 26 Starlink V3 satellites, three of which carried cameras to inspect its heat-shield tiles. It was scheduled to return to Starbase the next day after about 22 hours and 14 orbits, for an attempted tower catch; the cause of the booster failure has not been disclosed.

telegram · zaihuapd · Nov 14, 03:03

**「Background」** Horizon’s September 29 digest reported that Starship had reached orbit for the first time and deployed 26 next-generation Starlink satellites, but an early engine shutdown shortened that mission and led to a Pacific splashdown. The current flight instead plans to return the ship to Starbase for a tower catch.

**「Recovery attempt」** The booster’s loss rules out the planned recovery of both vehicle stages on this flight, while the spacecraft’s tower catch remains an uncompleted attempt.

<details><summary>References</summary>
<ul>
<li><a href="https://apnews.com/article/spacex-starship-orbit-262d3c58d56bf7a525b49115d6c5dfe8">2026-09-29 — SpaceX 星舰首次入轨，部署卫星后提前返航</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#星舰`, `#火箭回收`, `#Starlink`

---

<a id="item-tech-news-8"></a>
### [OpenAI Disbands Robotics Team, Citing General-Purpose Models](https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/) ⭐️ 6.0/10

According to a report attributed to Fortune, OpenAI has disbanded its standalone robotics team and reassigned its researchers to more general research teams. The company says models such as GPT-6 Astra can directly control robots, though the account provides no technical evidence or details of their capabilities. The report also says OpenAI is still developing a humanoid robot and aims to show it publicly in 2027.

telegram · zaihuapd · Nov 14, 04:00

**「Background」** OpenAI previously disbanded a robotics team in 2020 and rebuilt it in 2024. Its partnership with Figure ended in February 2025.

**Tags**: `#OpenAI`, `#机器人`, `#通用模型`, `#人工智能`, `#科技行业`

---

<a id="item-tech-news-9"></a>
### [W5000 uncrewed cargo aircraft completes test flight](https://www.ithome.com/1/027/068.htm) ⭐️ 6.0/10

White Whale Airlines says its W5000 uncrewed cargo aircraft completed a technical test flight in Inner Mongolia, including climb, cruise, turns, descent and landing. The company claims it has the world’s largest payload capacity for an uncrewed cargo aircraft, with a maximum takeoff weight of 10.8 tonnes, a maximum payload of 5 tonnes and a design range of 2,600 kilometers. The turboprop aircraft is designed for autonomous flight with ground monitoring, with one crew overseeing six or seven aircraft; airworthiness certification is targeted for the first half of 2027.

telegram · zaihuapd · Nov 14, 05:00

**「Background」** Airworthiness certification is the regulatory process for establishing that an aircraft meets applicable safety standards. A successful test flight does not by itself grant certification.

**Tags**: `#autonomous aircraft`, `#cargo drones`, `#flight testing`, `#aviation certification`

---

<a id="item-tech-news-10"></a>
### [Anthropic IPO orders from China reportedly rejected](https://m.economictimes.com/markets/us-stocks/news/anthropic-ipo-share-orders-from-china-are-said-to-be-rebuffed/articleshow/135809948.cms) ⭐️ 6.0/10

A Telegram post citing Economic Times reports that orders for Anthropic’s planned IPO from investors in mainland China and Hong Kong have been rejected. It attributes the restriction to U.S. International Traffic in Arms Regulations export controls, citing unnamed sources. The post says the offering is scheduled to price on November 18 and list the next day under the ticker ANT, seeking to raise up to $90.4 billion at a $1.4 trillion valuation. These claims have not been independently verified in the supplied material.

telegram · zaihuapd · Nov 14, 10:18

**「Background」** Horizon’s September 13 digest reported that, according to Reuters sources, Anthropic’s IPO was targeting a roughly $2 trillion valuation and Nvidia was in talks to be an anchor investor. The current report puts the proposed valuation at $1.4 trillion.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/legal/transactional/nvidia-talks-invest-anthropics-mega-ipo-sources-say-2026-09-11/">2026-09-13 — 消息人士透露 Nvidia 正洽谈投资 Anthropic 的超大规模 IPO</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#Export controls`, `#AI industry`

---


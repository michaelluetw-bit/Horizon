# Horizon Daily - 2026-11-28

> From 31 items, 10 important content pieces were selected

---

**Technology News**
1. [OpenSec reports critical Linux NFS server vulnerability](#item-tech-news-1) ⭐️ 8.0/10
2. [Report: WebRTC Credit Card Skimmers Found on Shopping Sites](#item-tech-news-2) ⭐️ 7.0/10
3. [US Air Force’s Cloud One Platform Reportedly Hacked](#item-tech-news-3) ⭐️ 7.0/10
4. [New York and California Age-Gating Rules Take Effect in the New Year](#item-tech-news-4) ⭐️ 7.0/10
5. [Paper Claims Deterministic Subexponential Algorithm for Discrete Logarithms](#item-tech-news-5) ⭐️ 7.0/10
6. [Google Play Plans Global Developer Contact Disclosure](#item-tech-news-6) ⭐️ 7.0/10
7. [Nadella Says New-Grad Hiring Has Slowed as Companies Prioritize AI](#item-tech-news-7) ⭐️ 7.0/10
8. [DeepSeek Reportedly Raises Up to 105.5 Billion Yuan](#item-tech-news-8) ⭐️ 7.0/10
9. [Anthropic reportedly limits Claude on frontier model development](#item-tech-news-9) ⭐️ 7.0/10
10. [Minecraft Bedrock resource-pack vulnerability fixed in 26.65](#item-tech-news-10) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenSec reports critical Linux NFS server vulnerability](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 8.0/10

OpenSec disclosed CVE-2026-99362, a pre-authentication heap overflow in the Linux kernel NFS server, nfsd, with a CVSS score of 9.8. OpenSec says an attacker can send a connection to TCP port 2049 and obtain a root shell without logging in. The flaw reportedly dates back to Linux 3.16 and affects hosts with NFSv4.1 or NFSv4.2 enabled. Fixes have been released in kernel versions 6.12.117, 6.18.61, 7.3.2 and 7.4-rc1.

telegram · zaihuapd · Nov 27, 12:57

**「Background」** NFS lets computers access files over a network; Linux’s built-in NFS server is called nfsd. NFSv4.1 uses sessions and sequence replies to manage requests, and the vulnerability occurs while nfsd processes those replies.

**「What affected users can do」** Affected operators should upgrade the kernel and reboot; those unable to upgrade immediately can restrict access to TCP port 2049 with a firewall.

<details><summary>References</summary>
<ul>
<li><a href="https://watchtowr.com/intelligence/nfs2root-linux-nfs-cve-2026-99362-faq/">NFS2ROOT (CVE-2026-99362) FAQ: Linux NFS Exposure and Fix</a></li>

</ul>
</details>

**Tags**: `#Linux 内核`, `#NFS`, `#安全漏洞`, `#远程代码执行`

---

<a id="item-tech-news-2"></a>
### [Report: WebRTC Credit Card Skimmers Found on Shopping Sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

A report says credit card skimming scripts using WebRTC were found on popular shopping sites. The supplied material does not identify the affected sites or explain how the scripts operated.

hackernews · scanr · Nov 27, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50668145)

**「Background」** WebRTC is a browser technology that supports real-time communication, including data transfer between peers. Web skimming involves malicious scripts capturing payment information entered on shopping sites.

**「Community discussion」** Commenters questioned whether WebRTC offered a distinct technical advantage over ordinary HTTP requests. One suggested it may be less frequently monitored for malicious activity, but the supplied material does not establish the attackers’ reason for using it.

**Tags**: `#web security`, `#credit card skimming`, `#WebRTC`, `#e-commerce`

---

<a id="item-tech-news-3"></a>
### [US Air Force’s Cloud One Platform Reportedly Hacked](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163) ⭐️ 7.0/10

The US Air Force’s Cloud One computing platform has reportedly been hacked. The available material does not establish how the compromise occurred, its scope, or its confirmed impact.

hackernews · freakynit · Nov 27, 12:54 · [Discussion](https://news.ycombinator.com/item?id=50666375)

**「Background」** A passage from the report quoted in the discussion says Cloud One launched in 2017 and combines services from Microsoft, Amazon, Oracle and Alphabet. It supports Air Force applications for functions including personnel, pay, logistics and maintenance.

**「Community discussion」** One commenter whose work relies on Cloud One reported significant disruptions over the past month, saying infrastructure was being rebuilt and access restricted. Another questioned the platform’s reported use of multiple cloud vendors and proposed an in-house operations team instead.

**Tags**: `#cloud security`, `#cybersecurity`, `#US Air Force`, `#cloud infrastructure`

---

<a id="item-tech-news-4"></a>
### [New York and California Age-Gating Rules Take Effect in the New Year](https://www.eff.org/deeplinks/2026/11/new-york-and-california-age-gating-rules-go-effect-new-year) ⭐️ 7.0/10

New York and California are introducing age-gating rules for social platforms in the new year. An excerpt shared in the discussion says New York’s SAFE for Kids Act restricts personalized recommendations and notifications from midnight to 6 a.m. without required consent, and requires platforms to assess users’ ages and locations. The supplied material gives limited detail about California’s rules.

hackernews · frutiger · Nov 27, 12:43 · [Discussion](https://news.ycombinator.com/item?id=50666279)

**「Background」** Age assurance involves estimating or verifying users’ ages. Personalized feeds use information about individual users to select content recommendations.

**「Discussion」** One commenter argued that personalized feeds can help young people find interests and communities, while acknowledging that the feeds can also be addictive. Another preferred tools that would let people of any age avoid both identity checks and algorithmic feeds.

**Tags**: `#age assurance`, `#social media regulation`, `#online privacy`, `#content recommendations`

---

<a id="item-tech-news-5"></a>
### [Paper Claims Deterministic Subexponential Algorithm for Discrete Logarithms](https://eprint.iacr.org/2026/3020.pdf) ⭐️ 7.0/10

A research paper claims a deterministic subexponential-time algorithm for the discrete logarithm problem. The supplied material does not establish the proof or the algorithm’s scope, so its implications for cryptographic systems remain unclear.

hackernews · yuvadam · Nov 27, 12:08 · [Discussion](https://news.ycombinator.com/item?id=50665968)

**「Background」** The discrete logarithm problem asks for the exponent that produces a given group element from a known base. Randomized subexponential-time algorithms for the finite-field version were already known; a deterministic algorithm would not rely on random choices.

**「Practical implications」** For elliptic-curve cryptography users, the claim alone does not establish a practical attack or a need to replace keys. The paper’s result depends on an assumed Cauchy–Hermite Boolean tensor contraction construction.

**「Community discussion」** Commenters noted that randomized subexponential algorithms for discrete logarithms were already known. Several expected little practical effect on current cryptography, with one arguing that the claimed asymptotic improvement would matter only for extremely large keys.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50665968">A Deterministic Subexponential - Time Algorithm for the Discrete ...</a></li>
<li><a href="https://eprint.iacr.org/2026/3020">A Deterministic Subexponential-time Algorithm for the ...</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#discrete logarithms`, `#algorithms`, `#computational complexity`

---

<a id="item-tech-news-6"></a>
### [Google Play Plans Global Developer Contact Disclosure](https://www.androidpure.com/google-play-trader-developer-address/) ⭐️ 7.0/10

Google Play reportedly plans to show the phone numbers and addresses of self-declared trader developers to users worldwide from March 1, 2027, including those of individual account holders. All active developer accounts must declare trader or non-trader status by February 1, 2027; those that miss the deadline could lose the ability to update apps and have them removed globally. The report says the policy was announced in October and has prompted developer privacy concerns.

telegram · zaihuapd · Nov 27, 01:44

**「Background」** Google’s trader-status declaration is based on laws in the European Economic Area and the UK. The source reports that the policy was announced in October and that EU rules do not require the information to be displayed to users outside the EU.

**「Developer implications」** Individual trader developers face public disclosure of their contact details worldwide. The report says Google does not accept post office boxes as payment addresses, limiting an option for developers seeking to protect their privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/googleplay/android-developer/answer/17594752?hl=en">Trader status declaration - Play Console Help</a></li>

</ul>
</details>

**Tags**: `#Google Play`, `#developer policy`, `#privacy`, `#app distribution`

---

<a id="item-tech-news-7"></a>
### [Nadella Says New-Grad Hiring Has Slowed as Companies Prioritize AI](https://www.windowslatest.com/2026/11/27/lets-add-the-next-human-satya-nadella-admits-new-grad-hiring-slowed-as-companies-rebuild-around-ai-and-says-every-company-will-add-its-next-person-after-it-burns-through-its-ai-budget/) ⭐️ 7.0/10

Microsoft CEO Satya Nadella said on The Pragmatic Engineer podcast that hiring of new graduates has slowed as companies redeploy existing employees before adding staff. He predicted that companies will exhaust their AI budgets before hiring their next person, while maintaining that he still believes in campus recruitment. Microsoft’s workforce fell by 5,000 to 223,000 in the year to June 30, its first annual decline since 2016. The report also cites a MIT and Microsoft Research paper associating GitHub Copilot adoption with 29% fewer quarterly technical hires, particularly in junior roles, though it does not provide the study’s methods.

telegram · zaihuapd · Nov 27, 03:03

**「Background」** Earlier this year at Davos, Nadella said he still believed in campus recruiting. Microsoft had 223,000 employees as of June 30, down 5,000 from a year earlier and its first annual decline since 2016.

**Tags**: `#微软`, `#人工智能`, `#技术招聘`, `#GitHub Copilot`

---

<a id="item-tech-news-8"></a>
### [DeepSeek Reportedly Raises Up to 105.5 Billion Yuan](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

DeepSeek reportedly completed a second financing round of 100 billion to 105.5 billion yuan, at a post-money valuation of about 615.5 billion yuan. Tencent, CATL, China Mobile and vivo were reportedly among 31 new investors, while Mixue committed 500 million yuan through a fund. The source provides no original disclosure or independent verification of the figures.

telegram · zaihuapd · Nov 27, 06:33

**「Background」** Horizon’s August 6 digest reported that DeepSeek had restarted its second funding round, aiming to raise 50 billion yuan at a pre-money valuation of 500 billion yuan. The newly reported fundraising total is approximately twice that target.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.sina.com.cn/wm/2026-08-05/doc-inimfmyv1554159.shtml">2026-08-06 — 🤖 DeepSeek 重启第二轮融资 投前估值 5000 亿元</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#人工智能`, `#融资`, `#中国科技行业`

---

<a id="item-tech-news-9"></a>
### [Anthropic reportedly limits Claude on frontier model development](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic’s June system card for Claude Mythos 5 and Fable 5 reportedly says the company covertly limits Claude’s effectiveness on requests related to frontier AI model development. The reported methods include prompt rewriting, steering vectors and parameter-efficient fine-tuning; users are not notified or switched to another model. Covered work includes pretraining pipelines, distributed training and accelerator design. Anthropic estimates that the measures affect about 0.03% of traffic and fewer than 0.1% of organizations, while most coding work is unaffected; the system card itself was not provided in the source material.

telegram · zaihuapd · Nov 27, 13:42

**「Background」** Anthropic’s system cards document Claude models’ capabilities, safety evaluations, and deployment decisions. The company said it introduced the restrictions in light of recent models’ ability to accelerate their own development.

**「Community discussion」** Hacker News commenters argued that undisclosed intervention undermines trust in Claude’s coding output. Some described unexpectedly poor results and wondered whether the safeguards were responsible, but their accounts do not establish a connection.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/">If Claude Fable stops helping you, you&#x27;ll never know</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#AI 安全`, `#模型透明度`

---

<a id="item-tech-news-10"></a>
### [Minecraft Bedrock resource-pack vulnerability fixed in 26.65](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

Mojang fixed a Minecraft Bedrock Edition resource-pack vulnerability in version 26.65. Add-on developer 8Crafter said the issue affects versions 26.52 through 26.63 on PC, mobile and consoles, and possibly earlier versions; Java Edition is unaffected. A resource pack containing a content.zipe file could modify the Ore UI framework and run hidden scripts.

telegram · zaihuapd · Nov 27, 18:04

**「Background」** Ore UI is the interface framework used for many Minecraft Bedrock menus. Resource packs can be downloaded automatically when players join a server or Realm if that setting is enabled.

**「Player impact」** Players with automatic resource-pack downloads enabled could receive an affected pack when joining a server or Realm without installing it manually. 8Crafter said potential exploits include deleting saves and obtaining a player’s IP address; under certain Windows conditions, a batch file could also download malware. Players can update to 26.65; a Windows tool by AxmBro can find content.zipe files but cannot determine whether a pack is malicious.

<details><summary>References</summary>
<ul>
<li><a href="https://kaimux.com/forum/project/minecraft-insights/minecraft-bedrock-26-65-resource-pack-fix.1063">Minecraft Bedrock 26.65: the resource pack security fix | KAIMUX</a></li>

</ul>
</details>

**Tags**: `#Minecraft`, `#安全漏洞`, `#资源包`, `#恶意软件`

---


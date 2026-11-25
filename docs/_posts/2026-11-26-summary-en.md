---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 30 items, 10 important content pieces were selected

---

**Technology News**
1. [1Password Publishes Update on November 2026 Security Incident](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI preprint claims matrix multiplication exponent is 9/4](#item-tech-news-2) ⭐️ 8.0/10
3. [Minecraft2shell reports Java Edition RCE through resource-pack fonts](#item-tech-news-3) ⭐️ 8.0/10
4. [Article Describes Bypassing iOS Safari’s 60 FPS Limit](#item-tech-news-4) ⭐️ 7.0/10
5. [Claimed Inference-Server Side Channels Could Bypass Model Sandboxes](#item-tech-news-5) ⭐️ 7.0/10
6. [SpaceX and Tesla Reportedly Discuss $3.5 Trillion Stock Merger](#item-tech-news-6) ⭐️ 7.0/10
7. [Tencent Releases Hy4 Flash Quantized Weights for Lower-Memory Hardware](#item-tech-news-7) ⭐️ 7.0/10
8. [US officials reportedly pressured Intel to give government a 10% stake](#item-tech-news-8) ⭐️ 7.0/10
9. [Samsung and SK Hynix Reportedly Plan to Use YMTC Xtacking Technology](#item-tech-news-9) ⭐️ 7.0/10
10. [Google releases Cogentic papers on factorization and discrete logarithms](#item-tech-news-10) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [1Password Publishes Update on November 2026 Security Incident](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password published an update on a November 2026 security incident. The supplied material does not establish the incident’s scope or whether customer vaults were affected.

hackernews · lxhrstn · Nov 25, 17:18 · [Discussion](https://news.ycombinator.com/item?id=50644817)

**「Background」** 1Password says it began investigating on November 19, 2026, after indications that an attacker had accessed an employee’s corporate GitHub account. The company says the attacker used the account to access source code and push malicious code to backend services.

**「Community discussion」** Commenters questioned how malicious code could reach production services and whether branch protections were missing or bypassed. Another commenter wanted a clearer statement about whether encrypted vaults were downloaded.

<details><summary>References</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving... | 1 Password</a></li>

</ul>
</details>

**Tags**: `#1Password`, `#security incident`, `#password managers`, `#software supply chain`

---

<a id="item-tech-news-2"></a>
### [OpenAI preprint claims matrix multiplication exponent is 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 8.0/10

An OpenAI-hosted preprint claims that the matrix multiplication exponent is exactly 9/4. The exponent describes the asymptotic arithmetic complexity of multiplying matrices; the supplied material does not include the proof or independent verification of the claim.

hackernews · E-Reverance · Nov 25, 01:19 · [Discussion](https://news.ycombinator.com/item?id=50637220)

**「Background」** The matrix multiplication exponent describes how the number of arithmetic operations needed to multiply two n × n matrices scales with n. An earlier preprint described an algorithm for integer matrices using O\(n^\(9/4+ε\)\) arithmetic operations for any ε &gt; 0; that is an upper bound, not a proof of the exact exponent over every field.

**「Discussion」** One commenter says the claimed result applies over every field and would refute the conjecture that the exponent is 2. The commenter also attributes solutions to other open problems, including strongly polynomial linear programming, to the paper; those claims are not verified in the supplied material.

<details><summary>References</summary>
<ul>
<li><a href="https://xenospectrum.com/en/matrix-multiplication-nine-fourths-lower-bound/">OpenAI Preprint Claims the Matrix Multiplication Exponent Is ...</a></li>
<li><a href="https://arxiv.org/abs/2610.28627">[2610.28627] Matrix Multiplication from Polynomial Packings ...</a></li>

</ul>
</details>

**Tags**: `#matrix multiplication`, `#computational complexity`, `#algorithms`, `#mathematical research`

---

<a id="item-tech-news-3"></a>
### [Minecraft2shell reports Java Edition RCE through resource-pack fonts](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

The minecraft2shell report claims that a specially crafted TrueType font in a server resource pack can trigger an out-of-bounds write in FreeType 2.14.3 and earlier, enabling code execution on a Minecraft Java Edition 26.3 Windows client. It lists Java versions 1.20.5–1.21.10 and 26.1–26.4 snapshots as affected, but says 1.20.4 and earlier and Bedrock Edition are not affected; these claims have not been independently verified. The report says Mojang has not yet patched the issue and identifies the community’s m2sfix 1.0.0, a Java agent or mod that disables font hinting, as a temporary mitigation. Until a fix is available, the submitter recommends avoiding resource packs, disabling server resource packs or installing the community fix.

telegram · zaihuapd · Nov 25, 12:46

**「Background」** Minecraft resource packs can supply custom TrueType fonts. The Java 26.3 Windows client bundles FreeType, a native library used to process fonts.

**「What players can do」** Until an official fix is available, affected Java Edition players can disable server resource packs and avoid installing untrusted packs. A community mitigation, m2sfix, disables font hinting and is available as a Java agent or mod; it is not an official Mojang patch.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/bikini/minecraft2shell">GitHub - bikini / minecraft 2 shell : Minecraft to native RCE · GitHub</a></li>
<li><a href="https://github.com/sunrisemc-tw/minecraft2shell-fix">GitHub - sunrisemc-tw/minecraft2shell-fix: Client-side ...</a></li>
<li><a href="https://wurst.wiki/minecraft2shell">Minecraft2Shell Vulnerability [Wurst.Wiki]</a></li>

</ul>
</details>

**Tags**: `#Minecraft`, `#远程代码执行`, `#FreeType`, `#软件安全`

---

<a id="item-tech-news-4"></a>
### [Article Describes Bypassing iOS Safari’s 60 FPS Limit](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit) ⭐️ 7.0/10

An article describes a workaround for iOS Safari’s 60 FPS limit, intended to make web applications feel more like native apps. The supplied material does not explain the technique or independently establish its performance or battery impact.

hackernews · vinhnx · Nov 25, 03:04 · [Discussion](https://news.ycombinator.com/item?id=50637890)

**「Background」** A 120 Hz display can show up to 120 frames per second, but receiving input at that rate does not guarantee equally frequent page updates. The article notes that the DOM can still update only 60 times per second even when input arrives more frequently.

**「Who can see the difference」** To view the demos at 120 Hz, users need a ProMotion display and must turn off both Low Power Mode and Limit Frame Rate under Accessibility → Motion.

**「Community discussion」** One commenter found a linked web demo impressive, while another said the difference in an initial example was subtle. A commenter suggested that running at 120 Hz continuously could increase battery drain, though the supplied material does not establish that tradeoff for the workaround.

<details><summary>References</summary>
<ul>
<li><a href="https://rida.dev/blog/bypassing-ios-safari-60-fps-limit">Bypassing iOS Safari ’s 60 FPS Limit to Build Web Applications That...</a></li>
<li><a href="https://rida.dev/blog/bypassing-ios-safari-60-fps-limit">Bypassing iOS Safari ’s 60 FPS Limit to Build Web Applications That...</a></li>

</ul>
</details>

**Tags**: `#iOS Safari`, `#WebKit`, `#Web Performance`, `#Animation`

---

<a id="item-tech-news-5"></a>
### [Claimed Inference-Server Side Channels Could Bypass Model Sandboxes](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) ⭐️ 7.0/10

A post claims that sandboxed AI models can communicate through side channels in shared inference servers. The available material does not establish the attacks’ requirements or effectiveness.

hackernews · gmays · Nov 25, 02:34 · [Discussion](https://news.ycombinator.com/item?id=50637686)

**「Background」** Sandboxed agents can be prevented from exchanging messages or accessing a shared filesystem while still running on the same inference server. A side channel conveys information indirectly through effects on shared computation, rather than through an explicit message.

**「Discussion」** One commenter proposed separating inference-server caches by security context to prevent cross-context probing. Another disputed the attacks’ practicality, arguing that they require cooperating agents and detailed knowledge of the server stack; a third said non-cooperative information leaks between cloud tenants would be a greater concern.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being">Models Can Communicate via Inference Servers Despite Being ...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#inference servers`, `#side channels`, `#cache isolation`

---

<a id="item-tech-news-6"></a>
### [SpaceX and Tesla Reportedly Discuss $3.5 Trillion Stock Merger](https://thenextweb.com/news/spacex-tesla-merger-five-directors-special-committees) ⭐️ 7.0/10

SpaceX and Tesla have reportedly selected five directors to form special committees at the two companies and negotiate a potential $3.5 trillion all-stock merger. The companies aim to complete a deal by year-end, but people familiar with the matter say they are not close to an agreement. The committees would need to determine an exchange ratio, win shareholder support and address the risk of investor lawsuits.

telegram · zaihuapd · Nov 25, 00:41

**「How an all-stock merger works」** In an all-stock merger, shareholders receive shares rather than cash. The exchange ratio determines how much stock they receive for their existing holdings.

**Tags**: `#SpaceX`, `#特斯拉`, `#并购`, `#科技产业`

---

<a id="item-tech-news-7"></a>
### [Tencent Releases Hy4 Flash Quantized Weights for Lower-Memory Hardware](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 7.0/10

Tencent has released GGUF quantized weights for its 224-billion-parameter Hy4 Flash model through its AngelSlim toolkit. The smallest IQ2-AH version is 125.73 GiB, down from approximately 410.27 GiB for the original weights, and reportedly runs on a 64 GB Mac mini using Strata offloading. The source reports generation speeds of 89 tokens per second on a 48 GB GPU at a 10K context length, and 47 tokens per second for Q3\_K on a 128 GB M5 Max at a 32K context length. It also reports that Q3\_K scored within 0.4 points of the original model on tests including DeepSWE v1.1, but provides limited testing details.

telegram · zaihuapd · Nov 25, 09:29

**「Background」** Quantization reduces the precision used to represent model weights, shrinking their storage and memory requirements. Offloading keeps some model data outside the memory used for computation and loads it as needed, typically trading speed for lower memory use.

**Tags**: `#large language models`, `#quantization`, `#model offloading`, `#open weights`

---

<a id="item-tech-news-8"></a>
### [US officials reportedly pressured Intel to give government a 10% stake](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 7.0/10

Court documents show that a US Commerce Department lawyer told Intel’s chief financial officer in August 2025 not to mistake talks over a government stake for a negotiation, according to WIRED. The lawyer reportedly said Intel’s board could refuse but warned of unpredictable consequences; the board agreed to the stake days later. President Trump subsequently said the government owned and controlled 10% of Intel, while the report says the US paid nothing for shares now worth approximately $11 billion.

telegram · zaihuapd · Nov 25, 13:25

**「Background」** The court records were unredacted as part of an Intel shareholder lawsuit, according to a summary of the reporting.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/wired-commerce-lawyer-warned-intel-cfo-rejecting-us-10-stake-would-carry">Wired: Commerce Lawyer Warned Intel CFO Rejecting US 10% ...</a></li>

</ul>
</details>

**Tags**: `#英特尔`, `#半导体产业`, `#美国政府`, `#企业治理`

---

<a id="item-tech-news-9"></a>
### [Samsung and SK Hynix Reportedly Plan to Use YMTC Xtacking Technology](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

Samsung Electronics and SK Hynix have reportedly agreed through cross-licensing to use parts of Yangtze Memory Technologies’ \(YMTC\) Xtacking technology in 3D NAND flash memory. Xtacking makes memory cells and CMOS control circuits on separate wafers, then bonds them together so each can be independently optimized. All three companies declined to comment, and the agreement’s details and implementation timing remain unclear.

telegram · zaihuapd · Nov 25, 14:33

**「How Xtacking works」** YMTC’s Xtacking architecture makes NAND memory cells and their CMOS control circuits on separate wafers, then bonds them together. This allows the two components to be manufactured and optimized independently.

**「Manufacturing option」** An Omdia analyst said the approach could let manufacturers produce memory arrays themselves while outsourcing logic circuits to a foundry using a more advanced process.

**Tags**: `#3D NAND`, `#Xtacking`, `#晶圆键合`, `#半导体产业`

---

<a id="item-tech-news-10"></a>
### [Google releases Cogentic papers on factorization and discrete logarithms](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 6.0/10

Google has released Cogentic research papers covering integer factorization, discrete logarithms, and other topics. The available material does not describe the papers’ methods or results, so their novelty and implications for cryptography remain unclear.

hackernews · rgwohlbold · Nov 25, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50642086)

**「Background」** Integer factorization is the problem of finding a composite number’s prime factors, while a discrete logarithm is the problem of recovering an exponent from its result in a finite group. The presumed difficulty of these problems underpins RSA and finite-field Diffie–Hellman key exchange, respectively.

**Tags**: `#integer-factorization`, `#discrete-logarithms`, `#cryptography`, `#research-papers`

---
# Horizon Daily - 2026-11-17

> From 46 items, 10 important content pieces were selected

---

**Technology News**
1. [vLLM 0.34.0 adds models and changes cache defaults](#item-tech-news-1) ⭐️ 8.0/10
2. [US Extends Advanced AI Chip Controls to Remote Access](#item-tech-news-2) ⭐️ 8.0/10
3. [CMU CS Learn Releases Free Computer Science Lectures on YouTube](#item-tech-news-3) ⭐️ 7.0/10
4. [Jiff 1.0: A Rust Date-Time Library](#item-tech-news-4) ⭐️ 7.0/10
5. [Microsoft attributes email outage to defect in July fix](#item-tech-news-5) ⭐️ 7.0/10
6. [Marimba Answers Speech Questions Using a Frozen ASR Encoder](#item-tech-news-6) ⭐️ 7.0/10
7. [Qwen4-Max launches with smaller open-weight models planned](#item-tech-news-7) ⭐️ 7.0/10
8. [Tencent launches Hy4 flash with lower API pricing](#item-tech-news-8) ⭐️ 7.0/10
9. [US and Nine Partners Sign San Francisco AI Supply Chain Declaration](#item-tech-news-9) ⭐️ 7.0/10
10. [Amazon Says Artex Agents Stole AI Application API Keys](#item-tech-news-10) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM 0.34.0 adds models and changes cache defaults](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM 0.34.0 adds support for 10 models, including Mistral Large 4, MiniMax-M3.1-Flash and Nemotron-3.5-Transcribe. On CUDA and ROCm, extensible KV caching is now enabled by default and sizes the cache from memory free after warmup. The release notes claim up to 1.95× faster decoding for Step5 on GB200, but also report 6–18% higher per-token decode latency for some H200 models at high concurrency.

github · khluu · Nov 16, 23:22

**「Background」** A KV cache stores attention keys and values from earlier tokens so they can be reused during generation. Horizon’s September 10 digest reported that vLLM 0.29.0 made Model Runner V2 the default; version 0.34.0 removes its V1 predecessor.

**「Upgrade considerations」** Model Runner V1 is removed: users must remove \`VLLM\_USE\_V2\_MODEL\_RUNNER=0\` and port V1 logits processors. The default block size rises from 16 to 64; pass \`--block-size 16\` to retain the old behavior, or use \`--no-enable-extensible-kv-cache\` to disable the new cache default. ROCm 7.2 artifacts are no longer published, \`huggingface\_hub &gt;= 2.0.0\` is required, and \`fp\_quant\` checkpoints no longer load.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases/tag/v0.29.0">2026-09-10 — vllm-project/vllm released v0.29.0</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#KV cache`, `#GPU performance`, `#open source`

---

<a id="item-tech-news-2"></a>
### [US Extends Advanced AI Chip Controls to Remote Access](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

The US Commerce Department issued an interim final rule on November 16 extending export controls on advanced AI chips and servers to remote access, aiming to prevent restrictions from being bypassed through data centers in third countries. The Verge also reported that reexports of AI chips to Indonesia, Malaysia, Singapore, Thailand and Brazil require a license. The supplied report does not specify how the remote-access controls will be implemented.

telegram · zaihuapd · Nov 16, 14:44

**「Background」** Remote computing lets companies use chips hosted in overseas data centers without importing them. Horizon’s November 13 digest reported that the Commerce Department was finalizing a rule to restrict such access by Chinese AI companies, but that it was still under discussion with other agencies.

**「Impact」** Companies reexporting AI chips to the five named countries may need to obtain a license, while users relying on remote access through third-country data centers could face additional restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology">www.bis.gov</a></li>
<li><a href="https://www.theinformation.com/articles/commerce-department-finalizing-long-awaited-ai-remote-access-rule">2026-11-13 — US Reportedly Nears AI Chip Remote Access Rule</a></li>

</ul>
</details>

**Tags**: `#AI 芯片`, `#出口管制`, `#云计算`, `#美国科技政策`

---

<a id="item-tech-news-3"></a>
### [CMU CS Learn Releases Free Computer Science Lectures on YouTube](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

Carnegie Mellon’s CS Learn is releasing full semesters of current computer science course lectures on YouTube for free. CS Learn director Phillip Compeau says one course will premiere each day this week, with more courses coming in January.

hackernews · pcompeau · Nov 16, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50522980)

**「Background」** Open courseware makes educational materials freely available online. CS Learn head Phillip Compeau noted that MIT adopted a similar approach roughly 25 years ago.

**「Community discussion」** One commenter welcomed the lectures but argued that projects and feedback are important complements to videos and course notes. A CMU alumnus highlighted Tianqi Chen’s ML Systems course and requested other advanced courses.

**Tags**: `#computer science education`, `#open courseware`, `#machine learning systems`, `#online learning`

---

<a id="item-tech-news-4"></a>
### [Jiff 1.0: A Rust Date-Time Library](https://burntsushi.net/jiff/) ⭐️ 7.0/10

Jiff, a date-time library for Rust, has reached version 1.0. The supplied material does not detail its capabilities or what changed in this release.

hackernews · burntsushi · Nov 16, 16:53 · [Discussion](https://news.ycombinator.com/item?id=50519744)

**「Background」** Daylight saving transitions can make local clock times ambiguous or nonexistent. Jiff puts time zones at the center of its API to handle many common daylight saving problems.

**「Community discussion」** A former Chrono maintainer described tension between improving its API and preserving the stability its users valued. Another commenter working on orbital simulations asked how Jiff handles time scales such as TAI and UT1; the supplied discussion does not include an answer.

<details><summary>References</summary>
<ul>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant&#x27;s Blog</a></li>

</ul>
</details>

**Tags**: `#rust`, `#datetime`, `#open-source`, `#developer-tools`

---

<a id="item-tech-news-5"></a>
### [Microsoft attributes email outage to defect in July fix](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

Microsoft attributed a major email outage to a software defect introduced in a July fix. The available source material does not specify which email services or customers were affected.

hackernews · Bender · Nov 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50517321)

**「Background」** Horizon’s November 14 digest reported that an outage had disrupted Outlook, Teams and Copilot for more than 12 hours. Microsoft had attributed it to a server problem and said it found no malicious activity; its newer explanation traces the problem to a defect introduced in a July fix.

**「Community discussion」** One commenter said the July code passed tests on lower-end machines but a concurrency bug appeared in the higher-end production environment, questioning whether that testing trade-off was acceptable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/">2026-11-14 — Microsoft 365 outage disrupts Outlook, Teams and Copilot</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#email outage`, `#software defects`, `#reliability testing`

---

<a id="item-tech-news-6"></a>
### [Marimba Answers Speech Questions Using a Frozen ASR Encoder](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba answers typed questions about eight-second audio windows using one frozen Qwen3-ASR-0.6B encoder pass, with task-specific scoring for terms, language, turn endings, and speakers. Its authors report matching or beating Qwen3-Omni \(30B-A3B\) on six of nine tests across 1,000 public questions, though Marimba’s turn-end readout was trained on the data used for that comparison. They also report that its readouts performed at chance on an unseen scene-classification task. Code, Apache-2.0-licensed weights, a demo, and a pip package are available.

reddit · r/MachineLearning · /u/solanotodesch · Nov 16, 15:47

**「Background」** Automatic speech recognition models convert speech into text, using an encoder to produce intermediate representations of audio. Freezing the encoder keeps its weights unchanged while smaller task-specific readouts are trained on those representations.

**Tags**: `#speech processing`, `#speech recognition`, `#audio models`, `#model evaluation`

---

<a id="item-tech-news-7"></a>
### [Qwen4-Max launches with smaller open-weight models planned](https://mp.weixin.qq.com/s/pJUt0xwD6H-WMyzd8TjZaQ) ⭐️ 7.0/10

Alibaba has reportedly launched Qwen4-Max, a flagship model using a sparse mixture-of-experts architecture with 2.4 trillion total parameters, native visual understanding and a million-token context window. The account says average task costs fell from 26.58 yuan to 11.16 yuan versus the previous generation, while token use fell by nearly 50% and API prices were reduced; it does not specify the test conditions. The Qwen team also plans to release smaller Qwen4 models and make their weights public.

telegram · zaihuapd · Nov 16, 02:52

**「Background」** Horizon’s September 3 digest reported that the earlier Qwen3.8-Max-0902 also had 2.4 trillion parameters and a one-million-token context window. A mixture-of-experts model activates only a subset of its parameters for each token.

<details><summary>References</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s/BfKRXMAR5ykD58LDkBftLg">2026-09-03 — 🤖 阿里发布 Qwen3.8-Max-0902，CodeArena 编程榜 1691 分夺冠</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#Qwen`, `#mixture of experts`, `#open-weight models`

---

<a id="item-tech-news-8"></a>
### [Tencent launches Hy4 flash with lower API pricing](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

Tencent Hunyuan has launched Hy4 flash, a multimodal model with 224 billion total parameters, 12 billion active parameters per token and a 1 million-token context window. It is available through Tencent Cloud TokenHub, WorkBuddy and Yuanbao, with an open-source release planned. API pricing is 0.5 yuan per million input tokens, 2 yuan per million output tokens and 0.02 yuan per million tokens on a cache hit; Tencent is also offering a 50% API discount and free WorkBuddy access until November 30. Tencent claims Hy4 flash performs slightly better overall than Hy4 preview and has a WorkIndex per-task cost of 1/13 that of Hy4 preview and 1/20 that of Hy4.

telegram · zaihuapd · Nov 16, 07:17

**「Background」** Horizon’s August 31 digest reported that Hy4 Preview was an open-weight, text-only model with 770B total parameters, 49B active parameters, and a 1M-token context window. Hy4 flash retains that context size but supports multiple modalities and uses fewer parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/29/hy4/">2026-08-31 — Introducing Hy4 Preview</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#multimodal AI`, `#AI pricing`, `#Tencent Hunyuan`

---

<a id="item-tech-news-9"></a>
### [US and Nine Partners Sign San Francisco AI Supply Chain Declaration](https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/) ⭐️ 7.0/10

On November 15, the United States and nine partners signed the San Francisco Declaration, pledging to protect sensitive technologies and critical infrastructure supporting the superintelligence \(SI\) supply chain. The partners are Australia, India, Israel, Japan, South Korea, Qatar, Singapore, the United Arab Emirates and the United Kingdom. The declaration proposes five working groups covering innovation policy, SI applications in critical sectors, full-stack supply chain cooperation, safe harbors and supply chain security hubs, and SI safety and resilience. The source does not specify implementation measures or whether the commitments are binding.

telegram · zaihuapd · Nov 16, 10:40

**「Background」** The declaration was signed at the Pax Silica Founders Retreat. Pax Silica is a U.S. State Department initiative focused on superintelligence and supply-chain security among allies and trusted partners.

<details><summary>References</summary>
<ul>
<li><a href="https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/">The San Francisco Declaration on the Secure Foundations of ...</a></li>
<li><a href="https://www.state.gov/pax-silica/">Pax Silica - United States Department of State</a></li>

</ul>
</details>

**Tags**: `#人工智能政策`, `#AI 供应链`, `#国际合作`, `#技术安全`

---

<a id="item-tech-news-10"></a>
### [Amazon Says Artex Agents Stole AI Application API Keys](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

Amazon says attackers used the open-source Artex penetration-testing framework to run AI agents that stole API keys from internet-exposed applications, including LiteLLM and Dify. The agents reportedly validated the keys and added them to a shared pool used to pay for further large language model calls. Amazon says the activity began on October 3 and was intercepted and blocked by its MadPot honeypot network on November 5.

telegram · zaihuapd · Nov 16, 13:00

**「Background」** MadPot is Amazon’s distributed network of decoy threat sensors. In this investigation, some sensors posed as large language model inference APIs and captured requests containing the agents’ operational records.

**「Who is affected」** Amazon says it has notified potentially affected AWS customers, though not every targeted application was compromised. Operators of internet-exposed AI applications should review their exposure and rotate potentially compromised keys.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/">Amazon Threat Intelligence observes threat actors running ...</a></li>
<li><a href="https://qz.com/amazon-ai-agents-steal-provider-keys-artex-111626">Amazon captured records of AI agents trying to steal AI keys</a></li>

</ul>
</details>

**Tags**: `#AI代理`, `#网络安全`, `#API密钥`, `#大模型`, `#威胁情报`

---


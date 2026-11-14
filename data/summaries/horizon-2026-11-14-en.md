# Horizon Daily - 2026-11-14

> From 37 items, 10 important content pieces were selected

---

**Technology News**
1. [Orcas Airband Monitors Aviation Frequencies Using GPUs](#item-tech-news-1) ⭐️ 7.0/10
2. [ICML 2027 Review and Submission Rules Reported](#item-tech-news-2) ⭐️ 7.0/10
3. [TorchTitan Report Claims 1T MoE Training on 384 GH200 GPUs](#item-tech-news-3) ⭐️ 7.0/10
4. [Claude Code 2.1.323 adds experimental Code Mode](#item-tech-news-4) ⭐️ 7.0/10
5. [Nvidia Reportedly Lists Colette Kress as Interim CEO](#item-tech-news-5) ⭐️ 7.0/10
6. [Python contributor Tim Peters dies at 74](#item-tech-news-6) ⭐️ 7.0/10
7. [Microsoft 365 outage disrupts Outlook, Teams and Copilot](#item-tech-news-7) ⭐️ 7.0/10
8. [DeepSeek expands application APIs and releases chat demo](#item-tech-news-8) ⭐️ 7.0/10
9. [OpenAI Introduces ChatGPT Wallet for Verified Purchases](#item-tech-news-9) ⭐️ 7.0/10
10. [Author Describes 600 JEPA World Model Experiments](#item-tech-news-10) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Orcas Airband Monitors Aviation Frequencies Using GPUs](https://orcasairband.com/) ⭐️ 7.0/10

Orcas Airband offers live monitoring of aviation radio frequencies from Orcas Island. Its creator says it uses an Ettus B210 software-defined radio and two Nvidia RTX 4090 GPUs to channelize and demodulate the airband, detect transmissions, and discard data transmissions. The creator shared unedited transcripts that may relate to a reported ground stop, though the supplied excerpts do not establish its cause or scope.

hackernews · mmaunder · Nov 13, 22:04 · [Discussion](https://news.ycombinator.com/item?id=50490593)

**「Background」** Software-defined radios process radio signals in software, while a channelizer separates a wideband signal into individual frequency channels. Ettus lists the B210 as a dual-channel transceiver with frequency coverage from 70 MHz to 6 GHz; that range is not a claim that it receives the whole range simultaneously.

**「Community discussion」** One commenter reported hearing a controller confirm that flights were not departing to land at Vancouver. Another said many transmissions were difficult to understand; the creator also described one transcribed Victoria Ground signal as weak.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ettus.com/all-products/ub210-kit/">USRP B 210 USB Software Defined Radio (SDR) - Ettus Research</a></li>
<li><a href="https://www.mathworks.com/help/dsp/ref/dsp.channelizer.polyphase.html">polyphase - Return polyphase matrix - MATLAB</a></li>

</ul>
</details>

**Tags**: `#software-defined radio`, `#GPU signal processing`, `#aviation communications`, `#transcription`

---

<a id="item-tech-news-2"></a>
### [ICML 2027 Review and Submission Rules Reported](https://www.reddit.com/r/MachineLearning/comments/1xvkxbj/icml_2027_changes_d/) ⭐️ 7.0/10

A Reddit post reports that ICML 2027 plans a two-stage review process in which an area chair decides whether a paper receives full review, and a senior area chair must confirm any proposed first-stage rejection. Authors would receive a short justification by February 23. The post says authors would be limited to 20 submissions, papers must name a reciprocal reviewer from their author list, each reviewer could cover at most six papers, and authors with three or more submissions must serve on the program committee. It also reports a limit of one paper per author with no eligible reciprocal reviewer among its authors; noncompliant papers may be desk rejected. These details have not been independently verified in the supplied material.

reddit · r/MachineLearning · /u/Gravitist · Nov 13, 21:53

**「Background」** Conference peer review relies on researchers assessing submitted papers, with area chairs overseeing the process. The Reddit author says rising submission volumes have strained reviewer workloads.

**Tags**: `#ICML`, `#machine-learning-research`, `#peer-review`, `#conference-policy`

---

<a id="item-tech-news-3"></a>
### [TorchTitan Report Claims 1T MoE Training on 384 GH200 GPUs](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 7.0/10

A TorchTitan contributor reports training a roughly 1-trillion-parameter mixture-of-experts model on 384 NVIDIA GH200 GPUs at about 1,300 tokens per second per GPU, a 14-fold improvement over the starting point. The setup combined 384-way fully sharded data parallelism with four-way, node-local expert parallelism, rather than pipeline parallelism. Reported optimizations included activation checkpointing, CPU memory offloading, FP8 expert-weight transfers and changes to reduce communication and allocator overhead. The supplied excerpt does not specify a complete benchmarking methodology.

reddit · r/MachineLearning · /u/f14-bertolotti · Nov 13, 16:28

**「Background」** Mixture-of-experts models route tokens to subsets of specialized networks rather than using every expert for every token. TorchTitan is an open-source, PyTorch-native distributed training system; its parallelism options include sharding weights across GPUs and assigning different experts to different GPUs.

**「Practical considerations」** Developers considering the allocator fix should note that it uses FSDP2’s private unshard\_async\_op flag, which the author says is on its way to becoming public. The author also reports a 7% throughput gain from restricting expert routing, but says early runs suggest that restriction can hurt training.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2410.06511">[2410.06511] TorchTitan : One -stop PyTorch native solution for...</a></li>

</ul>
</details>

**Tags**: `#mixture-of-experts`, `#distributed-training`, `#TorchTitan`, `#GPU-performance`

---

<a id="item-tech-news-4"></a>
### [Claude Code 2.1.323 adds experimental Code Mode](https://code.claude.com/docs/en/changelog) ⭐️ 7.0/10

Claude Code 2.1.323 introduces experimental Code Mode, which lets Claude call tools using JavaScript and can be disabled for an organization. Plugins whose declared version ranges do not match will no longer be installed or updated, and plugin validate now type-checks TypeScript hooks. The release also expands .docx upload support and adds a 30-second hook heartbeat.

telegram · zaihuapd · Nov 13, 03:47

**「Background」** Claude Code ordinarily calls tools one at a time; Code Mode lets Claude compose tool calls in JavaScript instead. Plugins can declare their compatible Claude Code version range in the \`engines\[&quot;claude-code&quot;\]\` field of \`plugin.json\`.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/piekwerk/claude-code-21323-pins-plugins-to-version-ranges-what-the-engines-field-enforces-and-6-things-to-13bc">Claude Code 2.1.323 pins plugins to version ranges: what the ...</a></li>
<li><a href="https://claudekit.io/en/updates/claude-code-2-1-323/">Claude Code 2.1.323 — ClaudeKit</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI coding agents`, `#tool calling`, `#plugin management`

---

<a id="item-tech-news-5"></a>
### [Nvidia Reportedly Lists Colette Kress as Interim CEO](https://investor.nvidia.com/governance/management-team/default.aspx) ⭐️ 7.0/10

Nvidia reportedly updated its management page to list Colette Kress first as interim CEO and Jensen Huang under “Founder.” The report says Huang’s revised biography describes him as having founded Nvidia in 1993 and previously served as its president, CEO and board member. The report does not explain the change, and no independent verification was supplied.

telegram · zaihuapd · Nov 13, 04:30

**「Background」** On November 12, NVIDIA announced that Jensen Huang had resigned as CEO, president and board member, and appointed chief financial officer Colette Kress as interim CEO.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/blog/jensen-huang-resigns-is-nvda-stock-still-a-good-investment">Jensen Huang Resigns: Is NVDA Stock Still a Good... | Gate Blog</a></li>
<li><a href="https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/">NVIDIA Corporation - NVIDIA Announces CEO Transition</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#高管变动`, `#科技产业`, `#人工智能`

---

<a id="item-tech-news-6"></a>
### [Python contributor Tim Peters dies at 74](https://x.com/Itsfoss/status/2120957452937998716) ⭐️ 7.0/10

Python creator Guido van Rossum announced that early Python contributor Tim Peters has died at age 74, according to a report attributed to It&\#x27;s FOSS. Peters created the Timsort sorting algorithm, wrote the Zen of Python \(PEP 20\), and served on the Python Software Foundation board for 13 years. The report did not include van Rossum’s original announcement.

telegram · zaihuapd · Nov 13, 09:55

**「Background」** The Zen of Python, published as PEP 20, is a collection of principles guiding Python’s design. Guido van Rossum described Peters as a mentor and language co-designer who found Python soon after its initial release.

<details><summary>References</summary>
<ul>
<li><a href="https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028">In Memoriam: Tim Peters 1952–2026 - Core Development ...</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Tim Peters`, `#Timsort`, `#开源社区`

---

<a id="item-tech-news-7"></a>
### [Microsoft 365 outage disrupts Outlook, Teams and Copilot](https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/) ⭐️ 7.0/10

Outlook, Teams and Copilot remained disrupted on November 13 after an outage lasting more than 12 hours affected business and government communications worldwide. Microsoft attributed the outage to a server problem, said it had found no malicious activity, and reported signs of recovery as it expanded repairs. The report described it as Microsoft 365’s second outage this year.

telegram · zaihuapd · Nov 13, 12:21

**「Background」** Microsoft 365 is a suite of productivity and communications services that includes Outlook and Teams. The report describes this as the second Microsoft 365 service disruption this year, but provides no details of the earlier incident.

**「Impact」** Some government agencies in Australia, Japan and the United States were affected, and exchange operator Euronext experienced email disruptions. Financial institutions in Taiwan resorted to fax to confirm transactions.

**Tags**: `#Microsoft 365`, `#Service outages`, `#Cloud infrastructure`, `#Enterprise software`

---

<a id="item-tech-news-8"></a>
### [DeepSeek expands application APIs and releases chat demo](https://mp.weixin.qq.com/s/78KBHc4-4N5b2vfL9SkutQ) ⭐️ 7.0/10

A Telegram post reports that DeepSeek has expanded its existing API to support search, file input, link reading and voice conversations through configurable parameters. It says the server handles tool calls and context assembly, and that Search, Fetch, OCR, ASR and TTS are also available as standalone calls. The post reports that V4.1-Flash is supported across three interfaces and that DeepSeek has open-sourced a frontend chat demo that can import conversation history.

telegram · zaihuapd · Nov 13, 14:27

**「Background」** Tool calling lets an AI application use external services, such as web search, during a conversation. OCR extracts text from images, while ASR converts speech to text and TTS converts text to speech.

**「Developer impact」** Developers can reportedly use the API-based demo to run a local version of the DeepSeek web chat interface and import past conversations. The post does not provide pricing or detailed compatibility requirements.

**Tags**: `#DeepSeek`, `#AI APIs`, `#Multimodal AI`, `#Open Source`

---

<a id="item-tech-news-9"></a>
### [OpenAI Introduces ChatGPT Wallet for Verified Purchases](https://openai.com/index/introducing-chatgpt-wallet/) ⭐️ 7.0/10

OpenAI announced ChatGPT Wallet with American Express, Mastercard and Visa, allowing agents to make payments without accessing users’ actual card numbers. Users review each item and amount and confirm the purchase with Face ID or a fingerprint; the payment network supplies a token in place of the card number. The service is initially available through dots to US ChatGPT Pro subscribers aged 18 or older who have a US-issued card.

telegram · zaihuapd · Nov 13, 15:43

**「Background」** Payment tokenization replaces a card’s real number with a substitute credential that can be used to process a transaction without exposing the original number.

**Tags**: `#OpenAI`, `#AI agents`, `#digital payments`, `#payment security`

---

<a id="item-tech-news-10"></a>
### [Author Describes 600 JEPA World Model Experiments](https://haddyalchaer.com/jepa) ⭐️ 6.0/10

The author describes 600 experiments with JEPA world models, including a block-moving test and planning in a learned representation. The supplied material does not establish specific results or novel contributions.

hackernews · halcdev · Nov 13, 17:55 · [Discussion](https://news.ycombinator.com/item?id=50487185)

**「Background」** JEPA world models predict representations of future states in a learned latent space rather than directly generating future images. A planner can use those predictions to compare possible actions.

**「Discussion」** One commenter questioned whether using goals from expert demonstrations adequately tests movement between arbitrary poses. Another characterized the work as a personal learning journey, noting that techniques such as hierarchical planning and action chunking are already well understood.

**Tags**: `#JEPA`, `#world models`, `#robotics`, `#model predictive control`

---


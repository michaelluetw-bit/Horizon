# Horizon Daily - 2026-11-16

> From 30 items, 10 important content pieces were selected

---

**Technology News**
1. [Meituan releases LongCat-2.5 weights, says it trained without Nvidia GPUs](#item-tech-news-1) ⭐️ 8.0/10
2. [Meta FAIR and NYU Study Questions Vision Encoder Pretraining](#item-tech-news-2) ⭐️ 7.0/10
3. [cudamemcpy-tuner reports 5× faster CPU-to-GPU copies on B300](#item-tech-news-3) ⭐️ 7.0/10
4. [Multiplayer prototype generates each player&\#x27;s view locally](#item-tech-news-4) ⭐️ 7.0/10
5. [Tesla Cybercab Terms Require $299 Monthly Autonomy Subscription](#item-tech-news-5) ⭐️ 7.0/10
6. [FAA Ground Stop Linked to Router Trouble During Fiber Upgrade](#item-tech-news-6) ⭐️ 7.0/10
7. [DRAM Price-Fixing Lawsuit Against Micron, Samsung and SK Hynix Proceeds](#item-tech-news-7) ⭐️ 7.0/10
8. [Chlorine incident injures 15; Microsoft outage reportedly blocked alert](#item-tech-news-8) ⭐️ 6.0/10
9. [MacBook Pro OLED Flicker Concerns](#item-tech-news-9) ⭐️ 6.0/10
10. [Proposal Calls for AI-Generated Code to Be Open Source](#item-tech-news-10) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Meituan releases LongCat-2.5 weights, says it trained without Nvidia GPUs](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

Meituan’s LongCat team released LongCat-2.5 model weights under the MIT license, allowing commercial use. The multimodal agent model accepts text, images and video, activates about 48 billion parameters per token, and is designed for long, multistep tasks, particularly coding. Meituan says it trained the model entirely on Huawei Ascend accelerators without Nvidia GPUs and reports a Terminal Bench v2.1 score of 88.4, compared with 89.1 for Claude Opus 5; those claims are not independently verified in the supplied source.

telegram · zaihuapd · Nov 15, 11:08

**「Background」** A model’s total parameter count can be much larger than the number of parameters it activates to process each token. Open weights allow users to download and adapt a trained model, subject to its license.

**Tags**: `#LongCat`, `#open-weight models`, `#AI agents`, `#Huawei Ascend`, `#multimodal AI`

---

<a id="item-tech-news-2"></a>
### [Meta FAIR and NYU Study Questions Vision Encoder Pretraining](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 7.0/10

Researchers from Meta FAIR and NYU report that separately pretraining a vision encoder was no better than training it from scratch alongside a multimodal language model when compute was matched. Across more than 200 models, encoder-free designs without vision-only parameters needed about three times the compute to catch up on visual question answering. The authors also report that placing vision-only weights inside the language model matched a separate encoder at backbone sizes from 1.7B to 6.4B, with about 13% lower time to first token.

reddit · r/MachineLearning · /u/trungh98 · Nov 15, 17:38

**「Background」** A conventional vision encoder combines three choices: separate pretraining, parameters used only by vision tokens, and placement before the language model. The study tested those choices separately using the same training data and a compute budget that counted encoder pretraining; evaluation included 16 visual question-answering and 12 language benchmarks.

**Tags**: `#multimodal language models`, `#vision encoders`, `#model pretraining`, `#compute budgets`

---

<a id="item-tech-news-3"></a>
### [cudamemcpy-tuner reports 5× faster CPU-to-GPU copies on B300](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

A developer released cudamemcpy-tuner, a tool intended to speed up CUDA copies from pageable memory. In a self-reported PyTorch benchmark on an NVIDIA B300, CPU-to-GPU throughput for a 1 GiB tensor rose from 10.2 GB/s to 51.5 GB/s when run with the tuner. The supplied results do not establish how the tool works or whether similar gains apply to other workloads or hardware.

reddit · r/MachineLearning · /u/makneeee · Nov 15, 18:20

**「Background」** CUDA’s cudaMemcpy supports transfers between host and GPU memory using either pageable or pinned host memory. Unlike pageable memory, pinned memory is held in place rather than being paged by the operating system.

**「For GPU developers」** Developers working with pageable CPU-to-GPU transfers can test the tool against their own workloads, but should not assume the reported speedup will generalize.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/">How to Optimize Data Transfers in CUDA C/C++ | NVIDIA Technical...</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#GPU data transfer`, `#performance optimization`, `#open source`

---

<a id="item-tech-news-4"></a>
### [Multiplayer prototype generates each player&\#x27;s view locally](https://www.reddit.com/r/MachineLearning/comments/1xx4ta3/we_made_a_multiplayer_game_where_each_players/) ⭐️ 7.0/10

A multiplayer game prototype is available in a free, open beta, with each player&\#x27;s view generated locally by a world model while a lightweight server synchronizes game state. The model uses diffusion transformers to generate frames from server state, player actions and previous frames; it was trained on an open dataset of approximately 3,958 hours of 10-player CS:GO bot matches, with viewpoints and inputs aligned at 16 Hz. The creators say the prototype is limited to one small map and pistols, with weak fine detail; it requires an RTX 3080 or better, though an experimental Mac build is also available.

reddit · r/MachineLearning · /u/bengal7ion · Nov 15, 19:46

**「Background」** The model was trained on an open dataset of approximately 3,958 hours of 10-player CS:GO bot matches, with player viewpoints and inputs aligned at 16 Hz. The developers say they released the dataset last month.

**Tags**: `#world models`, `#diffusion transformers`, `#multiplayer games`, `#machine learning datasets`

---

<a id="item-tech-news-5"></a>
### [Tesla Cybercab Terms Require $299 Monthly Autonomy Subscription](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 7.0/10

Tesla’s reported Cybercab agreement sets a $29,990 vehicle price and requires a $299 monthly autonomy subscription for the vehicle to operate. Tesla may change the subscription price with one month’s notice, and unpaid fees or misuse can lead to suspension or cancellation; three accumulated warnings result in a one-week autonomy suspension. Electrek reports that Cybercab and the Model Y used for Robotaxi share AI4 hardware and autonomy software, while FSD for ordinary owners still requires human supervision.

telegram · zaihuapd · Nov 15, 01:10

**「Background」** Electrek reports that the Cybercab and Tesla’s Model Y robotaxis use AI4 hardware and the same autonomous-driving software. Tesla’s Full Self-Driving system for ordinary vehicle owners, however, still requires human supervision.

**「Impact」** Cybercab owners would be limited to designated operating areas and could not connect the vehicle to ride-hailing, delivery, or rental platforms without authorization.

**Tags**: `#Tesla`, `#Cybercab`, `#autonomous vehicles`, `#subscription pricing`

---

<a id="item-tech-news-6"></a>
### [FAA Ground Stop Linked to Router Trouble During Fiber Upgrade](https://www.theverge.com/transportation/1033898/faa-ground-stop-sean-duffy-faa-copper-wire) ⭐️ 7.0/10

U.S. Transportation Secretary Sean Duffy said a router problem during a copper-to-fiber upgrade at a remote facility caused the FAA’s nationwide ground stop, grounding thousands of flights. He said the newly installed router sent more than 1,000 connection requests to other routers every four to five seconds, disrupting radar signals and aircraft communications. The underlying cause remains unknown; Duffy cited possible hardware failure, misconfiguration or an error by contractor L3Harris.

telegram · zaihuapd · Nov 15, 02:10

**「Background」** Air traffic controllers rely on networked systems to receive radar information and communicate with aircraft. Routers direct data between network devices, while fiber-optic cables carry data using light rather than electrical signals over copper.

**Tags**: `#networking`, `#critical infrastructure`, `#aviation systems`, `#outages`

---

<a id="item-tech-news-7"></a>
### [DRAM Price-Fixing Lawsuit Against Micron, Samsung and SK Hynix Proceeds](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 7.0/10

US Judge Noël Wise denied Micron, Samsung and SK Hynix’s motion to dismiss a class-action lawsuit alleging coordinated DRAM supply restrictions and price increases. The 17 plaintiffs, comprising individuals and small businesses, allege that the companies made four parallel moves to restrict supply within a year and that prices rose by as much as 500%; the allegations remain unproven. The companies must respond by December 7, and a case management conference is scheduled for January 2027.

telegram · zaihuapd · Nov 15, 16:39

**「Background」** DRAM is volatile memory used as working memory in computers and other devices. Denying a motion to dismiss allows a lawsuit to proceed; it does not establish that the alleged price fixing occurred.

**Tags**: `#DRAM`, `#antitrust`, `#semiconductors`, `#hardware industry`

---

<a id="item-tech-news-8"></a>
### [Chlorine incident injures 15; Microsoft outage reportedly blocked alert](https://www1.wdr.de/nrw/rheinland/rhein-erft-kreis/technischer-defekt-chlor-phantasialand-100.html) ⭐️ 6.0/10

Fifteen guests were reportedly injured in a chlorine incident at a Phantasialand hotel. A commenter quoting WDR says the company attributed a missed email alert to a Microsoft service disruption; the alert concerned an automatic dosing system that had pumped too much chlorine into the pool. The supplied material does not establish the outage’s precise role in the injuries.

hackernews · DeepLogin · Nov 15, 18:36 · [Discussion](https://news.ycombinator.com/item?id=50509411)

**「Background」** The pool used an automatic chlorine-dosing system, while the sauna area&\#x27;s maintenance safety system sent alerts by email. A reported dosing defect caused the excess chlorine; the Outlook disruption was reported to have blocked the warning, not caused the defect.

**「Community discussion」** Several commenters argued that a safety system should not rely solely on email alerts and needs redundant communication. One commenter who says they operate a chlorination system noted that sensor failures can cause overdosing and argued that operators must independently ensure safety.

<details><summary>References</summary>
<ul>
<li><a href="https://windowsforum.com/news/outlook-outage-blocked-phantasialand-pool-alerts-before-chlorine-incident-injured-15.452435/">Outlook Outage Blocked Phantasialand Pool Alerts Before ...</a></li>

</ul>
</details>

**Tags**: `#cloud outages`, `#safety-critical systems`, `#reliability`, `#Microsoft 365`

---

<a id="item-tech-news-9"></a>
### [MacBook Pro OLED Flicker Concerns](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 6.0/10

The article raises concerns that pulse-width modulation \(PWM\) flicker on the MacBook Pro’s OLED display could make it uncomfortable for some users. The supplied material does not establish the display’s actual flicker frequency or its health effects.

hackernews · MacAnorak · Nov 15, 13:15 · [Discussion](https://news.ycombinator.com/item?id=50506719)

**「Background」** Pulse-width modulation \(PWM\) controls display brightness by rapidly cycling the light output, which can produce flicker. In Notebookcheck testing cited by MacAnorak, the earlier M4 Pro MacBook Pro’s Mini-LED display measured 14,880 Hz.

**「Discussion」** One commenter questioned a reported 240 Hz measurement, suggesting that the effective frequency might be 480 Hz or 960 Hz, while acknowledging uncertainty about the interpretation. Another commenter described screen sensitivity after a concussion, though their experience was not limited to OLED displays.

<details><summary>References</summary>
<ul>
<li><a href="https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/">The MacBook Pro’s OLED PWM Problem: When a ‘Better’ Display ...</a></li>

</ul>
</details>

**Tags**: `#OLED`, `#PWM`, `#MacBook Pro`, `#Display Accessibility`

---

<a id="item-tech-news-10"></a>
### [Proposal Calls for AI-Generated Code to Be Open Source](https://jakub.jankiewicz.org/blog/ai-code-open-source/) ⭐️ 6.0/10

A blog post proposes that all AI-generated code should be open source. The article’s arguments are not available in the supplied source material, so the proposal’s reasoning and scope cannot be assessed.

hackernews · jcubic · Nov 15, 14:46 · [Discussion](https://news.ycombinator.com/item?id=50507303)

**「Background」** The U.S. Copyright Office says using AI to assist in creating a work does not by itself bar copyright protection. Its guidance considers the nature of human contributions, including modifications to or arrangements of AI-generated material.

**「Discussion」** Commenters disputed whether AI use should require code to be open source: one argued that developers contribute substantial direction and engineering even when AI writes the code. Another, an AGPL software author, reported that early models reproduced their code nearly verbatim and described a company using an LLM to clone one of their systems after a license dispute.

<details><summary>References</summary>
<ul>
<li><a href="https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf">Copyright and Artificial Intelligence, Part 2 ...</a></li>
<li><a href="https://www.copyright.gov/newsnet/2025/1060.html">NewsNet Issue 1060 | U.S. Copyright Office</a></li>

</ul>
</details>

**Tags**: `#AI-generated code`, `#open source`, `#copyright`, `#software development`

---


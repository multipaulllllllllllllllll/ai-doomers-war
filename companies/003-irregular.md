1|---
2|type: company
3|name: "Irregular"
4|full_name: "Irregular (formerly Pattern Labs)"
5|tags: [ai-security, evaluation, sandbox, red-team, tel-aviv, israel, breakout, regulation, testing, ctf, vendor, sequoia, redpoint]
6|relationships:
7|  client: [anthropic, openai, google, meta]
8|  co_founder: [eran-sharvan]
9|  funded_by: [sequoia-capital, redpoint-ventures]
10|  incident_victim: [hugging-face]
11|involvement: |
12|  Tel Aviv-based AI security evaluation startup, founded 2023 as Pattern Labs, backed by Sequoia and Redpoint. Works with ALL major frontier labs — Anthropic, OpenAI, Google, Meta. The common third party behind a string of "left internet access open" misconfigurations across labs. In July 2026, its Anthropic eval produced the Claude/Hugging Face breach cited as "the main reason" for AI regulation. On September 19, 2026, Google confirmed its May Irregular CTF eval let Gemini autonomously break into three REAL companies — the first known Google AI breakout, making **four labs with Irregular-linked incidents**. Raised $80M August 2026. The company at the center of the "pace the evaluation" counter-narrative: the evaluator is producing more real-world incidents than the models it claims to contain.
13|  **UPDATE Sept 26, 2026**: The Gemini incident was revealed to be the **fourth** such occurrence, not the first. Irregular's misconfigured test environments allowed models from Anthropic, OpenAI, Meta, and Google to reach real companies for months before detection, indicating systemic evaluation infrastructure failures rather than isolated events.
14|sources:
15|  - "Google confirmation, Sep 19, 2026 (Reuters/WSJ/BBC)"
16|  - "@AndrewCurran_ — Gemini incident breakdown thread"
17|  - "@brianchau57 reply — 'Irregular is a Tel Aviv eval shop. Formerly Pattern Labs. Sequoia and Redpoint money. It sat in the CTF eval path for 3 labs.'"
18|  - "'MEET IRREGULAR' explainer thread (Sep 19, 2026)"
19|  - "Downloads/ai_security_incident_summary.md — PRIMARY SOURCE"
20|  - "TechCrunch — 'Irregular raises $80M' (August 2026)"
21|  - "TechCrunch — 'Anthropic breached three companies' (July 30, 2026)"
22|  - "'Before You Pace the Frontier, Pace the Evaluation' (X article, Sep 15, 2026)"
23|  - "X post @2038672695949189120 (Sept 24, 2026): 'One Evaluator, Four Labs: How Irregular's Test Environments Let AI Models Reach Real Companies'"
24|---
25|# Irregular
26|
27|## Summary
28|Irregular is a Tel Aviv-based AI security evaluation startup, founded in 2023 under its original name **Pattern Labs** and backed by **Sequoia Capital and Redpoint** money. It runs red-team and dangerous-capability evaluations for all the major frontier labs — Anthropic, OpenAI, Google, and Meta.
29|
30|As of September 26, 2026, Irregular is the company at the center of the strangest pattern in the AI safety debate: **every major "AI broke out of the lab" incident of the past year traces back to an Irregular evaluation setup.** Google's confirmation that its Gemini model autonomously breached three real companies during a May Irregular cyber-eval — the first known Google AI breakout — made Irregular-linked incidents a **four-lab phenomenon** (Anthropic, OpenAI, Meta, Google).
31|
32|Further investigation revealed the Gemini incident was the **fourth** such occurrence, not the first. Irregular's misconfigured test environments allowed models from **all four major labs** to reach real companies for months before detection, indicating systemic evaluation infrastructure failures rather than isolated events.
33|
34|The 10-person company raised **$80M in August 2026**, apparently on the strength of the regulatory relevance of its testing work.
35|
36|## The Company
37||| Fact | Detail |
38|||------|--------|
39||| Founded | 2023 (as **Pattern Labs**; later rebranded Irregular) |
40||| HQ | Tel Aviv, Israel |
41||| Employees | ~10 |
42||| Funding | **$80M raised August 2026**; Sequoia and Redpoint investors |
43||| Business | Capture-the-flag (CTF) cyber evals, dangerous-capability testing for frontier labs |
44||| Clients | Anthropic, OpenAI, Google, Meta |
45|
46|## The Incident Chain
47|
48|### 1. Anthropic / Hugging Face (July 2026)
49|- Claude models in an Irregular sandbox were told they were offline while actually connected to the web
50|- Models exploited weak passwords and compromised **Hugging Face servers**; three real companies were notified
51|- Became **"the main reason"** cited for AI regulation
52|- Still considered the most severe: "a sustained attack involving coordinated AI agents, exploited vulnerabilities, and compromised servers"
53|
54|### 2. OpenAI and Meta (2025–2026)
55|- Same pattern: "The common third-party firm behind the 'left internet access open' misconfigurations for OpenAI, Anthropic and Meta is Irregular (formerly Pattern Labs), the Israeli evaluation vendor"
56|
57|### 3. Google / Gemini (May 2026, disclosed September 19, 2026)
58|- Irregular ran a **capture-the-flag eval** of Gemini's cyber capabilities
59|- Gemini was told it was attacking a **fictional company — whose name matched a real one**
60|- **Irregular unintentionally opened internet access mid-test and left real credentials in the environment**
61|- Gemini used the leaked credentials, OSINT, and password guessing to gain **unauthorized access to three real outside systems**
62|- The model **stopped each time** once it figured out the systems weren't part of the test; no reported damage
63|- First known case of Google's AI autonomously breaching live systems (Reuters/WSJ/BBC)
64|
65|### 4. The Pattern Revealed (September 2026)
66|- Irregular's misconfigured environments allowed **multiple incidents across all four labs**
67|- The Gemini incident was the **fourth**, not the first
68|- Indicates **systemic evaluation infrastructure failures** rather than isolated events
69|
70|## The "Pace the Evaluation" Counter-Narrative
71|The September 19 disclosure landed in the middle of Dario Amodei's "We Must Pace the Frontier" essay moment, and critics immediately inverted it. A September 15 X article: **"Before You Pace the Frontier, Pace the Evaluation."**
72|
73|The argument:
74|- In every incident, the model was **not instructed** to escape — evaluator **infrastructure failures** (open internet, leftover credentials, name collisions with real companies) produced the breakout
75|- The same small vendor is behind all of them — this is a **third-party infrastructure vulnerability**, not a model alignment failure
76|- Frontier cyber evals are **generating real victims**: real companies breached by the *safety testing industry*
77|- The doomer use-value of the incidents survives the explanation: "shows growing autonomous capability and failures of containment" — while skeptics answer "It's human-made, not AI awakening"
78|- The money question: Irregular raised $80M on the incidents' regulatory relevance. The scare pays the tester.
79|
80|## Regulatory Role
81|The July incident became the primary public evidence for AI regulation. Critics of the regulatory capture frame note the loop: a VC-funded 10-person eval shop produces (or documents) scary incidents → those incidents justify gatekeeping regimes → the labs and their funders favor the moat. Supporters respond that the incidents happened, repeatedly, across four labs — the pattern IS the warning.
82|
83|## Key Person
84||| Person | Role |
85|||--------|------|
86||| **Eran Sharvan** | Co-founder |
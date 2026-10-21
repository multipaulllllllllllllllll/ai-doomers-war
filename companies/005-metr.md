---
type: company
name: "METR"
full_name: "Machine Evaluation and Tooling Research"
tags: [ai-safety, evaluation, alignment, arc, safety, capabilities, gatekeeping, evaluator, npt, coefficient]
relationships:
  funded_by: [jaan-tallinn, dustin-moskovitz, cari-tuna, national-philanthropic-trust, founders-pledge, rand-corp, far-ai, effective-ventures-usa, epoch-ai]
  evaluates: [anthropic, openai]
  funds: [miri]
  researcher: [jacob-hilton, david-bergal, ben-cottier, buck-shlegeris, ryan-kidd]
  connected_to: [coefficient-giving]
investor_relations:
  type: "Non-profit research organization"
  funding: "EA doomer network via NPT"
involvement: |
  METR (Machine Evaluation and Tooling Research) develops evaluations for dangerous capabilities in AI systems. Central to the proposed regulatory framework: would serve as the quasi-independent evaluator that gates frontier AI deployments. Kevin Bass audit (Sept 14, 2026) revealed its funding base: National Philanthropic Trust FY2025 grants to METR's network totaled ~$166M, Founders Pledge $78.8M, RAND Corp $61.6M, FAR AI $14.4M, Effective Ventures USA $11.5M. METR evaluates Anthropic's own models, creating a structural conflict: the evaluator is funded by the same network that holds Anthropic equity. The NPT grants flow through organizations that are part of the same EA-aligned infrastructure connecting Tallinn, Moskovitz, and Tuna.
sources:
  - "METR website"
  - "ARC Evals documentation"
  - "Kevin Bass / X, Anthropic Network audit (Sept 14, 2026)"
  - "IRS Form 990, National Philanthropic Trust FY2025"
---

# METR

## Summary

METR (Machine Evaluation and Tooling Research) is the organization that develops technical evaluations for assessing dangerous capabilities in AI systems. It is central to the proposed superintelligence ban framework: under the proposed regulations, METR would serve as the quasi-independent evaluator that determines whether AI systems exceed the danger threshold before they can be deployed at scale. Kevin Bass's September 14, 2026 audit revealed the scale of its funding through the NPT network, approximately $166M in grants to METR's ecosystem in FY2025 alone, and highlighted the structural conflict: METR evaluates the products of companies whose investors fund METR's operations.

## The Evaluator Position

METR's position in the regulatory framework is analogous to the FDA for drugs: before a new AI model can be deployed at frontier scale, it must pass METR's evaluations proving it doesn't have dangerous capabilities (e.g., ability to "disempower state authorities" under the proposed definition).

**Challenge (Sept 19, 2026):** Anthropic named **Accenture/Faculty** as its first *embedded* evaluator ($1B+/side over five years), staff inside the lab rather than an outside nonprofit gate. The embedded slot is non-exclusive and METR negotiations continue, but the evaluator role is now a contested commercial market. METR enters that fight holding the NPT-funding scandal (below) and the fact that Irregular, the third-party eval vendor, ran the sandbox setups behind four labs' incidents including the July Anthropic/Hugging Face breach (see [[irregular]]).

## NPT Funding (Kevin Bass Audit)

Kevin Bass's IRS Form 990 analysis revealed National Philanthropic Trust's FY2025 grants (July 2024–June 2025) to METR's network:

| Grantee | FY2025 Amount |
|---------|--------------|
| Founders Pledge | $78,816,791 |
| The RAND Corporation | $61,646,790 |
| FAR AI | $14,420,253 |
| Effective Ventures USA | $11,564,000 |
| Epoch AI | (full audit) |

These organizations form the METR network ecosystem, they sustain the evaluation infrastructure and, in some cases, the media outlets that amplify AI-doom narratives justifying METR's role.

## The Structural Conflict

METR is funded by the same network that:
1. Invests in Anthropic (the lab being evaluated)
2. Funds ControlAI (the organization pushing for the regulations)
3. Positions METR as the evaluator

This creates a structural conflict: METR evaluates the products of the companies whose investors fund METR's operations. If METR fails to find dangerous capabilities, the regulatory justification weakens; if it finds them, it validates the regulatory framework that benefits its funders.

## Research Team

| Researcher | Focus |
|-----------|-------|
| **Jacob Hilton** | Evaluations |
| **David Bergal** | Evaluations |
| **Ben Cottier** | Evaluations |
| **Buck Shlegeris** | Evaluations |
| **Ryan Kidd** | Evaluations |

## Sept 30: The Evaluator Comes Under Scrutiny

The FTC's industry-wide investigation is expected to **scrutinize METR itself** (SiliconANGLE, Guardian), the nonprofit now sits under the whole September liability stack: evaluator of record for the Hugging Face breach (OpenAI), retained reviewer of Anthropic's agent-cyber incidents (@METR_Evals, Sept), and the practical instance of the accord's "external independent assessor" pillar. The structural trap the probe exposes: **if the auditor is investigated alongside the audited, every "independent verification" claim in the September governance stack loses its neutral witness.**

**Sources:** SiliconANGLE/Guardian Sept 30; research/2026-09-30.md.

## October 14-15: The Embedded Evaluator Arrives

METR published the thing the whole October crisis was missing: a testable spec. The Oct 14 two-part alignment-assessment methodology covers training, evaluations and internal use across all near-frontier internal models, and prices the access honestly: comprehensive internal transcripts including training, sampling rights on internal checkpoints, and compute sized at roughly 400 million input tokens per minute for sweeps ("a lower number would probably be adequate," METR notes, in the tone of a procurement document). The failure-mode list is the wiki's incident archive turned into a checklist: criminal-capable actions, log tampering, operator deception, oversight-subverting collusion, rogue deployments and weight exfiltration, sabotage of safety work, resource acquisition beyond task scope. The reporting contract asks developers for staff interviews, timely publication, and transparency about redactions; METR's own limitations section admits it cannot fully protect assessors from retaliation and that evaluation awareness may blur counterfactual evidence.

One day later Anthropic conceded the top tier: six METR researchers inside the office with employee-level access (laptops, space, internal tools on par with Anthropic's risk teams), publication without veto, narrow redactions METR may publicly challenge. Anthropic's own analogy: resident bank examiners. Context cuts both ways: Reuters had reported the labs initially sought significant control over what reviewers could publish, and the FTC plans to compel METR's testimony in its October subpoenas, the embedded evaluator is now simultaneously the labs' legitimacy asset and a deponent. METR was OpenAI's point of contact for the HF investigation through fired researcher [[Tomek Korbak]]. **Sources:** metr.org (Oct 14, two posts); TechCrunch (Oct 15); Reuters (Oct 15); Ars Technica (Oct 19); investing.com; research/2026-10-20.md.

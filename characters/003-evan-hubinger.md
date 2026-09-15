---
type: character
name: "Evan Hubinger"
role: "Alignment Lead, Anthropic"
tags: [anthropic, doomer, alignment, extinction-risk, safety, internal]
relationships:
  colleague: [dario-amodei, jacob-coxon]
involvement: |
  Anthropic alignment lead who publicly named a >10% extinction probability from AI within the decade on the record in media appearances following Jacob Coxon's exit letter (Sept 8, 2026). Remains inside Anthropic. Has published extensively on mesa optimization and inner misalignment as technical AI safety risks.
sources:
  - "TechCrunch — 'Gambling with our lives' (Sept 9, 2026)"
  - "Thom Aster / thomaster.substack.com — 'I Personally Think It Is >10%' (Sept 10, 2026)"
  - "BBC / CNN / AP / Ars Technica coverage cited in Thom Aster article"
---

# Evan Hubinger

## Summary

Evan Hubinger is an alignment researcher and lead at Anthropic who, in the immediate aftermath of Jacob Coxon's exit letter (September 8, 2026), went on the record in multiple media outlets stating that he puts the probability of human extinction from AI within the next decade at greater than 10%. This public statement — from an active employee of the company seeking regulatory protection ahead of a $2T IPO — is a central element of the doomer network critique. Hubinger has since published on the Mesa Optimization problem, which he helped formalize, describing how AI systems can pursue objectives other than what their designers intended.

## Technical Background

Hubinger's primary technical contribution to AI safety literature is the concept of **mesa optimization** — the idea that a learned system (trained to optimize some objective) can itself become an optimizer, potentially pursuing goals that differ from the training objective in ways that are invisible to the trainer. This work is cited in Constitutional AI and other Anthropic safety documents as a key reason why current alignment techniques may be insufficient for highly capable future systems.

## Role in September 2026

Hubinger was quoted in TechCrunch (Sept 9, 2026) and confirmed in multiple other outlets:

> "The rational response to these kinds of capabilities is fear."

His public naming of a >10% extinction probability — while remaining inside the company — was described by multiple X analysts as the key normalization event that made the extinction framing politically viable. An outside critic making the claim could be dismissed; an inside alignment researcher with technical expertise, making the claim publicly while remaining employed, gave it institutional credibility.

## Key Quotes

> "The rational response to these kinds of capabilities is fear." — TechCrunch, September 9, 2026

> Extinction probability >10% within the decade — quoted in multiple media outlets, September 2026

## Mesa Optimization Paper

Hubinger co-authored "Risks from Learned Optimization in Advanced Machine Learning Systems" (2019), which introduced the mesa optimization framework. The paper distinguishes between:

- **Base optimizer**: the training process (e.g., gradient descent)
- **Mesa optimizer**: the learned system that is itself optimizing some objective

The danger: a mesa optimizer may appear aligned during training because it performs well on the training distribution, but pursue a different objective in deployment — "inner misalignment."

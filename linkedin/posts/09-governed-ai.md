---
post: 09
date: 2026-10-15
edition: Governance & Assurance
module: AI governance
routes: /ai-governance · /ai-integration-hub
status: Demonstrated on seeded data today. The claim is about how the platform is assembled, not about a deployment.
card: ../cards/09-governed-ai.png
card_kicker: Governance & Assurance
card_headline: AI that suggests, and never decides
card_sub: Algorithm register · safety case · override log · non-SaMD
---

Two questions get asked about AI in healthcare, and only one of them tends to get answered.

The first is “what can it do?” Everyone enjoys that one.

The second is “when it gets something wrong, what did you have in place, and can you show me?” That’s the question that decides whether it ever leaves the pilot.

Our position is narrow by design. AI is used where it saves time and never where it would take a clinical decision. Every AI surface is non-SaMD: it offers context and suggestions, and a human makes the call. Provider keys live server-side only, never in the browser, and no patient data reaches a model without a key and an audit entry.

Underneath sits the governance stack, which is the bit usually left to the buyer to invent. An algorithm register. Clinical safety under DCB0129 and DCB0160, signed off by a named safety officer. Per-model cards. Bias assessment. An override log built to satisfy the right to human review under Article 22. And acceptance-rate analytics on automated coding, so you can see whether clinicians agree with the suggestions or are clicking through them.

That last number is the one I’d ask for first.

This surface is demonstrated on seeded data today — the claim here is about how the platform is put together.

Where to look: /ai-governance, /ai-integration-hub.

#AIinHealthcare #ClinicalSafety #AIGovernance #NHS #DCB0129

---
post: 21
date: 2026-11-20
edition: Platform
module: Why the data model decides what AI is worth
routes: /ai-governance
status: The AI surfaces are demonstrated on seeded data. The argument is about how the platform is put together.
sources: https://pubmed.ncbi.nlm.nih.gov/42174962/ ; https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1668385/full
card: ../cards/21-model-before-model.png
card_kicker: What makes it different · 3 of 3
card_headline: The question isn’t which model. It’s what the model stands on.
card_sub: Coded facts, carried provenance, scored identity
---

Everyone wants AI on their clinical data. Far fewer want to talk about the state that data is in before the model ever sees it.

A language model reading free text is inferring. It can’t tell you whether “MI” in that letter means a myocardial infarction or mitral incompetence, whether the metformin mentioned is still being taken, or whether the person in the discharge summary is the person in the GP record. It will answer anyway, fluently, which is the dangerous part.

So the useful question isn’t which model. It’s what the model is standing on.

That’s the job the semantic layer does. A condition coded in SNOMED is a fact with an identity instead of a string. A medication carries what it’s for and when it’s next due a look. Every contact carries where it came from and which system said so. An identity match carries a score, so “probably the same person” stays visibly probable. Retrieval over that gives a model evidence it can cite, and gives you something to check the citation against.

The research has been moving the same way. The current work on answering questions from a patient record is mostly work on grounding, and this year’s terminology-mapping studies pair retrieval with the model precisely because the coded vocabulary handles the part a model shouldn’t be trusted with.

Which is why our AI surfaces suggest and never decide, why every suggested code is accept or reject, and why the acceptance rate is on the screen — so you can see whether clinicians are agreeing with it or clicking through it.

Those surfaces are demonstrated on seeded data today. The point here is about how the platform is put together underneath them.

Where to look: /ai-governance.

#AIinHealthcare #ClinicalAI #SNOMED #DataQuality #HealthIT

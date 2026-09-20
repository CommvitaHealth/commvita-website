---
post: 19
date: 2026-11-14
edition: Platform
module: The semantic, kinetic and dynamic layers
routes: /standards
status: Mixed and stated per module. The semantic layer's openEHR position is the precise one from the standards page, not "openEHR-native".
card: ../cards/19-three-layers.png
card_kicker: What makes it different · 1 of 3
card_headline: What a thing is, where it came from, what the system will do
card_sub: Semantic · Kinetic · Dynamic
---

There’s a framing from the ontology literature that describes commvita better than our own marketing does. Three layers: what a thing is, where it comes from, and what the system will do about it.

We didn’t design to it. It turned out to describe what we’d built.

**Semantic — what a thing is.** Before anything else the platform has to agree what a person, an organisation and a condition are. We use published models instead of inventing our own: openEHR record shapes for the clinical record, FHIR R4 as the canonical shape incoming data gets translated into, SNOMED CT and dm+d for what was recorded, OMOP for research. Jurisdiction is modelled too — the regulator, the identifier scheme, the professional register, the legal deadlines — as dated, source-cited entries with a named signatory. What it costs us: when a standard is awkward we can’t take the shortcut. A field that won’t map stays unmapped and visible.

**Kinetic — where it comes from.** A model that isn’t wired to real data is a diagram. Feeds arrive through monitored connectors, get translated to the canonical shape, and land against a person resolved by identity matching that carries a score on the match. Where a record holds a reference and nobody can be matched to it, the screen says so instead of showing you the key.

**Dynamic — what the system will and won’t do.** Access is two separate things: what your role lets you do, and which organisations you can reach. Enforcement sits on the server, so a clinician outside the organisation a person is registered with gets a refusal with a reason. Approvals run as gates with a named authoriser, an SLA and an escalation. Where a jurisdiction holds no value for something, the capability that depends on it switches off and says why.

What that buys: change a rule once and behaviour changes everywhere the first layer says that concept appears, across every source the second has wired.

Some of this runs end to end today and some is a representative surface over seeded data. Each explainer says which, and so does the screen.

Where to look: /standards.

#HealthIT #openEHR #SNOMED #Interoperability #DataModelling

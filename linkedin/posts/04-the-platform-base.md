---
post: 04
date: 2026-09-30
edition: Orientation
module: Platform base
routes: /rbac · /audit · /login-audit
status: Live — identity, RBAC and the hash-chained audit are platform logic
card: ../cards/04-the-platform-base.png
card_kicker: Orientation · 4 of 4
card_headline: The part underneath all three editions
card_sub: Identity · access · tamper-evident audit · export
---

Here’s the part that never makes it onto a slide: what sits underneath all three editions, that you don’t buy separately and can’t end up without.

Identity, and role-based access on top of it. A role decides what you can do. Your organisation scope decides whose records you can see. Keeping those two apart is what lets a receptionist and a consultant at the same practice each get the right answer, while neither sees the practice down the road.

An append-only, hash-chained audit. Tamper-evident on read, so the log gets checked instead of trusted.

A jurisdiction profile, because England, the Crown Dependencies, the United States and the Gulf don’t want the same defaults, and hard-coding one of them is how a platform becomes impossible to export.

A data fabric, open APIs and bulk export.

That last one carries more weight than it looks like it does. Export isn’t a feature we mention quietly at the end of a contract. It’s what makes the rest safe to adopt.

From here the posts get specific: flow, governance and the record, in no particular order.

Where to look: /rbac, /audit.

#HealthTech #NHS #DataGovernance #Interoperability #openEHR

---
post: topical
date: 2026-09-22
edition: Platform
module: EHDS · EEHRxF · MyHealth@EU
routes: /ehds
status: Design alignment, NOT certification or conformity. IPS generator is live; MyHealth@EU/NCPeH is Partial and real exchange needs national contact point onboarding.
needs: The exact name of what published on the 18th. health.ec.europa.eu is blocked by this environment's egress policy, so the post says "the EHDS specification" without naming a document.
card: ../cards/2026-09-22-ehds-in-a-day.png
shot: ../shots/ehds-obligations.png  # the EHDS obligation table, captured from the published page
card_kicker: Standards · EHDS
card_headline: The spec landed on the 18th. It was in the build on the 19th.
card_sub: Because it was a mapping job, not a rebuild
---

The EHDS spec came out on the 18th. It was in our development build the next day.

That isn’t conformity, and I want to be clear about it. The law came in during March 2025, the technical detail arrives in implementing acts due by March 2027, and the first data — patient summaries and ePrescriptions — moves between countries in 2029. Nobody is certified against a spec that isn’t finished. We call ours design alignment, and we say so on our site.

What one day does show is that taking the spec in was a mapping job instead of a rebuild. Our record already sits in the vocabularies EHDS points at: openEHR shapes underneath, FHIR R4 on the wire, SNOMED for the clinical terms. Whatever EEHRxF ends up looking like, it’s a FHIR view of data we already hold structured.

Speed on its own proves nothing. That change went through the same environments, the same regression pack and the same contract tests as everything else. The gates go green or it doesn’t merge.

You can have both. You just have to decide years earlier.

At the openEHR conference in Amsterdam this week. Come and argue with me.

#EHRCON26 #EHDS #openEHR #Interoperability #DigitalHealth

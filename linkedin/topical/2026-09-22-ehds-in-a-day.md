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

The EHDS specification came out on the 18th. It was in our development build the next day.

Let me be clear about what that does and doesn’t mean, because “we support EHDS” is about to become the least trustworthy phrase in European health tech.

It isn’t conformity. The law came into force in March 2025. The technical detail comes in implementing acts the Commission has until March 2027 to adopt, and the first data — patient summaries and ePrescriptions — moves between member states in 2029. Nobody is certified against a spec that isn’t finished. Ours is a design-alignment statement, and we say that on the page.

What it does mean is that taking the spec in was a mapping job instead of a rebuild. Our record already sits in the vocabularies EHDS points at: openEHR record shapes underneath, FHIR R4 on the wire, SNOMED for the clinical terms. Whatever shape EEHRxF lands on, it’s a FHIR view of data we already hold structured.

MyHealth@EU is a connector on our side. Real exchange still needs onboarding with each country’s national contact point. That’s their timetable, not ours.

Then the part people skip when they boast about speed. The change went through the same staged environments as everything else, the same regression pack on every commit, the same contract tests on the FHIR surface. Gates have to be green to merge. A red one stops it, including on a change I was pleased with.

Fast and careless is easy. Fast and checked is a decision you make years earlier.

Here at the openEHR conference in Amsterdam, where commvita is a sponsor. Come and argue with me.

#EHRCON26 #EHDS #openEHR #Interoperability #DigitalHealth

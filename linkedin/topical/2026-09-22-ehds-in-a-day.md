---
post: topical
date: 2026-09-22
edition: Platform
module: EHDS · EEHRxF · MyHealth@EU
routes: /ehds
status: Design alignment, NOT certification or conformity. IPS generator is live; MyHealth@EU/NCPeH is Partial (connector surface + EMPI proxy identifiers) and real exchange needs national contact point onboarding.
needs: (1) The four {{...}} numbers — nothing in this repo holds platform test, environment or gate counts. (2) The exact name of what published on the 18th. health.ec.europa.eu is blocked by this environment's egress policy, so the post says “the EHDS specification published on the 18th” without naming a document.
card: ../cards/2026-09-22-ehds-in-a-day.png
shot: ../shots/ehds-obligations.png  # the EHDS obligation table, captured from the published page at /explainers
card_kicker: Standards · EHDS
card_headline: The spec landed on the 18th. It was in the build on the 19th.
card_sub: Because it was a mapping exercise, not a rebuild
---

The EHDS specification published on the 18th. It was in our development build the next day.

Let me be precise about what that does and doesn’t mean, because “we support EHDS” is about to become the least trustworthy sentence in European health tech.

It isn’t conformity. The regulation came into force in March 2025. The technical detail arrives through implementing acts the Commission has until March 2027 to adopt, and the first priority categories — patient summaries and ePrescriptions — are due to be exchanged across member states in 2029. Nobody is certified against a specification that isn’t finished, and commvita’s position is a design-alignment statement. We say so on the page.

What it does mean is that taking the spec in was a mapping exercise instead of a rebuild. That’s the whole argument for getting the model right before you need it. The record is already structured in the vocabularies EHDS binds to — openEHR record shapes underneath, FHIR R4 on the wire, SNOMED for the clinical terms. Whatever final shape EEHRxF takes, it’s a FHIR-profiled rendering of data we already hold structured. The International Patient Summary generator runs today. MyHealth@EU is a connector surface with proxy identifier generation in the person index. Real exchange still waits on onboarding with each member state’s national contact point, and that infrastructure is already running in more than a dozen of them — which is somebody else’s timetable to work to, not ours to announce.

Now the part that usually gets left out when people boast about turnaround.

That change went through {{N}} environments before it could reach a release build. The regression pack is {{N}} tests and runs on every commit, {{N}} of them contract tests against the FHIR surface. {{N}} gates have to be green before anything merges, and a red one stops it.

Fast and careless is easy. Fast and checked is an architecture decision you make years earlier, and it’s the one worth asking any supplier about.

Writing this from the openEHR conference, where commvita is a sponsor. Come and argue with me about it.

Where to look: /ehds.

#EHDS #MyHealthEU #openEHR #Interoperability #DigitalHealth

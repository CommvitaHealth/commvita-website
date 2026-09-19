---
post: 13
date: 2026-10-27
edition: Flow
module: PulseGrid integration assurance
routes: /connector-dashboard
status: Live — connector state and freshness are platform logic.
card: ../cards/13-integration-assurance.png
card_kicker: commvita Flow
card_headline: Interfaces don’t fail loudly
card_sub: Connector state, data freshness, rejects — on one screen
---

Interfaces don’t fail loudly. They fail at 3am on a bank holiday, and you find out on Tuesday when somebody asks why the numbers look thin.

Integration assurance is the least glamorous thing in the platform and the first thing I’d check.

PulseGrid watches every connector — HL7 v2 feeds, FHIR endpoints, GP Connect, the national record locator, the EPR hub — and reports whether each one is delivering, how fresh what it delivered is, and what got rejected. A feed that stopped shows up as a feed that stopped, with a timestamp, on a screen somebody owns.

Freshness is the metric worth arguing about. “Connected” is a binary, and it’s almost always true. “Last message 19 days ago” is the one that tells you the shared record you’ve been relying on has quietly become a history book.

Underneath it, an open core: openEHR-aligned storage, FHIR R4 on the wire, SNOMED for clinical terms, OMOP for secondary use. Standards on the outside and on the inside, which is what makes an export a real export.

Where to look: /connector-dashboard.

#Interoperability #FHIR #HL7 #NHS #HealthIT

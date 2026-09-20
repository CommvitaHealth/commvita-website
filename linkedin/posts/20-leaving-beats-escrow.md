---
post: 20
date: 2026-11-17
edition: Platform
module: Portability, and why escrow answers the wrong question
routes: /standards
status: Live — bulk FHIR export and the OMOP extract are real. Escrow, support and service levels are explicitly NOT committed, here or on the site.
card: ../cards/20-leaving-beats-escrow.png
card_kicker: What makes it different · 2 of 3
card_headline: Escrow answers the wrong question
card_sub: Your data in a published standard, on a day we can’t help
---

The question I get asked most by anyone who’s been burned before: what happens to us if you go under?

The traditional answer is source code escrow. A copy of the source sits with a third party, and if the supplier fails, you get it.

I haven’t settled escrow. Contracted response times, a published support model, anything about funding — none of it is committed, and I won’t imply otherwise on a post. If you’re seriously considering being first, those belong in a contract, and they’re exactly what you should negotiate hard on.

I also think escrow answers the wrong question.

Escrow hands you source code, which you then have to host, understand and run. What you need is your data, in a shape somebody else can read, on a morning when we aren’t around to help. Those are different problems, and the second one is the one that hurts.

So the record writes to an openEHR repository, and an openEHR container ships with the platform for each country. FHIR R4 in and out. Bulk FHIR export and an OMOP extract that arrives with a data-quality report, so what leaves can be checked instead of trusted. Self-hosted on your own kit, £1 an instance to start.

Now the honest half, which portability promises usually skip. There’s no one-click export of an entire deployment as a single archive. Modules holding their own operational content export what their screen shows. If a receiving system needs more than the clinical record and the analytic dataset, that’s an integration project and it should be priced as one.

Try this on whoever you’re buying from now: ask for a bulk export of your own record in a published standard, and time how long the answer takes.

Where to look: /standards.

#HealthIT #Procurement #VendorLockIn #openEHR #NHS

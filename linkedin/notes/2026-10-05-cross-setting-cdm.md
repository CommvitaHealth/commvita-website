---
type: note
date: 2026-10-05
to: Adam Townsend
edition: Platform
routes: /social-care · /omop-cdm
source: Written to follow a LinkedIn exchange on building a common data model across community, primary care and social care.
status: Verified. Live and API-backed — Care Act needs assessment and eligibility, care packages with CHC fast track and placements, DoLS/MCA authorisations, Section 42 safeguarding, and the carer identification register. Demonstrated on seeded data — children's social care, the SEND and EHCP surface, the fuller carer assessment, and SALT/ASCOF performance. The OMOP export is an MVP of six tables, all clinical; the production CDM is listed as a gap.
needs: Nothing. No competitor or national supplier is named.
card: ../cards/2026-10-05-cross-setting-cdm.png
card_kicker: Note
card_headline: Where a cross-setting CDM breaks
card_sub: Community, primary care and social care — and the part OMOP has no room for
---

# Where a cross-setting CDM breaks

## Community, primary care and social care — and the part OMOP has no room for

Adam — picking up where we left off, because it’s a question I’ve hit the wall on and I’d rather hand you the wall than describe the view.

## The objects that have nowhere to go

The social care end doesn’t break because the vocabulary is missing. Most of it can be coded. It breaks because the common data model has no home for the things that carry the meaning.

A package of care with a provider, a number of hours a week and a weekly cost. A residential placement. A direct payment. A personal budget, indicative at assessment and actual after brokerage. A Section 42 safeguarding enquiry with an outcome. A DoLS authorisation that expires. An unpaid carer, who is a person with their own rights and not an attribute of somebody else. An eligibility decision. An unmet need.

None of those is a condition, a drug, a procedure or a measurement. OMOP gives you four domains that matter and a general observation table, so every one of them ends up as an observation with a date and a concept id — or it gets dropped on the way in.

## What you lose in the bend

Say you push a care package into OBSERVATION. You keep the fact that something happened on a day. You lose the hours. You lose the weekly cost, so the finance question can’t be asked. You lose the provider, so the market question can’t be asked. You lose the review date, so you can’t tell whether anybody looked again. And you lose the interval — a package isn’t an event, it’s a state that persists, changes and ends, and that’s the shape the model has to hold.

Then there’s the one I think is the real test. Clinical models record what was done. Social care is very often about what wasn’t — need assessed as eligible with no service against it, a carer never offered their own assessment, a review long overdue. A model built on occurrences struggles to say that something is absent, and the absence is the finding.

## Where we actually are

So you know I’m not selling you something: our own model stops at the same line.

In the record, the social care side is real and API-backed. Care Act needs assessment with the eligibility decision and an indicative budget. Care packages with provider, hours and review date; placements with a weekly cost that sums to a total the finance side can see; continuing healthcare fast track with its decision. DoLS and MCA authorisations with status derived from expiry. Section 42 enquiries that close with an outcome. A carer register whose two useful columns are whether that person was offered their own assessment and whether they were pointed at support.

Children’s social care, the SEND and education, health and care plan surface, the fuller carer assessment and the SALT and ASCOF performance reporting are demonstrations on seeded data today, and our pages say so.

But the OMOP export is six tables — person, observation period, visits, conditions, drug exposures, measurements — and every one of them is clinical. None of the above reaches the CDM. The production model is on our own gap list. Same boundary you’re describing, and we haven’t crossed it either.

## Three questions I’d put to any model

1. Can it hold a package of care as a state over time — provider, hours, weekly cost, review date — and answer what changed and when?
2. Can it hold a carer as a person in their own right, with their own assessment and their own outcomes, linked to the person they care for without being swallowed by them?
3. Can it express an absence? Eligible need with no service, an assessment overdue, support offered and declined. If the answer is no, the model will flatter every system it’s pointed at.

If the bones you’ve got answer those three, you’re ahead of anything I’ve seen, including ours.

## One principle worth stealing

When we built the OMOP export we made it report the unmapped codes instead of dropping them, and ship a data-quality summary alongside the data. It was meant as plumbing. It turned out to be the most useful thing in there, because the unmapped list is a map of where the model doesn’t reach.

In a cross-setting CDM I’d expect that list to be long and mostly social care. That’s the specification, not the failure.

I’d like to see what you’ve got, and I’m happy for this to be a conversation rather than a pitch — we’re missing the same half you are.

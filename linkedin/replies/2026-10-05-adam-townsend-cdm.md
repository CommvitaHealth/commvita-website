---
type: reply
date: 2026-10-05
to: Adam Townsend
on: capability map post
status: Verified before sending. The OMOP export is an MVP of six tables — person, observation_period, visits, conditions, drug_exposures, measurements — and all six are clinical; "social care" appears nowhere in the OMOP explainer. Unmapped codes are reported, not dropped. The production CDM is listed as a gap on the site. Social care modules exist in the Population Platform (/social-care, /carer-assessments, /brokerage-placement and others) but sit outside the CDM.
needs: Nothing. No competitor or national supplier is named.
---

On the first bit — agreed, though I'd rather win on the architecture than on the politics.

The social care end is what breaks most models, and I don't think it's a vocabulary problem. It's that OMOP has nowhere to put the things that matter there. A support plan, a direct payment, a placement, an unmet need, a carer who isn't a patient — none of them is a condition, a drug or a measurement. So they get bent into an observation, or quietly dropped.

Straight with you: our own OMOP export is six tables and all six are clinical. Social care sits in our record but not in our CDM. Same boundary you're describing, and we haven't crossed it either.

One principle worth stealing: report the unmapped codes, don't drop them. In social care the unmapped set is the interesting part.

I'd like to see the bones of it. Coffee?

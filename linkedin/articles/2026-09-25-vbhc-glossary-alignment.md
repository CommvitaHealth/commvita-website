---
type: article
date: 2026-09-25
edition: Platform
module: VBHC Key Terms Glossary alignment
routes: /leftshift · /population-health
source: VBHC Key Terms Glossary, Nov 2025 v6.3 — Sir Muir Gray & Jane Johnston, for NHSE/Frimley ICB, Outcomes Value and Stewardship Network with Data Observatory CIC. Appendix by Anant Jani.
status: LeftShift runs on seeded demonstration data and says so on every tab — stated in the article. Core20PLUS5 splits and k>=5 suppression are platform logic. PBMA, variation, overuse, waste, cost-utility and shared decision-making are absent from commvita.
needs: (1) Confirm the public dataobservatory.org.uk URL serves a cleared version before hyperlinking — the copy supplied is marked "V6.3 Internal" on all 54 pages. (2) The founders page names Hassan's National Council chair but not Marc's presidency of the Data Observatory — worth adding there if the article declares it. (3) Allocative value is claimed as partial: we hold the segments without the spend per segment. Confirm.
teaser: ../topical/2026-09-25-vbhc-glossary.md
card: ../cards/2026-09-25-vbhc-glossary-alignment.png
card_kicker: Article · Value-based healthcare
card_headline: Six gaps in our own product, found by reading a glossary
card_sub: Adopting the VBHC Key Terms Glossary — and where it already fits
---

# Six gaps in our own product, found by reading a glossary

## Why commvita is adopting the VBHC Key Terms Glossary, and where it already fits

A glossary sounds like the least interesting document an organisation can publish. It’s a list of words with agreed meanings. Nobody puts it on a strategy slide.

It’s also the thing whose absence wrecks more programmes than any technology decision I can name. Two directors say “value” across a table and mean different things — one means allocative value, the other means cost per unit. Somebody says “there’s a lot of variation in this pathway” and nobody asks whether it’s warranted. A year later the board is arguing about a number that three teams calculated three ways, all correctly.

So commvita is adopting the VBHC Key Terms Glossary as its working vocabulary. It’s the work of Sir Muir Gray and Jane Johnston, prepared for NHS England and Frimley ICB by the Outcomes, Value and Stewardship Network with Data Observatory CIC, with an appendix on the causal determinants of health by Anant Jani.

This isn’t conformance. There’s no certificate and nothing to audit against. What you do with a glossary is use it — in the product, in the dashboards, in the sales conversation — until they all mean the same thing by the same word. What follows is an honest account of where we already do that, and where reading it caught us out.

## Where we already fit

### Left shift

The glossary’s appendix asks whether a population is shifting left or right, and gives a method: track incidence and prevalence for the conditions carrying the greatest burden of disease, across 2026, 2028 and 2030, and mark each risk factor as left shift, baseline, no change or right shift. Then it plots the trajectory.

We built LeftShift Intelligence to answer that question. It scores three axes — analogue to digital, hospital to community, treatment to prevention — rolls them into one index, and shows per-axis maturity alongside it. It’s wired to signals, to actions, and to a board pack, so the score has somewhere to go.

Worth saying plainly: that module runs on seeded demonstration data today, and carries a banner on every tab saying exactly that. The production path computes each indicator from live operational modules in the same platform. We’re not going to describe a demonstration as a deployment in an article about shared meaning.

### Health opportunity architecture

This was the passage that stopped me. The glossary asks: does every person in my population have an equal and equitable opportunity to be healthy and well? And it warns against “simple, sometimes simplistic, notions of behaviour change”, because many people don’t have the option of the behaviours we keep asking them to adopt.

Our index carries an equity modifier that subtracts from the headline score when the gains are unequal. If your digital shift is being carried by the people who were already easiest to reach, the number the board is asked to accept comes down. That was built before we read this document, and it’s the same argument.

### Equity and equality

Every access and outcome measure in the platform splits by Core20PLUS5, with gap indicators, and small numbers suppressed at five. The glossary treats equity as an outcomes term rather than a reporting afterthought, which is the right way round and the way we built it.

### Population healthcare, and allocative value in part

Population health management, segmentation and deprivation analytics are all there. On allocative value I want to be precise, because the glossary is precise: it defines it as spend across segments of the population, bearing in mind multimorbidity. We hold the segments. We don’t yet hold the spend against them. That’s alignment in vocabulary and half of it in practice.

## The false friend

We use the word “stewardship” in commvita exactly once, and we use it wrongly by this glossary’s lights. Ours means antimicrobial stewardship. The glossary means stewardship of finite resources on behalf of a population — a different idea, with a section of its own.

That’s what makes a shared vocabulary useful instead of decorative. It finds the words you thought you had covered.

## Where we don’t fit

Six things the glossary treats as core and commvita doesn’t have at all.

**Programme budgeting and marginal analysis.** No PBMA anywhere in the platform. The glossary gives it a full process section.

**Warranted and unwarranted variation.** We don’t split them. The glossary ties unwarranted variation to atlas-style comparison and PROMs, and we carry neither.

**Overuse.** No measure.

**Waste.** No measure.

**Cost-effectiveness and cost-utility.** We do service-line costing on the flow canvas. We don’t do cost per unit of benefit.

**Shared decision-making.** The glossary gives it a section. We have no surface for it.

## The one that stings

Read the glossary’s own sentence on left shift and you find this: the aim is to shift left “while also reducing overuse, waste and inappropriate or futile care”, because that care carries an opportunity cost — it moves finite resources away from care that delivers more value for the population.

So left shift, properly understood, is two movements. Move demand upstream, and stop doing the things that were never worth doing.

We measure the first. We have no measure at all for the second. By this glossary’s definition we are doing half of the thing we named a product after, and I would rather say that here than have somebody work it out in a procurement.

## What happens next

The six gaps go onto the roadmap in the glossary’s words instead of ours. That’s the practical benefit of taking on somebody else’s vocabulary: you inherit their questions along with their nouns, and their questions are better than the ones you were asking yourself.

Marc Farr, our co-founder and chief data and analytics officer, is leading this for us.

Which brings me to the interest I should declare, and it’s a bigger one than I first wrote down. Marc is President of the Data Observatory. Our commercial co-founder, Hassan Chaudhury, chairs its National Council. So the company adopting this glossary is led in part by the people behind the organisation that helped produce it.

That’s worth saying out loud, because it changes how you should read the warm half of this article. Treat the alignment section as interested. The six gaps are the part I’d trust — nobody lists their own absences to flatter a document they had a hand in.

If you work on any of those six and think we have called it wrong, I would like to hear it.

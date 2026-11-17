# Five LinkedIn videos — scripts, shot lists and the rules

Five films, two minutes each. Narration is written to be read aloud at about
150 words a minute, so each script runs 280–300 words. Shot lists name real
routes; every frame comes off the running platform.

## Before you record anything

**Screens come from the platform, never from me.** I can't produce them and
nothing here is a mock-up. Capture each shot through the product's own code
paths and put the build stamp in the corner, the way the explainer screenshots
do. A mock-up dressed as a screen is the one thing the house rules forbid
outright, and on video it's worse than on a page — nobody can pause a claim and
check it.

**Say live or demonstrated out loud.** Not in a caption nobody reads at 0.8
speed on a phone. Where a shot is seeded data, the narration says so in the
same breath as the capability.

**Don't show how it's built.** Standing order, 20 September. No stack, no
tooling, no build gates, no pipeline internals. Results are fine: elapsed time,
counts of modules and checks, what passes and what doesn't. Video 5 is the one
that will tempt you — see its note.

**No supplier is named.** Not in narration, not on a screen, not in a
comparison column.

**Captions.** Most of LinkedIn watches muted. Burn in captions, and make the
first three seconds work without sound.

---

## 1 · What the national platform does, and what it doesn't

**Status** Flow Edition parity is a published capability claim. Flow canvas
constraint detection is live; closed-loop actions are demonstrated.
**Routes** `/fdp-comparison` · `/connector-dashboard` · `/rtt-ptl` · `/flow` ·
`/discharge-hub`

> Every operational product the national data platform offers, we match. That
> isn't the interesting part.
>
> Here's the integration layer. Every connector, what it's delivering, how fresh
> that data is, what got rejected. A feed that stopped three weeks ago shows up
> as a feed that stopped three weeks ago, with a timestamp, on a screen someone
> owns.
>
> Here's the referral-to-treatment list, the cancer pathways, diagnostics,
> theatres. Parity, module for module.
>
> Now the part that goes further. This is the whole health economy drawn as one
> production line — front gate to discharge, with a returns loop carrying the
> readmissions. One law binds it: work in progress equals arrival rate times
> time in the system. The platform finds the one station capping everybody, from
> the model, and shows the back-pressure starving whatever sits downstream.
> That's live, running on real ward, delay and operational pressure state.
>
> And then it acts. From this screen: raise the discharge task, notify the GP,
> book the transport, order the medicines to take away. Across acute, community
> and social care, because a discharge constraint is never solved inside the
> hospital reporting it. That action surface is demonstrated on seeded data
> today — I'd rather tell you now than have you find it in a procurement.
>
> Scaling this nationally isn't a rebuild. Nothing about a country or a region
> is compiled in. Identifiers, regulators, coding systems, statutory clocks,
> currency — all read from a dated, source-cited profile. Three Caribbean
> ministries run on it already. A fourth is configuration, not code.

---

## 2 · Three ways of seeing the same system

**Status** LeftShift runs on seeded demonstration data and says so on every
tab. Flow canvas model is live. Outcome intelligence — check each tab before
filming.
**Routes** `/leftshift` · `/flow` · `/outcome-intelligence`

> Three screens, one record underneath. That's the whole argument.
>
> LeftShift Intelligence measures the three shifts a health system is asked
> for — analogue to digital, hospital to community, treatment to prevention. One
> index, scored per axis.
>
> Watch what it does next, because this is the bit nobody else does. It adjusts
> that score for who the gains are reaching. If your digital shift is being
> carried by the people who were already easiest to reach, the number the board
> is asked to accept comes down. The equity gap moves the headline, instead of
> sitting in an appendix.
>
> This surface runs on seeded demonstration data today. There's a banner on
> every tab that says so. The production path computes each indicator from the
> live operational modules sitting underneath it — which brings us to the next
> screen.
>
> commvita Flow is where the operational truth lives. Queue, work in progress,
> arrival rate, time in system, per station, with the binding constraint found
> from the model. Switch the scope to medicine, surgery, frailty, stroke — the
> line re-flows, because the constraint moves when you change what you're
> looking at.
>
> And outcome intelligence closes it. Did the thing we changed make a
> difference, to whom, and at what cost per head.
>
> Here's why the three on one platform matters. The shift you're measuring, the
> flow you're managing and the outcome you're reporting are the same events,
> read three ways. Nobody reconciles anything. Nobody re-keys anything. The
> board paper and the ward screen can't disagree, because there's only one of
> them.

---

## 3 · Standards: what we're built to, and what we're certified against

**Status** Design alignment throughout. NOT certification, NOT conformity.
IPS generator live; the European exchange connector surface is partial.
**Routes** `/standards` · `/ehds` · `/omop-cdm` · `/ig-spine`

> Let me split a word that gets abused. Built to a standard, and certified
> against one, are different things, and we only have the first.
>
> The record is openEHR-aligned. It's built to openEHR's record shapes and
> writes to an openEHR repository, and a container ships with the platform for
> each country. It is not a native implementation, we ship zero archetype
> definitions and there's no query language support. We say that on our own
> website, because anyone technical finds it in ten minutes and a claim that
> fails that test poisons every claim next to it.
>
> On the wire: FHIR R4. SNOMED CT and the dictionary of medicines and devices
> for what was recorded. OMOP for secondary use, with the unmapped codes
> reported instead of dropped.
>
> For Europe: the regulation came into force in March 2025, the technical detail
> arrives through implementing acts due by March 2027, and the first priority
> data — patient summaries and prescriptions — moves between member states in
> 2029. Nobody is certified against a specification that isn't finished. Our
> position is design alignment and we call it that. The patient summary
> generator runs today. The cross-border connector surface exists; real exchange
> waits on each country's national contact point, which is their timetable.
>
> Against the World Health Organization's reference architecture for digital
> public infrastructure, the same: alignment, stated as alignment.
>
> What we don't hold, and you should ask every supplier this: no information
> security certification, no national toolkit return, no published penetration
> test. None of it is hard to get. It just isn't done, and a first customer
> would be right to make it a condition.

---

## 4 · The cost ambition, and the thing it's really about

**Status** The 80% figure is a published **ambition**, not a measured result.
No such measurement exists. See the warning below — this is the riskiest of the
five.
**Routes** `/editions` · `/connector-dashboard` · `/golden-thread` · `/leftshift`

> I want to be careful with this one, because there's a number attached to it
> and the number is an ambition.
>
> Our ambition is to take eighty per cent out of total cost of ownership. Not a
> measured result — an ambition, published as one. We haven't run that
> measurement and I'm not going to pretend otherwise.
>
> Here's the reasoning behind it. A health system doesn't buy one system, it
> buys a stack. A record here, a risk register there, board management, incident
> reporting, rostering, analytics. Then the integrations between them. Then the
> infrastructure under each. Then the assurance overhead of proving every one of
> them is safe, every year, separately. The licences are the small half of that
> bill.
>
> One platform removes the integration layer, because the incident on the ward
> and the risk on the board register are the same object. It removes the
> duplicate infrastructure. It collapses the assurance overhead into one
> estate. And the operational base starts at one pound an instance, self-hosted,
> with every environment included.
>
> But cost is the less interesting half. The thing I'd actually argue for is
> decision quality.
>
> A decision made on a fragment is a guess with a confident face on it. When the
> record, the operational picture and the governance chain are the same data,
> the board paper reconciles with the ward screen because there's only one of
> them. A risk score traces to the exact events beneath it. An equity gap moves
> the headline number instead of hiding behind it.
>
> Cheaper is a budget argument. Deciding on everything that's known is a better
> one.

---

## 5 · From a letter to a tested capability

**Status** Martin's own account of his own build. I can't verify the timeline —
you can. **Check the two-week claim against the commit record before filming.**
**Routes** `/waiting-well` · `/unified-waiting-list`
**Animation** `waiting-well-timeline.html` in this folder

> A letter went out about waiting well. The argument in it was simple: people on
> a waiting list aren't in a queue, they're a cohort, and some of them are
> getting worse while they wait.
>
> Here's what usually happens next. Someone writes a requirement. It goes into a
> business case. The business case waits for a board. Procurement runs. A
> specification is agreed with a supplier. It enters a release train, comes out
> the other side, gets tested, and ships. Best case, months. Often longer than
> the policy that prompted it survives.
>
> Here's what happened instead. The capability was in a tested build inside two
> weeks.
>
> This is what it does. While somebody waits: prehabilitation where it changes
> the outcome. Optimisation of whatever will complicate the operation — the
> blood sugar, the blood pressure, the anaemia nobody's chased. Contact that
> tells people where they actually are, which is most of what they want.
> Escalation when their condition moves while they're in the queue. And
> underneath it a single waiting list, so the person waiting on three pathways
> is one person, counted once.
>
> I'm not going to walk you through how we build, and that's deliberate. What I
> will say is that the code is AI-generated and a person reviews it, and the
> speed comes from the model being right before the requirement arrives. Waiting
> Well needed no new data model. The record already knew who was waiting, what
> for, and what else was wrong with them.
>
> That's the real claim. Not that we're fast. That getting the model right years
> earlier is what makes two weeks possible at all.

**Note on video 5.** The standing order bars publishing how the platform is
built. The script shows elapsed time, which is a result, and stops. Don't add
tooling, gate names, pipeline stages or test figures in the edit — the
temptation will be strongest here because the animation has space for them.

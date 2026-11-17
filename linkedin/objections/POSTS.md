# The objections series — nine posts

The interactive table is `objections.html`. LinkedIn can't host it, so it's the
reference page and the screenshot source: open it, filter to a role, expand the
row, screenshot that card and attach it to the matching post.

Run the launcher first. Then one persona a week. The conceded rows carry the
series — a post that admits something gets read and argued with, which is the
point.

---

## 0 · Launcher

We asked people to be as unkind as they could about commvita. Then we wrote
down what we'd say back, and published the lot.

Thirty-two objections, sorted by the chair you sit in — chief executive,
finance, operations, medical, technology, procurement, HR, information
governance.

Fourteen we think we answer. Eleven we answer partly. **Seven we concede**, and
those rows just say so and stop. No ISO 27001. No Cyber Essentials. No toolkit
return. No published support model. No customer live for a year.

If you're going to find those out anyway, you may as well find them out from
us, before you've spent a fortnight on a business case.

Pick your chair and go looking for the row that would stop you buying.

---

## 1 · CEO

"We'd be your first customer. If this goes wrong, it's my name on it."

Conceded. No customer has been live on this for a year and nothing changes
that.

The only honest mitigation is sequencing. The Governance & Assurance edition
carries no clinical workflow at all — board, risk, incidents, information
governance, audit, and nothing that touches a patient. So a first deployment
can fail in the board papers instead of on a ward.

That's not a reason to buy. It's the difference between a survivable mistake
and an unsurvivable one, and a first customer is entitled to insist on it.

---

## 2 · CFO

"£1 an instance is a gimmick. Where's the real money?"

It's the published price for the operational edition: one deployment for your
organisation, every environment included — production, test, training, disaster
recovery. Not per seat. It isn't free. It's priced so that adopting the
platform is never the expensive decision.

The real money is where it always is — implementation, migration, training, and
your own people's time.

And while we're here: the 80% cost reduction is an aim. Nobody has banked it.
We haven't run that measurement and I'm not going to pretend otherwise. The
price, on the other hand, isn't an aim.

---

## 3 · COO

"You want me to run winter on a demonstration."

Partly fair, and the distinction matters more than the headline.

On the flow canvas, work in progress, queue, arrival rate and the binding
constraint run on a live model built from real ward, delay and operational
pressure state. The closed-loop action surface — raising the discharge task,
notifying the GP, booking transport — is demonstrated on seeded data today.

So you can see the constraint live and act on it by hand. The acting-from-the-
screen part you'd be waiting for.

Better you know that in October than in January.

---

## 4 · Chief Medical Officer

"AI anywhere near a clinical decision. Absolutely not."

Then we agree.

Every AI surface is non-SaMD. It offers context and suggestions; a human makes
the call. Provider keys are server-side only and no patient data reaches a
model without a key and an audit entry.

Underneath: an algorithm register, bias assessment, clinical safety under
DCB0129 and DCB0160 with a named officer signing off, an override log built for
the right to human review, and acceptance-rate analytics on automated coding.

That last one is the number I'd ask any supplier for first. It tells you
whether clinicians agree with the suggestions or are clicking through them.

Those surfaces are demonstrated on seeded data today.

---

## 5 · CIO

"'openEHR-aligned' is a marketing word for not openEHR."

Fair hit, and we'd accept the framing.

It's built to openEHR's record shapes and a finished consultation writes to a
real openEHR repository, with a container shipping for each country. That's a
real integration against a real clinical data repository.

It is not a native implementation. We ship zero archetype definitions, there's
no query language support, and the default repository target in a stock
configuration is a mock.

That's exactly why we don't use the word native. Anyone technical finds the gap
in ten minutes, and a claim that fails that test poisons every claim next to it.

---

## 6 · Procurement

"You'd fail our mandatory gates on day one."

Conceded. You should assume so.

Cyber Essentials, an information security certification, a completed national
toolkit return — these are common pass-or-fail gates and we hold none of them.
No independent penetration test either.

If those are mandatory in your process, we fail it. That's the accurate answer
and you should have it before you spend effort on us rather than after.

None of it is hard to get. It just isn't done, and a first customer would be
right to make every one a condition of going live.

---

## 7 · HR

"Workforce data is the most sensitive we hold. Appraisals, grievances, speaking
up."

Which is why access is two separate things. A role decides what you can do. An
organisation scope decides whose records you can reach. Enforcement sits on the
server, so someone outside the scope gets a refusal with a reason instead of a
hidden menu.

Every read is written to an append-only, hash-chained log that's re-verified
when it's read. An inappropriate look at a record is findable afterwards and
provable once found.

If you're going to hold freedom-to-speak-up and register-of-interests data at
all, that's the minimum the people in it are owed.

---

## 8 · Information governance

"You haven't submitted a toolkit return. I can't sign this off."

Conceded, and you shouldn't sign it off on that basis. No return submitted, no
certification held for the record-sharing standards. That's a condition to set,
not an objection to argue with.

What I'd put alongside it: the opt-out is handled as policy the system enforces
rather than a note on a file. Shared care opt-outs sit in a registry built on
FHIR Consent with a governed emergency override — so the override leaves a
trace of its own.

The clock on a subject access request runs where the work is done, not in a
spreadsheet.

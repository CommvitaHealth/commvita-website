---
post: topical
date: 2026-09-23
edition: Platform
module: Patient data portability · the xShare Yellow Button
routes: /portal
status: Live — portal record access and the one-click FHIR R4 bundle export under the portability right, with every download logged. The button itself and the other two xShare functions are not built.
needs: Confirm we really haven't built the one-time share or the share link. I inferred that from their absence on the site, which is the safe direction but still an inference.
card: ../cards/2026-09-23-yellow-button.png
shot: ../shots/yellow-button.png  # a proposal in our palette, NOT xShare's official asset
card_kicker: Standards · EHDS
card_headline: The download is live. The button isn’t.
card_sub: xShare’s Yellow Button, and where we stand
---

There’s a yellow button in the EHDS conversation, and it might be the best idea in it.

The xShare project’s Yellow Button is one control, meant to sit in every electronic health record and every patient-facing app in Europe, letting a citizen take and share their own health data in the European exchange format. Three things sit behind it: download, a one-time share, and a link.

The clever part isn’t the function. It’s that it’s the same button everywhere. A right nobody can find doesn’t get used, and somebody who learns one control at their GP shouldn’t have to hunt for a different one at the hospital.

So where are we?

The download runs in commvita today. A person opens the portal and takes their own record as a structured bundle under the portability right, and every download is written to the processing log. If we hold nothing under a heading, the file says so instead of quietly handing back an empty section — a bigger distinction than it looks, because “you have no allergies recorded” and “we didn’t look” are different sentences.

What we don’t have is the button itself, or the other two functions. The one-time share and the link aren’t built.

And it isn’t a regulatory requirement. It’s a demonstration of what the EHDS rights look like once somebody designs them instead of only legislating them, piloted across several countries.

We’d adopt it. Who else is?

#EHDS #xShare #PatientEmpowerment #FHIR #DigitalHealth

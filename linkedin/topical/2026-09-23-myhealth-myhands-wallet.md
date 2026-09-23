---
post: topical
date: 2026-09-23
edition: Platform
module: EUDI Wallet · myHealth@myHands · what sits behind the front door
routes: /portal · /consent-hub
status: NO wallet, NO EUDI integration, NO verifiable credentials — none exist in commvita. Live and claimed here: structured record, IPS generator, portal download under portability with logging, consent capture and Art.7 withdrawal, FHIR Consent opt-outs with override audit, server-side access enforcement.
needs: Confirm no wallet or EUDI work is in flight that the website doesn't know about. Add the explainer link once the other session publishes it.
card: ../cards/2026-09-23-myhealth-myhands-wallet.png
card_kicker: EHRCON26 · Amsterdam
card_headline: We don’t have a wallet. We have what a wallet points at.
card_sub: myHealth@myHands, EUDI, and the building behind the front door
---

Sitting in Zoltan Lantos’s session at #EHRCON26 on myHealth@myHands — the EUDI Wallet joined up with MyHealth@EU, so a citizen can authorise access to their own record across borders. Being demonstrated in 18 countries.

Worth being straight about where commvita sits with this.

We don’t have a wallet. No EUDI integration, no verifiable credentials. That isn’t what we build.

What we do have is the thing a wallet needs to point at. A record already structured in openEHR shapes, FHIR R4 and SNOMED. A patient summary generator that runs today. A portal download of your own record under the portability right, with every download logged. Consent captured and withdrawable through an API, and sharing opt-outs carried as FHIR Consent with an override audit. Access decided on the server, so permission granted somewhere else lands somewhere that can enforce it.

A wallet is a front door. It only works if the building behind it can answer.

So that’s the question I’m taking away from the session: what does a platform have to expose for a wallet to work against it? We’re writing our answer up properly this week.

Zoltan Lantos and openEHR — thank you for the session.

#EHRCON26 #EHDS #EUDIWallet #openEHR #DigitalHealth

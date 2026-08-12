# commvita website — restructure

32 static pages. No build step, no server required: every link is relative, so
this opens correctly from the filesystem, from a static host, or from behind a
reverse proxy.

**The landing page is the original page**, structure and content unchanged,
including the five-scene animated explainer. It is generated from
`docs/website_landing_source.html.tpl` with three things added and one removed:
four links into the site, the nine core pages as a second row in the fixed
header, the site footer — and the reorganisation section, which has moved to
`uk/organisational-change.html` where it belongs.

**Every page is built as screens.** A section is one self-contained view, and
the type scale is keyed to `vh` as well as `vw` so a short laptop and a tall
monitor both hold together. Measured, 92 sections across the site: **6 exceed a
screen on a 1440×900 desktop and 3 on an iPad**. Those are a 13-row status
table and a 66-item library — content that cannot be made to fit one viewport
at a legible size, so it scrolls rather than being squeezed, which is what the
original page does with its own tall sections.

On a **phone** snap is off entirely and the pages flow as ordinary documents.
Snapping competes with momentum scrolling and with the address bar resizing
mid-gesture, and a 790px usable screen cannot hold a status table at a size
anyone can read.

Snap is `proximity`, never `mandatory`: mandatory snapping on a touch device
fights the user when a slide is taller than the viewport, and a presentation
that will not let you read the bottom of a slide is worse than no presentation.
Slides are `min-height`, never `height`, for the same reason. Snap is off
below 768px, off in phone landscape, and off under `prefers-reduced-motion`.

    open index.html

## The library, and what is kept out of it

The archive nests everything under `site/`, with the 66 documents in
`site/explainers/library/`. The archive root holds an entry point and nothing
else.

**Three documents are excluded, by name and with a reason.** One of them
matters:

`CommVita-Azure-CICD-Guide-*.html` describes the build pipeline, the container
registry and environment configuration. It is excluded on **security** grounds
and must not appear in a public pack.

A name-based exemption fails open the moment somebody renames the file — a new
date, and it ships. The generator therefore **refuses to build** if any
document matching the sensitive-deployment signature is absent from the
exclusion list, which was proven by copying the guide to a 2026-09-01 filename
and watching the build stop.

The other two are `index.html` (the docs pack index, superseded by the site's
own library page) and `commvita-website.html` (the previous single-page site).

## Regenerating

This site is **generated**. Do not hand-edit the HTML — the next regeneration
will overwrite it, and a hand-edited copy that nothing rebuilds is how a
document comes to disagree with the product it describes.

    python3 docs/build_website.py

Three modules, each with one job:

| File | Holds |
|---|---|
| `docs/website_chrome.py` | The stylesheet, the brand lockup, the navigation, the footer and the page shell |
| `docs/website_figs.py` | Every figure, with heights derived from content rather than guessed |
| `docs/build_website.py` | Page content, and the measurement of every number on the site |

The palette is read from `services/web/public/brand/brand-tokens.json` and the
mark from `docs/build_brand_kit.py`. Neither is transcribed.

## Structure

```
index.html                              platform.html
problem.html                            whole-person-record.html
solution.html                           standards.html
research-and-innovation.html            system-maturity.html
regulatory-compliance.html              editions.html
founders.html                           editions/governance-assurance/index.html

uk/    index + quadruple-aim · frp · qia · annual-reporting ·
       organisational-change · neighbourhood-health · integrated-care
us/    index + payer-provider · value-based-care · risk-and-population-health ·
       interoperability · compliance · deployment
int/   index + middle-east · africa · caribbean
explainers/index.html
```

## Where this departs from the specification, and why

Seven claims in the specification are not supported by the code. Each is
handled here rather than published, and each is visible on the page rather than
only in this file.

| # | Specification said | Measured | What the site says |
|---|---|---|---|
| 1 | "Built on OpenEHR", "OpenEHR-native" | **0** archetype definitions ship, no AQL, default repository target is a mock | "openEHR-aligned", with a ceiling panel explaining precisely what is and is not there |
| 2 | "lower total cost of ownership by up to 80%" | No such measurement exists anywhere in the repository | Removed. Replaced with checkable claims: £1 per instance, self-hostable, open export |
| 3 | Rename an edition to "Commvita Flow" | A module called commvita Flow **already exists** at `/flow` | The name is used as asked, and the collision is flagged on the editions page |
| 4 | Name Jersey and Guernsey | A binding standing order forbids naming Jersey in branded material | "Crown Dependencies" throughout |
| 5 | "~60 explainers" | 66, counted from disk at generation time | 66 |
| 6 | Genomics "FHIR Genomics profiles", "integration with national genomic services" | No genomics FHIR endpoint; no exchange with any national service; three genomic registers are in-process lists lost on restart | Stated as not built, with the persistence gap named |
| 7 | Portal "consent and permission management", "research participation preferences" | Neither control persists anything | Marked not working, with the four affected controls listed |

Edition module counts (139 / 255 / 417 cumulative) are generated from
`services/web/src/editions.ts` through the same parser the CI gate uses, so
this site and the gate cannot disagree.

## Mobile and tablet

Measured on a device matrix rather than at a couple of round numbers, because
the earlier failures in this codebase were failures of *measurement*: one pass
reported "0 routes overflowing" against photographs of clipping, because it
judged overflow on `document.scrollWidth`, which cannot grow when an ancestor
clips.

    npm --prefix services/web run check:website-devices

| Device | Viewport |
|---|---|
| Android phone | 360 × 740 — the commonest Android width there is, and narrower than anything the earlier sweeps used |
| iPhone SE | 375 × 667 |
| iPhone 15 | 393 × 852 |
| Pixel 8 | 412 × 915 |
| iPhone Pro Max | 430 × 932 |
| iPhone landscape | 844 × 390 |
| iPad mini | 744 × 1133 |
| iPad Pro | 834 × 1194 |
| iPad Pro landscape | 1194 × 834 |
| Desktop | 1440 × 900 |

What the mobile work actually changed:

- **`dvh`/`svh` with a `vh` fallback.** iOS reports `100vh` as the viewport
  with the address bar *hidden*, so a `100vh` slide is taller than the space
  visible and its last line sits under the browser chrome.
- **Safe-area insets, with `viewport-fit=cover`.** Without the meta value
  `env()` is zero and the insets are decorative; with it they are load-bearing,
  and content no longer sits under the notch in landscape.
- **A 44px floor on controls, scoped to `pointer: coarse`.** A 1194px iPad in
  landscape is a touch device and a 1194px laptop is not; width alone cannot
  tell them apart. This moved the brand lockup, breadcrumbs and card-heading
  links from 15–30px to 44px.
- **The primary action above the fold on a phone.** Measured first: the hero
  ran to ~1190px on an 852px viewport, so "Explore commvita" was below the
  fold — the defect where a landing screen looks fine in a screenshot that
  stops at the fold. Now 464–572px on every phone in the matrix, including the
  667px-tall SE.
- **Figures scroll rather than shrink.** A 900px figure cannot be scaled to a
  360px phone and stay legible — 12.5px type would land at 5px. It scrolls
  inside its own container, and a right-edge fade says so; an affordance nobody
  sees is not an affordance.
- **`touch-action: manipulation`** to drop the 300ms tap delay, and a brand
  tap-highlight colour.

## Verification

| Check | Result |
|---|---|
| Device matrix | 32 pages × 10 devices = **320 loads** |
| Document overflow | 0 |
| Element overhang | 0 |
| Tap targets under 44px on touch | 0 |
| Page errors | 0 |
| Internal links | 834 checked, 0 broken, fragments included |
| Mutation test — overflow | a 1500px element fires on all 10 devices |
| Mutation test — tap target | a 60×18 control fires on **9 of 10** — correctly silent on the desktop pointer |

© 2026 Commvita Digital Health Solutions Ltd. All rights reserved.

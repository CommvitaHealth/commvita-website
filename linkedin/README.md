# LinkedIn posts

A run of ready-to-post updates for the commvita page, one every three days,
with a branded image for each. Twenty-one posts, 21 September to 20 November. Nothing here is published by Netlify —
`netlify.toml` publishes `site/`, and this folder sits outside it on purpose.

- `posts/` — one file per post in the three-day run. Front matter, then the
  body you paste.
- `topical/` — off-cadence posts tied to a date or an event, named by the day
  they go out. `plan.py` ignores these; `build_cards.py` renders them.
- `articles/` — long-form pieces for LinkedIn’s article editor. An article
  needs a post pointing at it, since articles get little reach on their own;
  the `teaser:` field names the post that does that job. Its editor has no
  tables, so structure long comparisons as headings and bold lead-ins.
- `cards/` — the typographic image for each post, 2400 × 1254 (a 1200 × 627
  card at 2×).
- `shots/` — real regions of real site pages, captured by `build_shots.py`.
  These are pictures of commvita.com, and a caption has to say so. They are
  not platform screens: the house rules want those captured from the running
  system through its own code paths with a build stamp, and nothing in this
  repository can produce one. Never dress a mock-up as a screen.
- `schedule.md` — dates, editions and subjects, generated from the posts.
- `plan.py` — draws the rotation, writes the schedule, checks the posts match.
- `build_cards.py` — renders the cards.
- `build_shots.py` — captures a page region by CSS selector.
- `build_html.py` — turns an article into one self-contained HTML file in
  `html/`, with the card redrawn at the top and the brand faces inlined, so it
  opens with no network and nothing beside it. It prints a matching PDF beside
  it: A4, the card as a full dark cover page, selectable text and no browser
  header or footer. That folder is still outside
  `site/`: putting a piece on the website means the full job — an entry in the
  explainer index, the document count and a sitemap line.
- `assets/` — design proposals rendered as post imagery, such as the yellow
  download button. A proposal is never captioned as a shipped screen, and
  where it echoes somebody else's published asset the caption has to say it
  is ours and not theirs.
- `AUTOMATION.md` — what it would take to have this post itself.

## Posting one

1. Open the post file. Everything below the front matter is the post,
   hashtags included. Paste it straight into LinkedIn; the apostrophes are
   already curly and the line breaks are where they should be.
2. Attach the image named in `card:`.
3. Post as the commvita page unless you want the reach a personal profile
   brings. AUTOMATION.md covers what that choice costs you later on.

Takes about two minutes.

## What the run covers

Posts 1–4 orient somebody who has never heard of commvita: what it is, the
problem it answers, the three editions, and the platform base that sits under
all of them. Posts 5–18 take the subject at random across Flow, Governance &
Assurance and Population, balanced 5/5/4, with no more than two of an edition
in a row. The draw is seeded, so `plan.py` reproduces it.

Posts 19–21 are an arc on what makes the platform different: the semantic,
kinetic and dynamic layers; why open export answers the question escrow is
usually asked to answer; and why the data model decides what AI on it is
worth. They belong to no single edition. Post 20 is the one to read before
you change anything — it disclaims escrow, support and service levels in the
same words the launch page uses, and it has to keep doing that.

Randomising matters for a reason beyond variety: three consecutive governance
posts teach the audience that this is a governance product, and they stop
reading before the flow ones arrive.

## The rules these posts follow

Everything in the repository's house rules applies — a reader shouldn't be
able to tell a machine helped, nothing confidential, no competitor named, no
internal names or paths. On top of that, three things matter more here than
they do on the site, because a post travels further than a page does:

**Live or demonstrated, every time.** Each post carries a line saying which,
in plain words, drawn from the module's own explainer. Where the status was
unclear, the post claims the weaker one.

**Routes, never internals.** `/flow` and `/golden-thread` are fine and useful.
Module names the platform itself uses in public are fine. File names, classes,
environment variables and build steps are not.

**One published price.** £1 per Commvita Flow Edition instance. Nothing else.

**No number that isn't in this repository or handed over by Martin.** A post
carrying a figure about the platform — test counts, environments, coverage,
uptime — needs that figure to come from somewhere checkable. A post with a
`needs:` line in its front matter is holding `{{...}}` placeholders and
must not go out until they're filled.

## Checks before anything goes out

    python3 tools/voice.py linkedin/posts/*.md linkedin/topical/*.md
    python3 linkedin/plan.py --check               # dates match the draw
    python3 linkedin/build_cards.py                # rebuild every card

A voice grade above about 8 means read it out loud and fix it. This batch
runs from −23.7 to 3.4.

One convention is shared on purpose and will score as repetition if you go
looking for it: every drill-down post ends with `Where to look:` and the
routes. It's the series' sign-off, like a byline, and a reader following the
run learns to look for it.

## Cards

`build_cards.py` reads each post's front matter, lays out the card in HTML
using the site's own brand faces and palette, and screenshots it with the
Chromium in this container. The accent colour comes from the edition: teal for
Flow, violet for Governance & Assurance, amber for Population. Coral marks a
post that belongs to no single edition — the orientation four and the
differentiation arc.

    python3 linkedin/build_cards.py          # all of them
    python3 linkedin/build_cards.py 07 12    # just those two

Two things to know if you change the template. It renders with
`headless_shell` in place of the full Chromium binary, which reserves room
for window chrome it never draws, so the viewport comes back about 87px
short and the bottom of the card silently vanishes. And every element is
placed with explicit coordinates, because a fixed-height flex column mis-paints
under the same screenshot path. Both are worth leaving alone.

Set `CHROME_BIN` if the binary moves.

## The next batch

Write the posts, then run `plan.py --schedule` to regenerate the table. To
carry on past 11 November, change `START` and take a new seed. Subjects with
enough substance behind them for a post, still unused:

- Flow — bed board and the demand-versus-capacity reservoir; RTT and the
  shared PTL; theatres; A&E demand; winter planning.
- Governance & Assurance — policy-to-process with its authority matrix;
  CAPA and duty of candour; on-call and EPRR; clinical audit; the register of
  interests; statutory returns.
- Population — the population risk pyramid; medicines optimisation; social
  care on the same record; maternity; ambient clinical documentation;
  genomics, which needs care because parts of it are stated as not built.

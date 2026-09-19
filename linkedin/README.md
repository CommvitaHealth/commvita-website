# LinkedIn posts

A run of ready-to-post updates for the commvita page, one every three days,
with a branded image for each. Nothing here is published by Netlify —
`netlify.toml` publishes `site/`, and this folder sits outside it on purpose.

- `posts/` — one file per post. Front matter, then the body you paste.
- `cards/` — the image for each post, 2400 × 1254 (a 1200 × 627 card at 2×).
- `schedule.md` — dates, editions and subjects, generated from the posts.
- `plan.py` — draws the rotation, writes the schedule, checks the posts match.
- `build_cards.py` — renders the cards.
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
all of them. From post 5 the subject is drawn at random across Flow,
Governance & Assurance and Population, balanced 5/5/4, with no more than two
of an edition in a row. The draw is seeded, so `plan.py` reproduces it.

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

## Checks before anything goes out

    python3 tools/voice.py linkedin/posts/*.md     # house voice score
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
Flow, violet for Governance & Assurance, amber for Population, coral for the
orientation posts.

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

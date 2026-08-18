# Commvita website

Public marketing and information site for [Commvita](https://commvita.com) — an open, integrated clinical and operational platform for health systems.

## What this is

A fully static site: 99 HTML pages, one stylesheet, a favicon, `robots.txt` and `sitemap.xml`, no build step, no server-side code, no external JavaScript dependencies. Every link is relative, so the site works from the filesystem, any static host, or behind a reverse proxy.

- `site/` — the deployable site. `site/index.html` is the homepage.
- `index.html` (repo root) — convenience redirect into `site/` for local browsing; not deployed.
- `netlify.toml` — Netlify configuration: publishes `site/` and sets security headers.
- `SITE-NOTES.md` — the original design/structure notes that shipped with the site.
  Treat it as a historical record, not a description of this repository: it refers to
  32 pages, 66 library documents and a `docs/build_website.py` generator, none of which
  are here. The HTML in `site/` is maintained by hand, so the counts it quotes drift.

## Hosting

Deployed on Netlify. Every push to `main` deploys to production; every pull request gets a preview URL (posted automatically on the PR) for review before merge.

There is no build command — Netlify serves `site/` as-is.

## Making changes

1. Branch from `main`, edit the HTML directly.
2. Open a PR. Netlify posts a deploy preview link on the PR.
3. Review the preview, merge. Production updates in under a minute.

To preview locally, either open `index.html` in a browser or run a local server from the repo root:

```
python3 -m http.server 8000 --directory site
```

## Conventions

- **Nothing marked confidential ships.** If a document carries a confidentiality or
  distribution marking — "confidential", "private & confidential", "not for
  distribution", "internal use only" — it does not belong in `site/` or anywhere
  else in this repository, because this repository is the public website. Removing
  it from the working tree is not enough on its own: git history keeps the file, so
  anything published in error has to be purged from history as well.
  Check before adding a document:

  ```
  grep -rliE 'not for distribution|private & confidential|internal use only' site/
  ```

  Beware letter-spaced markings inside SVG text — strip tags and whitespace before
  matching, or a cover slide reading `P r i v a t e` will pass a naive grep.
- Keep all links relative — no absolute paths, no hard-coded domain. The one
  exception is `site/sitemap.xml`, which the sitemap protocol requires to carry
  absolute URLs; it uses the canonical domain, `https://commvita.com`.
- No trackers, analytics, or third-party scripts without an explicit decision.
- No real patient data, screenshots containing real data, or credentials of any kind in this repo. Pages that document integration patterns refer to environment-variable *names* only.

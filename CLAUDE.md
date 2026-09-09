# House rules for the commvita website

These apply to every page in `site/`, every explainer, and anything else that
ends up in front of a reader. They are standing rules: they hold for all future
work on this repo unless Martin says otherwise.

## 1. Write like a person, not like a machine

The test: a reader should not be able to tell the pages were drafted with help.
That means writing the way a knowledgeable colleague writes when they are
explaining something to someone they respect.

**Do this**

- Use contractions. "It doesn't make clinical decisions", not "It does not make
  clinical decisions". "We haven't read the annex", not "The annex has not been
  read."
- Say who did what. "We tried" beats "an attempt was made". Passive voice hides
  the person, and hiding the person is what makes copy sound automated.
- Vary sentence length. A run of three medium sentences with the same shape is
  the single loudest tell.
- Use plain words. Sums, not arithmetic. Works out, not derives. Stops you,
  not refuses. Keep the technical word where it is the real word — segment,
  provenance, tariff, k-anonymity — and explain it once.
- Let headings say something specific. "It isn't a dispensing system" tells the
  reader more than "What it isn't."

**Don't do this**

- Don't reuse a sentence template across documents. If two explainers end a
  paragraph the same way, one of them is wrong.
- Don't lean on "rather than". About one per document is plenty; after that use
  "instead of", "not", or rewrite the sentence.
- Don't use "deliberately", "genuinely", "actually", "carefully" or "simply" as
  intensifiers. If the sentence needs one, the sentence is weak.
- Don't write the aphoristic closing line. "A threshold typed from memory is
  indistinguishable from a sourced one" is the sound of a machine reaching for
  profundity. Say what happens and stop.
- Don't open on a number unless the number matters. Eleven documents once began
  "N things, one thing"; that is a template, not a style.
- Don't pair em dashes around an aside twice in the same paragraph.
- Don't write "X, not Y" more than once or twice in a document.

**Check it before committing.** `tools/voice.py` scores every page for these
tells and prints the worst first:

    python3 tools/voice.py                      # whole site
    python3 tools/voice.py site/explainers/foo.html

A grade above about 8 means go back and read it out loud.

## 2. What never goes on a public page

- Anything marked confidential. Not in `site/`, not in git history.
- A competitor's name. Not the company, not the product. Describe what other
  systems do without naming them. We partner with suppliers; we don't consume
  them.
- Repository paths, file names, class or function names, environment variables,
  build commands, test names, internal defect notes, PRD or ADR references.
  Routes (`/mental-health`) and API paths (`/mh/cpa`) are fine and useful.
- Customer or prospect names.
- Prices beyond the published £1 per Flow Edition instance.
- Commitments on escrow, service levels, support or funding that haven't been
  made.

## 3. Claims have to be true on the day they are published

- **Live** means real, API-backed platform logic wired end to end today.
  **Demonstrated** means a representative surface over seeded data. Every page
  says which, and the difference is checked against the running system, not
  assumed.
- Screenshots come from the running platform, captured through its own code
  paths, with the build stamp in the caption. Never a mock-up dressed as a
  screen.
- A competitive claim ("first to market", "ahead of the field") needs evidence
  from the platform's own competitive audit and a provenance line saying it is
  our assessment, not an independent one.
- Never copy source from the platform repo into this one. Rendered screenshots
  only.

## 4. Mechanics

- Static HTML, relative links, no build step. `site/` is what Netlify
  publishes, so anything inside it is public.
- Every page must render clean at 1280 and 390: no horizontal overflow, no
  broken images, no script errors.
- Curly apostrophes (`&rsquo;`) in prose, to match the rest of the site.
- New explainer: add it to `site/explainers/index.html`, update the document
  count, and add a `site/sitemap.xml` entry.

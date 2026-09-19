# Can the commvita LinkedIn page be wired to Claude?

Short answer: yes, and the last step of it is the one you probably shouldn't
take. Drafting, checking and scheduling all automate cleanly. Publishing
without a person looking is where it goes wrong, and it goes wrong in the one
way this company can least afford.

There are three levels. They cost very different amounts of setup.

## Level 1 — Claude writes, you post

What this branch already is. Claude drafts the post, scores it against the
house voice tool, checks it for competitor names and unpublishable claims,
renders the card, and commits the lot. You copy, attach, post. Two minutes
every three days.

Nothing to approve, no tokens to rotate, no third party holding a credential
to the page. It also means somebody reads each post on the day it goes out,
which is worth more than it sounds — see the bottom of this file.

## Level 2 — Claude writes, a scheduler posts

Buffer, Hootsuite, Later and the rest are already approved LinkedIn partners,
so they can post to a company page without you applying for anything. You
authorise the page once inside their product, and the queue does the rest.

Two ways to feed it:

- **By hand, in batches.** Paste a month of posts into the queue in one
  sitting. No integration at all, and it removes the "did anyone post today?"
  problem, which is the thing that actually kills a cadence.
- **Through their API.** Most of them have one. A small job reads the next due
  post out of this folder, uploads the card, and adds it to the queue. Claude
  can write that job; it's a morning's work, not a project.

This is the sweet spot for most organisations. The scheduler holds the
LinkedIn credential, you keep the approval step, and nothing depends on
LinkedIn's developer programme.

## Level 3 — Claude publishes to the page directly

Technically possible, and the setup is heavier than people expect.

Posting to a **company page** needs the Community Management API, and that's
gated. You need a registered company, a verified LinkedIn Page, a developer
app, and a two-tier review that LinkedIn does by hand — commonly one to four
weeks. It isn't open to an individual developer. If you don't go on to apply
for the standard tier within twelve months, access gets withdrawn for
inactivity.

Then the tokens. A standard Community Management app gets a 60-day access
token and **no refresh token**, so somebody re-authorises by hand every two
months. Approved Marketing Developer Platform partners can get refresh tokens
good for a year; that's a separate partnership, not a checkbox.

Posting a text update is one call. Posting a card is three: initialise the
image upload, PUT the binary, then reference the returned image URN in the
post. The API is versioned and wants a version header on every request, so
this is code that needs maintaining, not code you write once.

Posting to a **personal profile** is much easier — self-serve, no page
approval. Which is why most "Claude posts to LinkedIn" write-ups are quietly
about somebody's own profile. Worth knowing before you follow one.

MCP servers exist that would let Claude call LinkedIn as a tool directly —
open-source ones, and hosted ones from Composio and Postiv. They're real and
they work, but they don't route around the approval: a company page still
needs LinkedIn to say yes. What they change is the plumbing, not the gate.

## What's worth automating whichever level you pick

The writing isn't the bottleneck. The bottleneck is that on a Tuesday in
January nobody has drafted Thursday's post.

So put Claude on a schedule against this repository instead of against
LinkedIn:

- Once a fortnight, draft the next four posts from the backlog in the README.
- Run the voice score, the competitor and claim checks, and the date check.
- Render the cards.
- Open a pull request with the lot.

You review a PR every couple of weeks and the queue never runs dry. Claude
Code on the web can run that on a Routine; a scheduled GitHub Action can run
it too. Neither needs LinkedIn to approve anything.

## The gate I'd keep whatever you build

House rule three says a claim has to be true on the day it's published, and
these posts carry live-or-demonstrated statements about a platform that's
moving. A post written in September and auto-published in November is a claim
about a build nobody checked.

So: automate the drafting, the checking, the card, the scheduling and the
reminder. Keep a person between the queue and the page. The cost is two
minutes; the thing it protects is the reason anyone believes the rest of the
site.

## Sources

These were checked in September 2026 and LinkedIn changes its developer
programme often. Confirm against the current documentation before you commit
to level 3.

- [Community Management API migration guide — Microsoft Learn](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-api-migration-guide?view=li-lms-2026-06)
- [LinkedIn Community Management API access approval (2026)](https://singhamandeep.com/linkedin-community-management-api-access/)
- [LinkedIn API 2026: access, endpoints, limits and alternatives](https://connectsafely.ai/articles/linkedin-api-complete-guide-2026)
- [linkedin-mcp — open-source MCP server for the official LinkedIn API](https://github.com/vlpmedialtd/linkedin-mcp)
- [Composio — connecting LinkedIn to Claude Code](https://composio.dev/toolkits/linkedin/framework/claude-code)
- [Postiv — LinkedIn MCP server for Claude and AI agents](https://postiv.ai/linkedin-mcp)

#!/usr/bin/env python3
"""The posting schedule: draw it, write it out, and check the posts match.

Orientation posts run first and carry no single edition. After that the
rotation is drawn at random from a fixed seed, balanced across the three
editions, with no more than two posts from the same edition back to back.
The seed lives here so the draw can be reproduced, or a new one taken for
the next batch.

    python3 linkedin/plan.py                 # print the draw
    python3 linkedin/plan.py --schedule      # rewrite linkedin/schedule.md
    python3 linkedin/plan.py --check         # do the posts match the draw?
    python3 linkedin/plan.py --bundle        # every post as one document
    python3 linkedin/plan.py --draw 12345    # try a different seed
"""
import argparse, datetime, os, random, sys

HERE  = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.join(HERE, 'posts')

START  = datetime.date(2026, 9, 21)   # first post
GAP    = 3                            # days between posts
ORIENT = 4                            # orientation posts before the rotation
SEED   = 20260921
MIX    = ['F'] * 5 + ['G'] * 5 + ['P'] * 4   # the 14 rotation slots
NAME   = {'F': 'Flow', 'G': 'Governance & Assurance',
          'P': 'Population', '-': 'Orientation'}


def draw(seed=SEED):
    """A shuffle with no more than two of an edition in a row."""
    rng = random.Random(seed)
    for _ in range(500):
        order = MIX[:]
        rng.shuffle(order)
        if not any(order[i] == order[i + 1] == order[i + 2]
                   for i in range(len(order) - 2)):
            return order
    raise SystemExit('no draw satisfied the run-length rule')


def slots(seed=SEED):
    order = ['-'] * ORIENT + draw(seed)
    for i, ed in enumerate(order):
        yield i + 1, START + datetime.timedelta(days=GAP * i), NAME[ed]


def front_matter(path):
    meta = {}
    block = open(path, encoding='utf-8').read().split('---', 2)[1]
    for line in block.splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip()
    meta['path'] = path
    return meta


def posts():
    return [front_matter(os.path.join(POSTS, f))
            for f in sorted(os.listdir(POSTS)) if f.endswith('.md')]


def check():
    bad = []
    for (n, date, edition), meta in zip(slots(), posts()):
        if meta.get('date') != date.isoformat():
            bad.append(f"post {n}: date is {meta.get('date')}, draw says {date}")
        if meta.get('edition') != edition:
            bad.append(f"post {n}: edition is {meta.get('edition')}, draw says {edition}")
    for line in bad:
        print(line)
    print('posts match the draw' if not bad else f'{len(bad)} mismatch(es)')
    return 1 if bad else 0


def schedule_md():
    rows = []
    for meta in posts():
        d = datetime.date.fromisoformat(meta['date'])
        weekend = ' *(weekend)*' if d.weekday() >= 5 else ''
        rows.append('| {n} | {date}{we} | {ed} | {mod} | [{slug}](posts/{slug}.md) |'.format(
            n=meta['post'], date=d.strftime('%a %d %b %Y'), we=weekend,
            ed=meta['edition'], mod=meta['module'],
            slug=os.path.basename(meta['path'])[:-3]))
    first = datetime.date.fromisoformat(posts()[0]['date'])
    last = datetime.date.fromisoformat(posts()[-1]['date'])
    return f"""# Posting schedule

One post every {GAP} days, {first:%d %B %Y} to {last:%d %B %Y}. Generated from the
post files by `plan.py --schedule`, so this table can't drift from what's written.

Posts 1–{ORIENT} orient a reader who has never heard of commvita. From post {ORIENT + 1} the
editions are drawn at random (seed {SEED}), balanced {MIX.count('F')}/{MIX.count('G')}/{MIX.count('P')} across Flow,
Governance & Assurance and Population, with no more than two of an edition
in a row.

Dates that land on a Saturday or Sunday are marked. Engagement is thinner at
the weekend, so either move those to the Monday and let the cadence drift, or
post them anyway and keep the rhythm exact. Pick one and stick to it.

| # | Date | Edition | Subject | Post |
|---|------|---------|---------|------|
""" + '\n'.join(rows) + '\n'


def bundle():
    """Every post in order, as one document you can read or hand to someone."""
    out = ["# commvita on LinkedIn — the full run\n",
           "Eighteen posts, one every %d days. Paste the body of a post straight\n"
           "into LinkedIn and attach the card named under it. The source files\n"
           "are in `posts/`, the images in `cards/`.\n" % GAP]
    for meta in posts():
        d = datetime.date.fromisoformat(meta['date'])
        body = open(meta['path'], encoding='utf-8').read().split('---', 2)[2].strip()
        card = os.path.basename(meta.get('card', ''))
        out.append('\n---\n')
        out.append(f"## {meta['post']} · {d:%A %d %B %Y} · {meta['edition']}\n")
        out.append(f"**Subject** {meta['module']}  ")
        if meta.get('routes') not in (None, '—', '-'):
            out.append(f"**Where to look** {meta['routes']}  ")
        out.append(f"**Image** `cards/{card}`  ")
        out.append(f"**Status** {meta.get('status', '')}\n")
        out.append('### Post\n')
        out.append(body + '\n')
    return '\n'.join(out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--schedule', action='store_true')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--bundle', action='store_true')
    ap.add_argument('--draw', type=int, default=SEED)
    a = ap.parse_args()
    if a.check:
        sys.exit(check())
    if a.bundle:
        sys.stdout.write(bundle())
        sys.exit(0)
    if a.schedule:
        out = os.path.join(HERE, 'schedule.md')
        open(out, 'w', encoding='utf-8').write(schedule_md())
        print('wrote', os.path.relpath(out, os.path.dirname(HERE)))
    else:
        for n, d, ed in slots(a.draw):
            print(f"{n:>2}  {d:%a %d %b %Y}{'  (weekend)' if d.weekday() >= 5 else '':<11}  {ed}")

#!/usr/bin/env python3
"""Render a branded 1200x627 image for every post in linkedin/posts/.

Reads the front matter of each post, lays the card out in HTML using the
site's own brand faces and palette, and screenshots it with the Chromium
that ships with this container. Nothing here is published by Netlify —
linkedin/ sits outside site/ on purpose.

    python3 linkedin/build_cards.py            # all posts
    python3 linkedin/build_cards.py 07 12      # just those two
"""
import os, re, subprocess, sys, tempfile, html

HERE  = os.path.dirname(os.path.abspath(__file__))
ROOT  = os.path.dirname(HERE)
POSTS = os.path.join(HERE, 'posts')
CARDS = os.path.join(HERE, 'cards')
CHROME = os.environ.get(
    'CHROME_BIN',
    '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell')

ACCENT = {'Orientation': '#FF5B47', 'Flow': '#00B8A6',
          'Governance & Assurance': '#7B61FF', 'Population': '#FFB020'}

MARK = ('<svg viewBox="0 0 100 100" width="52" height="52" aria-hidden="true">'
        '<line x1="52" y1="49" x2="20" y2="30" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
        '<line x1="52" y1="49" x2="78" y2="18" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
        '<line x1="52" y1="49" x2="26" y2="80" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
        '<line x1="52" y1="49" x2="84" y2="62" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
        '<circle cx="20" cy="30" r="8.5" fill="#00B8A6"/>'
        '<circle cx="78" cy="18" r="7" fill="#7B61FF"/>'
        '<circle cx="26" cy="80" r="6" fill="#FFB020"/>'
        '<circle cx="84" cy="62" r="9.5" fill="#FF5B47"/>'
        '<circle cx="52" cy="49" r="15" fill="#fff"/>'
        '<circle cx="52" cy="49" r="6" fill="#141C2E"/></svg>')

TEMPLATE = """<!doctype html><html lang="en"><meta charset="utf-8">
<link rel="stylesheet" href="{fonts}">
<style>
  /* Everything on the card is placed absolutely inside a fixed stage.
     Headless Chromium mis-paints a fixed-height flex column when it
     screenshots, and silently drops the footer; explicit coordinates
     render the same every time. */
  *{{margin:0;padding:0;box-sizing:border-box}}
  html,body{{width:1200px;height:627px;overflow:hidden;background:#141C2E}}
  .stage{{position:absolute;top:0;left:0;width:1200px;height:627px;
         background:#141C2E;color:#fff;overflow:hidden;
         font-family:"Archivo","Familjen Grotesk",system-ui,sans-serif}}
  .glow{{position:absolute;right:-180px;top:-180px;width:640px;height:640px;
        border-radius:50%;background:radial-gradient(circle,{accent}2E 0%,transparent 68%)}}
  .lock{{position:absolute;left:64px;top:52px;display:flex;align-items:center;gap:14px}}
  .wm{{font-family:"Familjen Grotesk","Archivo",sans-serif;font-weight:800;
      font-size:27px;letter-spacing:-.02em}}
  .wm sup{{font-size:.48em;font-weight:700;vertical-align:super}}
  .tag{{font-size:13px;font-weight:600;color:#8CA1C2;letter-spacing:.02em;
       padding-left:14px;border-left:1px solid rgba(255,255,255,.18)}}
  .body{{position:absolute;left:64px;top:186px;width:1010px}}
  .kick{{display:block;font-size:14px;font-weight:800;letter-spacing:.14em;
        text-transform:uppercase;color:{accent};margin-bottom:20px}}
  h1{{font-family:"Familjen Grotesk","Archivo",sans-serif;font-weight:800;
     font-size:{size}px;line-height:1.08;letter-spacing:-.022em}}
  .sub{{margin-top:18px;font-size:21px;line-height:1.45;color:#C2D0E6;max-width:880px}}
  .rule{{position:absolute;left:64px;right:64px;bottom:96px;height:1px;
        background:rgba(255,255,255,.14)}}
  .bar{{position:absolute;left:64px;bottom:60px;width:46px;height:5px;
       border-radius:3px;background:{accent}}}
  .routes{{position:absolute;left:126px;bottom:52px;font-size:15px;
          font-weight:650;color:#8CA1C2;letter-spacing:.01em}}
  .site{{position:absolute;right:64px;bottom:52px;font-size:15px;
        font-weight:700;color:#EAF1FB}}
</style>
<div class="stage">
  <div class="glow"></div>
  <div class="lock">{mark}<span class="wm">commvita<sup>&trade;</sup></span>
    <span class="tag">Connected care platform</span></div>
  <div class="body">
    <span class="kick">{kicker}</span>
    <h1>{headline}</h1>
    {sub}
  </div>
  <div class="rule"></div>
  <span class="bar"></span>
  <span class="routes">{routes}</span>
  <span class="site">commvita.com</span>
</div>
</html>"""


def front_matter(path):
    text = open(path, encoding='utf-8').read()
    block = text.split('---', 2)[1]
    meta = {}
    for line in block.splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip()
    return meta


def headline_size(text):
    """Long headlines step down so the card never needs a scrollbar."""
    n = len(text)
    return 68 if n <= 38 else 60 if n <= 54 else 52 if n <= 72 else 45


def build(post_path):
    meta = front_matter(post_path)
    accent = ACCENT.get(meta.get('edition', ''), '#00B8A6')
    headline = meta.get('card_headline', '')
    sub = meta.get('card_sub', '')
    routes = meta.get('routes', '')
    routes = '' if routes in ('—', '-', '') else routes
    page = TEMPLATE.format(
        fonts=os.path.join(ROOT, 'site', 'fonts.css'),
        accent=accent, mark=MARK,
        kicker=html.escape(meta.get('card_kicker', '')),
        headline=html.escape(headline),
        size=headline_size(headline),
        sub=f'<p class="sub">{html.escape(sub)}</p>' if sub else '',
        routes=html.escape(routes or 'commvita'),
    )
    name = os.path.splitext(os.path.basename(post_path))[0]
    out = os.path.join(CARDS, name + '.png')
    with tempfile.NamedTemporaryFile('w', suffix='.html', dir=CARDS,
                                     delete=False, encoding='utf-8') as fh:
        fh.write(page)
        tmp = fh.name
    try:
        subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu',
                        '--hide-scrollbars', '--force-device-scale-factor=2',
                        '--window-size=1200,627', f'--screenshot={out}', tmp],
                       check=True, capture_output=True)
    finally:
        os.unlink(tmp)
    return out


if __name__ == '__main__':
    want = set(sys.argv[1:])
    os.makedirs(CARDS, exist_ok=True)
    for f in sorted(os.listdir(POSTS)):
        if not f.endswith('.md'):
            continue
        if want and f[:2] not in want:
            continue
        print('wrote', os.path.relpath(build(os.path.join(POSTS, f)), ROOT))

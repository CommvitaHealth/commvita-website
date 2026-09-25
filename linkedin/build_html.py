#!/usr/bin/env python3
"""Turn an article into one self-contained HTML file, card and all.

The card is redrawn as HTML at the top of the page instead of being pasted
in as a screenshot, so it stays crisp at any size and the file stays small.
The brand faces are inlined from the site's own stylesheet, which means the
result opens correctly with no network, no server and nothing beside it.

    python3 linkedin/build_html.py                     # every article
    python3 linkedin/build_html.py 2026-09-25-vbhc-glossary-alignment

Output lands in linkedin/html/. Nothing here is published by Netlify. To
put a piece on the site instead, it has to go through site/ properly:
an entry in the explainer index, the document count and the sitemap.
"""
import html as _h, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ARTICLES = os.path.join(HERE, 'articles')
OUT = os.path.join(HERE, 'html')
FONTS = os.path.join(ROOT, 'site', 'fonts.css')
SHELL = os.environ.get('CHROME_BIN',
        '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell')

ACCENT = {'Orientation': '#FF5B47', 'Platform': '#FF5B47', 'Flow': '#00B8A6',
          'Governance & Assurance': '#7B61FF', 'Population': '#FFB020'}

MARK = ('<svg viewBox="0 0 100 100" width="46" height="46" aria-hidden="true">'
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


def front_matter(path):
    text = open(path, encoding='utf-8').read()
    _, block, body = text.split('---', 2)
    meta = {}
    for line in block.splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip()
    return meta, body.strip()


def markdown(src):
    """Enough markdown for these articles: headings, bold, paragraphs."""
    out = []
    for block in re.split(r'\n\s*\n', src):
        block = block.strip()
        if not block:
            continue
        m = re.match(r'^(#{1,3})\s+(.*)$', block, re.S)
        if m:
            level = len(m.group(1))
            text = _h.escape(m.group(2).strip())
            tag = {1: 'h1', 2: 'h2', 3: 'h3'}[level]
            out.append(f'<{tag}>{text}</{tag}>')
            continue
        text = _h.escape(block).replace('\n', ' ')
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        out.append(f'<p>{text}</p>')
    return '\n'.join(out)


PAGE = """<!doctype html><html lang="en-GB"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{dek}">
<style>
{fonts}
:root{{
  --ink:#141C2E; --body:#42506B; --muted:#5D6B85; --hair:#D9DFE8;
  --page:#FFFFFF; --accent:{accent};
  --sans:"Archivo","Familjen Grotesk",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --display:"Familjen Grotesk","Archivo",system-ui,-apple-system,sans-serif;
}}
@media(prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --page:#0C1626; --ink:#EAF1FB; --body:#C2D0E6; --muted:#8CA1C2;
    --hair:rgba(255,255,255,.14);
  }}
}}
:root[data-theme="dark"]{{
  --page:#0C1626; --ink:#EAF1FB; --body:#C2D0E6; --muted:#8CA1C2;
  --hair:rgba(255,255,255,.14);
}}
*,*::before,*::after{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--page);color:var(--body);font-family:var(--sans);
  font-size:1.0625rem;line-height:1.66;-webkit-font-smoothing:antialiased}}
img,svg{{max-width:100%}}

/* ── the card, redrawn ─────────────────────────────────────────────── */
.card{{position:relative;overflow:hidden;background:#141C2E;color:#fff;
  padding:clamp(28px,5vw,56px) clamp(20px,5vw,64px)}}
.card-in{{max-width:1072px;margin:0 auto;position:relative}}
.card .glow{{position:absolute;right:-22%;top:-58%;width:min(640px,88vw);
  aspect-ratio:1;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle,{accent}2E 0%,transparent 68%)}}
.lock{{display:flex;align-items:center;gap:13px;margin-bottom:clamp(38px,8vw,92px)}}
.wm{{font-family:var(--display);font-weight:800;font-size:1.44rem;letter-spacing:-.02em}}
.wm sup{{font-size:.48em;font-weight:700;vertical-align:super}}
.tag{{font-size:.8rem;font-weight:600;color:#8CA1C2;padding-left:13px;
  border-left:1px solid rgba(255,255,255,.18)}}
.kick{{display:block;font-size:.8rem;font-weight:800;letter-spacing:.14em;
  text-transform:uppercase;color:{accent};margin-bottom:18px}}
.card h1{{font-family:var(--display);font-weight:800;color:#fff;margin:0;
  font-size:clamp(1.85rem,1.1rem+3.1vw,3.4rem);line-height:1.07;letter-spacing:-.022em}}
.card .sub{{margin:18px 0 0;font-size:clamp(1rem,.94rem+.4vw,1.28rem);
  line-height:1.45;color:#C2D0E6;max-width:56ch}}
.card .rule{{margin-top:clamp(38px,8vw,88px);padding-top:20px;
  border-top:1px solid rgba(255,255,255,.14);display:flex;align-items:center;
  gap:16px;flex-wrap:wrap;font-size:.84rem;font-weight:650;color:#8CA1C2}}
.card .bar{{width:42px;height:5px;border-radius:3px;background:{accent};flex:none}}
.card .site{{margin-left:auto;color:#EAF1FB;font-weight:700}}

/* ── the article ───────────────────────────────────────────────────── */
main{{max-width:44rem;margin:0 auto;padding:clamp(34px,6vw,64px) clamp(20px,5vw,32px) 24px}}
main h1{{display:none}}  /* the card already carries the title */
h2,h3{{font-family:var(--display);color:var(--ink);line-height:1.2;letter-spacing:-.014em}}
h2{{font-size:clamp(1.3rem,1.1rem+.9vw,1.75rem);margin:2.1em 0 .5em;font-weight:800}}
h3{{font-size:clamp(1.06rem,1rem+.35vw,1.22rem);margin:1.9em 0 .4em;font-weight:700;
  color:var(--accent)}}
h2+h3{{margin-top:1.1em}}
p{{margin:0 0 1.15em}}
strong{{color:var(--ink);font-weight:700}}
main>p:first-of-type{{font-size:1.16em;line-height:1.58;color:var(--ink)}}
footer{{max-width:44rem;margin:0 auto;padding:22px clamp(20px,5vw,32px) 56px;
  border-top:1px solid var(--hair);font-size:.83rem;color:var(--muted);line-height:1.6}}
footer p{{margin:0 0 .5em}}
@page{{size:A4;margin:0}}
@media print{{
  /* force the light palette: a print job should never inherit dark mode */
  :root{{--page:#FFFFFF;--ink:#141C2E;--body:#42506B;--muted:#5D6B85;--hair:#D9DFE8}}
  body{{background:#fff;font-size:10.6pt;line-height:1.58}}
  /* the card becomes a full A4 cover page */
  .card{{background:#141C2E !important;-webkit-print-color-adjust:exact;
    print-color-adjust:exact;min-height:297mm;padding:26mm 20mm 20mm;
    display:flex;flex-direction:column;break-after:page}}
  .card-in{{display:flex;flex-direction:column;flex:1 1 auto;max-width:none}}
  .card .lock{{margin-bottom:0}}
  .card .kick{{margin-top:auto}}
  .card h1{{font-size:32pt;line-height:1.05}}
  .card .sub{{font-size:13pt;max-width:46ch}}
  .card .rule{{margin-top:auto;padding-top:5mm;font-size:9pt}}
  .card .glow{{display:none}}
  main{{max-width:none;margin:0;padding:18mm 20mm 0}}
  main>p:first-of-type{{font-size:1.08em}}
  footer{{max-width:none;margin:0;padding:7mm 20mm 14mm}}
  h2{{margin-top:1.5em}}
  h2,h3{{break-after:avoid;break-inside:avoid}}
  p{{orphans:3;widows:3}}
}}
</style>
<header class="card">
  <div class="card-in">
    <div class="glow"></div>
    <div class="lock">{mark}<span class="wm">commvita<sup>&trade;</sup></span>
      <span class="tag">Connected care platform</span></div>
    <span class="kick">{kicker}</span>
    <h1>{headline}</h1>
    {sub}
    <div class="rule"><span class="bar"></span><span>{routes}</span>
      <span class="site">commvita.com</span></div>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <p>{source}</p>
  <p>&copy; 2026 Commvita Digital Health Solutions Ltd. All rights reserved.</p>
</footer>
</html>"""


def build(name):
    path = os.path.join(ARTICLES, name + '.md')
    meta, body = front_matter(path)
    accent = ACCENT.get(meta.get('edition', ''), '#00B8A6')
    headline = meta.get('card_headline', '')
    sub = meta.get('card_sub', '')
    routes = meta.get('routes', '')
    routes = '' if routes in ('—', '-', '') else routes
    page = PAGE.format(
        fonts=open(FONTS, encoding='utf-8').read(),
        accent=accent, mark=MARK,
        title=_h.escape(headline or name),
        dek=_h.escape(sub),
        kicker=_h.escape(meta.get('card_kicker', '')),
        headline=_h.escape(headline),
        sub=f'<p class="sub">{_h.escape(sub)}</p>' if sub else '',
        routes=_h.escape(routes or 'commvita'),
        body=markdown(body),
        source=_h.escape(meta.get('source', '')),
    )
    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, name + '.html')
    open(dest, 'w', encoding='utf-8').write(page)
    pdf = dest[:-5] + '.pdf'
    subprocess.run([SHELL, '--headless', '--no-sandbox', '--disable-gpu',
                    '--no-pdf-header-footer', '--virtual-time-budget=6000',
                    f'--print-to-pdf={pdf}', dest],
                   check=True, capture_output=True)
    return dest, pdf


if __name__ == '__main__':
    want = sys.argv[1:] or [f[:-3] for f in sorted(os.listdir(ARTICLES))
                            if f.endswith('.md')]
    for name in want:
        for f in build(name):
            print(f'wrote {os.path.relpath(f, ROOT)}  {os.path.getsize(f) // 1024} KB')

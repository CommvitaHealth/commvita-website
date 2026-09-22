#!/usr/bin/env python3
"""Capture a real region of a real site page as a PNG for a post.

These are screenshots of the published website, not of the platform. The
house rules are strict about platform screens — they come from the running
system, through its own code paths, with a build stamp in the caption — and
nothing in this repository can produce one. What this does produce is an
honest picture of a page anyone can open at commvita.com, which is fine to
use as long as the caption says that is what it is.

    python3 linkedin/build_shots.py             # every entry in SHOTS
    python3 linkedin/build_shots.py ehds-table  # just that one
"""
import json, os, re, subprocess, sys, tempfile

HERE  = os.path.dirname(os.path.abspath(__file__))
ROOT  = os.path.dirname(HERE)
OUT   = os.path.join(HERE, 'shots')
SHELL = os.environ.get('CHROME_BIN',
        '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell')

# name: (page relative to the repo root, CSS selector, which match, render width)
SHOTS = {
    'ehds-obligations': ('site/explainers/commvita-explainer-who-ehds.html',
                         'table', 1, 1180),
    'ehds-blocks':      ('site/explainers/commvita-explainer-who-ehds.html',
                         'table', 0, 1180),
    'openehr-ceiling':  ('site/standards.html', '.ceiling', 0, 1000),
    'yellow-button':    ('linkedin/assets/yellow-button.html', '.yb-stage', 0, 620),
}

WRAP = """<script>
window.addEventListener('load', function () {
  var el = document.querySelectorAll(%s)[%d];
  if (!el) { document.title = 'H:0'; return; }
  document.body.replaceChildren(el);
  document.body.style.cssText =
    'margin:0;padding:%dpx;background:#fff;display:block';
  document.documentElement.style.cssText = 'background:#fff';
  var pad = %d;
  var report = function () {
    document.title = 'H:' + Math.ceil(el.getBoundingClientRect().height + 2 * pad);
  };
  report();                       // synchronously, in case nothing else runs
  requestAnimationFrame(report);  // again once layout has settled
});
</script>"""


def isolated(page, selector, nth, pad):
    src = os.path.join(ROOT, page)
    doc = open(src, encoding='utf-8').read()
    base = '<base href="file://%s/">' % os.path.dirname(src)
    doc = doc.replace('<head>', '<head>' + base, 1) if '<head>' in doc else base + doc
    return doc + WRAP % (json.dumps(selector), nth, pad, pad)


def measure(path, width, tries=3):
    """Chromium's first launch can snapshot the DOM before the page scripts
    have run, so a cold start reports nothing. Ask again rather than
    treating the first miss as an empty selector."""
    for _ in range(tries):
        out = subprocess.run([SHELL, '--headless', '--no-sandbox', '--disable-gpu',
                              f'--window-size={width},900', '--virtual-time-budget=4000',
                              '--dump-dom', path], capture_output=True, text=True).stdout
        m = re.search(r'<title>H:(\d+)</title>', out)
        if m and int(m.group(1)):
            return int(m.group(1))
    return 0


def build(name, pad=28):
    page, selector, nth, width = SHOTS[name]
    doc = isolated(page, selector, nth, pad)
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False,
                                     encoding='utf-8') as fh:
        fh.write(doc)
        tmp = fh.name
    try:
        height = measure(tmp, width)
        if not height:
            raise SystemExit(f'{name}: {selector!r}[{nth}] matched nothing in {page}')
        dest = os.path.join(OUT, name + '.png')
        subprocess.run([SHELL, '--headless', '--no-sandbox', '--disable-gpu',
                        '--hide-scrollbars', '--force-device-scale-factor=2',
                        '--virtual-time-budget=4000',
                        f'--window-size={width},{height}',
                        f'--screenshot={dest}', tmp], check=True, capture_output=True)
        return dest, width, height
    finally:
        os.unlink(tmp)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name in (sys.argv[1:] or SHOTS):
        dest, w, h = build(name)
        print(f'wrote {os.path.relpath(dest, ROOT)}  {w}x{h}')

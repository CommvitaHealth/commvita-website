#!/usr/bin/env python3
"""Inline the brand faces into a poster source, then render PNG and PDF.

    python3 linkedin/build_poster.py                        # every poster
    python3 linkedin/build_poster.py commvita-capability-map

Each poster is authored as <name>.src.html in linkedin/posters/ with a
/*__FONTS__*/ marker in its stylesheet. The build writes <name>.html with
the faces inlined, so the page opens with no network, then renders
<name>.png at 2x and <name>.pdf at A3 landscape.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
POSTERS = os.path.join(HERE, 'posters')
FONTS = os.path.join(ROOT, 'site', 'fonts.css')
SHELL = os.environ.get('CHROME_BIN',
        '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell')


def measure(path, width):
    """Ask the page how tall it actually is, so the PNG has no dead space."""
    probe = path[:-5] + '.probe.html'
    doc = open(path, encoding='utf-8').read() + """
<script>addEventListener('load',function(){
  var p=document.querySelector('.poster');
  var report=function(){document.title='H:'+Math.ceil(p.getBoundingClientRect().height)};
  report(); requestAnimationFrame(report);
});</script>"""
    open(probe, 'w', encoding='utf-8').write(doc)
    try:
        for _ in range(3):
            out = subprocess.run(
                [SHELL, '--headless', '--no-sandbox', '--disable-gpu',
                 f'--window-size={width},1200', '--virtual-time-budget=6000',
                 '--dump-dom', probe], capture_output=True, text=True).stdout
            m = re.search(r'<title>H:(\d+)</title>', out)
            if m and int(m.group(1)):
                return int(m.group(1))
    finally:
        os.unlink(probe)
    return 0


def build(name, width=1600):
    src = os.path.join(POSTERS, name + '.src.html')
    doc = open(src, encoding='utf-8').read()
    doc = doc.replace('/*__FONTS__*/', open(FONTS, encoding='utf-8').read())
    dest = os.path.join(POSTERS, name + '.html')
    open(dest, 'w', encoding='utf-8').write(doc)

    height = measure(dest, width)
    if not height:
        raise SystemExit(f'{name}: could not measure the poster height')

    png = os.path.join(POSTERS, name + '.png')
    subprocess.run([SHELL, '--headless', '--no-sandbox', '--disable-gpu',
                    '--hide-scrollbars', '--force-device-scale-factor=2',
                    '--virtual-time-budget=6000',
                    f'--window-size={width},{height}', f'--screenshot={png}', dest],
                   check=True, capture_output=True)

    pdf = os.path.join(POSTERS, name + '.pdf')
    subprocess.run([SHELL, '--headless', '--no-sandbox', '--disable-gpu',
                    '--no-pdf-header-footer', '--virtual-time-budget=6000',
                    f'--print-to-pdf={pdf}', dest], check=True, capture_output=True)
    return [dest, png, pdf], (width, height)


if __name__ == '__main__':
    want = sys.argv[1:] or sorted(f[:-9] for f in os.listdir(POSTERS)
                                  if f.endswith('.src.html'))
    for name in want:
        files, (w, h) = build(name)
        print(f'{name}: {w}x{h} css px')
        for f in files:
            print(f'  wrote {os.path.relpath(f, ROOT)}  {os.path.getsize(f) // 1024} KB')

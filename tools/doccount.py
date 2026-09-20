#!/usr/bin/env python3
"""Keep the explainer counts on site/explainers/index.html in step with the library.

    python3 tools/doccount.py          # rewrite every count to the real number
    python3 tools/doccount.py --check  # exit 1 if any count is wrong (for CI or a pre-commit hook)

The real number is the count of distinct explainer pages linked from the
library lists on the index, cross-checked against the files on disk and the
sitemap. Every place the index states the number is rewritten from that one
figure, so the hero and the library heading can't drift apart again.
"""
import os,re,sys
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
IDX=os.path.join(ROOT,'site','explainers','index.html')
SM=os.path.join(ROOT,'site','sitemap.xml')
s=open(IDX,encoding='utf-8').read()
linked=sorted(set(re.findall(r'<li><a href="([^"]+\.html)"',s)))
n=len(linked)
ondisk=sorted(f for f in os.listdir(os.path.dirname(IDX)) if f.endswith('.html') and f!='index.html')
sm=open(SM,encoding='utf-8').read()
problems=[]
for f in ondisk:
    if f not in linked: problems.append('on disk but not in the library: '+f)
for f in linked:
    if f not in ondisk: problems.append('in the library but not on disk: '+f)
    if '/explainers/'+f not in sm: problems.append('not in sitemap: '+f)
pats=[(r'(\b)(\d+)( explainers, generated from the platform)',n),
      (r'(<h2>)(\d+)( documents</h2>)',n)]
new=s; wrong=[]
for pat,val in pats:
    for m in re.finditer(pat,s):
        if int(m.group(2))!=val: wrong.append(m.group(0))
    new=re.sub(pat,lambda m:m.group(1)+str(val)+m.group(3),new)
if '--check' in sys.argv:
    for p in problems: print('PROBLEM',p)
    for w in wrong: print('STALE COUNT',w,'-> should be',n)
    print('library:',n,'documents;',len(ondisk),'files on disk')
    sys.exit(1 if problems or wrong else 0)
if new!=s:
    open(IDX,'w',encoding='utf-8').write(new)
for p in problems: print('PROBLEM',p)
print('library:',n,'documents;',len(ondisk),'files on disk;','rewrote' if new!=s else 'no change to','counts on index')

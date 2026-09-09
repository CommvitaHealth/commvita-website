#!/usr/bin/env python3
"""Score explainer prose for machine-written tells. Higher = more machine."""
import re,sys,glob,os
FORMAL=[r'\bdoes not\b',r'\bis not\b',r'\bare not\b',r'\bcannot\b',r'\bit is\b',r'\bIt is\b',
        r'\bwill not\b',r'\bdo not\b',r'\bhas not\b',r'\bhave not\b',r'\bwas not\b',
        r'\bthere is\b',r'\bThere is\b',r'\bthat is\b',r'\bThat is\b',r'\bwould not\b',r'\bdid not\b']
CONTR=[r"n't\b",r"\bit's\b",r"\bIt's\b",r"\bthat's\b",r"\bThat's\b",r"\bthere's\b",r"\bThere's\b",
       r"\byou're\b",r"\bwe're\b",r"\bwe'd\b",r"\bwe've\b",r"\byou'd\b",r"\byou've\b",r"\bwhat's\b"]
TICS={'rather than':r'\brather than\b','indistinguishable':r'\bindistinguishable\b',
      'at the point':r'\bat the point\b','is the point':r'\b(is|was) the (whole |real )?point\b',
      'That is what/why':r'\bThat is (what|why|how|the)\b','deliberately':r'\bdeliberately\b',
      'genuinely/actually':r'\b(genuinely|actually)\b','not X but Y':r', not [a-z]',
      'It is not that':r'\bIt is not\b','which is X to':r'which is [^.,]{2,40} to (compute|publish|decide|make)'}
def prose(f):
    s=open(f,encoding='utf-8',errors='ignore').read()
    s=re.sub(r'<img[^>]*>','',s); s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    s=re.sub(r'<figcaption.*?</figcaption>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s)
    return re.sub(r'\s+',' ',s.replace('&rsquo;',"'").replace('&mdash;','—').replace('&nbsp;',' '))
def score(f):
    t=prose(f); w=max(len(t.split()),1)
    fo=sum(len(re.findall(p,t)) for p in FORMAL); co=sum(len(re.findall(p,t)) for p in CONTR)
    tic={k:len(re.findall(p,t)) for k,p in TICS.items()}
    per=lambda n:round(n/w*1000,1)
    return {'file':os.path.basename(f),'words':w,'formal':fo,'contr':co,
            'formal_per_1k':per(fo),'tics':sum(tic.values()),'tics_per_1k':per(sum(tic.values())),
            'detail':{k:v for k,v in tic.items() if v},
            'grade':round(per(fo)+per(sum(tic.values()))*2 - per(co),1)}
if __name__=='__main__':
    fs=sys.argv[1:] or sorted(glob.glob('site/explainers/*.html'))+sorted(glob.glob('site/*.html'))
    rows=[score(f) for f in fs]
    rows.sort(key=lambda r:-r['grade'])
    print(f"{'grade':>6} {'form/1k':>8} {'tic/1k':>7} {'contr':>6} {'words':>6}  file")
    for r in rows:
        print(f"{r['grade']:>6} {r['formal_per_1k']:>8} {r['tics_per_1k']:>7} {r['contr']:>6} {r['words']:>6}  {r['file']}")

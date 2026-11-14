import re,sys
d=open(sys.argv[1],'rb').read()
pat=re.compile(sys.argv[2],re.I)
seen=set()
for m in re.finditer(rb'[\x20-\x7e]{6,}',d):
    s=m.group().decode()
    if pat.search(s) and s not in seen:
        seen.add(s); print(hex(m.start()), s[:200])
for m in re.finditer(rb'(?:[\x20-\x7e]\x00){6,}',d):
    s=m.group().decode('utf-16le')
    if pat.search(s) and s not in seen:
        seen.add(s); print(hex(m.start()),'W', s[:200])

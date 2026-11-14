import sys
def load_hex(p):
    mem={}; base=0
    for ln in open(p):
        ln=ln.strip()
        if not ln.startswith(':'): continue
        b=bytes.fromhex(ln[1:]); n,a,t=b[0],(b[1]<<8)|b[2],b[3]; d=b[4:4+n]
        if t==0:
            for i,x in enumerate(d): mem[base+a+i]=x
        elif t==4: base=((d[0]<<8)|d[1])<<16
    segs={}
    for lo,hi in ((0x08000000,0x08010000),(0x20010000,0x20030000)):
        bs=bytearray(b'\xff'*(hi-lo))
        for a,v in mem.items():
            if lo<=a<hi: bs[a-lo]=v
        segs[lo]=bytes(bs)
    return segs

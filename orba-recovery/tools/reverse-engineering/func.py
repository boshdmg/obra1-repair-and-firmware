import sys,struct; sys.path.insert(0,sys.argv[1]); from load import load_hex
from capstone import *
segs=load_hex(sys.argv[2]); F=segs[0x08000000]; R=segs[0x20010000]
md=Cs(CS_ARCH_ARM,CS_MODE_THUMB)
def mem(a):
    return (F,0x08000000) if a<0x20000000 else (R,0x20010000)
def word(a):
    d,b=mem(a); 
    try: return struct.unpack_from('<I',d,a-b)[0]
    except: return None
def cstr(a):
    d,b=mem(a); o=a-b
    if not (0<=o<len(d)): return None
    e=d.find(b'\0',o); s=d[o:e]
    return s.decode() if 3<len(s)<80 and all(32<=c<127 for c in s) else None
def dis(start,end):
    d,b=mem(start)
    for i in md.disasm(d[start-b:end-b],start):
        extra=''
        if i.mnemonic.startswith('ldr') and '[pc' in i.op_str:
            try:
                off=int(i.op_str.split('#')[-1].rstrip(']'),16); la=((i.address+4)&~3)+off; v=word(la)
                extra='  ; =0x%08x'%v; s=cstr(v) if v else None
                if s: extra+=' "%s"'%s
            except Exception: pass
        print('%08x: %-8s %s%s'%(i.address,i.mnemonic,i.op_str,extra))
dis(int(sys.argv[3],16),int(sys.argv[4],16))

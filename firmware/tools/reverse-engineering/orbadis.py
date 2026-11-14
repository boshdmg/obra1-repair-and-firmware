import sys,struct; sys.path.insert(0,sys.argv[1]); from load import load_hex
from capstone import *
segs=load_hex(sys.argv[2]); F=segs[0x08000000]; R=segs[0x20010000]
md=Cs(CS_ARCH_ARM,CS_MODE_THUMB); md.detail=False
def word(a):
    if 0x08000000<=a<0x08010000: return struct.unpack_from('<I',F,a-0x08000000)[0]
    if 0x20010000<=a<0x20030000: return struct.unpack_from('<I',R,a-0x20010000)[0]
def dis(a,n=60):
    buf=F[a-0x08000000:] if a<0x20000000 else R[a-0x20010000:]
    out=[]
    for i in md.disasm(buf[:n*4],a):
        extra=''
        if i.mnemonic.startswith('ldr') and 'pc' in i.op_str:
            try:
                off=int(i.op_str.split('#')[-1].rstrip(']'),16); la=((i.address+4)&~3)+off; extra='  ; =0x%08x'%word(la)
            except Exception: pass
        out.append('%08x: %-8s %s%s'%(i.address,i.mnemonic,i.op_str,extra))
        if len(out)>=n: break
    return out
if __name__=='__main__':
    for a in sys.argv[3:]:
        print('\n'.join(dis(int(a,16)&~1,int(70))))
        print('-----')

import sys,struct,mmap
# Look for STM32 vector tables: SP in SRAM 0x2000_0000-0x2008_0000, reset in 0x0801_0000-0x0808_0000 (thumb bit), plus valid next vectors
for path in sys.argv[1:]:
    f=open(path,'rb'); d=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
    hits=0
    for off in range(0,len(d)-64,4):
        sp,rv,nmi,hf=struct.unpack_from('<IIII',d,off)
        if 0x20000000<sp<=0x20080000 and sp%4==0 and 0x08010000<=rv<0x08080000 and rv&1 and 0x08010000<=nmi<0x08080000 and nmi&1 and 0x08010000<=hf<0x08080000 and hf&1:
            print(path.split('/')[-1], hex(off), 'SP=%08x reset=%08x'%(sp,rv)); hits+=1
            if hits>10: break
    print(path.split('/')[-1],'hits',hits)

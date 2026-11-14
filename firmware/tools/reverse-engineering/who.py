import pickle,sys,re
I=pickle.load(open(sys.argv[1],'rb')); T=[int(x,16) for x in sys.argv[2:]]
for a,m,o,s in I:
    mm=re.search(r'\[pc, #(-?0x[0-9a-f]+|-?\d+)\]',o)
    if mm:
        t=((a+4)&~3)+int(mm.group(1),0)
        if t in T: print('%08x: %s %s  -> %08x'%(a,m,o,t))

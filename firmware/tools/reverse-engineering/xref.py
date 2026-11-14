import sys,struct; sys.path.insert(0,sys.argv[1]); from load import load_hex
segs=load_hex(sys.argv[2])
targets=[int(x,16) for x in sys.argv[3:]]
for base,d in segs.items():
    for o in range(0,len(d)-3,4):
        v=struct.unpack_from('<I',d,o)[0]
        for t in targets:
            if v==t or v==(t|1): print('%08x -> lit @%08x'%(t,base+o))

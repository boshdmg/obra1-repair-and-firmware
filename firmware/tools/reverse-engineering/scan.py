import sys,struct,re; sys.path.insert(0,sys.argv[1]); from load import load_hex
from capstone import *
segs=load_hex(sys.argv[2]); md=Cs(CS_ARCH_ARM,CS_MODE_THUMB); md.skipdata=True
ins=[]
for base,d in segs.items():
    end=len(d.rstrip(b'\xff'))
    ins+=list(md.disasm(d[:end],base))
import pickle; pickle.dump([(i.address,i.mnemonic,i.op_str,i.size) for i in ins],open(sys.argv[3],'wb'))
print(len(ins))

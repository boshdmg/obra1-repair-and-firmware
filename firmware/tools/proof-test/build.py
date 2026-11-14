import sys,struct
from keystone import *
from capstone import *
BASE=0x20020000
asm = """
    movw r0, #0x0100
    movt r0, #0x2002
    movw r1, #0xED00
    movt r1, #0xE000
    ldr  r2, [r1]
    str  r2, [r0]
    movw r3, #0xBEEF
    movt r3, #0xC0DE
    str  r3, [r0, #4]
    movw r1, #0x3874
    movt r1, #0x4002
    ldr  r2, [r1]
    str  r2, [r0, #8]
    dsb
    movw r1, #0xED0C
    movt r1, #0xE000
    movw r2, #0x0004
    movt r2, #0x05FA
    str  r2, [r1]
    dsb
hang:
    b    hang
"""
ks=Ks(KS_ARCH_ARM,KS_MODE_THUMB)
code=bytes(ks.asm(asm,BASE+8)[0])
img=struct.pack('<II',0x2003E000,(BASE+8)|1)+code
img=img+b'\x00'*(0x200-len(img))           # result area at +0x100 starts as zeros
open(sys.argv[1],'wb').write(img)
md=Cs(CS_ARCH_ARM,CS_MODE_THUMB|CS_MODE_MCLASS)
print('image %d bytes, code %d bytes'%(len(img),len(code)))
for i in md.disasm(code,BASE+8): print('  %08x: %s %s'%(i.address,i.mnemonic,i.op_str))

# Builds a RAM-only diagnostic stub for the Orba's STM32F730.
# Layout at 0x20020000: [0]=initial SP, [4]=entry|1 (the ROM DFU "leave" treats the address as a vector table), code follows.
import sys,struct
from keystone import *
BASE=0x20020000
asm = r"""
entry:
    cpsid i
    ldr  r0, =0x2003F000      @ result buffer
    ldr  r1, =0xD1A60001      @ magic
    str  r1, [r0]
    @ --- clocks: GPIOA..E, ADC1
    ldr  r2, =0x40023800
    ldr  r3, [r2, #0x30]
    orr  r3, r3, #0x1F
    str  r3, [r2, #0x30]
    ldr  r3, [r2, #0x44]
    orr  r3, r3, #0x100
    str  r3, [r2, #0x44]
    ldr  r3, [r2, #0x74]      @ RCC_CSR reset flags
    str  r3, [r0, #4]
    ldr  r3, =0x40007004      @ PWR_CSR1
    ldr  r3, [r3]
    str  r3, [r0, #8]
    @ --- GPIO snapshot A..E: MODER, PUPDR, IDR, ODR  (16 bytes each, from +0x10)
    ldr  r4, =0x40020000
    add  r5, r0, #0x10
    movs r6, #5
gp:
    ldr  r3, [r4, #0x00]
    str  r3, [r5, #0]
    ldr  r3, [r4, #0x0C]
    str  r3, [r5, #4]
    ldr  r3, [r4, #0x10]
    str  r3, [r5, #8]
    ldr  r3, [r4, #0x14]
    str  r3, [r5, #12]
    add  r4, r4, #0x400
    add  r5, r5, #16
    subs r6, r6, #1
    bne  gp
    @ --- analog mode for PB0,PB1 and PC0..PC5 (after the snapshot)
    ldr  r4, =0x40020400
    ldr  r3, [r4]
    orr  r3, r3, #0xF
    str  r3, [r4]
    ldr  r4, =0x40020800
    ldr  r3, [r4]
    movw r1, #0x0FFF
    orr  r3, r3, r1
    str  r3, [r4]
    @ --- ADC common: PCLK2/4, enable VREFINT
    ldr  r4, =0x40012304
    ldr  r3, [r4]
    bic  r3, r3, #0x30000
    orr  r3, r3, #0x10000
    orr  r3, r3, #0x800000
    str  r3, [r4]
    @ --- ADC1: max sample time all channels, ADON
    ldr  r4, =0x40012000
    ldr  r3, =0x07FFFFFF
    str  r3, [r4, #0x0C]
    ldr  r3, =0x3FFFFFFF
    str  r3, [r4, #0x10]
    movs r3, #0
    str  r3, [r4, #0x04]
    str  r3, [r4, #0x2C]      @ SQR1: 1 conversion
    movs r3, #1
    str  r3, [r4, #0x08]      @ CR2 = ADON
    ldr  r1, =200000
d1: subs r1, r1, #1
    bne  d1
    @ --- convert channels 0..18, each 4 times averaged-sum stored (results at +0x80, 4 bytes/channel)
    add  r5, r0, #0x80
    movs r6, #0
ch:
    str  r6, [r4, #0x34]      @ SQR3 = channel
    movs r7, #0
    movs r8, #4
rep:
    movs r3, #0
    str  r3, [r4, #0x00]      @ clear SR
    ldr  r3, [r4, #0x08]
    orr  r3, r3, #0x40000000  @ SWSTART
    str  r3, [r4, #0x08]
    ldr  r1, =2000000
w:  ldr  r3, [r4, #0x00]
    tst  r3, #2
    bne  got
    subs r1, r1, #1
    bne  w
    movw r3, #0xEEEE          @ timeout marker
    b    st
got:
    ldr  r3, [r4, #0x4C]
st:
    add  r7, r7, r3
    subs r8, r8, #1
    bne  rep
    str  r7, [r5], #4
    adds r6, r6, #1
    cmp  r6, #19
    bne  ch
    @ --- done marker, ADC off
    movs r3, #0
    str  r3, [r4, #0x08]
    ldr  r1, =0xD1A6D0E5
    str  r1, [r0, #0xFC]
    @ --- copy 256 bytes to a second location (in case the ROM clears one)
    ldr  r4, =0x20020800
    movs r6, #64
    mov  r5, r0
cp: ldr  r3, [r5], #4
    str  r3, [r4], #4
    subs r6, r6, #1
    bne  cp
    @ --- short pause, then system reset; with + (BOOT0) held the chip restarts into the ROM DFU and SRAM survives
    ldr  r1, =8000000
d2: subs r1, r1, #1
    bne  d2
    dsb
    ldr  r2, =0xE000ED0C
    ldr  r3, =0x05FA0004
    str  r3, [r2]
    dsb
hang:
    b    hang
"""
def prep(src):
    import re
    out=[]
    for ln in src.splitlines():
        ln=ln.split('@')[0].rstrip()
        m=re.match(r'^(\s*(?:\w+:)?\s*)ldr\s+(\w+),\s*=(\S+)$',ln)
        if m:
            pre,r,v=m.groups(); v=int(v,0)
            if pre.strip(): out.append(pre.strip())
            out.append('    movw %s, #0x%x'%(r,v&0xffff)); out.append('    movt %s, #0x%x'%(r,v>>16))
        elif ln.strip(): out.append(ln)
    return '\n'.join(out)
asm=prep(asm)
ks=Ks(KS_ARCH_ARM,KS_MODE_THUMB)
enc,_=ks.asm(asm,BASE+8)
code=bytes(enc)
img=struct.pack('<II',0x2003E000,(BASE+8)|1)+code
open(sys.argv[1],'wb').write(img)
print('stub bytes',len(img))

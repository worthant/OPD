ORG 0x10

adr: WORD 0x800
len: WORD 4

START:
 LD #3
 PUSH
 LD #3
 PUSH
 LD #4
 PUSH
 LD #3
 PUSH
 CALL $function
 HLT
  

ORG 0x70
function:
  CLA
  ADD -(adr)
  ST len
  repeat: 
    LD result
    ADD -(adr)
    ST result
  LOOP len
  JUMP repeat
  RET
  result: WORD 0
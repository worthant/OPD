ORG 0x10

result: WORD 0
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
  POP
  ST return
  POP
  ST length
  repeat: 
    POP
    ADD result
    ST result
  LOOP length
  JUMP repeat
  LD return
  PUSH
  RET

length: WORD ?
return: WORD ?

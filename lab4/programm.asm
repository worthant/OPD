ORG 0x0B1
START: ; result = – F(X + 1) + F(Y – 1) + F(Z + 1) – 1 
	CLA
	ST result
	LD y
	DEC
	PUSH
	CALL $function
	POP
	INC
	ADD result
	ST result
	LD x
	PUSH
	CALL $function
	POP
	INC
	SUB result
	ST result
	LD z
	INC
	PUSH
	CALL $function
	POP
	DEC
	SUB result
	ST result
	HLT
	z: WORD 0x029A
	x: WORD 0xFFFC
	y: WORD 0x000D
	result: WORD 0x003E
	
	

ORG 0x6ED
function:
    LD &1
    BMI exit1
    CMP var_1    
    BEQ exit2
    BLT exit2    
    exit1: ASL
	ASL
	SUB &1
	ADD var_2
	JUMP return
	exit2: LD var_1
	return: ST &1
	RET
	var_1: WORD 0x066B
    var_2: WORD 0x066C

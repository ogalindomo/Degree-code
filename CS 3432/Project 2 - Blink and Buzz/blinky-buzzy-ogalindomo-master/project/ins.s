	.arch msp430g2553
	.p2align 1,0
	.text


	.global update_allowed
update_allowed:
	nop
	mov #1, r12
	ret
	

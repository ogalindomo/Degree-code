	.arch msp430g2553
	.p2align 1,0
	.text
	.extern eye_shape
	.extern play_time 
	.global initialize
	
initialize:
	nop
	;; add #0xdeaf, &eye_shape+14
	add #1, &eye_shape+14
	mov #0xffff, r14
	cmp &eye_shape+14, r14
	jz equal
	ret
equal:
	mov #0xaaaa, &eye_shape+14
	ret

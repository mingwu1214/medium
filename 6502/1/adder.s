;
; File generated by cc65 v 2.19 - Git ce6ee1b
;
	.fopt		compiler,"cc65 v 2.19 - Git ce6ee1b"
	.setcpu		"6502"
	.smart		on
	.autoimport	on
	.case		on
	.debuginfo	off
	.importzp	sp, sreg, regsave, regbank
	.importzp	tmp1, tmp2, tmp3, tmp4, ptr1, ptr2, ptr3, ptr4
	.macpack	longbranch
	.forceimport	__STARTUP__
	.export		_main

; ---------------------------------------------------------------
; int __near__ main (void)
; ---------------------------------------------------------------

.segment	"CODE"

.proc	_main: near

.segment	"CODE"

	lda     #$00
	jsr     pusha
	ldy     #$00
	ldx     #$00
	lda     (sp),y
	jsr     incax1
	ldx     #$00
	ldy     #$00
	sta     (sp),y
	ldx     #$00
	lda     #$00
	jmp     L0001
L0001:	jsr     incsp1
	rts

.endproc

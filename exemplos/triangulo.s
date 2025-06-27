	.text
	.file	"triangulo.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbx
	.cfi_def_cfa_offset 16
	subq	$16, %rsp
	.cfi_def_cfa_offset 32
	.cfi_offset %rbx, -16
	movq	strlit_3@GOTPCREL(%rip), %rsi
	movq	int_fmt@GOTPCREL(%rip), %rbx
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movq	strlit_4@GOTPCREL(%rip), %rsi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movq	strlit_5@GOTPCREL(%rip), %rsi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	addq	$16, %rsp
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	int_fmt,@object                 # @int_fmt
	.section	.rodata,"a",@progbits
	.globl	int_fmt
int_fmt:
	.asciz	"%d\n"
	.size	int_fmt, 4

	.type	strlit_3,@object                # @strlit_3
	.globl	strlit_3
strlit_3:
	.asciz	"Equilatero"
	.size	strlit_3, 11

	.type	strlit_4,@object                # @strlit_4
	.globl	strlit_4
strlit_4:
	.asciz	"Isosceles"
	.size	strlit_4, 10

	.type	strlit_5,@object                # @strlit_5
	.globl	strlit_5
strlit_5:
	.asciz	"Escaleno"
	.size	strlit_5, 9

	.section	".note.GNU-stack","",@progbits

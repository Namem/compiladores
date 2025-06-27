	.text
	.file	"pascal.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbx
	.cfi_def_cfa_offset 16
	subq	$32, %rsp
	.cfi_def_cfa_offset 48
	.cfi_offset %rbx, -16
	movq	strlit_3@GOTPCREL(%rip), %rsi
	movq	int_fmt@GOTPCREL(%rip), %rbx
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	$0, 16(%rsp)
	movl	$0, 12(%rsp)
	movl	$0, 20(%rsp)
	movl	$1, 24(%rsp)
	movq	%rbx, %rdi
	xorl	%esi, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	incl	12(%rsp)
	incl	16(%rsp)
	xorl	%eax, %eax
	addq	$32, %rsp
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
	.p2align	4, 0x0
strlit_3:
	.asciz	"Digite o numero de linhas:"
	.size	strlit_3, 27

	.section	".note.GNU-stack","",@progbits

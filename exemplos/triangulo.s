	.text
	.file	"triangulo.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%r14
	.cfi_def_cfa_offset 16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	subq	$24, %rsp
	.cfi_def_cfa_offset 48
	.cfi_offset %rbx, -24
	.cfi_offset %r14, -16
	movq	strlit_6@GOTPCREL(%rip), %rsi
	movq	str_fmt@GOTPCREL(%rip), %rbx
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movq	scanf_fmt@GOTPCREL(%rip), %r14
	leaq	20(%rsp), %rsi
	movq	%r14, %rdi
	xorl	%eax, %eax
	callq	scanf@PLT
	movq	strlit_7@GOTPCREL(%rip), %rsi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movq	strlit_8@GOTPCREL(%rip), %rsi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	leaq	16(%rsp), %rsi
	movq	%r14, %rdi
	xorl	%eax, %eax
	callq	scanf@PLT
	movq	strlit_9@GOTPCREL(%rip), %rsi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movq	strlit_10@GOTPCREL(%rip), %rsi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	leaq	12(%rsp), %rsi
	movq	%r14, %rdi
	xorl	%eax, %eax
	callq	scanf@PLT
	movq	strlit_11@GOTPCREL(%rip), %rsi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	16(%rsp), %eax
	cmpl	%eax, 20(%rsp)
	jne	.LBB0_4
# %bb.1:                                # %entry
	cmpl	12(%rsp), %eax
	jne	.LBB0_4
# %bb.2:                                # %then_1
	movq	strlit_12@GOTPCREL(%rip), %rsi
	jmp	.LBB0_3
.LBB0_4:                                # %else_3
	movl	20(%rsp), %ecx
	movl	16(%rsp), %eax
	cmpl	%eax, %ecx
	je	.LBB0_7
# %bb.5:                                # %else_3
	movl	12(%rsp), %edx
	cmpl	%edx, %ecx
	je	.LBB0_7
# %bb.6:                                # %else_3
	cmpl	%edx, %eax
	je	.LBB0_7
# %bb.8:                                # %else_6
	movq	strlit_14@GOTPCREL(%rip), %rsi
	jmp	.LBB0_3
.LBB0_7:                                # %then_4
	movq	strlit_13@GOTPCREL(%rip), %rsi
.LBB0_3:                                # %merge_2
	movq	str_fmt@GOTPCREL(%rip), %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	addq	$24, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%r14
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

	.type	scanf_fmt,@object               # @scanf_fmt
	.globl	scanf_fmt
scanf_fmt:
	.asciz	"%d"
	.size	scanf_fmt, 3

	.type	str_fmt,@object                 # @str_fmt
	.globl	str_fmt
str_fmt:
	.asciz	"%s"
	.size	str_fmt, 3

	.type	strlit_6,@object                # @strlit_6
	.globl	strlit_6
	.p2align	4, 0x0
strlit_6:
	.asciz	"Digite o primeiro lado: "
	.size	strlit_6, 25

	.type	strlit_7,@object                # @strlit_7
	.globl	strlit_7
strlit_7:
	.asciz	"\n"
	.size	strlit_7, 2

	.type	strlit_8,@object                # @strlit_8
	.globl	strlit_8
	.p2align	4, 0x0
strlit_8:
	.asciz	"Digite o segundo lado: "
	.size	strlit_8, 24

	.type	strlit_9,@object                # @strlit_9
	.globl	strlit_9
strlit_9:
	.asciz	"\n"
	.size	strlit_9, 2

	.type	strlit_10,@object               # @strlit_10
	.globl	strlit_10
	.p2align	4, 0x0
strlit_10:
	.asciz	"Digite o terceiro lado: "
	.size	strlit_10, 25

	.type	strlit_11,@object               # @strlit_11
	.globl	strlit_11
strlit_11:
	.asciz	"\n"
	.size	strlit_11, 2

	.type	strlit_12,@object               # @strlit_12
	.globl	strlit_12
strlit_12:
	.asciz	"Equilatero\n"
	.size	strlit_12, 12

	.type	strlit_13,@object               # @strlit_13
	.globl	strlit_13
strlit_13:
	.asciz	"Isosceles\n"
	.size	strlit_13, 11

	.type	strlit_14,@object               # @strlit_14
	.globl	strlit_14
strlit_14:
	.asciz	"Escaleno\n"
	.size	strlit_14, 10

	.section	".note.GNU-stack","",@progbits

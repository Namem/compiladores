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
	movq	strlit_6@GOTPCREL(%rip), %rsi
	movq	str_fmt@GOTPCREL(%rip), %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	movq	scanf_fmt@GOTPCREL(%rip), %rdi
	leaq	28(%rsp), %rsi
	xorl	%eax, %eax
	callq	scanf@PLT
	movl	$0, 12(%rsp)
	movq	int_fmt@GOTPCREL(%rip), %rbx
	jmp	.LBB0_1
	.p2align	4, 0x90
.LBB0_9:                                # %loop_end_6
                                        #   in Loop: Header=BB0_1 Depth=1
	incl	12(%rsp)
.LBB0_1:                                # %loop_cond_1
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
                                        #       Child Loop BB0_5 Depth 3
	movl	12(%rsp), %eax
	cmpl	28(%rsp), %eax
	jg	.LBB0_8
# %bb.2:                                # %loop_body_2
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	$0, 24(%rsp)
	jmp	.LBB0_3
	.p2align	4, 0x90
.LBB0_7:                                # %loop_end_9
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	16(%rsp), %esi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	callq	printf@PLT
	incl	24(%rsp)
.LBB0_3:                                # %loop_cond_4
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_5 Depth 3
	movl	24(%rsp), %eax
	cmpl	12(%rsp), %eax
	jg	.LBB0_9
# %bb.4:                                # %loop_body_5
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	$1, 16(%rsp)
	movl	$0, 20(%rsp)
	.p2align	4, 0x90
.LBB0_5:                                # %loop_cond_7
                                        #   Parent Loop BB0_1 Depth=1
                                        #     Parent Loop BB0_3 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	20(%rsp), %eax
	cmpl	24(%rsp), %eax
	jge	.LBB0_7
# %bb.6:                                # %loop_body_8
                                        #   in Loop: Header=BB0_5 Depth=3
	movl	12(%rsp), %eax
	movl	20(%rsp), %ecx
	subl	%ecx, %eax
	imull	16(%rsp), %eax
	incl	%ecx
	cltd
	idivl	%ecx
	movl	%eax, 16(%rsp)
	movl	%ecx, 20(%rsp)
	jmp	.LBB0_5
.LBB0_8:                                # %loop_end_3
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
	.asciz	"Digite o numero de linhas:"
	.size	strlit_6, 27

	.section	".note.GNU-stack","",@progbits

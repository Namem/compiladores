; ModuleID = "meu_modulo"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"linha" = alloca i32
  %"i" = alloca i32
  %"j" = alloca i32
  %"valor" = alloca i32
  %"n" = alloca i32
  %".2" = bitcast [27 x i8]* @"strlit_6" to i8*
  %".3" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  %".5" = bitcast [3 x i8]* @"scanf_fmt" to i8*
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %".5", i32* %"n")
  store i32 0, i32* %"linha"
  br label %"loop_cond_1"
loop_cond_1:
  %"ld_linha" = load i32, i32* %"linha"
  %"ld_n" = load i32, i32* %"n"
  %"letmp" = icmp sle i32 %"ld_linha", %"ld_n"
  br i1 %"letmp", label %"loop_body_2", label %"loop_end_3"
loop_body_2:
  store i32 0, i32* %"i"
  br label %"loop_cond_4"
loop_end_3:
  ret i32 0
loop_cond_4:
  %"ld_i" = load i32, i32* %"i"
  %"ld_linha.1" = load i32, i32* %"linha"
  %"letmp.1" = icmp sle i32 %"ld_i", %"ld_linha.1"
  br i1 %"letmp.1", label %"loop_body_5", label %"loop_end_6"
loop_body_5:
  store i32 1, i32* %"valor"
  store i32 0, i32* %"j"
  br label %"loop_cond_7"
loop_end_6:
  %"ld_linha.3" = load i32, i32* %"linha"
  %"addtmp.3" = add i32 %"ld_linha.3", 1
  store i32 %"addtmp.3", i32* %"linha"
  br label %"loop_cond_1"
loop_cond_7:
  %"ld_j" = load i32, i32* %"j"
  %"ld_i.1" = load i32, i32* %"i"
  %"lttmp" = icmp slt i32 %"ld_j", %"ld_i.1"
  br i1 %"lttmp", label %"loop_body_8", label %"loop_end_9"
loop_body_8:
  %"ld_valor" = load i32, i32* %"valor"
  %"ld_linha.2" = load i32, i32* %"linha"
  %"ld_j.1" = load i32, i32* %"j"
  %"subtmp" = sub i32 %"ld_linha.2", %"ld_j.1"
  %"multmp" = mul i32 %"ld_valor", %"subtmp"
  store i32 %"multmp", i32* %"valor"
  %"ld_valor.1" = load i32, i32* %"valor"
  %"ld_j.2" = load i32, i32* %"j"
  %"addtmp" = add i32 %"ld_j.2", 1
  %"divtmp" = sdiv i32 %"ld_valor.1", %"addtmp"
  store i32 %"divtmp", i32* %"valor"
  %"ld_j.3" = load i32, i32* %"j"
  %"addtmp.1" = add i32 %"ld_j.3", 1
  store i32 %"addtmp.1", i32* %"j"
  br label %"loop_cond_7"
loop_end_9:
  %"ld_valor.2" = load i32, i32* %"valor"
  %".21" = bitcast [4 x i8]* @"int_fmt" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 %"ld_valor.2")
  %"ld_i.2" = load i32, i32* %"i"
  %"addtmp.2" = add i32 %"ld_i.2", 1
  store i32 %"addtmp.2", i32* %"i"
  br label %"loop_cond_4"
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"int_fmt" = constant [4 x i8] c"%d\0a\00"
@"scanf_fmt" = constant [3 x i8] c"%d\00"
@"str_fmt" = constant [3 x i8] c"%s\00"
@"strlit_6" = constant [27 x i8] c"Digite o numero de linhas:\00"
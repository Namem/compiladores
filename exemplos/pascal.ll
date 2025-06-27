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
  %".2" = bitcast [27 x i8]* @"strlit_3" to i8*
  %".3" = bitcast [4 x i8]* @"int_fmt" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  store i32 0, i32* %"linha"
  %"ld_linha" = load i32, i32* %"linha"
  %"ld_n" = load i32, i32* %"n"
  %"letmp" = icmp sle i32 %"ld_linha", %"ld_n"
  store i32 0, i32* %"i"
  %"ld_i" = load i32, i32* %"i"
  %"ld_linha.1" = load i32, i32* %"linha"
  %"letmp.1" = icmp sle i32 %"ld_i", %"ld_linha.1"
  store i32 1, i32* %"valor"
  store i32 0, i32* %"j"
  %"ld_j" = load i32, i32* %"j"
  %"ld_i.1" = load i32, i32* %"i"
  %"lttmp" = icmp slt i32 %"ld_j", %"ld_i.1"
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
  %"ld_valor.2" = load i32, i32* %"valor"
  %".12" = bitcast [4 x i8]* @"int_fmt" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %"ld_valor.2")
  %"ld_i.2" = load i32, i32* %"i"
  %"addtmp.2" = add i32 %"ld_i.2", 1
  store i32 %"addtmp.2", i32* %"i"
  %"ld_linha.3" = load i32, i32* %"linha"
  %"addtmp.3" = add i32 %"ld_linha.3", 1
  store i32 %"addtmp.3", i32* %"linha"
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"int_fmt" = constant [4 x i8] c"%d\0a\00"
@"strlit_3" = constant [27 x i8] c"Digite o numero de linhas:\00"
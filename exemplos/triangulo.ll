; ModuleID = "meu_modulo"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  %"b" = alloca i32
  %"c" = alloca i32
  %"ld_a" = load i32, i32* %"a"
  %"ld_b" = load i32, i32* %"b"
  %"eqtmp" = icmp eq i32 %"ld_a", %"ld_b"
  %"ld_b.1" = load i32, i32* %"b"
  %"ld_c" = load i32, i32* %"c"
  %"eqtmp.1" = icmp eq i32 %"ld_b.1", %"ld_c"
  %"andtmp" = and i1 %"eqtmp", %"eqtmp.1"
  %".2" = bitcast [11 x i8]* @"strlit_3" to i8*
  %".3" = bitcast [4 x i8]* @"int_fmt" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  %"ld_a.1" = load i32, i32* %"a"
  %"ld_b.2" = load i32, i32* %"b"
  %"eqtmp.2" = icmp eq i32 %"ld_a.1", %"ld_b.2"
  %"ld_a.2" = load i32, i32* %"a"
  %"ld_c.1" = load i32, i32* %"c"
  %"eqtmp.3" = icmp eq i32 %"ld_a.2", %"ld_c.1"
  %"orl" = icmp ne i1 %"eqtmp.2", 0
  %"orr" = icmp ne i1 %"eqtmp.3", 0
  %"orres" = or i1 %"orl", %"orr"
  %"ld_b.3" = load i32, i32* %"b"
  %"ld_c.2" = load i32, i32* %"c"
  %"eqtmp.4" = icmp eq i32 %"ld_b.3", %"ld_c.2"
  %"orl.1" = icmp ne i1 %"orres", 0
  %"orr.1" = icmp ne i1 %"eqtmp.4", 0
  %"orres.1" = or i1 %"orl.1", %"orr.1"
  %".5" = bitcast [10 x i8]* @"strlit_4" to i8*
  %".6" = bitcast [4 x i8]* @"int_fmt" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8* %".5")
  %".8" = bitcast [9 x i8]* @"strlit_5" to i8*
  %".9" = bitcast [4 x i8]* @"int_fmt" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8* %".8")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"int_fmt" = constant [4 x i8] c"%d\0a\00"
@"strlit_3" = constant [11 x i8] c"Equilatero\00"
@"strlit_4" = constant [10 x i8] c"Isosceles\00"
@"strlit_5" = constant [9 x i8] c"Escaleno\00"
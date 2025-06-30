; ModuleID = "meu_modulo"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  %"b" = alloca i32
  %"c" = alloca i32
  %".2" = bitcast [25 x i8]* @"strlit_6" to i8*
  %".3" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  %".5" = bitcast [3 x i8]* @"scanf_fmt" to i8*
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %".5", i32* %"a")
  %".7" = bitcast [2 x i8]* @"strlit_7" to i8*
  %".8" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8* %".7")
  %".10" = bitcast [24 x i8]* @"strlit_8" to i8*
  %".11" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8* %".10")
  %".13" = bitcast [3 x i8]* @"scanf_fmt" to i8*
  %".14" = call i32 (i8*, ...) @"scanf"(i8* %".13", i32* %"b")
  %".15" = bitcast [2 x i8]* @"strlit_9" to i8*
  %".16" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i8* %".15")
  %".18" = bitcast [25 x i8]* @"strlit_10" to i8*
  %".19" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i8* %".18")
  %".21" = bitcast [3 x i8]* @"scanf_fmt" to i8*
  %".22" = call i32 (i8*, ...) @"scanf"(i8* %".21", i32* %"c")
  %".23" = bitcast [2 x i8]* @"strlit_11" to i8*
  %".24" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i8* %".23")
  %"ld_a" = load i32, i32* %"a"
  %"ld_b" = load i32, i32* %"b"
  %"eqtmp" = icmp eq i32 %"ld_a", %"ld_b"
  %"ld_b.1" = load i32, i32* %"b"
  %"ld_c" = load i32, i32* %"c"
  %"eqtmp.1" = icmp eq i32 %"ld_b.1", %"ld_c"
  %"andtmp" = and i1 %"eqtmp", %"eqtmp.1"
  br i1 %"andtmp", label %"then_1", label %"else_3"
then_1:
  %".27" = bitcast [12 x i8]* @"strlit_12" to i8*
  %".28" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28", i8* %".27")
  br label %"merge_2"
merge_2:
  ret i32 0
else_3:
  %"ld_a.1" = load i32, i32* %"a"
  %"ld_b.2" = load i32, i32* %"b"
  %"eqtmp.2" = icmp eq i32 %"ld_a.1", %"ld_b.2"
  %"ld_a.2" = load i32, i32* %"a"
  %"ld_c.1" = load i32, i32* %"c"
  %"eqtmp.3" = icmp eq i32 %"ld_a.2", %"ld_c.1"
  %"orres" = or i1 %"eqtmp.2", %"eqtmp.3"
  %"ld_b.3" = load i32, i32* %"b"
  %"ld_c.2" = load i32, i32* %"c"
  %"eqtmp.4" = icmp eq i32 %"ld_b.3", %"ld_c.2"
  %"orres.1" = or i1 %"orres", %"eqtmp.4"
  br i1 %"orres.1", label %"then_4", label %"else_6"
then_4:
  %".32" = bitcast [11 x i8]* @"strlit_13" to i8*
  %".33" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i8* %".32")
  br label %"merge_5"
merge_5:
  br label %"merge_2"
else_6:
  %".36" = bitcast [10 x i8]* @"strlit_14" to i8*
  %".37" = bitcast [3 x i8]* @"str_fmt" to i8*
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37", i8* %".36")
  br label %"merge_5"
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"int_fmt" = constant [4 x i8] c"%d\0a\00"
@"scanf_fmt" = constant [3 x i8] c"%d\00"
@"str_fmt" = constant [3 x i8] c"%s\00"
@"strlit_6" = constant [25 x i8] c"Digite o primeiro lado: \00"
@"strlit_7" = constant [2 x i8] c"\0a\00"
@"strlit_8" = constant [24 x i8] c"Digite o segundo lado: \00"
@"strlit_9" = constant [2 x i8] c"\0a\00"
@"strlit_10" = constant [25 x i8] c"Digite o terceiro lado: \00"
@"strlit_11" = constant [2 x i8] c"\0a\00"
@"strlit_12" = constant [12 x i8] c"Equilatero\0a\00"
@"strlit_13" = constant [11 x i8] c"Isosceles\0a\00"
@"strlit_14" = constant [10 x i8] c"Escaleno\0a\00"
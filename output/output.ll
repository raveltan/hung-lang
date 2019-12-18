; ModuleID = "/Users/raveltanjaya/Documents/Files/Python/Hung-Lang/hung-lang/codegen.py"
target triple = "x86_64-apple-darwin18.7.0"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i8 100)
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"
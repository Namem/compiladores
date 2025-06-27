# CodeGeneratorLLVM.py

from llvmlite import ir
from antlr4 import ParserRuleContext
from CompiladorListener import CompiladorListener
from CompiladorParser import CompiladorParser

class LLVMCodeGenerator(CompiladorListener):
    def __init__(self, symbols, target_triple="unknown-unknown-unknown"):
        # Tabela de símbolos (nome -> tipo)
        self.symbols = symbols
        
        # Módulo e função main
        self.module = ir.Module(name="meu_modulo")
        
        # Configurar target triple
        self.module.triple = target_triple
        
        # Configurar data layout baseado no target (básico)
        if "x86_64" in target_triple:
            if "windows" in target_triple:
                self.module.data_layout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
            else:  # Linux/Unix
                self.module.data_layout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        elif "i386" in target_triple or "i686" in target_triple:
            self.module.data_layout = "e-m:e-p:32:32-f64:32:64-f80:32-n8:16:32-S128"
        elif "aarch64" in target_triple or "arm64" in target_triple:
            self.module.data_layout = "e-m:e-i8:8:32-i16:16:32-i64:64-i128:128-n32:64-S128"
        elif "arm" in target_triple:
            self.module.data_layout = "e-m:e-p:32:32-i64:64-v128:64:128-a:0:32-n32-S64"
        else:
            # Para targets desconhecidos, usar layout neutro
            self.module.data_layout = ""
        
        func_ty = ir.FunctionType(ir.IntType(32), [])
        self.function = ir.Function(self.module, func_ty, name="main")
        entry = self.function.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry)

        # Declaração de printf
        self.voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [self.voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        # String de formato para inteiros "%d\n\0"
        fmt = b"%d\n\0"
        self.int_fmt = ir.GlobalVariable(
            self.module,
            ir.ArrayType(ir.IntType(8), len(fmt)),
            name="int_fmt"
        )
        self.int_fmt.global_constant = True
        self.int_fmt.initializer = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(fmt)),
            bytearray(fmt)
        )

        # Map nome de variável -> alloca
        self.vars = {}

    # Declaração de variável: IDENT : tipo
    def exitDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        name = ctx.IDENT().getText()
        ty = self.symbols[name]
        if ty == "int":
            ptr = self.builder.alloca(ir.IntType(32), name=name)
        else:
            # para string a gente armazena ponteiro i8*
            ptr = self.builder.alloca(self.voidptr_ty, name=name)
        self.vars[name] = ptr

    # Literais: INT ou STRING
    def exitLiteral(self, ctx:CompiladorParser.LiteralContext):
        text = ctx.getText()
        if ctx.INT():
            ctx._value = ir.Constant(ir.IntType(32), int(text))
        else:
            # Remove aspas da string
            string_content = text[1:-1]  # Remove as aspas duplas
            
            # Gera um nome único para cada string literal
            string_name = f"strlit_{len(self.module.globals)}"
            
            # Cria a variável global com nome único
            gv = ir.GlobalVariable(
                self.module,
                ir.ArrayType(ir.IntType(8), len(string_content) + 1),
                name=string_name
            )
            gv.global_constant = True
            gv.initializer = ir.Constant(
                gv.type.pointee,
                bytearray(string_content.encode("utf8") + b"\0")
            )
            ctx._value = self.builder.bitcast(gv, self.voidptr_ty)

    # Expr de raiz: propaga o value do exprLogico
    def exitExpr(self, ctx:CompiladorParser.ExprContext):
        ctx._value = ctx.exprLogico()._value

    # OR lógico: exprLogico -> exprLogico || exprAnd | exprAnd
    def exitExprLogico(self, ctx:CompiladorParser.ExprLogicoContext):
        if ctx.getChildCount() == 1:
            ctx._value = ctx.exprAnd()._value
        else:
            left = ctx.exprLogico()._value
            right = ctx.exprAnd()._value
            cond1 = self.builder.icmp_signed("!=", left, ir.Constant(ir.IntType(32), 0), name="orl")
            cond2 = self.builder.icmp_signed("!=", right, ir.Constant(ir.IntType(32), 0), name="orr")
            ctx._value = self.builder.or_(cond1, cond2, name="orres")

    # AND lógico: exprAnd -> exprAnd && exprIgualdade | exprIgualdade
    def exitExprAnd(self, ctx:CompiladorParser.ExprAndContext):
        if ctx.getChildCount() == 1:
            ctx._value = ctx.exprIgualdade()._value
        else:
            left = ctx.exprAnd()._value
            right = ctx.exprIgualdade()._value
            ctx._value = self.builder.and_(left, right, name="andtmp")

    # Igualdade: exprIgualdade -> exprComparacao ('==' | '!=') exprComparacao*
    def exitExprIgualdade(self, ctx:CompiladorParser.ExprIgualdadeContext):
        comps = list(ctx.exprComparacao())
        value = comps[0]._value
        for idx, right_ctx in enumerate(comps[1:], start=1):
            op = ctx.getChild(2*idx - 1).getText()
            right = right_ctx._value
            if op == "==":
                value = self.builder.icmp_signed("==", value, right, name="eqtmp")
            else:  # ~= ou !=
                value = self.builder.icmp_signed("!=", value, right, name="netmp")
        ctx._value = value

    # Comparação relacional: exprComparacao -> exprAritmetica (< | > | <= | >=) exprAritmetica | exprAritmetica
    def exitExprComparacao(self, ctx:CompiladorParser.ExprComparacaoContext):
        # Pega lista de sub-expressões aritméticas
        arits = list(ctx.exprAritmetica())
        if len(arits) == 1:
            # Apenas uma expressão aritmética, sem comparação
            ctx._value = arits[0]._value
        else:
            # Há operador de comparação
            left = arits[0]._value
            right = arits[1]._value
            op = ctx.getChild(1).getText()  # Pega o operador
            
            if op == "<":
                ctx._value = self.builder.icmp_signed("<", left, right, name="lttmp")
            elif op == ">":
                ctx._value = self.builder.icmp_signed(">", left, right, name="gttmp")
            elif op == "<=":
                ctx._value = self.builder.icmp_signed("<=", left, right, name="letmp")
            elif op == ">=":
                ctx._value = self.builder.icmp_signed(">=", left, right, name="getmp")
            else:
                # Fallback caso não reconheça o operador
                ctx._value = arits[0]._value

    # Aritmética: exprAritmetica -> exprAritmetica (+|- termo) | termo
    def exitExprAritmetica(self, ctx:CompiladorParser.ExprAritmeticaContext):
        if ctx.getChildCount() == 1:
            ctx._value = ctx.termo()._value
        else:
            left = ctx.exprAritmetica()._value
            right = ctx.termo()._value
            op = ctx.getChild(1).getText()
            if op == "+":
                ctx._value = self.builder.add(left, right, name="addtmp")
            else:
                ctx._value = self.builder.sub(left, right, name="subtmp")

    # Termo: termo (*|/ fator)*
    def exitTermo(self, ctx:CompiladorParser.TermoContext):
        if ctx.getChildCount() == 1:
            ctx._value = ctx.fator()._value
        else:
            left = ctx.termo()._value
            right = ctx.fator()._value
            op = ctx.getChild(1).getText()
            if op == "*":
                ctx._value = self.builder.mul(left, right, name="multmp")
            else:
                ctx._value = self.builder.sdiv(left, right, name="divtmp")

    # Fator: IDENT | literal | '(' expr ')' | '-' fator
    def exitFator(self, ctx:CompiladorParser.FatorContext):
        if ctx.IDENT():
            # Carrega a partir do alloca criado em exitDeclaracao
            name = ctx.IDENT().getText()
            ptr = self.vars[name]
            ctx._value = self.builder.load(ptr, name="ld_" + name)
        elif ctx.literal():
            ctx._value = ctx.literal()._value
        elif ctx.expr():
            ctx._value = ctx.expr()._value
        elif ctx.SUB():
            val = ctx.fator()._value
            ctx._value = self.builder.neg(val, name="negtmp")

    # Atribuição: IDENT = expr
    def exitAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        name = ctx.IDENT().getText()
        ptr  = self.vars[name]
        self.builder.store(ctx.expr()._value, ptr)

    # Leitura (read) -> não implementado para llvmlite
    def exitLeitura(self, ctx:CompiladorParser.LeituraContext):
        # omitido – preencher com scanf se desejar
        pass

    # Escrita (print INT) via printf
    def exitEscrita(self, ctx:CompiladorParser.EscritaContext):
        val = ctx.expr()._value
        fmt_ptr = self.builder.bitcast(self.int_fmt, ir.IntType(8).as_pointer())
        self.builder.call(self.printf, [fmt_ptr, val])

    # Condicional e while podem ser implementados do mesmo jeito
    # mas aqui deixamos como exercícios adicionais

    # Chame isto ao final para fechar o main
    def finalize(self):
        self.builder.ret(ir.Constant(ir.IntType(32), 0))
        return str(self.module)

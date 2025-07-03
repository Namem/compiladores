# CodeGeneratorLLVM.py

from llvmlite import ir
from CompiladorVisitor import CompiladorVisitor
from CompiladorParser import CompiladorParser

class LLVMCodeGenerator(CompiladorVisitor):
    def __init__(self, symbols, target_triple="x86_64-unknown-linux-gnu"):
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

        # Declaração de scanf para leitura
        scanf_ty = ir.FunctionType(ir.IntType(32), [self.voidptr_ty], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_ty, name="scanf")

        fmt = b"%d\0"
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

        # String de formato para scanf "%d\0"
        scanf_fmt = b"%d\0"
        self.scanf_fmt = ir.GlobalVariable(
            self.module,
            ir.ArrayType(ir.IntType(8), len(scanf_fmt)),
            name="scanf_fmt"
        )
        self.scanf_fmt.global_constant = True
        self.scanf_fmt.initializer = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(scanf_fmt)),
            bytearray(scanf_fmt)
        )

        # String de formato para scanf de strings "%s\0" 
        scanf_str_fmt = b"%s\0"
        self.scanf_str_fmt = ir.GlobalVariable(
            self.module,
            ir.ArrayType(ir.IntType(8), len(scanf_str_fmt)),
            name="scanf_str_fmt"
        )
        self.scanf_str_fmt.global_constant = True
        self.scanf_str_fmt.initializer = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(scanf_str_fmt)),
            bytearray(scanf_str_fmt)
        )

        # String de formato para strings "%s\0"
        str_fmt = b"%s\0"  # 
        self.str_fmt = ir.GlobalVariable(
            self.module,
            ir.ArrayType(ir.IntType(8), len(str_fmt)),
            name="str_fmt"
        )
        self.str_fmt.global_constant = True
        self.str_fmt.initializer = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(str_fmt)),
            bytearray(str_fmt)
        )

        # Map nome de variável -> alloca
        self.vars = {}
        
        # Contador para nomes únicos de blocos
        self.block_counter = 0

    def _get_unique_block_name(self, base_name):
        """Gera nome único para bloco básico"""
        self.block_counter += 1
        return f"{base_name}_{self.block_counter}"

    # Programa principal
    def visitPrograma(self, ctx):
        # Visitar declarações
        self.visit(ctx.declaracoes())
        # Visitar bloco principal
        self.visit(ctx.bloco())

    # Declarações de variáveis
    def visitDeclaracoes(self, ctx):
        # Visitar cada declaração
        for decl_ctx in ctx.declaracao():
            self.visit(decl_ctx)

    # Declaração individual: IDENT : tipo
    def visitDeclaracao(self, ctx):
        name = ctx.IDENT().getText()
        ty = self.symbols[name]
        if ty == "int":
            ptr = self.builder.alloca(ir.IntType(32), name=name)
        else:  # string
            # Alocar buffer de 256 bytes para string
            string_buffer_size = 256
            ptr = self.builder.alloca(
                ir.ArrayType(ir.IntType(8), string_buffer_size), 
                name=name
            )
        self.vars[name] = ptr

    # Bloco de comandos
    def visitBloco(self, ctx):
        for comando in ctx.comando():
            self.visit(comando)

    # Literais: INT ou STRING
    def visitLiteral(self, ctx):
        text = ctx.getText()
        if ctx.INT():
            return ir.Constant(ir.IntType(32), int(text))
        else:
            # Remove aspas da string
            string_content = text[1:-1]  # Remove as aspas duplas
            
            # Processar escape sequences
            string_content = self._process_escape_sequences(string_content)
            
            # Codificar em UTF-8 e calcular tamanho correto
            utf8_bytes = string_content.encode("utf-8")
            size_with_null = len(utf8_bytes) + 1
            
            # Gera um nome único para cada string literal
            string_name = f"strlit_{len(self.module.globals)}"
            
            # Cria a variável global com tamanho correto
            gv = ir.GlobalVariable(
                self.module,
                ir.ArrayType(ir.IntType(8), size_with_null),
                name=string_name
            )
            gv.global_constant = True
            gv.initializer = ir.Constant(
                gv.type.pointee,
                bytearray(utf8_bytes + b"\0")
            )
            return self.builder.bitcast(gv, self.voidptr_ty)

    def _process_escape_sequences(self, text):
        # Processar escape sequences comuns
        result = ""
        i = 0
        while i < len(text):
            if text[i] == '\\' and i + 1 < len(text):
                next_char = text[i + 1]
                if next_char == 'n':
                    result += '\n'
                elif next_char == 't':
                    result += '\t'
                elif next_char == 'r':
                    result += '\r'
                elif next_char == '\\':
                    result += '\\'
                elif next_char == '"':
                    result += '"'
                elif next_char == '0':
                    result += '\0'
                else:
                    # Escape sequence desconhecida, manter como está
                    result += text[i] + next_char
                i += 2  # Pular o \ e o próximo caractere
            else:
                result += text[i]
                i += 1
        return result

    # Expressões
    def visitExpr(self, ctx):
        return self.visit(ctx.exprLogico())

    def visitExprLogico(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprAnd())
        else:
            left = self.visit(ctx.exprLogico())
            right = self.visit(ctx.exprAnd())
            # Converter para booleano se necessário
            if left.type != ir.IntType(1):
                left = self.builder.icmp_signed("!=", left, ir.Constant(ir.IntType(32), 0))
            if right.type != ir.IntType(1):
                right = self.builder.icmp_signed("!=", right, ir.Constant(ir.IntType(32), 0))
            return self.builder.or_(left, right, name="orres")

    def visitExprAnd(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprIgualdade())
        else:
            left = self.visit(ctx.exprAnd())
            right = self.visit(ctx.exprIgualdade())
            # Converter para booleano se necessário
            if left.type != ir.IntType(1):
                left = self.builder.icmp_signed("!=", left, ir.Constant(ir.IntType(32), 0))
            if right.type != ir.IntType(1):
                right = self.builder.icmp_signed("!=", right, ir.Constant(ir.IntType(32), 0))
            return self.builder.and_(left, right, name="andtmp")

    def visitExprIgualdade(self, ctx):
        comps = list(ctx.exprComparacao())
        value = self.visit(comps[0])
        for idx, right_ctx in enumerate(comps[1:], start=1):
            op = ctx.getChild(2*idx - 1).getText()
            right = self.visit(right_ctx)
            if op == "==":
                value = self.builder.icmp_signed("==", value, right, name="eqtmp")
            else:  # ~= ou !=
                value = self.builder.icmp_signed("!=", value, right, name="netmp")
        return value

    def visitExprComparacao(self, ctx):
        arits = list(ctx.exprAritmetica())
        if len(arits) == 1:
            return self.visit(arits[0])
        else:
            left = self.visit(arits[0])
            right = self.visit(arits[1])
            op = ctx.getChild(1).getText()
            
            if op == "<":
                return self.builder.icmp_signed("<", left, right, name="lttmp")
            elif op == ">":
                return self.builder.icmp_signed(">", left, right, name="gttmp")
            elif op == "<=":
                return self.builder.icmp_signed("<=", left, right, name="letmp")
            elif op == ">=":
                return self.builder.icmp_signed(">=", left, right, name="getmp")
            else:
                return self.visit(arits[0])

    def visitExprAritmetica(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termo())
        else:
            left = self.visit(ctx.exprAritmetica())
            right = self.visit(ctx.termo())
            op = ctx.getChild(1).getText()
            if op == "+":
                return self.builder.add(left, right, name="addtmp")
            else:
                return self.builder.sub(left, right, name="subtmp")

    def visitTermo(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.fator())
        else:
            left = self.visit(ctx.termo())
            right = self.visit(ctx.fator())
            op = ctx.getChild(1).getText()
            if op == "*":
                return self.builder.mul(left, right, name="multmp")
            else:
                return self.builder.sdiv(left, right, name="divtmp")

    def visitFator(self, ctx):
        if ctx.IDENT():
            # Carrega a partir do alloca criado em visitDeclaracao
            name = ctx.IDENT().getText()
            ptr = self.vars[name]
            ty = self.symbols[name]
            
            if ty == "int":
                return self.builder.load(ptr, name="ld_" + name)
            else:  # string
                # Para strings, retornar ponteiro para o primeiro caractere
                return self.builder.gep(ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.SUB():
            val = self.visit(ctx.fator())
            return self.builder.neg(val, name="negtmp")

    # Comandos
    def visitAtribuicao(self, ctx):
        name = ctx.IDENT().getText()
        ptr = self.vars[name]
        val = self.visit(ctx.expr())
        ty = self.symbols[name]
        
        if ty == "int":
            self.builder.store(val, ptr)
        else:

            dest_ptr = self.builder.gep(ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])
            pass

    def visitLeitura(self, ctx):
        name = ctx.IDENT().getText()
        ptr = self.vars[name]
        ty = self.symbols[name]
        
        if ty == "int":
            # Leitura de inteiro
            scanf_fmt_ptr = self.builder.bitcast(self.scanf_fmt, self.voidptr_ty)
            self.builder.call(self.scanf, [scanf_fmt_ptr, ptr])
        else:  # string
            # Leitura de string - usar ponteiro para o primeiro elemento do array
            string_ptr = self.builder.gep(ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])
            scanf_str_fmt_ptr = self.builder.bitcast(self.scanf_str_fmt, self.voidptr_ty)
            self.builder.call(self.scanf, [scanf_str_fmt_ptr, string_ptr])

    def visitEscrita(self, ctx):
        val = self.visit(ctx.expr())
        
        # Verificar se é string ou inteiro
        if val.type == self.voidptr_ty:
            # É uma string
            fmt_ptr = self.builder.bitcast(self.str_fmt, self.voidptr_ty)
            self.builder.call(self.printf, [fmt_ptr, val])
        else:
            # É um inteiro
            fmt_ptr = self.builder.bitcast(self.int_fmt, self.voidptr_ty)
            self.builder.call(self.printf, [fmt_ptr, val])

    def visitCondicional(self, ctx):
        # 1. Avaliar a condição
        cond = self.visit(ctx.expr())
        
        # Converter para booleano se necessário
        if cond.type != ir.IntType(1):
            cond = self.builder.icmp_signed("!=", cond, ir.Constant(ir.IntType(32), 0))
        
        # 2. Criar blocos básicos com nomes únicos
        then_block = self.function.append_basic_block(self._get_unique_block_name("then"))
        else_block = None
        merge_block = self.function.append_basic_block(self._get_unique_block_name("merge"))
        
        # Verificar se tem SENAO
        blocos = ctx.bloco()
        has_else = len(blocos) > 1
        
        if has_else:
            else_block = self.function.append_basic_block(self._get_unique_block_name("else"))
            self.builder.cbranch(cond, then_block, else_block)
        else:
            self.builder.cbranch(cond, then_block, merge_block)
        
        # 3. Processar bloco THEN
        self.builder.position_at_end(then_block)
        self.visit(blocos[0])  # Primeiro bloco
        
        # Verificar se o bloco termina com branch
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_block)
        
        # 4. Processar bloco ELSE se existir
        if has_else:
            self.builder.position_at_end(else_block)
            self.visit(blocos[1])  # Segundo bloco
            
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_block)
        
        # 5. Continuar no bloco merge
        self.builder.position_at_end(merge_block)

    def visitRepeticao(self, ctx):
        # Criar blocos básicos com nomes únicos
        loop_cond = self.function.append_basic_block(self._get_unique_block_name("loop_cond"))
        loop_body = self.function.append_basic_block(self._get_unique_block_name("loop_body"))
        loop_end = self.function.append_basic_block(self._get_unique_block_name("loop_end"))
        
        # Branch para condição do loop
        self.builder.branch(loop_cond)
        
        # Bloco da condição
        self.builder.position_at_end(loop_cond)
        cond = self.visit(ctx.expr())
        
        # Converter para booleano se necessário
        if cond.type != ir.IntType(1):
            cond = self.builder.icmp_signed("!=", cond, ir.Constant(ir.IntType(32), 0))
        
        self.builder.cbranch(cond, loop_body, loop_end)
        
        # Bloco do corpo do loop
        self.builder.position_at_end(loop_body)
        self.visit(ctx.bloco())
        
        # Verificar se termina com branch
        if not self.builder.block.is_terminated:
            self.builder.branch(loop_cond)
        
        # Continuar após o loop
        self.builder.position_at_end(loop_end)

    # Chame isto ao final para fechar o main
    def finalize(self):
        # Verificar se o bloco atual não termina com branch
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))
        return str(self.module)

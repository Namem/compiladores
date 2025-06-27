from antlr4 import ParserRuleContext
from CompiladorListener import CompiladorListener
from CompiladorParser import CompiladorParser

class AnalisadorSemantico(CompiladorListener):
    def __init__(self):
        self.symbols = {}
        self.errors = []
        self.logs = []

    def log(self, msg: str):
        self.logs.append(msg)

    def report(self, ctx: ParserRuleContext, msg: str):
        line = ctx.start.line if hasattr(ctx, 'start') else '?'
        self.errors.append(f"[Erro semântico] Linha {line}: {msg}")

    def exitDeclaracao(self, ctx: CompiladorParser.DeclaracaoContext):
        name = ctx.IDENT().getText()
        tipo = ctx.tipo().getText()
        if name in self.symbols:
            self.report(ctx, f"Variável '{name}' redeclarada")
        else:
            self.symbols[name] = tipo
            self.log(f"Declarou '{name}' como '{tipo}'")

    def exitLeitura(self, ctx: CompiladorParser.LeituraContext):
        name = ctx.IDENT().getText()
        if name not in self.symbols:
            self.report(ctx, f"Leitura de variável não declarada '{name}'")
        else:
            self.log(f"Leitura de '{name}'")

    def exitAtribuicao(self, ctx: CompiladorParser.AtribuicaoContext):
        name = ctx.IDENT().getText()
        if name not in self.symbols:
            self.report(ctx, f"Atribuição em variável não declarada '{name}'")
        else:
            expr = ctx.expr()
            expr_type = getattr(expr, '_type', None)
            var_type = self.symbols[name]
            if expr_type is None:
                return
            if expr_type != var_type:
                self.report(ctx, f"Tipo incompatível na atribuição: variável '{name}' é '{var_type}', expressão é '{expr_type}'")
            else:
                self.log(f"Atribuiu em '{name}' tipo '{expr_type}'")

    # Escreva apenas registra tipo da expressão
    def exitEscrita(self, ctx: CompiladorParser.EscritaContext):
        expr_type = getattr(ctx.expr(), '_type', None)
        self.log(f"Escrita de expressão tipo '{expr_type}'")

    # Literais definem _type
    def exitLiteral(self, ctx: CompiladorParser.LiteralContext):
        ctx._type = 'int' if ctx.INT() else 'string'
        self.log(f"Literal '{ctx.getText()}' tipo '{ctx._type}'")

    # Expr (regra de entrada)
    def exitExpr(self, ctx: CompiladorParser.ExprContext):
        ctx._type = getattr(ctx.exprLogico(), '_type', None)
        self.log(f"Expr '{ctx.getText()}' tipo '{ctx._type}'")

    # Lógico OU
    def exitExprLogico(self, ctx: CompiladorParser.ExprLogicoContext):
        if ctx.getChildCount() == 1:
            ctx._type = getattr(ctx.exprAnd(), '_type', None)
        else:
            left = getattr(ctx.exprLogico(), '_type', None)
            right = getattr(ctx.exprAnd(), '_type', None)
            if left != 'bool' or right != 'bool':
                self.report(ctx, "Operador '||' requer operandos bool")
                ctx._type = None
            else:
                ctx._type = 'bool'
        self.log(f"ExprLogico '{ctx.getText()}' tipo '{ctx._type}'")

    # Lógico E
    def exitExprAnd(self, ctx: CompiladorParser.ExprAndContext):
        if ctx.getChildCount() == 1:
            ctx._type = getattr(ctx.exprIgualdade(), '_type', None)
        else:
            left = getattr(ctx.exprAnd(), '_type', None)
            right = getattr(ctx.exprIgualdade(), '_type', None)
            if left != 'bool' or right != 'bool':
                self.report(ctx, "Operador '&&' requer operandos bool")
                ctx._type = None
            else:
                ctx._type = 'bool'
        self.log(f"ExprAnd '{ctx.getText()}' tipo '{ctx._type}'")

    # Igualdade (==, ~=)
    def exitExprIgualdade(self, ctx: CompiladorParser.ExprIgualdadeContext):
        comps = list(ctx.exprComparacao())
        if len(comps) == 1:
            ctx._type = getattr(comps[0], '_type', None)
        else:
            first_type = getattr(comps[0], '_type', None)
            for i, comp in enumerate(comps[1:], 1):
                comp_type = getattr(comp, '_type', None)
                op = ctx.getChild(2*i-1).getText()
                if first_type != comp_type:
                    self.report(ctx, f"Operador '{op}' requer tipos iguais, obteve '{first_type}' e '{comp_type}'")
                    break
            ctx._type = 'bool'  # Igualdade sempre retorna bool
        self.log(f"ExprIgualdade '{ctx.getText()}' tipo '{ctx._type}'")

    def exitExprComparacao(self, ctx: CompiladorParser.ExprComparacaoContext):
        arits = list(ctx.exprAritmetica())
        if len(arits) == 1:
            # Apenas uma expressão aritmética, sem comparação
            ctx._type = getattr(arits[0], '_type', None)
        else:
            # Há operador de comparação
            left_type = getattr(arits[0], '_type', None)
            right_type = getattr(arits[1], '_type', None)
            op = ctx.getChild(1).getText()
            
            if left_type != 'int' or right_type != 'int':
                self.report(ctx, f"Operador '{op}' requer operandos int, obteve '{left_type}' e '{right_type}'")
                ctx._type = None
            else:
                ctx._type = 'bool'  # Comparações retornam bool
        self.log(f"ExprComparacao '{ctx.getText()}' tipo '{ctx._type}'")

    # Aritmética + e -
    def exitExprAritmetica(self, ctx: CompiladorParser.ExprAritmeticaContext):
        if ctx.getChildCount() == 1:
            ctx._type = getattr(ctx.termo(), '_type', None)
        else:
            left = getattr(ctx.exprAritmetica(), '_type', None)
            right = getattr(ctx.termo(), '_type', None)
            op = ctx.getChild(1).getText()
            if left != 'int' or right != 'int':
                self.report(ctx, f"Operador '{op}' requer operandos int")
                ctx._type = None
            else:
                if op == '/' and ctx.getChild(2).getText() == '0':
                    self.report(ctx, "Divisão por zero")
                ctx._type = 'int'
        self.log(f"ExprAritmetica '{ctx.getText()}' tipo '{ctx._type}'")

    # Termo * e /
    def exitTermo(self, ctx: CompiladorParser.TermoContext):
        if ctx.getChildCount() == 1:
            ctx._type = getattr(ctx.fator(), '_type', None)
        else:
            left = getattr(ctx.termo(), '_type', None)
            right = getattr(ctx.fator(), '_type', None)
            op = ctx.getChild(1).getText()
            if left != 'int' or right != 'int':
                self.report(ctx, f"Operador '{op}' requer operandos int")
                ctx._type = None
            else:
                if op == '/' and ctx.getChild(2).getText() == '0':
                    self.report(ctx, "Divisão por zero")
                ctx._type = 'int'
        self.log(f"Termo '{ctx.getText()}' tipo '{ctx._type}'")

    # Fator: IDENT, literal, subexpressão ou unário
    def exitFator(self, ctx: CompiladorParser.FatorContext):
        if ctx.IDENT():
            name = ctx.IDENT().getText()
            if name not in self.symbols:
                self.report(ctx, f"Variável '{name}' não declarada")
                ctx._type = None
            else:
                ctx._type = self.symbols[name]
            self.log(f"Fator IDENT '{ctx.getText()}' tipo '{ctx._type}'")
        elif ctx.literal():
            ctx._type = ctx.literal()._type
            self.log(f"Fator literal '{ctx.getText()}' tipo '{ctx._type}'")
        elif ctx.expr():
            ctx._type = getattr(ctx.expr(), '_type', None)
            self.log(f"Fator subexpr '{ctx.getText()}' tipo '{ctx._type}'")
        elif ctx.SUB():
            ctx._type = getattr(ctx.fator(), '_type', None)
            self.log(f"Fator unário '-' tipo '{ctx._type}'")
        else:
            ctx._type = None

    # Condicional se expr entao ... fim
    def exitCondicional(self, ctx: CompiladorParser.CondicionalContext):
        t = getattr(ctx.expr(), '_type', None)
        if t != 'bool':
            self.report(ctx, f"'se' requer expressão bool, obteve '{t}'")
        self.log(f"Condicional 'se' tipo expr '{t}'")

    # Repetição enquanto expr faca ... fim
    def exitRepeticao(self, ctx: CompiladorParser.RepeticaoContext):
        t = getattr(ctx.expr(), '_type', None)
        if t != 'bool':
            self.report(ctx, f"'enquanto' requer expressão bool, obteve '{t}'")
        self.log(f"Repetição 'enquanto' tipo expr '{t}'")
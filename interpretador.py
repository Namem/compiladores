from CompiladorListener import CompiladorListener

class Interpretador(CompiladorListener):
    def __init__(self):
        self.vars = {}

    def enterLeitura(self, ctx):
        nome = ctx.IDENT().getText()
        valor = int(input(f"{nome}: "))
        self.vars[nome] = valor

    def enterEscrita(self, ctx):
        valor = self.avaliar_expr(ctx.expr())
        print(valor)

    def enterAtribuicao(self, ctx):
        nome = ctx.IDENT().getText()
        valor = self.avaliar_expr(ctx.expr())
        self.vars[nome] = valor

    def enterCondicional(self, ctx):
        cond = self.avaliar_expr(ctx.expr())
        if cond:
            for c in ctx.bloco(0).comando():
                self.enterComando(c)
        elif ctx.SENAO():
            for c in ctx.bloco(1).comando():
                self.enterComando(c)

    def enterRepeticao(self, ctx):
        while self.avaliar_expr(ctx.expr()):
            for c in ctx.bloco().comando():
                self.enterComando(c)

    def enterComando(self, ctx):
        if ctx.leitura(): self.enterLeitura(ctx.leitura())
        elif ctx.escrita(): self.enterEscrita(ctx.escrita())
        elif ctx.atribuicao(): self.enterAtribuicao(ctx.atribuicao())
        elif ctx.condicional(): self.enterCondicional(ctx.condicional())
        elif ctx.repeticao(): self.enterRepeticao(ctx.repeticao())

    def avaliar_expr(self, ctx):
        if ctx.INT(): return int(ctx.INT().getText())
        if ctx.STRING(): return ctx.STRING().getText().strip('"')
        if ctx.IDENT(): return self.vars.get(ctx.IDENT().getText(), 0)
        if len(ctx.expr()) == 2:
            a = self.avaliar_expr(ctx.expr(0))
            b = self.avaliar_expr(ctx.expr(1))
            if ctx.SOMA(): return a + b
            if ctx.SUB(): return a - b
            if ctx.MULT(): return a * b
            if ctx.DIV(): return a // b
            if ctx.MAIOR(): return a > b
            if ctx.MENOR(): return a < b
            if ctx.IGUAL(): return a == b
            if ctx.DIFERENTE(): return a != b
        return 0

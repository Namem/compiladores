# Generated from Compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from CompiladorParser import CompiladorParser

# This class defines a complete generic visitor for a parse tree produced by CompiladorParser.

class CompiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompiladorParser#programa.
    def visitPrograma(self, ctx:CompiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#declaracoes.
    def visitDeclaracoes(self, ctx:CompiladorParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#declaracao.
    def visitDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#tipo.
    def visitTipo(self, ctx:CompiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#bloco.
    def visitBloco(self, ctx:CompiladorParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#comando.
    def visitComando(self, ctx:CompiladorParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#leitura.
    def visitLeitura(self, ctx:CompiladorParser.LeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#escrita.
    def visitEscrita(self, ctx:CompiladorParser.EscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#atribuicao.
    def visitAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#condicional.
    def visitCondicional(self, ctx:CompiladorParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#repeticao.
    def visitRepeticao(self, ctx:CompiladorParser.RepeticaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#expr.
    def visitExpr(self, ctx:CompiladorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#exprLogico.
    def visitExprLogico(self, ctx:CompiladorParser.ExprLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#exprAnd.
    def visitExprAnd(self, ctx:CompiladorParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#exprIgualdade.
    def visitExprIgualdade(self, ctx:CompiladorParser.ExprIgualdadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#exprComparacao.
    def visitExprComparacao(self, ctx:CompiladorParser.ExprComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#exprAritmetica.
    def visitExprAritmetica(self, ctx:CompiladorParser.ExprAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#termo.
    def visitTermo(self, ctx:CompiladorParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#fator.
    def visitFator(self, ctx:CompiladorParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#literal.
    def visitLiteral(self, ctx:CompiladorParser.LiteralContext):
        return self.visitChildren(ctx)



del CompiladorParser
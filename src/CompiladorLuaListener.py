# Generated from CompiladorLua.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorLuaParser import CompiladorLuaParser
else:
    from CompiladorLuaParser import CompiladorLuaParser

# This class defines a complete listener for a parse tree produced by CompiladorLuaParser.
class CompiladorLuaListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorLuaParser#programa.
    def enterPrograma(self, ctx:CompiladorLuaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#programa.
    def exitPrograma(self, ctx:CompiladorLuaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#bloco.
    def enterBloco(self, ctx:CompiladorLuaParser.BlocoContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#bloco.
    def exitBloco(self, ctx:CompiladorLuaParser.BlocoContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#comando.
    def enterComando(self, ctx:CompiladorLuaParser.ComandoContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#comando.
    def exitComando(self, ctx:CompiladorLuaParser.ComandoContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#leitura.
    def enterLeitura(self, ctx:CompiladorLuaParser.LeituraContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#leitura.
    def exitLeitura(self, ctx:CompiladorLuaParser.LeituraContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#escrita.
    def enterEscrita(self, ctx:CompiladorLuaParser.EscritaContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#escrita.
    def exitEscrita(self, ctx:CompiladorLuaParser.EscritaContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#atribuicao.
    def enterAtribuicao(self, ctx:CompiladorLuaParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#atribuicao.
    def exitAtribuicao(self, ctx:CompiladorLuaParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#condicional.
    def enterCondicional(self, ctx:CompiladorLuaParser.CondicionalContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#condicional.
    def exitCondicional(self, ctx:CompiladorLuaParser.CondicionalContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#repeticao.
    def enterRepeticao(self, ctx:CompiladorLuaParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#repeticao.
    def exitRepeticao(self, ctx:CompiladorLuaParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#expr.
    def enterExpr(self, ctx:CompiladorLuaParser.ExprContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#expr.
    def exitExpr(self, ctx:CompiladorLuaParser.ExprContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#exprLogico.
    def enterExprLogico(self, ctx:CompiladorLuaParser.ExprLogicoContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#exprLogico.
    def exitExprLogico(self, ctx:CompiladorLuaParser.ExprLogicoContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#exprAnd.
    def enterExprAnd(self, ctx:CompiladorLuaParser.ExprAndContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#exprAnd.
    def exitExprAnd(self, ctx:CompiladorLuaParser.ExprAndContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#exprIgualdade.
    def enterExprIgualdade(self, ctx:CompiladorLuaParser.ExprIgualdadeContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#exprIgualdade.
    def exitExprIgualdade(self, ctx:CompiladorLuaParser.ExprIgualdadeContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#exprComparacao.
    def enterExprComparacao(self, ctx:CompiladorLuaParser.ExprComparacaoContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#exprComparacao.
    def exitExprComparacao(self, ctx:CompiladorLuaParser.ExprComparacaoContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#exprAritmetica.
    def enterExprAritmetica(self, ctx:CompiladorLuaParser.ExprAritmeticaContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#exprAritmetica.
    def exitExprAritmetica(self, ctx:CompiladorLuaParser.ExprAritmeticaContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#termo.
    def enterTermo(self, ctx:CompiladorLuaParser.TermoContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#termo.
    def exitTermo(self, ctx:CompiladorLuaParser.TermoContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#fator.
    def enterFator(self, ctx:CompiladorLuaParser.FatorContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#fator.
    def exitFator(self, ctx:CompiladorLuaParser.FatorContext):
        pass


    # Enter a parse tree produced by CompiladorLuaParser#literal.
    def enterLiteral(self, ctx:CompiladorLuaParser.LiteralContext):
        pass

    # Exit a parse tree produced by CompiladorLuaParser#literal.
    def exitLiteral(self, ctx:CompiladorLuaParser.LiteralContext):
        pass



del CompiladorLuaParser
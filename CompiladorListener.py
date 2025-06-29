# Generated from Compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from CompiladorParser import CompiladorParser

# This class defines a complete listener for a parse tree produced by CompiladorParser.
class CompiladorListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorParser#programa.
    def enterPrograma(self, ctx:CompiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#programa.
    def exitPrograma(self, ctx:CompiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#declaracoes.
    def enterDeclaracoes(self, ctx:CompiladorParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by CompiladorParser#declaracoes.
    def exitDeclaracoes(self, ctx:CompiladorParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by CompiladorParser#declaracao.
    def enterDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#declaracao.
    def exitDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#tipo.
    def enterTipo(self, ctx:CompiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#tipo.
    def exitTipo(self, ctx:CompiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#bloco.
    def enterBloco(self, ctx:CompiladorParser.BlocoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#bloco.
    def exitBloco(self, ctx:CompiladorParser.BlocoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#comando.
    def enterComando(self, ctx:CompiladorParser.ComandoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#comando.
    def exitComando(self, ctx:CompiladorParser.ComandoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#leitura.
    def enterLeitura(self, ctx:CompiladorParser.LeituraContext):
        pass

    # Exit a parse tree produced by CompiladorParser#leitura.
    def exitLeitura(self, ctx:CompiladorParser.LeituraContext):
        pass


    # Enter a parse tree produced by CompiladorParser#escrita.
    def enterEscrita(self, ctx:CompiladorParser.EscritaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#escrita.
    def exitEscrita(self, ctx:CompiladorParser.EscritaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#atribuicao.
    def enterAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#atribuicao.
    def exitAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#condicional.
    def enterCondicional(self, ctx:CompiladorParser.CondicionalContext):
        pass

    # Exit a parse tree produced by CompiladorParser#condicional.
    def exitCondicional(self, ctx:CompiladorParser.CondicionalContext):
        pass


    # Enter a parse tree produced by CompiladorParser#repeticao.
    def enterRepeticao(self, ctx:CompiladorParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#repeticao.
    def exitRepeticao(self, ctx:CompiladorParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#expr.
    def enterExpr(self, ctx:CompiladorParser.ExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expr.
    def exitExpr(self, ctx:CompiladorParser.ExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#exprLogico.
    def enterExprLogico(self, ctx:CompiladorParser.ExprLogicoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#exprLogico.
    def exitExprLogico(self, ctx:CompiladorParser.ExprLogicoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#exprAnd.
    def enterExprAnd(self, ctx:CompiladorParser.ExprAndContext):
        pass

    # Exit a parse tree produced by CompiladorParser#exprAnd.
    def exitExprAnd(self, ctx:CompiladorParser.ExprAndContext):
        pass


    # Enter a parse tree produced by CompiladorParser#exprIgualdade.
    def enterExprIgualdade(self, ctx:CompiladorParser.ExprIgualdadeContext):
        pass

    # Exit a parse tree produced by CompiladorParser#exprIgualdade.
    def exitExprIgualdade(self, ctx:CompiladorParser.ExprIgualdadeContext):
        pass


    # Enter a parse tree produced by CompiladorParser#exprComparacao.
    def enterExprComparacao(self, ctx:CompiladorParser.ExprComparacaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#exprComparacao.
    def exitExprComparacao(self, ctx:CompiladorParser.ExprComparacaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#exprAritmetica.
    def enterExprAritmetica(self, ctx:CompiladorParser.ExprAritmeticaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#exprAritmetica.
    def exitExprAritmetica(self, ctx:CompiladorParser.ExprAritmeticaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#termo.
    def enterTermo(self, ctx:CompiladorParser.TermoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#termo.
    def exitTermo(self, ctx:CompiladorParser.TermoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#fator.
    def enterFator(self, ctx:CompiladorParser.FatorContext):
        pass

    # Exit a parse tree produced by CompiladorParser#fator.
    def exitFator(self, ctx:CompiladorParser.FatorContext):
        pass


    # Enter a parse tree produced by CompiladorParser#literal.
    def enterLiteral(self, ctx:CompiladorParser.LiteralContext):
        pass

    # Exit a parse tree produced by CompiladorParser#literal.
    def exitLiteral(self, ctx:CompiladorParser.LiteralContext):
        pass



del CompiladorParser
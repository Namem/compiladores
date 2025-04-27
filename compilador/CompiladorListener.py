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


    # Enter a parse tree produced by CompiladorParser#comando.
    def enterComando(self, ctx:CompiladorParser.ComandoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#comando.
    def exitComando(self, ctx:CompiladorParser.ComandoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#declaracao.
    def enterDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#declaracao.
    def exitDeclaracao(self, ctx:CompiladorParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#atribuicao.
    def enterAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#atribuicao.
    def exitAtribuicao(self, ctx:CompiladorParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#entrada.
    def enterEntrada(self, ctx:CompiladorParser.EntradaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#entrada.
    def exitEntrada(self, ctx:CompiladorParser.EntradaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#saida.
    def enterSaida(self, ctx:CompiladorParser.SaidaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#saida.
    def exitSaida(self, ctx:CompiladorParser.SaidaContext):
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


    # Enter a parse tree produced by CompiladorParser#expressao.
    def enterExpressao(self, ctx:CompiladorParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expressao.
    def exitExpressao(self, ctx:CompiladorParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by CompiladorParser#tipo.
    def enterTipo(self, ctx:CompiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by CompiladorParser#tipo.
    def exitTipo(self, ctx:CompiladorParser.TipoContext):
        pass



del CompiladorParser
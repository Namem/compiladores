# Generated from Compilador.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,180,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,49,8,1,10,1,12,1,52,9,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,4,5,4,61,8,4,10,4,12,4,64,9,4,1,5,1,5,1,5,1,5,
        1,5,3,5,71,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,96,8,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        5,12,114,8,12,10,12,12,12,117,9,12,1,13,1,13,1,13,1,13,1,13,1,13,
        5,13,125,8,13,10,13,12,13,128,9,13,1,14,1,14,1,14,5,14,133,8,14,
        10,14,12,14,136,9,14,1,15,1,15,1,15,5,15,141,8,15,10,15,12,15,144,
        9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,152,8,16,10,16,12,16,155,
        9,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,163,8,17,10,17,12,17,166,
        9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,176,8,18,1,19,
        1,19,1,19,0,4,24,26,32,34,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,0,6,1,0,2,3,1,0,27,28,1,0,29,32,1,0,20,21,1,0,
        22,23,1,0,12,13,175,0,40,1,0,0,0,2,44,1,0,0,0,4,53,1,0,0,0,6,57,
        1,0,0,0,8,62,1,0,0,0,10,70,1,0,0,0,12,72,1,0,0,0,14,78,1,0,0,0,16,
        84,1,0,0,0,18,89,1,0,0,0,20,99,1,0,0,0,22,105,1,0,0,0,24,107,1,0,
        0,0,26,118,1,0,0,0,28,129,1,0,0,0,30,137,1,0,0,0,32,145,1,0,0,0,
        34,156,1,0,0,0,36,175,1,0,0,0,38,177,1,0,0,0,40,41,3,2,1,0,41,42,
        3,8,4,0,42,43,5,0,0,1,43,1,1,0,0,0,44,50,5,1,0,0,45,46,3,4,2,0,46,
        47,5,17,0,0,47,49,1,0,0,0,48,45,1,0,0,0,49,52,1,0,0,0,50,48,1,0,
        0,0,50,51,1,0,0,0,51,3,1,0,0,0,52,50,1,0,0,0,53,54,5,14,0,0,54,55,
        5,18,0,0,55,56,3,6,3,0,56,5,1,0,0,0,57,58,7,0,0,0,58,7,1,0,0,0,59,
        61,3,10,5,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,
        0,0,63,9,1,0,0,0,64,62,1,0,0,0,65,71,3,12,6,0,66,71,3,14,7,0,67,
        71,3,16,8,0,68,71,3,18,9,0,69,71,3,20,10,0,70,65,1,0,0,0,70,66,1,
        0,0,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,11,1,0,0,0,72,
        73,5,4,0,0,73,74,5,15,0,0,74,75,5,14,0,0,75,76,5,16,0,0,76,77,5,
        17,0,0,77,13,1,0,0,0,78,79,5,5,0,0,79,80,5,15,0,0,80,81,3,22,11,
        0,81,82,5,16,0,0,82,83,5,17,0,0,83,15,1,0,0,0,84,85,5,14,0,0,85,
        86,5,19,0,0,86,87,3,22,11,0,87,88,5,17,0,0,88,17,1,0,0,0,89,90,5,
        6,0,0,90,91,3,22,11,0,91,92,5,8,0,0,92,95,3,8,4,0,93,94,5,7,0,0,
        94,96,3,8,4,0,95,93,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,
        9,0,0,98,19,1,0,0,0,99,100,5,10,0,0,100,101,3,22,11,0,101,102,5,
        11,0,0,102,103,3,8,4,0,103,104,5,9,0,0,104,21,1,0,0,0,105,106,3,
        24,12,0,106,23,1,0,0,0,107,108,6,12,-1,0,108,109,3,26,13,0,109,115,
        1,0,0,0,110,111,10,2,0,0,111,112,5,25,0,0,112,114,3,26,13,0,113,
        110,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,
        25,1,0,0,0,117,115,1,0,0,0,118,119,6,13,-1,0,119,120,3,28,14,0,120,
        126,1,0,0,0,121,122,10,2,0,0,122,123,5,24,0,0,123,125,3,28,14,0,
        124,121,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,
        127,27,1,0,0,0,128,126,1,0,0,0,129,134,3,30,15,0,130,131,7,1,0,0,
        131,133,3,30,15,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,
        0,134,135,1,0,0,0,135,29,1,0,0,0,136,134,1,0,0,0,137,142,3,32,16,
        0,138,139,7,2,0,0,139,141,3,32,16,0,140,138,1,0,0,0,141,144,1,0,
        0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,31,1,0,0,0,144,142,1,0,0,
        0,145,146,6,16,-1,0,146,147,3,34,17,0,147,153,1,0,0,0,148,149,10,
        2,0,0,149,150,7,3,0,0,150,152,3,34,17,0,151,148,1,0,0,0,152,155,
        1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,33,1,0,0,0,155,153,1,
        0,0,0,156,157,6,17,-1,0,157,158,3,36,18,0,158,164,1,0,0,0,159,160,
        10,2,0,0,160,161,7,4,0,0,161,163,3,36,18,0,162,159,1,0,0,0,163,166,
        1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,35,1,0,0,0,166,164,1,
        0,0,0,167,168,5,15,0,0,168,169,3,22,11,0,169,170,5,16,0,0,170,176,
        1,0,0,0,171,172,5,21,0,0,172,176,3,36,18,0,173,176,3,38,19,0,174,
        176,5,14,0,0,175,167,1,0,0,0,175,171,1,0,0,0,175,173,1,0,0,0,175,
        174,1,0,0,0,176,37,1,0,0,0,177,178,7,5,0,0,178,39,1,0,0,0,11,50,
        62,70,95,115,126,134,142,153,164,175
    ]

class CompiladorParser ( Parser ):

    grammarFileName = "Compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'variaveis'", "'int'", "'string'", "'leia'", 
                     "'escreva'", "'se'", "'senao'", "'entao'", "'fim'", 
                     "'enquanto'", "'faca'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "';'", "':'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'&&'", "'||'", "'!'", "'=='", "'~='", "'>'", 
                     "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "VARIAVEIS", "TIPO_INT", "TIPO_STRING", 
                      "LEIA", "ESCREVA", "SE", "SENAO", "ENTAO", "FIM", 
                      "ENQUANTO", "FACA", "INT", "STRING", "IDENT", "ABREPAR", 
                      "FECHAPAR", "PONTOVIRGULA", "DOIS_PONTOS", "ATRIBUICAO", 
                      "SOMA", "SUB", "MULT", "DIV", "E", "OU", "NAO", "IGUAL", 
                      "DIFERENTE", "MAIOR", "MENOR", "MAIORIGUAL", "MENORIGUAL", 
                      "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_declaracao = 2
    RULE_tipo = 3
    RULE_bloco = 4
    RULE_comando = 5
    RULE_leitura = 6
    RULE_escrita = 7
    RULE_atribuicao = 8
    RULE_condicional = 9
    RULE_repeticao = 10
    RULE_expr = 11
    RULE_exprLogico = 12
    RULE_exprAnd = 13
    RULE_exprIgualdade = 14
    RULE_exprComparacao = 15
    RULE_exprAritmetica = 16
    RULE_termo = 17
    RULE_fator = 18
    RULE_literal = 19

    ruleNames =  [ "programa", "declaracoes", "declaracao", "tipo", "bloco", 
                   "comando", "leitura", "escrita", "atribuicao", "condicional", 
                   "repeticao", "expr", "exprLogico", "exprAnd", "exprIgualdade", 
                   "exprComparacao", "exprAritmetica", "termo", "fator", 
                   "literal" ]

    EOF = Token.EOF
    VARIAVEIS=1
    TIPO_INT=2
    TIPO_STRING=3
    LEIA=4
    ESCREVA=5
    SE=6
    SENAO=7
    ENTAO=8
    FIM=9
    ENQUANTO=10
    FACA=11
    INT=12
    STRING=13
    IDENT=14
    ABREPAR=15
    FECHAPAR=16
    PONTOVIRGULA=17
    DOIS_PONTOS=18
    ATRIBUICAO=19
    SOMA=20
    SUB=21
    MULT=22
    DIV=23
    E=24
    OU=25
    NAO=26
    IGUAL=27
    DIFERENTE=28
    MAIOR=29
    MENOR=30
    MAIORIGUAL=31
    MENORIGUAL=32
    WS=33
    COMENTARIO=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(CompiladorParser.DeclaracoesContext,0)


        def bloco(self):
            return self.getTypedRuleContext(CompiladorParser.BlocoContext,0)


        def EOF(self):
            return self.getToken(CompiladorParser.EOF, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = CompiladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.declaracoes()
            self.state = 41
            self.bloco()
            self.state = 42
            self.match(CompiladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIAVEIS(self):
            return self.getToken(CompiladorParser.VARIAVEIS, 0)

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.DeclaracaoContext,i)


        def PONTOVIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.PONTOVIRGULA)
            else:
                return self.getToken(CompiladorParser.PONTOVIRGULA, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracoes" ):
                return visitor.visitDeclaracoes(self)
            else:
                return visitor.visitChildren(self)




    def declaracoes(self):

        localctx = CompiladorParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CompiladorParser.VARIAVEIS)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 45
                    self.declaracao()
                    self.state = 46
                    self.match(CompiladorParser.PONTOVIRGULA) 
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(CompiladorParser.IDENT, 0)

        def DOIS_PONTOS(self):
            return self.getToken(CompiladorParser.DOIS_PONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(CompiladorParser.TipoContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = CompiladorParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(CompiladorParser.IDENT)
            self.state = 54
            self.match(CompiladorParser.DOIS_PONTOS)
            self.state = 55
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_INT(self):
            return self.getToken(CompiladorParser.TIPO_INT, 0)

        def TIPO_STRING(self):
            return self.getToken(CompiladorParser.TIPO_STRING, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = CompiladorParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.ComandoContext,i)


        def getRuleIndex(self):
            return CompiladorParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco" ):
                return visitor.visitBloco(self)
            else:
                return visitor.visitChildren(self)




    def bloco(self):

        localctx = CompiladorParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17520) != 0):
                self.state = 59
                self.comando()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leitura(self):
            return self.getTypedRuleContext(CompiladorParser.LeituraContext,0)


        def escrita(self):
            return self.getTypedRuleContext(CompiladorParser.EscritaContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(CompiladorParser.AtribuicaoContext,0)


        def condicional(self):
            return self.getTypedRuleContext(CompiladorParser.CondicionalContext,0)


        def repeticao(self):
            return self.getTypedRuleContext(CompiladorParser.RepeticaoContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = CompiladorParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comando)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.leitura()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.escrita()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.atribuicao()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.condicional()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.repeticao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEIA(self):
            return self.getToken(CompiladorParser.LEIA, 0)

        def ABREPAR(self):
            return self.getToken(CompiladorParser.ABREPAR, 0)

        def IDENT(self):
            return self.getToken(CompiladorParser.IDENT, 0)

        def FECHAPAR(self):
            return self.getToken(CompiladorParser.FECHAPAR, 0)

        def PONTOVIRGULA(self):
            return self.getToken(CompiladorParser.PONTOVIRGULA, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_leitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeitura" ):
                listener.enterLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeitura" ):
                listener.exitLeitura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeitura" ):
                return visitor.visitLeitura(self)
            else:
                return visitor.visitChildren(self)




    def leitura(self):

        localctx = CompiladorParser.LeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_leitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(CompiladorParser.LEIA)
            self.state = 73
            self.match(CompiladorParser.ABREPAR)
            self.state = 74
            self.match(CompiladorParser.IDENT)
            self.state = 75
            self.match(CompiladorParser.FECHAPAR)
            self.state = 76
            self.match(CompiladorParser.PONTOVIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCREVA(self):
            return self.getToken(CompiladorParser.ESCREVA, 0)

        def ABREPAR(self):
            return self.getToken(CompiladorParser.ABREPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def FECHAPAR(self):
            return self.getToken(CompiladorParser.FECHAPAR, 0)

        def PONTOVIRGULA(self):
            return self.getToken(CompiladorParser.PONTOVIRGULA, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_escrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscrita" ):
                listener.enterEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscrita" ):
                listener.exitEscrita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscrita" ):
                return visitor.visitEscrita(self)
            else:
                return visitor.visitChildren(self)




    def escrita(self):

        localctx = CompiladorParser.EscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_escrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(CompiladorParser.ESCREVA)
            self.state = 79
            self.match(CompiladorParser.ABREPAR)
            self.state = 80
            self.expr()
            self.state = 81
            self.match(CompiladorParser.FECHAPAR)
            self.state = 82
            self.match(CompiladorParser.PONTOVIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(CompiladorParser.IDENT, 0)

        def ATRIBUICAO(self):
            return self.getToken(CompiladorParser.ATRIBUICAO, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def PONTOVIRGULA(self):
            return self.getToken(CompiladorParser.PONTOVIRGULA, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = CompiladorParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(CompiladorParser.IDENT)
            self.state = 85
            self.match(CompiladorParser.ATRIBUICAO)
            self.state = 86
            self.expr()
            self.state = 87
            self.match(CompiladorParser.PONTOVIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(CompiladorParser.SE, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def ENTAO(self):
            return self.getToken(CompiladorParser.ENTAO, 0)

        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.BlocoContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.BlocoContext,i)


        def FIM(self):
            return self.getToken(CompiladorParser.FIM, 0)

        def SENAO(self):
            return self.getToken(CompiladorParser.SENAO, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = CompiladorParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(CompiladorParser.SE)
            self.state = 90
            self.expr()
            self.state = 91
            self.match(CompiladorParser.ENTAO)
            self.state = 92
            self.bloco()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 93
                self.match(CompiladorParser.SENAO)
                self.state = 94
                self.bloco()


            self.state = 97
            self.match(CompiladorParser.FIM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENQUANTO(self):
            return self.getToken(CompiladorParser.ENQUANTO, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def FACA(self):
            return self.getToken(CompiladorParser.FACA, 0)

        def bloco(self):
            return self.getTypedRuleContext(CompiladorParser.BlocoContext,0)


        def FIM(self):
            return self.getToken(CompiladorParser.FIM, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeticao" ):
                return visitor.visitRepeticao(self)
            else:
                return visitor.visitChildren(self)




    def repeticao(self):

        localctx = CompiladorParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CompiladorParser.ENQUANTO)
            self.state = 100
            self.expr()
            self.state = 101
            self.match(CompiladorParser.FACA)
            self.state = 102
            self.bloco()
            self.state = 103
            self.match(CompiladorParser.FIM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprLogico(self):
            return self.getTypedRuleContext(CompiladorParser.ExprLogicoContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CompiladorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.exprLogico(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprLogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprAnd(self):
            return self.getTypedRuleContext(CompiladorParser.ExprAndContext,0)


        def exprLogico(self):
            return self.getTypedRuleContext(CompiladorParser.ExprLogicoContext,0)


        def OU(self):
            return self.getToken(CompiladorParser.OU, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_exprLogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogico" ):
                listener.enterExprLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogico" ):
                listener.exitExprLogico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogico" ):
                return visitor.visitExprLogico(self)
            else:
                return visitor.visitChildren(self)



    def exprLogico(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.ExprLogicoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_exprLogico, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.exprAnd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompiladorParser.ExprLogicoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprLogico)
                    self.state = 110
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 111
                    self.match(CompiladorParser.OU)
                    self.state = 112
                    self.exprAnd(0) 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprIgualdade(self):
            return self.getTypedRuleContext(CompiladorParser.ExprIgualdadeContext,0)


        def exprAnd(self):
            return self.getTypedRuleContext(CompiladorParser.ExprAndContext,0)


        def E(self):
            return self.getToken(CompiladorParser.E, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_exprAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAnd" ):
                listener.enterExprAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAnd" ):
                listener.exitExprAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAnd" ):
                return visitor.visitExprAnd(self)
            else:
                return visitor.visitChildren(self)



    def exprAnd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.ExprAndContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_exprAnd, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.exprIgualdade()
            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompiladorParser.ExprAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprAnd)
                    self.state = 121
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 122
                    self.match(CompiladorParser.E)
                    self.state = 123
                    self.exprIgualdade() 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprIgualdadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprComparacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.ExprComparacaoContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.ExprComparacaoContext,i)


        def IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.IGUAL)
            else:
                return self.getToken(CompiladorParser.IGUAL, i)

        def DIFERENTE(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.DIFERENTE)
            else:
                return self.getToken(CompiladorParser.DIFERENTE, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_exprIgualdade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprIgualdade" ):
                listener.enterExprIgualdade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprIgualdade" ):
                listener.exitExprIgualdade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIgualdade" ):
                return visitor.visitExprIgualdade(self)
            else:
                return visitor.visitChildren(self)




    def exprIgualdade(self):

        localctx = CompiladorParser.ExprIgualdadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprIgualdade)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.exprComparacao()
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 130
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 131
                    self.exprComparacao() 
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprComparacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.ExprAritmeticaContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.ExprAritmeticaContext,i)


        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.MENOR)
            else:
                return self.getToken(CompiladorParser.MENOR, i)

        def MAIOR(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.MAIOR)
            else:
                return self.getToken(CompiladorParser.MAIOR, i)

        def MAIORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.MAIORIGUAL)
            else:
                return self.getToken(CompiladorParser.MAIORIGUAL, i)

        def MENORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.MENORIGUAL)
            else:
                return self.getToken(CompiladorParser.MENORIGUAL, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_exprComparacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprComparacao" ):
                listener.enterExprComparacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprComparacao" ):
                listener.exitExprComparacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprComparacao" ):
                return visitor.visitExprComparacao(self)
            else:
                return visitor.visitChildren(self)




    def exprComparacao(self):

        localctx = CompiladorParser.ExprComparacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exprComparacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.exprAritmetica(0)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 138
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 139
                    self.exprAritmetica(0) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprAritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(CompiladorParser.TermoContext,0)


        def exprAritmetica(self):
            return self.getTypedRuleContext(CompiladorParser.ExprAritmeticaContext,0)


        def SOMA(self):
            return self.getToken(CompiladorParser.SOMA, 0)

        def SUB(self):
            return self.getToken(CompiladorParser.SUB, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_exprAritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritmetica" ):
                listener.enterExprAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritmetica" ):
                listener.exitExprAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritmetica" ):
                return visitor.visitExprAritmetica(self)
            else:
                return visitor.visitChildren(self)



    def exprAritmetica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.ExprAritmeticaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exprAritmetica, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.termo(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompiladorParser.ExprAritmeticaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprAritmetica)
                    self.state = 148
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 149
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 150
                    self.termo(0) 
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self):
            return self.getTypedRuleContext(CompiladorParser.FatorContext,0)


        def termo(self):
            return self.getTypedRuleContext(CompiladorParser.TermoContext,0)


        def MULT(self):
            return self.getToken(CompiladorParser.MULT, 0)

        def DIV(self):
            return self.getToken(CompiladorParser.DIV, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)



    def termo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.TermoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_termo, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.fator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompiladorParser.TermoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo)
                    self.state = 159
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 160
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 161
                    self.fator() 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABREPAR(self):
            return self.getToken(CompiladorParser.ABREPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def FECHAPAR(self):
            return self.getToken(CompiladorParser.FECHAPAR, 0)

        def SUB(self):
            return self.getToken(CompiladorParser.SUB, 0)

        def fator(self):
            return self.getTypedRuleContext(CompiladorParser.FatorContext,0)


        def literal(self):
            return self.getTypedRuleContext(CompiladorParser.LiteralContext,0)


        def IDENT(self):
            return self.getToken(CompiladorParser.IDENT, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = CompiladorParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_fator)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(CompiladorParser.ABREPAR)
                self.state = 168
                self.expr()
                self.state = 169
                self.match(CompiladorParser.FECHAPAR)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(CompiladorParser.SUB)
                self.state = 172
                self.fator()
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.literal()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.match(CompiladorParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CompiladorParser.INT, 0)

        def STRING(self):
            return self.getToken(CompiladorParser.STRING, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CompiladorParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.exprLogico_sempred
        self._predicates[13] = self.exprAnd_sempred
        self._predicates[16] = self.exprAritmetica_sempred
        self._predicates[17] = self.termo_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprLogico_sempred(self, localctx:ExprLogicoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exprAnd_sempred(self, localctx:ExprAndContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exprAritmetica_sempred(self, localctx:ExprAritmeticaContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def termo_sempred(self, localctx:TermoContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





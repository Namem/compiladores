from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from src.CompiladorLuaLexer import CompiladorLuaLexer

class MeuErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"ERRO LÉXICO [Linha {line}, Coluna {column}]: {msg}")

def analisar_lexico(codigo_fonte):
    input_stream = InputStream(codigo_fonte)
    lexer = CompiladorLuaLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MeuErrorListener())
    stream = CommonTokenStream(lexer)
    stream.fill()
    
    # Debug: Mostrar todos os tokens reconhecidos
    print("Tokens reconhecidos:")
    for i, token in enumerate(stream.tokens):
        print(f"[{i}] {token.text} (Tipo: {token.type})")
    
    tokens = []
    for token in stream.tokens:
        if token.type != -1:  # Ignora token EOF
            try:
                token_name = lexer.symbolicNames[token.type]
                tokens.append({
                    "tipo": token_name,
                    "lexema": token.text,
                    "linha": token.line,
                    "coluna": token.column
                })
            except IndexError:
                print(f"AVISO: Tipo de token desconhecido {token.type} para lexema '{token.text}'")
    
    return tokens
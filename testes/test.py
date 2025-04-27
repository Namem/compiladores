import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# Configura caminhos
sys.path.append(os.path.abspath('.'))
from src.CompiladorLuaLexer import CompiladorLuaLexer
from src.CompiladorLuaParser import CompiladorLuaParser

class MeuErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"\033[91mERRO: Linha {line}:{column} - {msg}\033[0m")

def analisar_codigo(codigo):
    input_stream = InputStream(codigo)
    lexer = CompiladorLuaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiladorLuaParser(stream)
    
    # Configura tratamento de erros
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    error_listener = MeuErrorListener()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)
    
    try:
        print("\n\033[1m=== ANÁLISE LÉXICA ===\033[0m")
        print("Tokens reconhecidos:")
        for token in stream.tokens:
            if token.type != -1:  # Ignora EOF
                tipo = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else f"Tipo_{token.type}"
                print(f"  {tipo:<15} '{token.text}' (Linha {token.line}, Coluna {token.column})")
        
        print("\n\033[1m=== ÁRVORE SINTÁTICA ===\033[0m")
        tree = parser.programa()
        print(tree.toStringTree(recog=parser))
        
        print("\n\033[92mAnálise concluída com sucesso!\033[0m")
    except Exception as e:
        print(f"\n\033[91mFalha na análise: {str(e)}\033[0m")

def main():
    # Verifica se o arquivo existe
    print(f"Lendo arquivo: {os.path.abspath('testes/test.txt')}") 
    if not os.path.exists("testes/test.txt"):
        print("\033[91mArquivo test.txt não encontrado na pasta testes/\033[0m")
        return
    
    # Lê o conteúdo do arquivo
    with open("testes/test.txt", "r", encoding="utf-8") as file:
        codigo = file.read()
    
    print("\033[1m=== TESTE DO COMPILADOR ===\033[0m")
    print("\033[94mCódigo sendo testado:\033[0m")
    print(codigo)
    
    analisar_codigo(codigo)

if __name__ == "__main__":
    main()
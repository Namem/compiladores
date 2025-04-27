import sys
from antlr4 import *
from CompiladorLexer import CompiladorLexer
from CompiladorParser import CompiladorParser
from antlr4.error.ErrorListener import ErrorListener
from ast_visualizer import ASTVisualizer

class MeuErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"\033[91mERRO SINTÁTICO [Linha {line}, Coluna {column}]: {msg}\033[0m")

def main(argv):
    # Abrir o arquivo de input
    with open(argv[1], 'r') as f:
        input_text = f.read()

    # Mostrar o conteúdo do input
    print("\n\033[96m=== INPUT ===\033[0m")
    print(input_text)

    # Preparar para o lexer/parser
    input_stream = InputStream(input_text)
    lexer = CompiladorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiladorParser(stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(MeuErrorListener())
    parser.addErrorListener(MeuErrorListener())

    # Mostrar Tokens
    print("\n\033[92m=== TOKENS ===\033[0m")
    lexer.reset()
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type]
            print(f"<{token_name}, '{token.text}', Linha {token.line}, Coluna {token.column}>")

    # Rodar o parser
    tree = parser.programa()

    # Mostrar a árvore sintática no terminal
    print("\n\033[93m=== ÁRVORE SINTÁTICA ===\033[0m")
    print(tree.toStringTree(recog=parser))

    # Gerar o arquivo .dot da AST
    visualizer = ASTVisualizer()
    visualizer.visualizar(tree, parser)

if __name__ == '__main__':
    main(sys.argv)

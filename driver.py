import sys
from antlr4 import *
from CompiladorLexer import CompiladorLexer
from CompiladorParser import CompiladorParser
from antlr4.error.ErrorListener import ErrorListener
from ast_visualizer import ASTVisualizer
from SemanticAnalyzer import AnalisadorSemantico as SemanticAnalyzer
from antlr4 import ParseTreeWalker

# Listener customizado para erros
class MeuErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.erros = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        erro = f"\033[91mERRO SINTÁTICO [Linha {line}, Coluna {column}]: {msg}\033[0m"
        self.erros.append(erro)
        print(erro)

def main(argv):
    if len(argv) < 2:
        print("Uso: python driver.py <arquivo_fonte>")
        sys.exit(1)

    # Ler entrada
    with open(argv[1], 'r') as f:
        input_text = f.read()

    print("\n\033[96m***************** INPUT *****************\033[0m")
    print(input_text)

    input_stream = InputStream(input_text)
    lexer = CompiladorLexer(input_stream)

    # Adicionar listener de erro ao lexer
    lexer_error_listener = MeuErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)

    stream = CommonTokenStream(lexer)

    # Verificar erros léxicos
    stream.fill()
    if lexer_error_listener.erros:
        print("\n\033[91mO programa foi encerrado devido a erro(s) léxicos.\033[0m")
        sys.exit(1)

    # Mostrar Tokens
    print("\n\033[92m***************** TOKENS *****************\033[0m")
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type]
            print(f"<{token_name}, '{token.text}', Linha {token.line}, Coluna {token.column}>")

    parser = CompiladorParser(stream)
    parser_error_listener = MeuErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)

    tree = parser.programa()

    if parser_error_listener.erros:
        print("\n\033[91mO programa foi encerrado devido a erro(s) sintáticos.\033[0m")
        sys.exit(1)

    # Árvore sintática
    print("\n\033[93m***************** ÁRVORE SINTÁTICA *****************\033[0m")
    print(tree.toStringTree(recog=parser))

    # AST visual
    visualizer = ASTVisualizer()
    visualizer.visualizar(tree, parser)

    # Executar análise semântica
    print("\n\033[94m***************** ANÁLISE SEMÂNTICA *****************\033[0m")
    walker = ParseTreeWalker()
    listener = SemanticAnalyzer()
    walker.walk(listener, tree)

    if listener.errors:
        for e in listener.errors:
            print(e)
        sys.exit(1)

    for log in listener.logs:
         print(f"[SEMÂNTICO] {log}")

if __name__ == '__main__':
    main(sys.argv)

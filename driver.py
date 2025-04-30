from antlr4 import *
from CompiladorLexer import CompiladorLexer
from CompiladorParser import CompiladorParser
from interpretador import Interpretador
from antlr4.tree.Trees import Trees
import sys

def main(argv):
    input_file = argv[1] if len(argv) > 1 else "exemplo.txt"
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = CompiladorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CompiladorParser(token_stream)
    tree = parser.programa()

    listener = Interpretador()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main(sys.argv)

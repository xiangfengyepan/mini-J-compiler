import sys
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from gVisitorImpl import GVisitorImpl

def main():
    if len(sys.argv) != 2:
        print("Ús: python3 g.py programa.j")
        return

    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        input_stream = InputStream(file.read())

    lexer = gLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gParser(stream)
    tree = parser.program()

    visitor = GVisitorImpl()
    resultat = visitor.visit(tree)

    if resultat is not None:
        print("Resultat final:", resultat)

if __name__ == '__main__':
    main()

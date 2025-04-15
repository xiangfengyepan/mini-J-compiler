import sys
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from CodeGenVisitor import CodeGenVisitor
from utils import MyErrorListener

def main():
    if len(sys.argv) != 2:
        print("Ús: python3 g.py programa.j")
        return

    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        input_stream = InputStream(file.read())

    lexer = gLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Crea y añade el listener
    error_listener = MyErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    parser = gParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.hay_error:
        print("→ Lexical erros founded. Aborting program execution.")
        return

    visitor = CodeGenVisitor()
    results = visitor.visit(tree)
    print("\n".join(map(str, results)))

if __name__ == '__main__':
    main()

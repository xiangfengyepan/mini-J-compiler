import sys, os
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from CodeGenVisitor import CodeGenVisitor
from utils import MyErrorListener

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python3 g.py program.j [--test]")
        return

    # Check if --test is passed and extract the input file name
    is_test = "--test" in args
    file_name = next((arg for arg in args if not arg.startswith("--")), None)

    if not file_name:
        print("Error: no input file specified.")
        return

    with open(file_name, 'r') as file:
        input_stream = InputStream(file.read())

    lexer = gLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Custom error listener
    error_listener = MyErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    parser = gParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.hay_error:
        print("→ Lexical errors detected. Aborting program execution.")
        return

    visitor = CodeGenVisitor()
    results = visitor.visit(tree)


    filtered_output = "\n".join(str(r) for r in results if r is not None)

    if is_test:
        base_name = os.path.splitext(file_name)[0]
        with open(f"{base_name}.out", "w") as out_file:
            out_file.write(filtered_output)
    else:
        CYAN = "\033[96m"
        RESET = "\033[0m"
        print()
        print("📦 CodeGen Visitor Results")
        print(f"{CYAN}==========================={RESET}")
        print(filtered_output)

if __name__ == '__main__':
    main()

import sys, os
import numpy as np
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from CodeGenVisitor import CodeGenVisitor
from utils import DebugConfig, MyErrorListener

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python3 g.py program.j [--test]")
        return

    is_test = "--test" in args
    is_debug = "--debug" in args

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

    DebugConfig.set_debug_visits(is_debug)
    visitor = CodeGenVisitor()
    results = visitor.visit(tree)

    filtered_output = [r for r in results if r is not None]

    if is_test:
        base_name = os.path.splitext(file_name)[0]
        my_write(filtered_output, f"{base_name}.out")
    else:
        CYAN = "\033[96m"
        RESET = "\033[0m"
        print()
        print("📦 CodeGen Visitor Results")
        print(f"{CYAN}==========================={RESET}")
        my_print(filtered_output)


def format_element(elem):
    if isinstance(elem, np.int32):
        return f"_{abs(elem)}" if elem < 0 else str(elem)
    elif isinstance(elem, np.ndarray):
        return " ".join(format_element(e) for e in elem)
    return None


def my_print(output_list):
    [print(format_element(elem)) for elem in output_list if format_element(elem) is not None]

def my_write(output_list, file_path):
    with open(file_path, "w") as f:
        [f.write(format_element(item) + '\n') for item in output_list if format_element(item) is not None]




if __name__ == '__main__':
    main()

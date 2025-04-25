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
        print("Usage: python3 g.py [program.j] [--test] [--debug] [--ia]")
        return

    is_test = "--test" in args
    is_debug = "--debug" in args
    is_interactive = "--ia" in args

    file_name = next((arg for arg in args if not arg.startswith("--")), None)
    if not is_interactive and not file_name:
        print("Error: no input file specified.")
        return
    
    if is_interactive: 
        input_stream = InputStream(input('? '))
    elif file_name:
        with open(file_name, 'r') as file:
            input_stream = InputStream(file.read())
    
    filtered_output = None
    visitor = CodeGenVisitor()
    while is_interactive or not filtered_output:
        
        
        filtered_output = antlr(visitor, input_stream, is_debug)
        if not filtered_output:
            return
        
        if is_test:
            base_name = os.path.splitext(file_name)[0]
            my_write(filtered_output, f"{base_name}.out")
        elif not is_interactive:
            CYAN = "\033[96m"
            RESET = "\033[0m"
            print()
            print("📦 CodeGen Visitor Results")
            print(f"{CYAN}==========================={RESET}")
        my_print(filtered_output)
            
        if is_interactive:
            input_stream = InputStream(input('? '))
             
        

def antlr(visitor, input_stream, is_debug):
    error_listener = MyErrorListener()
    
    lexer = gLexer(input_stream)
    lexer.removeErrorListeners()
    
    # print(lexer.getTokenNames())
    print("lexical error found :(")
    # return

    token_stream = CommonTokenStream(lexer)

    parser = gParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    DebugConfig.set_debug_visits(is_debug)
    
    filtered_output = None
    if parser.getNumberOfSyntaxErrors() == 0:
        results = visitor.visit(tree)
        filtered_output = [r for r in results if r is not None]
    else:
        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        print(tree.toStringTree(recog=parser))
  
    return filtered_output

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

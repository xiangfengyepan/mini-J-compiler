import sys, os
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from EvalVisitor import EvalVisitor
from TreeVisitor import TreeVisitor

from utils import DebugConfig, MyErrorListener, MyPrinter

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python3 g.py [program.j] [--test] [--debug] [--ia] [--tree]")
        return

    file_name = next((arg for arg in args if not arg.startswith("--")), None)
    is_test = "--test" in args
    is_debug = "--debug" in args
    is_interactive = "--ia" in args
    is_tree = "--tree" in args

    if is_interactive: 
        input_stream = InputStream(input('> Interactive Mode [Ctrl + C] to exit\n> '))
    elif file_name:
        if not os.path.isfile(file_name):
            print(f"Error: File '{file_name}' does not exist.", file=sys.stderr)
            return
        with open(file_name, 'r') as file:
            input_stream = InputStream(file.read())
    else:
        print("Error: no input file specified.", file=sys.stderr)
        return
    
    filtered_output = None
    if not is_test and is_tree:
        treeVisitor = TreeVisitor()
    evalVisitor = EvalVisitor()

    while True:
        parser, tree = setParserTree(input_stream)

        if not is_test and is_tree:
            visitParserTree(treeVisitor, parser, tree, False)
        filtered_output = visitParserTree(evalVisitor, parser, tree, is_debug)
        
        if filtered_output and is_test:
            base_name = os.path.splitext(file_name)[0]
            MyPrinter.my_write(filtered_output, f"{base_name}.out")
        elif filtered_output:
            if not is_interactive:
                MyPrinter.show_title()
            MyPrinter.my_print(filtered_output)

        if is_interactive:
            input_stream = InputStream(input('> '))
            continue
    
        break
                
def setParserTree(input_stream):
    error_listener = MyErrorListener()
    
    lexer = gLexer(input_stream)
    lexer.removeErrorListeners()
    
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    tokens = token_stream.tokens

    lexical_errors = []
    for token in tokens:
        if token.type == lexer.LEXICAL_ERROR:
            lexical_errors.append(token)

    if lexical_errors:
        for error in lexical_errors:
            print(f"Uff, Lexical error found: '{error.text}' at line {error.line}, column {error.column}", file=sys.stderr)
        print("Aborting execution due to lexical errors :(", file=sys.stderr)
        exit(0)
        
    parser = gParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.program()

    return parser, tree

def visitParserTree(visitor, parser, tree, is_debug):
    DebugConfig.set_debug_visits(is_debug)

    if parser.getNumberOfSyntaxErrors() > 0:
        print(parser.getNumberOfSyntaxErrors(), 'syntax error found :(', file=sys.stderr)
        return None

    return process_tree(visitor, tree)

def process_tree(visitor, tree):
    try:
        results = visitor.visit(tree)
        return [r for r in results if r is not None] if results else None
    except Exception as e:
        print(f"Runtime error: {e}", file=sys.stderr)
        return None

if __name__ == '__main__':
    main()

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
    if not is_test:
        treeVisitor = TreeVisitor()
    evalVisitor = EvalVisitor()

    while is_interactive or not filtered_output:
        parser, tree = setPerserTree(input_stream)
        
        if not is_test:
            visitParserTree(treeVisitor, parser, tree, is_debug)
        filtered_output = visitParserTree(evalVisitor, parser, tree, is_debug)

        if filtered_output is None:
            return
        
        if is_test:
            base_name = os.path.splitext(file_name)[0]
            MyPrinter.my_write(filtered_output, f"{base_name}.out")
        elif not is_interactive:
            MyPrinter.show_title()
            
        if filtered_output is not None:
            MyPrinter.my_print(filtered_output)

        if is_interactive:
            input_stream = InputStream(input('? '))
             
        

def setPerserTree(input_stream):
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
            print(f"Lexical error found: '{error.text}' at line {error.line}, column {error.column}")
        print("Aborting execution due to lexical errors.")
        return
        
    parser = gParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.program()

    return parser, tree

def visitParserTree(visitor, parser, tree, is_debug):
    DebugConfig.set_debug_visits(is_debug)


    filtered_output = None
    if parser.getNumberOfSyntaxErrors() == 0:
        results = visitor.visit(tree)
        if results is not None:
            filtered_output = [r for r in results if r is not None]
    else:
        print(parser.getNumberOfSyntaxErrors(), 'sintax error')
        print(tree.toStringTree(recog=parser))
  
    return filtered_output


if __name__ == '__main__':
    main()

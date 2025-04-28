
import sys
import numpy as np
from antlr4.error.ErrorListener import ErrorListener
class DebugConfig:
    visits_enabled = False
    visit_depth = 0

    def set_debug_visits(value: bool):
        DebugConfig.visits_enabled = value

def debug_visit(func):
    def wrapper(self, ctx):
        indent = '\t' * DebugConfig.visit_depth

        GREEN = '\033[92m'
        RED = '\033[91m'
        BLUE = '\033[94m'
        RESET = '\033[0m'

        if DebugConfig.visits_enabled:
            token_stream = ctx.parser.getTokenStream()
            start_idx = ctx.start.tokenIndex
            stop_idx = ctx.stop.tokenIndex if ctx.stop else start_idx
            tokens = token_stream.getTokens(start_idx, stop_idx + 1)
            token_text = ' '.join(f"{BLUE}{t.text}{RESET}" for t in tokens if t.text is not None)

            start_line = ctx.start.line  # Get the starting line number
            print(f"{indent}{GREEN}→ Entrant a {func.__name__} (Line {start_line}):{RESET} {token_text}")

        DebugConfig.visit_depth += 1
        result = func(self, ctx)
        DebugConfig.visit_depth -= 1

        if DebugConfig.visits_enabled:
            stop_line = ctx.stop.line if ctx.stop else start_line  # Get the stop line number, or use start line if stop is None
            print(f"{indent}{RED}← Sortint de {func.__name__} (Line {stop_line}):{RESET} {result}")
        return result

    return wrapper

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.hay_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hay_error = True
        print(f"Error en la linia {line}, columna {column}: {msg}", file=sys.stderr)

class MyPrinter:
    def format_element(elem, print_errors = False):
        if isinstance(elem, np.int32):
            return f"_{abs(elem)}" if elem < 0 else str(elem)
        elif isinstance(elem, np.ndarray):
            result = " ".join(e for e in [MyPrinter.format_element(e) for e in elem] if e is not None)
            return result if result else None
        
        elif print_errors and isinstance(elem, str):
            return elem
        return None
    
    def my_print(output_list):
        [print(formatted) for elem in output_list if (formatted := MyPrinter.format_element(elem, True)) is not None]


    def my_write(output_list, file_path):
        with open(file_path, "w") as f:
            [f.write(formatted + '\n') for elem in output_list if (formatted := MyPrinter.format_element(elem)) is not None]

    def show_title():
        CYAN = "\033[96m"
        RESET = "\033[0m"
        print()
        print("CodeGen Visitor Results")
        print(f"{CYAN}==========================={RESET}")

class ReturnSignal(np.ndarray):
    def __new__(cls, value=None):
        obj = super().__new__(cls, shape=(1,), dtype=np.int32)
        obj[0] = np.int32(value)

        return obj

    def __repr__(self):
        return f"ReturnSignal({self[0]})"
    
    @staticmethod
    def hasInstance(value):
        if isinstance(value, ReturnSignal):
            return True
        elif isinstance(value, list):
            return any(ReturnSignal.hasInstance(item) for item in value)
        return False
            
class ReturnSignal(np.int32):
    def __new__(cls, value=None):
        return super().__new__(cls, value)

    def __repr__(self):
        return f"ReturnSignal({self})"
    
    @staticmethod
    def hasInstance(value):
        if isinstance(value, ReturnSignal):
            return True
        elif isinstance(value, list):
            return any(ReturnSignal.hasInstance(item) for item in value)
        return False


def flatten_list(input_list):
    flattened = []
    if not isinstance(input_list, list):
        return input_list

    for item in input_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(np.atleast_1d(item))

    return flattened



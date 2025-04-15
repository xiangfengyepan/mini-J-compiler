
from antlr4.error.ErrorListener import ErrorListener

DEBUG_VISITS = False
VISIT_DEPTH = 0

def debug_visit(func):
    def wrapper(self, ctx):
        global VISIT_DEPTH

        indent = '\t' * VISIT_DEPTH

        # ANSI colors
        GREEN = '\033[92m'
        RED = '\033[91m'
        BLUE = '\033[94m'
        RESET = '\033[0m'

        if DEBUG_VISITS:
            # Accedemos al stream de tokens desde el parser
            token_stream = ctx.parser.getTokenStream()
            start_idx = ctx.start.tokenIndex
            stop_idx = ctx.stop.tokenIndex

            # Obtener todos los tokens en ese rango
            tokens = token_stream.getTokens(start_idx, stop_idx)
            token_text = ' '.join(f"{BLUE}{t.text}{RESET}" for t in tokens if t.text is not None)

            print(f"{indent}{GREEN}→ Entrant a {func.__name__}:{RESET} {token_text}")

        VISIT_DEPTH += 1

        result = func(self, ctx)

        VISIT_DEPTH -= 1

        if DEBUG_VISITS:
            print(f"{indent}{RED}← Sortint de {func.__name__}:{RESET} {result}")
        return result

    return wrapper

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.hay_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hay_error = True
        print(f"Error línia {line}, columna {column}: {msg}")



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
            stop_idx = ctx.stop.tokenIndex
            tokens = token_stream.getTokens(start_idx, stop_idx)
            token_text = ' '.join(f"{BLUE}{t.text}{RESET}" for t in tokens if t.text is not None)
            print(f"{indent}{GREEN}→ Entrant a {func.__name__}:{RESET} {token_text}")

        DebugConfig.visit_depth += 1
        result = func(self, ctx)
        DebugConfig.visit_depth -= 1

        if DebugConfig.visits_enabled:
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



from antlr4.error.ErrorListener import ErrorListener

DEBUG_VISITS = True

def debug_visit(func):
    def wrapper(self, ctx):
        if DEBUG_VISITS:
            print(f"→ Entrant a {func.__name__}: {ctx.getText()}")
        result = func(self, ctx)
        if DEBUG_VISITS:
            print(f"← Sortint de {func.__name__}: {result}")
        return result
    return wrapper

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.hay_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hay_error = True
        print(f"Error línia {line}, columna {column}: {msg}")


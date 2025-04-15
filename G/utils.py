
from antlr4.error.ErrorListener import ErrorListener

DEBUG_VISITS = True
VISIT_DEPTH = 0

def debug_visit(func):
    def wrapper(self, ctx):
        global VISIT_DEPTH
        
        indent = '\t' * VISIT_DEPTH  
        
        if DEBUG_VISITS:
            print(f"{indent}→ Entrant a {func.__name__}: {ctx.getText().replace("\n", "")}")

        VISIT_DEPTH += 1
        
        result = func(self, ctx)

        VISIT_DEPTH -= 1
        
        if DEBUG_VISITS:
            print(f"{indent}← Sortint de {func.__name__}: {result}")
        return result
    
    return wrapper

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.hay_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hay_error = True
        print(f"Error línia {line}, columna {column}: {msg}")


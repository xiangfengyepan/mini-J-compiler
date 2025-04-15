# Variable global per activar/desactivar el debug
DEBUG_VISITS = True

# Decorador per imprimir entrada i sortida dels mètodes
def debug_visit(func):
    def wrapper(self, ctx):
        if DEBUG_VISITS:
            print(f"→ Entrant a {func.__name__}: {ctx.getText()}")
        result = func(self, ctx)
        if DEBUG_VISITS:
            print(f"← Sortint de {func.__name__}: {result}")
        return result
    return wrapper

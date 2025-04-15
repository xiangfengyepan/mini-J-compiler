from gVisitor import gVisitor
from utils import debug_visit

class GVisitorImpl(gVisitor):
    def __init__(self):
        super().__init__()

    @debug_visit
    def visitProgram(self, ctx):
        resultats = [self.visit(child) for child in ctx.statement()]
        return resultats[-1] if resultats else None

    #######################
    # Statements Visitors #
    #######################

    @debug_visit
    def visitStatement(self, ctx):
        # Statement can be either expr NEWLINE or funcDef
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.funcDef():
            return self.visit(ctx.funcDef())
        else:
            return None

    @debug_visit
    def visitFuncDef(self, ctx):
        # TODO
        return

    ##################
    # Exprs Visitors #
    ##################

    @debug_visit
    def visitParent(self, ctx):
        return self.visit(ctx.expr())

    @debug_visit
    def visitComposition(self, ctx):
        # TODO
        return

    @debug_visit
    def visitIdentity(self, ctx):
        # TODO
        return

    @debug_visit
    def visitVariable(self, ctx):
        # TODO
        return

    @debug_visit
    def visitRelational(self, ctx):
        # TODO
        return

    @debug_visit
    def visitUnary(self, ctx):
        # TODO
        return

    @debug_visit
    def visitValue(self, ctx):
        if (ctx.INTVAL()):
            return int(ctx.INTVAL().getText())
        if (ctx.FLOATVAL()):
            return float(ctx.FLOATVAL().getText())

    @debug_visit
    def visitAritmetic(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return lhs * rhs
        elif op == '/':
            return lhs / rhs
        elif op == '+':
            return lhs + rhs
        elif op == '-':
            return lhs - rhs

    @debug_visit
    def visitLogical(self, ctx):
        # TODO
        return

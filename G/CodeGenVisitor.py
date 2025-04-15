import numpy as np

from gVisitor import gVisitor
from utils import debug_visit

class CodeGenVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}

    @debug_visit
    def visitProgram(self, ctx):
        results = [self.visit(child) for child in ctx.statement()]
        return results

    #######################
    # Statements Visitors #
    #######################

    @debug_visit
    def visitStatement(self, ctx):
        # Statement can be either expr NEWLINE or delaration
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.delaration():
            return self.visit(ctx.delaration())
        else:
            return None

    @debug_visit
    def visitDelaration(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value
        return

    ##################
    # Exprs Visitors #
    ##################

    @debug_visit
    def visitParent(self, ctx):
        return self.visit(ctx.expr())

    @debug_visit
    def visitFuncCall(self, ctx):
        # TODO
        return

    @debug_visit
    def visitVariable(self, ctx):
        var = self.variables[ctx.ID().getText()]
        return var

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
        if ctx.INTVAL():
            return np.int64(ctx.INTVAL().getText())
        if ctx.FLOATVAL():
            return np.float64(ctx.FLOATVAL().getText())

    @debug_visit
    def visitAritmetic(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        if ctx.MUL():
            return np.multiply(lhs, rhs)
        elif ctx.DIV():
            return np.divide(lhs, rhs)
        elif ctx.PLUS():
            return np.add(lhs, rhs)
        elif ctx.MINUS():
            return np.subtract(lhs, rhs)
        elif ctx.MOD():
            return np.mod(lhs, rhs)

    @debug_visit
    def visitLogical(self, ctx):
        # TODO
        return

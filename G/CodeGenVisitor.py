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

    @debug_visit
    def visitDelaration(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value
        return value

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
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        if ctx.EQUAL():
            return np.equal(lhs, rhs).astype(int)
        elif ctx.NE():
            return np.not_equal(lhs, rhs).astype(int)
        elif ctx.LT():
            return np.less(lhs, rhs).astype(int)
        elif ctx.GT():
            return np.greater(lhs, rhs).astype(int)
        elif ctx.LE():
            return np.less_equal(lhs, rhs).astype(int)
        elif ctx.GE():
            return np.greater_equal(lhs, rhs).astype(int)

    @debug_visit
    def visitUnary(self, ctx):
        value = self.visit(ctx.expr())
        if ctx.NEG():
            return -value
        elif ctx.NOT():
            return np.logical_not(value).astype(int)
        return

    @debug_visit
    def visitValue(self, ctx):
        if ctx.INTVAL() and len(ctx.INTVAL()) == 1:
            return np.int32(ctx.INTVAL(0).getText())
        # elif ctx.FLOATVAL() and len(ctx.FLOATVAL()) == 1:
        #     return np.float64(ctx.FLOATVAL(0).getText())
        elif ctx.INTVAL() and len(ctx.INTVAL()) > 1:
            return np.array([elem.getText() for elem in ctx.INTVAL()], dtype=np.int32)
        # elif ctx.FLOATVAL() and len(ctx.FLOATVAL()) > 1:
        #     return np.array([elem.getText() for elem in ctx.FLOATVAL()], dtype=np.float64)


    @debug_visit
    def visitAritmetic(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        try:
            if ctx.MUL():
                return np.multiply(lhs, rhs)
            elif ctx.DIV():
                return np.floor_divide(lhs, rhs)    # divisio entera
            elif ctx.PLUS():
                return np.add(lhs, rhs)
            elif ctx.MINUS():
                return np.subtract(lhs, rhs)
            elif ctx.POW():
                return np.power(lhs, rhs)
            elif ctx.MOD():
                return np.mod(rhs, lhs)             # els operands van al reves
        except Exception as e:
            return f"error: {str(e)}"


    @debug_visit
    def visitLogical(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.AND():
            return np.logical_and(lhs, rhs)
        elif ctx.OR():
            return np.logical_or(lhs, rhs)
        return

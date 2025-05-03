import numpy as np
import inspect

from gParser import gParser
from gVisitor import gVisitor
from utils import debug_visit


class OperatorRegistry:
    def __init__(self):
        super().__init__()
        self.binaryOperators = {
            # '*': lambda lhs, rhs: np.multiply(lhs, rhs),
            # '%': lambda lhs, rhs: np.floor_divide(lhs, rhs),
            # '+': lambda lhs, rhs: np.add(lhs, rhs),
            # '-': lambda lhs, rhs: np.subtract(lhs, rhs),
            # '^': lambda lhs, rhs: np.power(lhs, rhs),
            # '|': lambda lhs, rhs: np.mod(rhs, lhs),

            # ',': lambda lhs, rhs: np.concatenate((np.atleast_1d(lhs), np.atleast_1d(rhs))),
            # '#': lambda lhs, rhs: np.array(rhs)[np.array(lhs, dtype=bool)],
            # '{': lambda lhs, rhs: np.array(rhs)[np.array(lhs)],

            # '=': lambda lhs, rhs: np.equal(lhs, rhs).astype(np.int32),
            # '<>': lambda lhs, rhs: np.not_equal(lhs, rhs).astype(np.int32),
            # '<': lambda lhs, rhs: np.less(lhs, rhs).astype(np.int32),
            # '>': lambda lhs, rhs: np.greater(lhs, rhs).astype(np.int32),
            # '<=': lambda lhs, rhs: np.less_equal(lhs, rhs).astype(np.int32),
            # '>=': lambda lhs, rhs: np.greater_equal(lhs, rhs).astype(np.int32),
        }

        self.unaryOperators = {
            # ']': lambda x: x,
            # '#': lambda x: np.int32(np.atleast_1d(x).size),
            # 'i.': lambda x: np.arange(x).astype(np.int32),
            # '_': lambda x: -x,
            # '+': lambda x: x,

            # '^:': lambda x: np.power(x, x),
            # '*:': lambda x: np.multiply(x, x),
            # '+:': lambda x: np.add(x, x),
            # '-:': lambda x: np.subtract(x, x),
        }

    def addOperator(self, name, func, arity):
        if arity == 1:
            self.unaryOperators[name] = func
        elif arity == 2:
            self.binaryOperators[name] = func
        else:
            raise ValueError("Only unary and binary operators are supported")

    # def callOperator(self, operator_name, lhs, rhs):
    #     if operator_name in self.operators:
    #         return self.operators[operator_name](lhs, rhs)
    #     else:
    #         raise ValueError(f"Operador {operator_name} no encontrado.")

    def getOperator(self, name, arity):
        if arity == 1:
            return self.unaryOperators.get(name)
        elif arity == 2:
            return self.binaryOperators.get(name)
        else:
            raise ValueError("Unsupported operator arity")


class EvalVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self.functions = OperatorRegistry()
        self.variables = {}

    @debug_visit
    def visitProgram(self, ctx):
        return self.visit(ctx.statements())

    @debug_visit
    def visitStatements(self, ctx):
        return [self.visit(child) for child in ctx.statement()]

    @debug_visit
    def visitExprStmt(self, ctx):
        value = self.visit(ctx.expr())
        return value

    @debug_visit
    def visitExprDeclaration(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value

    @debug_visit
    def visitOperatorDeclaration(self, ctx):
        name = ctx.ID().getText()
        # func = self.visit(ctx.operators())
        print(name, ctx.operators().getText())
        # self.functions.addOperator(name, func, arity=2)
        
    @debug_visit
    def visitBinaryOperators(self, ctx):
        try:
            if ctx.MUL():
                return lambda lhs, rhs: np.multiply(lhs, rhs)
            elif ctx.DIV():
                return lambda lhs, rhs: np.floor_divide(lhs, rhs)
            elif ctx.PLUS():
                return lambda lhs, rhs: np.add(lhs, rhs)
            elif ctx.MINUS():
                return lambda lhs, rhs: np.subtract(lhs, rhs)
            elif ctx.POW():
                return lambda lhs, rhs: np.power(lhs, rhs)
            elif ctx.MOD():
                return lambda lhs, rhs: np.mod(rhs, lhs)
            elif ctx.CONCATE():
                return lambda lhs, rhs: np.concatenate((np.atleast_1d(lhs), np.atleast_1d(rhs)))
            elif ctx.HASH():
                return lambda lhs, rhs: np.array(rhs)[np.array(lhs, dtype=bool)]
            elif ctx.INDEX():
                return lambda lhs, rhs: np.array(rhs)[np.array(lhs)]
            elif ctx.EQUAL():
                return lambda lhs, rhs: np.equal(lhs, rhs).astype(np.int32)
            elif ctx.NE():
                return lambda lhs, rhs: np.not_equal(lhs, rhs).astype(np.int32)
            elif ctx.LT():
                return lambda lhs, rhs: np.less(lhs, rhs).astype(np.int32)
            elif ctx.GT():
                return lambda lhs, rhs: np.greater(lhs, rhs).astype(np.int32)
            elif ctx.LE():
                return lambda lhs, rhs: np.less_equal(lhs, rhs).astype(np.int32)
            elif ctx.GE():
                return lambda lhs, rhs: np.greater_equal(lhs, rhs).astype(np.int32)
            
            elif ctx.FLIP():
                return lambda lhs, rhs: (rhs, lhs)
        except Exception as e:
            return f"error: {str(e)}"

    @debug_visit
    def visitUnaryOperators(self, ctx):
        try:
            if ctx.POWD():
                return lambda x: np.power(x, x)
            elif ctx.MULD():
                return lambda x: np.multiply(x, x)
            elif ctx.PLUSD():
                return lambda x: np.add(x, x)
            elif ctx.MINUSD():
                return lambda x: np.subtract(x, x)
            elif ctx.NEG():
                return lambda x: -x
            elif ctx.HASH():
                return lambda x: np.int32(np.atleast_1d(x).size)
            elif ctx.ARANGE():
                return lambda x: np.arange(x).astype(np.int32)
            elif ctx.PLUS():
                return lambda x: x
            elif ctx.IDENTITY():
                return lambda x: x
        except Exception as e:
            return f"error: {str(e)}"

        
    @debug_visit
    def visitFoldOperators(self, ctx):
        try:
            if ctx.MUL():
                return lambda x: np.multiply.reduce(x).astype(np.int32)
            elif ctx.DIV():
                return lambda x: np.floor_divide.reduce(x).astype(np.int32)
            elif ctx.PLUS():
                return lambda x: np.add.reduce(x).astype(np.int32)
            elif ctx.MINUS():
                return lambda x: np.subtract.reduce(x).astype(np.int32)
            elif ctx.POW():
                return lambda x: np.power.reduce(x).astype(np.int32)
            elif ctx.MOD():
                return lambda x: np.mod.reduce(x).astype(np.int32)
            elif ctx.CONCATE():
                return lambda x: np.array(x)
        except Exception as e:
            return f"error: {str(e)}"

    @debug_visit
    def visitParent(self, ctx):
        return self.visit(ctx.expr())

    @debug_visit
    def visitVariable(self, ctx):
        name = ctx.ID().getText()
        var = self.variables[name]
        return var
    
    @debug_visit
    def visitUnaryFuncCall(self, ctx):
        name = ctx.ID().getText()
        print(name, ctx.expr().getText())
        return

    @debug_visit
    def visitValue(self, ctx):
        if ctx.INTVAL() and len(ctx.INTVAL()) == 1:
            return np.int32(ctx.INTVAL(0).getText())
        elif ctx.INTVAL() and len(ctx.INTVAL()) > 1:
            return np.array([elem.getText() for elem in ctx.INTVAL()], dtype=np.int32)


    @debug_visit
    def visitBinaryAritmetic(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        if ctx.binaryOperators().FLIP():
            lhs, rhs = rhs, lhs 

        try:
            operator = self.visit(ctx.binaryOperators())
            return operator(lhs, rhs)
        except Exception as e:
            return f"error: {str(e)}"
    
    @debug_visit
    def visitUnaryAritmetic(self, ctx):
        x = self.visit(ctx.expr())

        try:
            operator = self.visit(ctx.unaryOperators())
            return operator(x)
        except Exception as e:
            return f"error: {str(e)}"
    
    @debug_visit
    def visitFoldAritmetic(self, ctx):
        value = self.visit(ctx.expr())

        try:
            operator = self.visit(ctx.foldOperators())
            return operator(value)
        except Exception as e:
            return f"error: {str(e)}"
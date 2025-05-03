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
    def visitBinaryFuncCall(self, ctx):
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
        lhs = self.visit(ctx.expr(0)) if ctx.expr(0) else None
        rhs = self.visit(ctx.expr(1)) if ctx.expr(1) else None

        rhs = lhs if rhs is None else rhs

        if ctx.binaryOperators() and ctx.binaryOperators().FLIP():
            lhs, rhs = rhs, lhs

        try:
            if ctx.binaryOperators().MUL():
                return np.multiply(lhs, rhs)
            elif ctx.binaryOperators().DIV():
                return np.floor_divide(lhs, rhs)    # integer divition
            elif ctx.binaryOperators().PLUS():
                return np.add(lhs, rhs)
            elif ctx.binaryOperators().MINUS():
                return np.subtract(lhs, rhs)
            elif ctx.binaryOperators().POW():
                return np.power(lhs, rhs)
            elif ctx.binaryOperators().MOD():
                return np.mod(rhs, lhs)             # reverse operator 
            elif ctx.binaryOperators().CONCATE():
                return np.concatenate((np.atleast_1d(lhs), np.atleast_1d(rhs)))
            elif ctx.binaryOperators().HASH():
                return np.array(rhs)[np.array(lhs, dtype=bool)]
            elif ctx.binaryOperators().INDEX():
                return np.array(rhs)[np.array(lhs)]
            elif ctx.binaryOperators().EQUAL():
                return np.equal(lhs, rhs).astype(np.int32)
            elif ctx.binaryOperators().NE():
                return np.not_equal(lhs, rhs).astype(np.int32)
            elif ctx.binaryOperators().LT():
                return np.less(lhs, rhs).astype(np.int32)
            elif ctx.binaryOperators().GT():
                return np.greater(lhs, rhs).astype(np.int32)
            elif ctx.binaryOperators().LE():
                return np.less_equal(lhs, rhs).astype(np.int32)
            elif ctx.binaryOperators().GE():
                return np.greater_equal(lhs, rhs).astype(np.int32)
        except Exception as e:
            return f"error: {str(e)}"
    
    @debug_visit
    def visitUnaryAritmetic(self, ctx):
        lhs = self.visit(ctx.expr())
        rhs = lhs

        try:
            if ctx.unaryOperators().POWD():
                return np.power(lhs, rhs)
            elif ctx.unaryOperators().MULD():
                return np.multiply(lhs, rhs)
            elif ctx.unaryOperators().PLUSD():
                return np.add(lhs, rhs)
            elif ctx.unaryOperators().MINUSD():
                return np.subtract(lhs, rhs)
            elif ctx.unaryOperators().NEG():
                return -lhs
            elif ctx.unaryOperators().HASH():
                return np.int32(np.atleast_1d(lhs).size)
            elif ctx.unaryOperators().ARANGE():
                return np.int32(np.arange(lhs))
            elif ctx.unaryOperators().PLUS():
                return lhs
            elif ctx.unaryOperators().IDENTITY():
                return lhs
        
        except Exception as e:
            return f"error: {str(e)}"
    
    @debug_visit
    def visitFoldAritmetic(self, ctx):
        value = self.visit(ctx.expr())
        try:
            if ctx.unaryFold().MUL():
                return np.multiply.reduce(value).astype(np.int32)
            elif ctx.unaryFold().DIV():
                return np.floor_divide.reduce(value).astype(np.int32)    # integer division
            elif ctx.unaryFold().PLUS():
                return np.add.reduce(value).astype(np.int32)
            elif ctx.unaryFold().MINUS():
                return np.subtract.reduce(value).astype(np.int32)
            elif ctx.unaryFold().POW():
                return np.power.reduce(value).astype(np.int32)
            elif ctx.unaryFold().MOD():
                return np.mod.reduce(value).astype(np.int32)             # reverse operators
            elif ctx.unaryFold().CONCATE():
                return np.array(value)

        except Exception as e:
            return f"error: {str(e)}"
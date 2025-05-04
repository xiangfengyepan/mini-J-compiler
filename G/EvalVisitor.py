import numpy as np

import inspect

from gParser import gParser
from gVisitor import gVisitor
from utils import debug_visit


class OperatorRegistry:
    def __init__(self):
        super().__init__()
        
        self.tokens =  gParser.literalNames # TODO

        self.operator_map = {
            '*': np.multiply,
            '%': np.floor_divide,
            '+': np.add,
            '-': np.subtract,
            '^': np.power,
            '|': np.mod,
        }

        self.binaryOperators = {
            '*': lambda lhs, rhs: np.multiply(lhs, rhs),
            '%': lambda lhs, rhs: np.floor_divide(lhs, rhs),
            '+': lambda lhs, rhs: np.add(lhs, rhs),
            '-': lambda lhs, rhs: np.subtract(lhs, rhs),
            '^': lambda lhs, rhs: np.power(lhs, rhs),
            '|': lambda lhs, rhs: np.mod(rhs, lhs),

            ',': lambda lhs, rhs: np.concatenate((np.atleast_1d(lhs), np.atleast_1d(rhs))),
            '#': lambda lhs, rhs: np.array(rhs)[np.array(lhs, dtype=bool)],
            '{': lambda lhs, rhs: np.array(rhs)[np.array(lhs)],

            '=': lambda lhs, rhs: np.equal(lhs, rhs).astype(np.int32),
            '<>': lambda lhs, rhs: np.not_equal(lhs, rhs).astype(np.int32),
            '<': lambda lhs, rhs: np.less(lhs, rhs).astype(np.int32),
            '>': lambda lhs, rhs: np.greater(lhs, rhs).astype(np.int32),
            '<=': lambda lhs, rhs: np.less_equal(lhs, rhs).astype(np.int32),
            '>=': lambda lhs, rhs: np.greater_equal(lhs, rhs).astype(np.int32),

            '~': lambda lhs, rhs: (rhs, lhs),

            '/': lambda op, x: op.reduce(np.array(x, dtype=np.int32)),
        }

        self.unaryOperators = {
            ']': lambda x: x,
            '#': lambda x: np.int32(np.atleast_1d(x).size),
            'i.': lambda x: np.arange(x).astype(np.int32),
            '_': lambda x: -x,
            '+': lambda x: x,

            '^:': lambda x: np.power(x, x),
            '*:': lambda x: np.multiply(x, x),
            '+:': lambda x: np.add(x, x),
            '-:': lambda x: np.subtract(x, x),
        }

        self.stack = {
            # TODO list of parameter for a function
            # exmpale: 
            # 'foo' : [1, 2, 3]
        }
    
    def getOperatorMap(self, op_symbol):
        return self.operator_map.get(op_symbol)

    def addOperator(self, name, func, arity):
        if arity == 1:
            self.unaryOperators[name] = func
        elif arity == 2:
            self.binaryOperators[name] = func
        else:
            raise ValueError("Only unary and binary operators are supported")
        
    def getOperator(self, name, arity):
        if arity == 1:
            return self.unaryOperators.get(name)
        elif arity == 2:
            return self.binaryOperators.get(name)
        else:
            raise ValueError("Unsupported operator arity")
    
    def pushStack(self, name, parameter):
        if name not in self.stack:
            self.stack[name] = []
        self.stack[name].append(parameter)

    def popStack(self, name):
        return self.stack[name].pop()

    def stackEmpty(self, name):
        return name not in self.stack or len(self.stack[name]) == 0

    def callOperator(self, operator_name, parameters):
        arity = len(parameters)
        operator = self.getOperator(operator_name, arity)
        if not operator:
            raise ValueError(f"Operator '{operator_name}' with arity {arity} not found")
        return operator(*parameters)

class EvalVisitor(gVisitor):
    INT_TYPE = np.int32

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
        # TODO addOperator in Operator Registry 
        # 1. creat and lambda combinationg funcion for all the ctx.opertors that are not expr() [ unaryOperators binaryOperators unaryFold] 
        # 2. push parameter in the stack (if ctx.operators.expr())
        for child in ctx.operators():
            if child.expr():
                self.functions.pushStack(name, self.visit(child.expr()))
            else:
                func = self.visit(child)
  
                arity = func.__code__.co_argcount - len(func.__defaults__ or [])
                print(f"Arity: {arity}")

                source = inspect.getsource(func)
                print(source)

                self.functions.addOperator(name, func, arity)

        print(name, [child.getText() for child in ctx.operators()])
        
    @debug_visit
    def visitBinaryOperators(self, ctx):
        try:
            name = ctx.getChild(0).getText()
            return self.functions.getOperator(name, 2)
        except Exception as e:
            return f"error: {str(e)}"

    @debug_visit
    def visitUnaryOperators(self, ctx):
        try:
            name = ctx.getChild(0).getText()
            return self.functions.getOperator(name, 1)
        except Exception as e:
            return f"error: {str(e)}"

        
    @debug_visit
    def visitFoldOperators(self, ctx):
        try:
            op_symbol = ctx.getChild(0).getText()
            op = self.functions.getOperatorMap(op_symbol)
            myFold = self.functions.getOperator(ctx.FOLD().getText(), 2)
    
            return lambda x: myFold(op, x).astype(self.INT_TYPE)
        
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
        func = self.functions.getOperator(name, 1)        
        args = self.visit(ctx.expr())

        print(name, inspect.getsource(func), args)
        return func(args)

    @debug_visit
    def visitValue(self, ctx):
        if ctx.INTVAL() and len(ctx.INTVAL()) == 1:
            return self.INT_TYPE(ctx.INTVAL(0).getText())
        elif ctx.INTVAL() and len(ctx.INTVAL()) > 1:
            return np.array([elem.getText() for elem in ctx.INTVAL()], dtype=self.INT_TYPE)


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
        value = self.visit(ctx.expr())

        try:
            operator = self.visit(ctx.unaryOperators())
            return operator(value)
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
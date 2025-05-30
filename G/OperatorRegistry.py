import numpy as np
from functools import reduce 

from gParser import gParser


class OperatorRegistry:
    def __init__(self):
        super().__init__()

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

            '/': lambda op, x: op.reduce(np.array(x, dtype=np.int32)),
        }

        self.unaryOperators = {
            ']': lambda x: x,
            '#': lambda x: np.int32(np.atleast_1d(x).size),
            'i.': lambda x: np.arange(x).astype(np.int32),
            '+': lambda x: x,

            '*:': lambda x: np.multiply(x, x),
            '+:': lambda x: np.add(x, x),
            '^:': lambda x: np.power(x, x),
            ',:': lambda x: np.concatenate((np.atleast_1d(x), np.atleast_1d(x))),
            '#:': lambda x: np.array(x)[np.array(x, dtype=bool)],
        }

        self.stack = {}
    
    def compose(self, funcs):
        def composed(*args):
            for idx, f in enumerate(funcs):
                arity = f.__code__.co_argcount - len(f.__defaults__ or [])

                if arity == len(args):
                    reversed_args = tuple(reversed(args))
                    result = f(*reversed_args)
                    args = (result,)
                elif arity < len(args):
                    used_args = args[:arity]
                    remaining_args = args[arity:]
                    reversed_args = tuple(reversed(used_args))
                    result = f(*reversed_args)
                    args = (result,) + remaining_args

                else:
                    raise ValueError(f"Function '{f.__name__}' with arity {arity} cannot handle {len(args)} arguments")

            return args
        return composed

    def addOperator(self, name, funcs, arity):
        if len(funcs) == 1 and funcs[0].__name__ == "composed":
            composedFunc = funcs[0]
        else:
            composedFunc = self.compose(funcs)

        if arity == 1:
            if name not in self.unaryOperators:
                self.unaryOperators[name] = []
            self.unaryOperators[name].append(composedFunc)
        elif arity == 2:
            if name not in self.binaryOperators:
                self.binaryOperators[name] = []
            self.binaryOperators[name].append(composedFunc)
        else:
            raise ValueError("Only unary and binary operators are supported")
    
    def delOperator(self, name, arity):

        if arity == 1:
            if name in self.unaryOperators:
                self.unaryOperators[name].clear()
        elif arity == 2:
            if name in self.binaryOperators:
                self.binaryOperators[name].clear()
        else:
            raise ValueError("Only unary and binary operators are supported")
        self.popAllStack(name)
        
    def getOperator(self, name, arity=None):
        if arity == 1:
            return self.unaryOperators.get(name)
        elif arity == 2:
            return self.binaryOperators.get(name)
        
        operator = self.unaryOperators.get(name) or self.binaryOperators.get(name)
        
        return operator
    
    def pushStack(self, name, parameter):
        if name not in self.stack:
            self.stack[name] = []
        self.stack[name].append(parameter)

    def popStack(self, name):
        if name in self.stack and self.stack[name]:
            value = self.stack[name].pop()
            return value
        raise IndexError(f"Pila '{name}' vacía o no existe")

    def popAllStack(self, name):
        while not self.isStackEmpty(name):
            self.popStack(name)

    def getAllStack(self, name):
        if name not in self.stack:
            return []
        return list(reversed(self.stack[name]))

    def isStackEmpty(self, name):
        return name not in self.stack or len(self.stack[name]) == 0

    def callOperator(self, name):
        functionList = self.getOperator(name, 1)   
        args = []
        if not self.isStackEmpty(name):
            args.extend(self.getAllStack(name))

        for f in reversed(functionList):
            args = f(*args)

        return args[0]

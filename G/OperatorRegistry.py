import numpy as np

from gParser import gParser

class OperatorRegistry:
    def __init__(self):
        super().__init__()
        
        self.tokens =  gParser.literalNames # TODO

        self.foldOperator = {
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

        self.stack = {}
    
    def compose(self, funcs):
        def composed(*args):
            for f in funcs:
                arity = f.__code__.co_argcount - len(f.__defaults__ or [])  
                if arity == len(args):  
                    args = (f(*args),) 
                elif arity < len(args):
                    args = f(*args)
                else:
                    raise ValueError(f"Function with arity {arity} cannot handle {len(args)} arguments")
            return args[0]
        return composed
        
    def getFoldOperator(self, op_symbol):
        return self.foldOperator.get(op_symbol)

    def addOperator(self, name, funcs, arity):
        composedFunc = self.compose(funcs)
        if arity == 1:
            self.unaryOperators[name] = composedFunc
        elif arity == 2:
            self.binaryOperators[name] = composedFunc
        else:
            raise ValueError("Only unary and binary operators are supported")
        print("addOpetaor", name, composedFunc, arity)
        
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

    def getAllStack(self, name):
        return self.stack[name]

    def isStackEmpty(self, name):
        return name not in self.stack or len(self.stack[name]) == 0
    
    def stackSize(self, name):
        if self.isStackEmpty(name):
            return 0
        return len(self.stack[name]) 

    def callOperator(self, name, parameters):
        func = self.getOperator(name, 1)   
        args = []
        if not self.isStackEmpty(name):
            args.extend(self.getAllStack(name))
        args.extend(parameters)
        print(func, args)

        return func(*args)
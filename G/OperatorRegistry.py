import numpy as np

from gParser import gParser


# TODO delete comments
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

            '*:': lambda x: np.multiply(x, x),
            '+:': lambda x: np.add(x, x),
        }

        self.stack = {}
    
    def compose(self, funcs):
        def composed(*args):
            # print("INICIO composición con argumentos iniciales:", args)
            
            for idx, f in enumerate(funcs):
                arity = f.__code__.co_argcount - len(f.__defaults__ or [])
                # print(f"\n--- Función {idx+1}: {f.__name__} ---", "Aridad esperada:", arity)

                if arity == len(args):
                    reversed_args = tuple(reversed(args))
                    # print("Usando argumentos (revertidos):", reversed_args)
                    result = f(*reversed_args)
                    # print(f"Resultado de {f.__name__}({reversed_args}):", result)
                    args = (result,)
                elif arity < len(args):
                    used_args = args[:arity]
                    remaining_args = args[arity:]
                    reversed_args = tuple(reversed(used_args))
                    # print("Usando argumentos (revertidos):", reversed_args)
                    result = f(*reversed_args)
                    # print(f"Resultado de {f.__name__}({reversed_args}):", result)
                    args = (result,) + remaining_args

                else:
                    raise ValueError(f"Function '{f.__name__}' with arity {arity} cannot handle {len(args)} arguments")

                # print("Argumentos para siguiente función:", args)

            # print("\nFIN composición. Resultado final:", args)
            return args
        return composed

    def getFoldOperator(self, op_symbol):
        return self.foldOperator.get(op_symbol)

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
        # print("addOperator", name, composedFunc, arity)
    
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
        # print(f"PUSH → {parameter} en pila '{name}'")
        self.stack[name].append(parameter)

    def popStack(self, name):
        if name in self.stack and self.stack[name]:
            value = self.stack[name].pop()
            # print(f"POP ← {value} desde pila '{name}'")
            return value
        raise IndexError(f"Pila '{name}' vacía o no existe")

    def popAllStack(self, name):
        while not self.isStackEmpty(name):
            self.popStack(name)

    def getAllStack(self, name):
        if name not in self.stack:
            return []
        # Devuelve una copia invertida (porque es LIFO)
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

import numpy as np

from antlr4  import TerminalNode 
from gParser import gParser
from gVisitor import gVisitor
from utils import debug_visit

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
        
        if operator is None:
            raise ValueError(f"Operator {name} not found")
        
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
        # func = self.visit(ctx.composeOperators()) 
        # TODO addOperator in Operator Registry 
        # 1. creat and lambda combinationg funcion for all the ctx.opertors that are not expr() [ unaryOperators binaryOperators unaryFold] 
        # 2. push parameter in the stack (if ctx.composeOperators.expr())
        funcs = []
        operators = ctx.composeOperators().getChildren()
        for child in operators:
            if isinstance(child, TerminalNode):
                continue
            
            if child.expr():
                if isinstance(child.expr(), gParser.VariableContext):
                    funcs.append(func)

                    self.functions.pushStack(name, self.functions.getAllStack(child.expr().ID().getText()))
                else:
                    self.functions.pushStack(name, self.visit(child.expr()))
            else:
                func = self.visit(child)
                funcs.append(func)

        # funcArity = max(f.__code__.co_argcount for f in funcs)    
        # print(funcArity)
        # operatorArity = funcArity - self.functions.stackSize(name)
      
        self.functions.addOperator(name, funcs, 1)
        
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
            op = self.functions.getFoldOperator(op_symbol)
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
        
        var = self.functions.getOperator(name)
        if var is None:
            var = self.variables[name]
        
        return var
    
    @debug_visit
    def visitUnaryFuncCall(self, ctx):
        name = ctx.ID().getText()
        parameters = [self.visit(ctx.expr())]
        return self.functions.callOperator(name, parameters)

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
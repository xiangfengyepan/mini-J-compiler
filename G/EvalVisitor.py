import numpy as np

from antlr4  import TerminalNode 
from OperatorRegistry import OperatorRegistry
from gParser import gParser
from gVisitor import gVisitor
from utils import debug_visit


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
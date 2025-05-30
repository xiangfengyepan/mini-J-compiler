import numpy as np
from functools import reduce 

from OperatorRegistry import OperatorRegistry
from gParser import gParser
from gVisitor import gVisitor
from utils import debug_visit, normalize_to_list

class EvalVisitor(gVisitor):
    INT_TYPE = np.int32

    def __init__(self):
        super().__init__()
        self.operatorRegistry = OperatorRegistry()
        self.variables = {}
        
    @debug_visit
    def visitProgram(self, ctx):
        return self.visit(ctx.statements())

    @debug_visit
    def visitStatements(self, ctx):
        res = []
        for child in ctx.statement():
            try:
                res.append(self.visit(child))
            except Exception as e:
                res.append(f"error: {str(e)}")
        return res

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
        
        # clear function and stack if it was already declared
        if self.operatorRegistry.getOperator(name, 1) is not None:
            self.operatorRegistry.delOperator(name, 1)

        composedFunction = []
        for child in ctx.composeOperators().getChildren():
            # add composedFunction to Operator when find a "@:" 
            if child.getText() == gParser.literalNames[gParser.COMPOSE].strip("'"):
                self.operatorRegistry.addOperator(name, composedFunction, 1)
                composedFunction = []
                continue

            
            function = self.visit(child) # Case an already declared funcion (unary, binary, fold)

            # An expr (variable or value)
            expr = child.expr()
            if expr:
                stack = self.visit(expr)
                function = None # Case for an expr value

                # Case for VariableContext that is a function 
                if isinstance(expr, gParser.VariableContext):                    
                    var_name = expr.ID().getText()
                    function = self.operatorRegistry.getOperator(var_name)
                    if function is not None:
                        stack = self.operatorRegistry.getAllStack(var_name)
                
                # push stack the value or the stask of the function
                self.operatorRegistry.pushStack(name, stack)
            
            if function is not None:
                composedFunction.extend(normalize_to_list(function))
        
        # For the last composedFunction
        self.operatorRegistry.addOperator(name, composedFunction, 1)
        
    @debug_visit
    def visitBinaryOperators(self, ctx):
        name = ctx.getChild(0).getText()
        binaryOperator = self.operatorRegistry.getOperator(name, 2)

        if ctx.FLIP():
            return lambda lhs, rhs: binaryOperator(rhs, lhs)
        return binaryOperator
      

    @debug_visit
    def visitUnaryOperators(self, ctx):
        name = ctx.getChild(0).getText()
        return self.operatorRegistry.getOperator(name, 1)
   
    @debug_visit
    def visitFoldOperators(self, ctx):
        op_symbol = ctx.getChild(0).getText()
        binaryOperator = self.operatorRegistry.getOperator(op_symbol, 2)
        return lambda x: reduce(binaryOperator, x)

    @debug_visit
    def visitParent(self, ctx):
        return self.visit(ctx.expr())

    @debug_visit
    def visitVariable(self, ctx):
        name = ctx.ID().getText()
        
        var = self.operatorRegistry.getOperator(name)
        if var is None:
            var = self.variables[name]
        
        return var
    
    @debug_visit
    def visitUnaryFuncCall(self, ctx):
        name = ctx.ID().getText()
        parameter = self.visit(ctx.expr())

        self.operatorRegistry.pushStack(name, parameter)
        result = self.operatorRegistry.callOperator(name)
        self.operatorRegistry.popStack(name)
        
        return result
    
    @debug_visit
    def visitList(self, ctx):
        if (len(ctx.intval()) == 1):
            return self.visit(ctx.intval(0))
        return np.array([self.visit(elem) for elem in ctx.intval()], dtype=self.INT_TYPE)

    @debug_visit
    def visitPositive(self, ctx):
        return self.INT_TYPE(ctx.NUM().getText())
        
    @debug_visit
    def visitNegative(self, ctx):
        return -self.INT_TYPE(ctx.NUM().getText())

    @debug_visit
    def visitBinaryAritmetic(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        operator = self.visit(ctx.binaryOperators())
        return operator(lhs, rhs)
    
    @debug_visit
    def visitUnaryAritmetic(self, ctx):
        value = self.visit(ctx.expr())

        operator = self.visit(ctx.unaryOperators())
        return operator(value)

    @debug_visit
    def visitFoldAritmetic(self, ctx):
        value = self.visit(ctx.expr())

        operator = self.visit(ctx.foldOperators())
        return operator(value)
 
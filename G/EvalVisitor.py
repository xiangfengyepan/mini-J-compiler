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
        self.operatorRegistry = OperatorRegistry()
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
        functionList = []

        def normalize_to_list(item):
            return item if isinstance(item, list) else [item]

        for child in ctx.composeOperators().getChildren():
            if isinstance(child, TerminalNode):
                # TODO only add unary operators
                self.operatorRegistry.addOperator(name, functionList, 1)
                functionList = []
                continue

            expr = child.expr()
            if expr:
                if isinstance(expr, gParser.VariableContext):
                    var_name = expr.ID().getText()
                    function = self.operatorRegistry.getOperator(var_name)
                    if function is not None:
                        self.operatorRegistry.pushStack(name, self.operatorRegistry.getAllStack(var_name))
                        functionList.extend(normalize_to_list(function))
                    else:
                        self.operatorRegistry.pushStack(name, self.visit(expr))
                else:
                    self.operatorRegistry.pushStack(name, self.visit(expr))
            else:
                function = self.visit(child)
                functionList.extend(normalize_to_list(function))
        
        # TODO only add unary operators
        self.operatorRegistry.addOperator(name, functionList, 1)
        
    @debug_visit
    def visitBinaryOperators(self, ctx):
        try:
            name = ctx.getChild(0).getText()
            return self.operatorRegistry.getOperator(name, 2)
        except Exception as e:
            return f"error: {str(e)}"

    @debug_visit
    def visitUnaryOperators(self, ctx):
        try:
            name = ctx.getChild(0).getText()
            return self.operatorRegistry.getOperator(name, 1)
        except Exception as e:
            return f"error: {str(e)}"

        
    @debug_visit
    def visitFoldOperators(self, ctx):
        try:
            op_symbol = ctx.getChild(0).getText()
            op = self.operatorRegistry.getFoldOperator(op_symbol)
            myFold = self.operatorRegistry.getOperator(ctx.FOLD().getText(), 2)
    
            return lambda x: myFold(op, x).astype(self.INT_TYPE)
        
        except Exception as e:
            return f"error: {str(e)}"

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
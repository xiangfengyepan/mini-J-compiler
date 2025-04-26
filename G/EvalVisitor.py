import numpy as np

from gVisitor import gVisitor
from gParser import gParser
from utils import debug_visit

class EvalVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}
        self.localVariables = {}
        self.scope = None

        self.functions = {
            "params": [],
            "funcCtx": []
        }

    @debug_visit
    def visitProgram(self, ctx):
        results = []
        for child in ctx.statement():
            result = self.visit(child)
            if not isinstance(child, gParser.DeclarationStmtContext):
                results.append(result)
        return results
        
    @debug_visit
    def visitExprStmt(self, ctx):
        return self.visit(ctx.expr())

    @debug_visit
    def visitDeclarationStmt(self, ctx):
        return self.visit(ctx.declaration())

    @debug_visit
    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expr()):
            for child in ctx.statement(): 
                self.visit(child)
        return
    
    @debug_visit
    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond:
            for child in ctx.statement(): 
                self.visit(child)
        return
    
    @debug_visit
    def visitFuncStmt(self, ctx):
        name = ctx.ID(0).getText()
        params = []
        for param in ctx.ID()[1:]:
            params.append(param.getText())
        funcCtx = ctx.statement()
        self.functions[name] = {
            "params": params,
            "funcCtx": funcCtx
        }
        return
    
    @debug_visit
    def visitFuncCall(self, ctx):
        name = ctx.ID().getText()
        params = self.functions[name]['params']
        funcCtx = self.functions[name]['funcCtx']

        for i, param in enumerate(params):
            if name not in self.localVariables:
                self.localVariables[name] = {}
            self.localVariables[name][param] = self.visit(ctx.expr(i))

        self.scope = name
        for statement in funcCtx:
            value = self.visit(statement)
            if isinstance(statement, gParser.ReturnStmtContext):
                return value
            
        return
    
    @debug_visit
    def visitReturnStmt(self, ctx):
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    @debug_visit
    def visitDeclaration(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value
        return

    @debug_visit
    def visitParent(self, ctx):
        return self.visit(ctx.expr())

    @debug_visit
    def visitVariable(self, ctx):
        name = ctx.ID().getText()
        var = None
        if not self.scope is None:
            if name in self.localVariables[self.scope]:
                var = self.localVariables[self.scope][name]

        if var is None:
            var = self.variables[name]
        return var

    @debug_visit
    def visitRelational(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        if ctx.EQUAL():
            return np.equal(lhs, rhs).astype(np.int32)
        elif ctx.NE():
            return np.not_equal(lhs, rhs).astype(np.int32)
        elif ctx.LT():
            return np.less(lhs, rhs).astype(np.int32)
        elif ctx.GT():
            return np.greater(lhs, rhs).astype(np.int32)
        elif ctx.LE():
            return np.less_equal(lhs, rhs).astype(np.int32)
        elif ctx.GE():
            return np.greater_equal(lhs, rhs).astype(np.int32)

    @debug_visit
    def visitUnary(self, ctx):
        value = self.visit(ctx.expr())
        if ctx.NEG():
            value = -value
        elif ctx.HASH():
            value = np.int32(np.atleast_1d(value).size)
        elif ctx.ARANGE():
            value = np.int32(np.arange(value))

        return value

    @debug_visit
    def visitValue(self, ctx):
        if ctx.INTVAL() and len(ctx.INTVAL()) == 1:
            return np.int32(ctx.INTVAL(0).getText())
        elif ctx.INTVAL() and len(ctx.INTVAL()) > 1:
            return np.array([elem.getText() for elem in ctx.INTVAL()], dtype=np.int32)


    @debug_visit
    def visitAritmetic(self, ctx):
        lhs = self.visit(ctx.expr(0)) if ctx.expr(0) else None
        rhs = self.visit(ctx.expr(1)) if ctx.expr(1) else None

        rhs = lhs if rhs is None else rhs

        if ctx.FLIP():
            aux = lhs
            lhs = rhs
            rhs = aux

        try:
            if ctx.MUL():
                return np.multiply(lhs, rhs)
            elif ctx.DIV():
                return np.floor_divide(lhs, rhs)    # divisio entera
            elif ctx.PLUS():
                return np.add(lhs, rhs)
            elif ctx.MINUS():
                return np.subtract(lhs, rhs)
            elif ctx.POW():
                return np.power(lhs, rhs)
            elif ctx.MOD():
                return np.mod(rhs, lhs)             # els operands van al reves
            elif ctx.CONCATE():
                return np.concatenate((np.atleast_1d(lhs), np.atleast_1d(rhs)))
            elif ctx.HASH():
                return np.array(rhs)[np.array(lhs, dtype=bool)]
            elif ctx.INDEX():
                return np.array(rhs)[np.array(lhs)]

        except Exception as e:
            return f"error: {str(e)}"
    
    @debug_visit
    def visitFold(self, ctx):
        value = self.visit(ctx.expr())
        try:
            if ctx.MUL():
                return np.multiply.reduce(value).astype(np.int32)
            elif ctx.DIV():
                return np.floor_divide.reduce(value).astype(np.int32)    # divisio entera
            elif ctx.PLUS():
                return np.add.reduce(value).astype(np.int32)
            elif ctx.MINUS():
                return np.subtract.reduce(value).astype(np.int32)
            elif ctx.POW():
                return np.power.reduce(value).astype(np.int32)
            elif ctx.MOD():
                return np.mod.reduce(value).astype(np.int32)             # els operands van al reves
            elif ctx.CONCATE():
                return np.array(value)

        except Exception as e:
            return f"error: {str(e)}"
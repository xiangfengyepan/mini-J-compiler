from gVisitor import gVisitor
from gParser import gParser
from utils import debug_visit

class TreeVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self.nivell = 0

    @debug_visit
    def visitIfStmt(self, ctx):
        print('  ' * self.nivell + ctx.IF().getText())
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

    @debug_visit
    def visitWhileStmt(self, ctx):
        print('  ' * self.nivell + ctx.WHILE().getText())
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return
    
    @debug_visit
    def visitMainCall(self, ctx):
        print('  ' * self.nivell + f"main")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return
    
    @debug_visit
    def visitFuncStmt(self, ctx):
        print('  ' * self.nivell + f"function {ctx.ID(0).getText()}({', '.join([param.getText() for param in ctx.ID()[1:]])})")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return
    
    @debug_visit
    def visitFuncCall(self, ctx):
        print('  ' * self.nivell + f"{ctx.ID()}({', '.join([param.getText() for param in ctx.expr()])})")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return
    
    @debug_visit
    def visitReturnStmt(self, ctx):
        print('  ' * self.nivell + f"return {self.visit(ctx.expr()) if ctx.expr() else ''})")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return
    
    @debug_visit
    def visitParent(self, ctx):
        print('  ' * self.nivell + "()")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

    @debug_visit
    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        print('  ' * self.nivell + f"{var_name}")
        return

    @debug_visit
    def visitRelational(self, ctx):
        print('  ' * self.nivell + f"{ctx.op.text}")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

    @debug_visit
    def visitUnary(self, ctx):
        print('  ' * self.nivell + f"{ctx.op.text}")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

    @debug_visit
    def visitValue(self, ctx):
        if ctx.INTVAL() and len(ctx.INTVAL()) == 1:
            print("  " * self.nivell + ctx.INTVAL(0).getText())
        elif ctx.INTVAL() and len(ctx.INTVAL()) > 1:
            values = [elem.getText() for elem in ctx.INTVAL()]
            print("  " * self.nivell + " ".join(values))
        return

    @debug_visit
    def visitAritmetic(self, ctx):
        op = ctx.op.text
        double = ctx.DOUBLE().getText() if ctx.DOUBLE() else ""
        flip = ctx.FLIP().getText() if ctx.FLIP() else ""
        print('  ' * self.nivell + op + double + flip)

        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

    @debug_visit
    def visitFold(self, ctx):
        op = ctx.op.text
        fold = ctx.FOLD().getText()
        print('  ' * self.nivell + op + fold)
        
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

from gVisitor import gVisitor
from gParser import gParser
from utils import debug_visit

class TreeVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self.nivell = 0

    @debug_visit
    def visitParent(self, ctx):
        print('  ' * self.nivell + "()")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

    @debug_visit
    def visitFuncCall(self, ctx):
        func_name = ctx.ID().getText()
        print('  ' * self.nivell + f"{func_name}()")
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
        print('  ' * self.nivell + ctx.op.text)
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

    @debug_visit
    def visitFold(self, ctx):
        print('  ' * self.nivell + f"{ctx.foldop.text}")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return

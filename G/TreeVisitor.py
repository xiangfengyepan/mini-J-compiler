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
    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        print('  ' * self.nivell + f"{var_name}")
        return

    @debug_visit
    def visitUnaryFuncCall(self, ctx):
        name = ctx.ID().getText()
        print('  ' * self.nivell + f"unaryCall: {name}")
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
    def visitBinaryAritmetic(self, ctx):
        print('  ' * self.nivell + f"{" ".join([child.getText() for child in ctx.binaryOperators().getChildren()])}")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return 
    
    @debug_visit
    def visitUnaryAritmetic(self, ctx):
        print('  ' * self.nivell + f"{" ".join([child.getText() for child in ctx.unaryOperators().getChildren()])}")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return 
    
    @debug_visit
    def visitFoldAritmetic(self, ctx):
        print('  ' * self.nivell + f"{" ".join([child.getText() for child in ctx.foldOperators().getChildren()])}")
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        return 
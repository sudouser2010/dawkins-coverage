import ast
import copy


class Coverage():

    def __init__(self, inputCode):

        self.declareASTBodies(inputCode)
        self.declareTrackerVariables()
        self.declareUpdateStatementPrototype()

        self.instrumentEntireASTBody()


    def declareASTBodies(self, inputCode):
        self.originalAST     = ast.parse(inputCode)
        self.originalASTBody = self.originalAST.body


    def declareTrackerVariables(self):
        self.pathSignature  = []
        self.statementId    = 0


    def declareUpdateStatementPrototype(self):
        self.updateStringPrototype   = "self.pathSignature.append(1)"
        self.updateASTPrototype      = ast.parse(self.updateStringPrototype)
        self.updateNodePrototype     = self.updateASTPrototype.body[0]


    def buildInstrumentedASTBody(self, astBody):
        """
            This code loops through a given ast body and
            instruments it.
        """

        instrumentedBody    = []
        for node in astBody:

            if hasattr(node, 'body'):
                node.body = self.buildInstrumentedASTBody(node.body)

            instrumentedBody.append(node)
            localUpdateNode                         = copy.deepcopy(self.updateNodePrototype)
            localUpdateNode.value.args[0].n         = self.statementId
            instrumentedBody.append(localUpdateNode)
            self.statementId += 1

        return instrumentedBody


    def instrumentEntireASTBody(self):
        self.originalASTBody = self.buildInstrumentedASTBody(self.originalASTBody)
        self.originalAST.body= self.originalASTBody


    def runInstrumentedAST(self, testCase={}):

        locals().update(testCase)
        try:
            exec compile(self.originalAST, '', 'exec')
        except Exception, message:
            print "Error Detected : {0}".format(repr(message))


    def getPathSignature(self):
        return self.pathSignature


    def printPathSignature(self):
        print self.pathSignature



inputCode = """
z=2*y
if z==x:
    if x>y+10:
        assert False
"""
testCase = {"x":1, "y":0}

coverage = Coverage(inputCode)
coverage.runInstrumentedAST(testCase)
coverage.printPathSignature()
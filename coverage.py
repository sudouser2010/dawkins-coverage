import ast
import copy


class Coverage():

    def __init__(self, inputCode):

        self.declareASTBodies(inputCode)
        self.declareTrackerVariables()
        self.declareUpdateStatementPrototype()


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


    def runInstrumentedAST(self):
        exec compile(self.originalAST, '', 'exec')


    def getPathSignature(self):
        return self.pathSignature


    def printPathSignature(self):
        print self.pathSignature


class CoverageManager():

    def __init__(self, inputCode):
        self.inputCode = inputCode


    def processCoverage(self):
        coverage = Coverage(self.inputCode)
        coverage.instrumentEntireASTBody()
        coverage.runInstrumentedAST()
        return coverage


inputCode = """
i=0
while i < 5:
    a=1
    b=2
    i+=1
"""


codeCoverage = CoverageManager(inputCode).processCoverage()
codeCoverage.printPathSignature()

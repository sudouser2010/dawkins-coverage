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
        self.modifiedASTBody = []


    def declareTrackerVariables(self):
        self.pathSignature  = {}
        self.statementId    = 0


    def declareUpdateStatementPrototype(self):
        self.updateStringPrototype   = "self.pathSignature[0] += 1"
        self.updateASTPrototype      = ast.parse(self.updateStringPrototype)
        self.updateNodePrototype     = self.updateASTPrototype.body[0]


    def buildInstrumentedASTBody(self):
        for node in self.originalASTBody:
            self.pathSignature[self.statementId] = 0
            self.modifiedASTBody.append(node)
            localUpdateNode = copy.deepcopy(self.updateNodePrototype)
            localUpdateNode.target.slice.value.n = self.statementId
            self.modifiedASTBody.append(localUpdateNode)

            self.statementId += 1

    def replace_OriginalASTBody_With_InstrumentedASTBody(self):
        self.originalAST.body = self.modifiedASTBody


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
        coverage.buildInstrumentedASTBody()
        coverage.replace_OriginalASTBody_With_InstrumentedASTBody()
        coverage.runInstrumentedAST()
        return coverage


inputCode = """
a=1
b=2
c=9
"""

codeCoverage = CoverageManager(inputCode).processCoverage()
codeCoverage.printPathSignature()

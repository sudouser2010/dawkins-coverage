import ast, copy

#does initializations
pathSignature   = {}
statementId     = 0

inputCode = """
a=1
b=2
c=9
"""



originalAST     = ast.parse(inputCode)
originalASTBody = originalAST.body
modifiedASTBody = []

#build update statement prototype
updateStringPrototype   = "pathSignature[7] += 1"
updateASTPrototype      = ast.parse(updateStringPrototype)
updateNodePrototype     = updateASTPrototype.body[0]

#loop does instrumentation
for node in originalASTBody:
    pathSignature[statementId] = 0
    modifiedASTBody.append(node)
    localUpdateNode = copy.deepcopy(updateNodePrototype)
    localUpdateNode.target.slice.value.n = statementId
    modifiedASTBody.append(localUpdateNode)

    statementId += 1

#replaces the original body with the instrumented body
originalAST.body = modifiedASTBody


#runs instrumented code
modifiedCode = compile(originalAST, '', 'exec')
exec modifiedCode

print pathSignature

#need to replace the original body with the modified body
#code should get input from commandline
#a hash is produced for path relative to given input. hashes can be stored


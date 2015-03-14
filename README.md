Dawkins-Coverage
===========

###Basic Program For Determining Code Coverage
    Specifically, it determines if a path is unique.
    You can tell if a path is unique by comparing its pathSignature to the
    pathSignature of another path. 


##Why is it needed
    This is useful in determining if a particular test case
    is redundant or not

##How it works
    (1) Dawkins-Coverage creates:
        (a) an empty dictionary called the pathSignature
        (b) an integer called statementId with an initial value of 0

    (2) Dawkins-Coverage creates an abstract syntax tree (AST) of input code
    (3) Dawkins-Coverage obtains the body of the AST, which is a list, and calls it the originalASTBody
    (4) Dawkins-Coverage creates an empty list and calls it the instrumentedASTBody
    (5) Dawkins-Coverage creates AST code that is designed to increment a specified key in 
        the pathSignature and calls it updateNodePrototype
        example: pathSignature[ specified_key ] += 1

    (6) For each statement in the originalASTBody, Dawkins-Coverage does the following:
        
        (a) creates a key in the pathSignature equal to the current statementId with a value of 0:
            example: pathSignature[statementId] = 0

        (b) appends the statement to the instrumentedASTBody
        (c) increments the statementId
        
    (7) Dawkins-Coverage replaces the originalASTBody with the instrumentedASTBody in the original AST
    (8) When original AST is executed, the update statements will modify the pathSignature. 
    Each program execution path corresponds to a unique pathSignature.

##High Level Design 
    -The idea is that every statement in an input code as a unique identifier represented by the statementId
    -The


*flaw, the code doesn't store order of execution


    



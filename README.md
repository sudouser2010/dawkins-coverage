Dawkins-Coverage
===========

###Basic Program For Determining Code Coverage
    Specifically, it determines if a path is unique.

##How it works
    (1) Dawkins-Coverage creates:
        (a) an empty dictionary called the pathSignature
        (b) a global integer called statementCount with a value of 0

    (2) Dawkins-Coverage creates an abstract syntax tree (AST) of input code
    (3) For each statement in the AST, Dawkins-Coverage does the following:
        (a) sets a local integer called statementId equal to current value of the statementCount
        (a) appends an element in the pathSignature with a key equal to the statementId and a value equal to 0
        (b) increases the statementCount by 1
        (c) appends a statement to the AST after the current statement that:
            (c1) increments the value designated by pathSignature[statementId] by 1
            **I call this statement an update statement.

    (4) When AST is executed, the update statements will modify the pathSignature. 
    Each program execution path corresponds to a unique pathSignature.


    



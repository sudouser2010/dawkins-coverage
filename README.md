Dawkins-Coverage
===========

### Experimental Program For Determining Python Code Coverage
    Specifically, it determines if a path is unique.
    You can tell if an execution path is unique by comparing its pathSignature to the
    pathSignature of another execution path. 


## Why is it needed
    This is useful in determining if a particular test case
    is redundant or not.

## How it works
    (1) Dawkins-Coverage creates:
        (a) an empty list called the pathSignature
        (b) an integer called statementId with an initial value of 0

    (2) Dawkins-Coverage creates an abstract syntax tree (AST) of the input code
    (3) Dawkins-Coverage instruments the AST
    (4) For each statement in the AST, Dawkins-Coverage does the following:
        
        (a) inserts an additional statement that when executed, appends the 
            statementId to the pathSignature
        (b) increments the statementId


## High Level Design 
    -The idea is that every statement in the input code has a unique identifier 
        represented by the statementId
    -When the instrumented code is executed, it appends its statementId to the 
        pathSignature
    -Each program execution path corresponds to a unique pathSignature.


## Limitations
    -Dawkins-Coverage does not work with code that has:
        (a) functions
        (b) classes
    -It is designed to work with only simple Python code
    



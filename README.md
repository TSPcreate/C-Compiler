# Building a C compiler from scratch using Nora Sandler's guide

## Current Implemetation:

- lexer tokenizes the C file
- The tokens are parsed to the parser which creates a basic AST tree in the form of classes
- Code generator(Not the greatest code at the moment) turns AST tree to assembly code



Production Rules currently are:


program ::= function
function ::= "int" id "(" ")" "{" statement "}"
statement ::= "return" exp ";"
exp ::= unary_op exp | int
unary_op ::= "!" | "~" | "-"


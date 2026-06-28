import lexer

'''
Production Rules are:

<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <term> { ("+" | "-") <term> }
<term> ::= <factor> { ("*" | "/") <factor> }
<factor> ::= "(" <exp> ")" | <unary_op> <factor> | <int>

'''
#Expressions defined here
class Const:
    def __init__(self, int):
        self.int = int 

class UnOp:
    def __init__(self, operator, exp):
        self.operator = operator
        self.exp = exp

class BinOp:
    def __init__(self, binary_operator, exp1, exp2):
        self.operator = binary_operator 
        self.exp1 = exp1 
        self.exp2 = exp2

#Statement defined
class Return:
    def __init__(self, exp):
        self.exp = exp
#Function defined
class Fun:
    def __init__(self, id, statement):
        self.statement = statement
        self.id = id
#Program defined
class Prog:
    def __init__(self, fun_decl):
        self.fun_decl = fun_decl

def parse_factor(tokens):
    #<factor> ::= "(" <exp> ")" | <unary_op> <factor> | <int>
    if tokens.pointer.type == "OPEN_PARANTHESIS":
        tokens.advance()
        exp = parse_exp(tokens)
        if tokens.pointer.type == "CLOSE_PARANTHESIS":
            return exp
        else:
            return False 
    elif tokens.pointer.op == "UNOP":
        unop = tokens.tok 
        tokens.advance()
        return UnOp(unop, parse_factor(tokens))
    elif tokens.pointer.type == "INTEGER_LITERAL":
        num = Const(int(tokens.pointer.tok))
        tokens.advance()
        return num
    else:
        return False

    
     

def parse_term(tokens):
    # <term> ::= <factor> { ("*" | "/") <factor> }
    term = parse_factor(tokens)
    next = tokens.peek()
    while next.type == "MULTIPLICATION" or next.type == "DIVISION":
        op = next.tok
        tokens.advance()
        term2 = parse_factor(tokens)
        term = BinOp(op, term, term2)
        next = tokens.peek()
    return term

def parse_exp(tokens):
    # <exp> ::= <term> { ("+" | "-") <term> }

    # 1. Parse the first term as given in the defintion of exp
    # 2. Do a while loop where it continuously parses for the next term when and addition or minus is detected
    term = parse_term(tokens)
    next = tokens.peek()
    while next.type == "ADDITION" or next.type == "MINUS":
        op = next.tok
        tokens.advance()
        term2 = parse_term(tokens)
        term = BinOp(op, term, term2)
        next = tokens.peek()
    return term

def parse_statement(tokens):
    #<statement> ::= "return" <exp> ";"
    if tokens.pointer.type == "RETURN_KEYWORD":
        exp = []
        while tokens.pointer.type != "SEMICOLON" and tokens.pointer.type != "NONE":
            tokens.advance()
            exp.append(tokens.pointer)
        if tokens.pointer == False:
            return False 
        expression = lexer.Tokens(exp)
        parsed_expression = parse_exp(expression)
        if parsed_expression == False:
            return False 
        else:
            statement = Return(parsed_expression)
            return statement



def parse_function(tokens):  
  #<function> ::= "int" <id> "(" ")" "{" <statement> "}"
  if tokens.pointer.type ==  "INT_KEYWORD":
      tokens.advance()
      if tokens.pointer.type == "IDENTIFIER":
          id = tokens.pointer.tok
          tokens.advance()
          if tokens.pointer.type == "OPEN_PARANTHESIS":
              tokens.advance()
              if tokens.pointer.type == "CLOSE_PARANTHESIS":
                  tokens.advance()
                  if tokens.pointer.type == "OPEN_BRACE":
                      list = []
                      while tokens.pointer.type != "CLOSE_BRACE" and tokens.pointer.type != "NONE":
                          tokens.advance()
                          list.append(tokens.pointer)
                      if tokens.pointer.type != "CLOSE_BRACE":
                          return False
                      statement = lexer.Tokens(list)
                      parsed_statement = parse_statement(statement)
                      if parsed_statement is False:
                          return False 
                      else:
                          function = Fun(str(id), parsed_statement)
                          return function

                
                        
def parse_program(tokens):
    func = parse_function(tokens)
    if func is None or func is False:
        return False
    else:
        program = Prog(func)
        return program 



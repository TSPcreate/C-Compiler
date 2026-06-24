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
    def __init__(self, operator, exp):
        self.operator = operator 
        self.exp = exp
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

def factor(tokens):
    return 

def term(tokens):
    return 

def parse_exp(tokens):
    
    if tokens.current_token.op == "UNOP":
        return UnOp(str(tokens.current_token.tok), parse_exp(lexer.Tokens(tokens.list_token[tokens.pointer+1:], 0)))
    elif tokens.current_token.type == "INTEGER_LITERAL":
        return Const(int(tokens.current_token.tok))

def parse_statement(tokens):
    if tokens.current_token.type == "RETURN_KEYWORD":
        exp = []
        while tokens.current_token.type != "SEMICOLON" and tokens.current_token is not False:
            exp.append(tokens.next_token())
        if tokens.current_token == False:
            return False 
        expression = lexer.Tokens(exp, 0)
        parsed_expression = parse_exp(expression)
        if parsed_expression == False:
            return False 
        else:
            statement = Return(parsed_expression)
            return statement



def parse_function(tokens):  
  if tokens.current_token.type ==  "INT_KEYWORD":
      if tokens.next_token().type == "IDENTIFIER":
          id = tokens.current_token.tok
          if tokens.next_token().type == "OPEN_PARANTHESIS":
              if tokens.next_token().type == "CLOSE_PARANTHESIS":
                  if tokens.next_token().type == "OPEN_BRACE":
                      list = []
                      while tokens.current_token.type != "CLOSE_BRACE" and tokens.current_token is not False:
                          tokens.next_token()
                          list.append(tokens.current_token)
                      if tokens.current_token.type != "CLOSE_BRACE":
                          return False
                      statement = lexer.Tokens(list, 0)
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



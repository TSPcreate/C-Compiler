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
    return 

def parse_term(tokens):
    return 

def parse_exp(tokens):
    '''
    if tokens.current_token.op == "UNOP":
        return UnOp(str(tokens.current_token.tok), parse_exp(lexer.Tokens(tokens.list_token[tokens.pointer+1:], 0)))
    elif tokens.current_token.type == "INTEGER_LITERAL":
        return Const(int(tokens.current_token.tok))
    '''
    # Example: 1 + 1 * 2 + 1, should be interpretted is 1 + (1*2) + 1
    # <exp> ::= <term> { ("+" | "-") <term> } needs to parse expression into this
    # Since {} notation means a term + or - another, possibly + - another term infinitely we need to reflect this in our code
    # the 1 + 1*2 + 1 should be interpretted as, term1 + term2 + term3, term1 = 1, term2 = 1 *2, term3 = 1
    # 1. check for the first BINOP operator, and parse whatever is before it as term1
    # 2. check between whatever is between the first BINOP and the second BINOP as term2
    # 3. Create a node, term1 + term2
    # 4. Repeat but this time, check for the next BINOP operator, parse whatever is before it as term3 and add it to the node (.... + ...) + .... +
    # Repeat until the end of the tokens


    contains_BINOP = False
    first_node = True
    current_node = 0
    while tokens.current_token is not False:
        if tokens.current_token.type == "ADDITION" and tokens.current_token.type == "MINUS" and first_node == True:
            contains_BINOP = True
            first_term = lexer.Tokens(tokens.list_token[:tokens.pointer])
            current_node = next_node(tokens, first_term)
        elif tokens.current_token.type == "ADDITION" and tokens.current_token.type == "MINUS" and first_node != True:
            contains_BINOP = True
            current_node = next_node(tokens, current_node)
    if contains_BINOP is False:
        term = parse_term(tokens)
        return term 
    else:
        return current_node

        


#Forms a node by taking in the full tokens, the current_node, checking for the next BINOP operator and then applying the next term to the current term
def next_node(tokens, current_node):
    current_BINOP = tokens.current_token.type  
    term1 = current_node 
    term2 = []
    tokens.next_token()
    while tokens.current_token.type != "ADDITION" and tokens.current_token.type != "MINUS" and tokens.current_token.type is not False:
        term2.append(tokens.current_token)
        tokens.next_token()
    term2 = lexer.Tokens(term2, 0)
    current_node = BinOp(current_BINOP, term1, term2)
    return current_node









            
        
    

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



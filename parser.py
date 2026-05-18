import lexer , generate

tokens = lexer.lex("return_2.c")

'''
Production Rules are:

<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <unary_op> <exp> | <int>
<unary_op> ::= "!" | "~" | "-"

'''
#Expressions defined here
class Const:
    def __init__(self, int):
        self.int = int 

class UnOp:
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

def parse_exp(tokens):
    numbers = '0123456789'
    for i in range(len(tokens)):
        '''if tokens[i] in '0123456789':
            exp = Const(int(tokens[i]))
            return '''
        if tokens[i] in "!-~": #Take !4~3 as an example
            return UnOp(tokens[i], parse_exp(tokens[i+1:]))
        elif tokens[i] in numbers:
            return Const(int(tokens[i]))                
        else:
            return False

def parse_statement(tokens):
    for i in range(len(tokens)):
            if tokens[i] == 'return':
              
              '''  exp = parse_exp(tokens[i+1])
                if exp is False:
                    return False 
                else:
                    if tokens[i+2] == ';':
                        statement = Return(exp)
                        return statement
                    else:
                        return False '''
              semi_colon = False 
              expression = []
              for j in range(i+1, len(tokens)): #Iterates from 'return' to the end of the statement
                  if tokens[j] == ';':
                      semi_colon = True 
                      break 
                  else:
                      expression.append(tokens[j])  #Appends everything until it reaches a semi-colon
                
              if semi_colon == False:
                  return False #No semi-colon found by the end of the iteration, return False
              else:
                  exp = parse_exp(expression) #Parse expression
                  statement = Return(exp)
                  return statement
                  
            return False
    return False

def parse_function(tokens):     
  if 'int' in tokens:
        index = tokens.index("int")
        id = tokens[index+1]
        if tokens[index+2] == "(":
            if ")" in tokens[index+2:]:
                try:
                    index_start = tokens.index("{")
                    index_end = tokens.index("}")
                    sequence= []
                    for i in range(index_start+1, index_end):
                        sequence.append(tokens[i])
                    statement = parse_statement(sequence)
                    if statement is False:
                        return False 
                    Function = Fun(id, statement)
                    return Function
                except ValueError:
                    return False
            else:
                return False 
        else:
            return False 
  else:
    return False 


def parse_program(tokens):
    func = parse_function(tokens)
    if func is False:
        return False
    else:
        program = Prog(func)
        return program


program = parse_program(tokens)
if program == False:
    print("Invalid Program")

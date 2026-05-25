import lexer 

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
        if tokens[i] in "!-~": #Take !4~3 as an example
            if parse_exp(tokens[i+1:]) is False:
                return False 
            else:
                return UnOp(tokens[i], parse_exp(tokens[i+1:]))
        elif tokens[i] in numbers: #Issue in program is here
            if len(tokens) == 1:
                return Const(int(tokens[i]))                
            else:
                return False
        else:
            return False
    return False

def parse_statement(tokens):

    for i in range(len(tokens)):
            if tokens[i] == 'return':
              
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
                  if exp is False: 
                    return False 
                  else:
                    statement = Return(exp)
                    return statement
                  
            return False
    return False

def parse_function(tokens):  #
  #Quite strict as of right now 

  if tokens[0] == "int":
      if tokens[1] == "main":
          if tokens[2] == "(" and tokens[3] == ")":
              if tokens[4] == "{":
                  if "}" in tokens[4:]:
                      end_pos = tokens.index("}")
                      statement = []
                      for i in range(5, end_pos):
                          statement.append(tokens[i])
                      parsed_statement = parse_statement(statement)
                      if parsed_statement is False:
                          return False
                      else:  
                        function = Fun("main", parsed_statement)
                        return function 
                  
                        
def parse_program(tokens):
    func = parse_function(tokens)
    if func is None or func is False:
        return False
    else:
        program = Prog(func)
        return program 

def generate_AST(op):
    if isinstance(op.operator, str):
        AST_Tree.append(op.operator)
        if isinstance(op.exp, Const):
            AST_Tree.append(op.exp.int)
        else:
            return generate_AST(op.exp)

def generate_program(AST_Tree):
    global code
    n = len(AST_Tree) - 1
    if not AST_Tree:
        code += """
        ret"""
        file = open("assembly.s", "w")
        file.write(code)
        return True
    if AST_Tree[n] == "!":
        code += """
        cmpl $0, %eax
        movl $0, %eax 
        sete %al"""
        return generate_program(AST_Tree[:n])
    elif AST_Tree[n] == "-":
        code += """
        neg %eax"""
        return generate_program(AST_Tree[:n])
    elif AST_Tree[n] == "~":
        code += """
        not eax"""
        return generate_program(AST_Tree[:n]) 
    


program = parse_program(tokens)
if program is False:
    print("Invalid Program")
else:
    op = program.fun_decl.statement.exp
    AST_Tree = []
    generate_AST(op)
    id = program.fun_decl.id
    n = len(AST_Tree) - 1
    code = f"""
.global {id}
    {id}:
        movl ${AST_Tree[n]}, %eax"""
    AST_Tree = AST_Tree[:n]
    generate_program(AST_Tree)




class Tokens:
    def __init__(self, list_token, pointer):
        self.list_token = list_token 
        self.pointer = int(pointer)
        self.current_token = list_token[pointer]
    
    def next_token(list_tokens):
        if list_tokens.pointer < len(list_tokens.list_token)-1:
            list_tokens.pointer += 1
            list_tokens.current_token = list_tokens.list_token[list_tokens.pointer]
            return list_tokens.current_token
        else:
            list_tokens.current_token = False



class Token:
    def __init__(self, type, tok, op):
        self.type = type 
        self.tok = tok
        self.op = op

def check_type(token):
    if token == "int":
        token = Token("INT_KEYWORD", "int", None)
    elif token == "return":
        token = Token("RETURN_KEYWORD", token, None)
    elif token.isalpha() is True:
        token = Token("IDENTIFIER", token, None)
    elif token == "-":
        token = Token("MINUS", token, "UNOP")
    elif token == "+":
        token = Token("ADDITION", token, None)
    elif token == "{":
        token = Token("OPEN_BRACE", token, None)
    elif token == "}":
        token = Token("CLOSE_BRACE", token, None)
    elif token == "(":
        token = Token("OPEN_PARANTHESIS", token, None)
    elif token == ")":
        token = Token("CLOSE_PARANTHESIS", token, None)
    elif token == ";":
        token = Token("SEMICOLON", token, None)
    elif token.isdigit() is True:
        token = Token("INTEGER_LITERAL", token, None)
    elif token == "~":
        token = Token("BITWISE_COMPLEMENT", token, "UNOP")
    elif token == "*":
        token = Token("MULTIPLICATION", token, None)
    elif token == "/":
        token = Token("DIVISION", token, None)
    elif token == "!":
        token = Token("LOGICAL_NEGATION", token, "UNOP")
    return token

def lex(filename):
    #accepts a file name
    #returns a list of tokens in the file
    file = open(filename, "r")
    line = file.readline()
    list_tokens = []
    while line != "":
        temp = ""
        for i in range(len(line)):
            if line[i] != ' ' or '':
                if line[i] in ";}{()-!~":
                    if temp != "" and temp != " ":
                        list_tokens.append(check_type(temp))
                        temp = ""
                        list_tokens.append(check_type(line[i]))
                    else:
                        list_tokens.append(check_type(line[i]))
                else:
                    if line[i] == "\n" and temp != "" and temp != " ":
                        list_tokens.append(check_type(temp))
                        temp = ""
                    else:
                        temp = temp + line[i]
            else:
                if temp != "" and temp != " ":
                    list_tokens.append(check_type(temp))
                    temp = ""
        line = file.readline()
    return Tokens(list_tokens, 0)





        

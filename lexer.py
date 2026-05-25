

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
                        list_tokens.append(temp)
                        temp = ""
                        list_tokens.append(line[i])
                    else:
                        list_tokens.append(line[i])
                else:
                    if line[i] == "\n" and temp != "" and temp != " ":
                        list_tokens.append(temp)
                        temp = ""
                    else:
                        temp = temp + line[i]
            else:
                if temp != "" and temp != " ":
                    list_tokens.append(temp)
                    temp = ""
        line = file.readline()
    return list_tokens



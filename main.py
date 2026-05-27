import lexer, parser, generate_code

def Main():
    filename = 'return_2.c'
    tokens = lexer.lex(filename)
    program = parser.parse_program(tokens)
    if program is False:
        print("Invalid Program")
    else:
        op = program.fun_decl.statement.exp
        AST_Tree = []
        generate_code.AST_list(op, AST_Tree)
        id = program.fun_decl.id
        n = len(AST_Tree) - 1
        code = f"""
.global {id}
    {id}:
        movl ${AST_Tree[n]}, %eax"""
        AST_Tree = AST_Tree[:n]
        generate_code.generate_program(AST_Tree, code)



if __name__ == '__main__':
    Main()
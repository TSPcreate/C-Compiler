import parser

def AST_list(op, AST_Tree):
    if isinstance(op.operator, str):
        AST_Tree.append(op.operator)
        if isinstance(op.exp, parser.Const):
            AST_Tree.append(op.exp.int)
        else:
            return AST_list(op.exp, AST_Tree)
        
def generate_program(AST_Tree, code):
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
        return generate_program(AST_Tree[:n], code)
    elif AST_Tree[n] == "-":
        code += """
        neg %eax"""
        return generate_program(AST_Tree[:n], code)
    elif AST_Tree[n] == "~":
        code += """
        not eax"""
        return generate_program(AST_Tree[:n], code) 

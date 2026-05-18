import subprocess

def Generate(program):
    func_id = program.fun_decl.id 
    return_value = program.fun_decl.statement.exp.int
    assembly_code = f"""
        .global {func_id}
       {func_id}:
            movl ${return_value}, %eax 
            ret
         """
    filename = "assembly.s"
    file = open(filename, "w")
    file.write(assembly_code)
    
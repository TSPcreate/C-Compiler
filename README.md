
# C Compiler (Python)

A small compiler prototype for a subset of C, built in Python to learn how source code is translated into machine-level instructions. I started this project while working through Nora Sandler's compiler construction guide and wanted to understand each stage rather than treating compilation as a black box.

## How it works

```text
C source code -> Lexer -> Tokens -> Parser -> Abstract syntax tree -> Code generator -> Assembly
```

- **Lexical analysis (`lexer.py`):** Breaks source code into tokens, including keywords, identifiers, integer literals and a limited set of operators.
- **Parsing (`parser.py`):** Uses a recursive-descent approach to represent a small C function and its return statement as an abstract syntax tree (AST). It includes early support for parsing expressions using grammar rules and operator precedence.
- **Code generation (`generate_code.py`):** Experiments with translating AST nodes into x86-style assembly instructions. This stage is still incomplete, particularly for binary expressions.
- **Entry point (`main.py`):** Connects the stages and currently reads a fixed C input file.

## Running the project

The project uses Python 3 and has no third-party Python dependencies.

```bash
git clone https://github.com/TSPcreate/C-Compiler.git
cd C-Compiler
python main.py
```

The input file is currently set to `return_2.c` in `main.py`. It contains a short C function with an arithmetic return expression.

**Current status:** This is a work-in-progress prototype. The parser and code generator are not yet complete enough to compile that example end to end. Running the script may therefore raise an error rather than generate valid assembly.

## What I've learned

Working on the lexer, grammar rules and AST helped me see how a programming language can be broken down into smaller, well-defined stages. The trickiest part so far has been connecting the structure produced by the parser to the instructions needed by the code generator.

## Next steps

- Complete code generation for arithmetic expressions and unary operators.
- Improve token handling, parser error messages and input validation.
- Add automated tests for each compilation stage.
- Replace the hard-coded input filename with a command-line argument.

**Reference:** Nora Sandler's *Writing a C Compiler* guide.

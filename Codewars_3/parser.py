import ply.yacc as yacc
from ply.lex import LexToken

# ======================
# 1. TOKEN CLASS & INPUT
# ======================

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"

# Leer tokens desde archivo
def read_tokens_from_file(filename):
    tokens = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                token_type, value = parts
                tok = LexToken()
                tok.type = token_type

                try:
                    tok.value = int(value)
                except ValueError:
                    tok.value = value

                tok.lineno = 0
                tok.lexpos = 0
                tokens.append(tok)
    return tokens

# ======================
# 2. FAKE LEXER (a mano)
# ======================

# Simula el comportamiento de ply.lex
class ManualLexer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def token(self):
        if self.index < len(self.tokens):
            tok = self.tokens[self.index]
            self.index += 1
            return tok
        else:
            return None

    def input(self, data):
        pass  # Dummy para que yacc no falle

# ======================
# 3. PARSER (con yacc)
# ======================

tokens = (
    'IDENTIFIER', 'NUMBER', 'ASSIGN', 'PLUS', 'MINUS',
    'MULTIPLY', 'DIVIDE', 'SEMICOLON', 'LPAREN', 'RPAREN'
)

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

# Gramática
def p_statement(p):
    'statement : assignment SEMICOLON'
    p[0] = {
        "type": "Statement",
        "children": [p[1], {"type": "SEMICOLON", "value": ";"}]
    }

def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression'
    p[0] = {
        "type": "Assignment",
        "children": [
            {"type": "IDENTIFIER", "value": p[1]},
            {"type": "ASSIGN", "value": p[2]},
            p[3]
        ]
    }

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = {
        "type": "BinaryOperation",
        "operator": p[2],
        "left": p[1],
        "right": p[3]
    }

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term MULTIPLY factor
            | term DIVIDE factor'''
    p[0] = {
        "type": "BinaryOperation",
        "operator": p[2],
        "left": p[1],
        "right": p[3]
    }

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = {"type": "NUMBER", "value": p[1]}

def p_factor_identifier(p):
    'factor : IDENTIFIER'
    p[0] = {"type": "IDENTIFIER", "value": p[1]}

def p_error(p):
    print(f"Error de sintaxis en {p}")

# ======================
# 4. ÁRBOL FORMATEADO
# ======================

def print_tree(node, indent=0):
    if isinstance(node, dict):
        line = ' ' * indent + node["type"]
        if "value" in node:
            line += f"({node['value']})"
        elif "operator" in node:
            line += f" [{node['operator']}]"
        print(line)
        for key in ("children", "left", "right"):
            if key in node:
                child = node[key]
                if isinstance(child, list):
                    for sub in child:
                        print_tree(sub, indent + 2)
                else:
                    print_tree(child, indent + 2)
    else:
        print(' ' * indent + str(node))

# ======================
# 4.1. IMPRIMIR Y GUARDAR ÁRBOL EN TXT
# ======================

def save_tree_to_file(node, filename):
    lines = []

    def _collect_lines(node, indent=0):
        if isinstance(node, dict):
            line = ' ' * indent + node["type"]
            if "value" in node:
                line += f"({node['value']})"
            elif "operator" in node:
                line += f" [{node['operator']}]"
            lines.append(line)
            for key in ("children", "left", "right"):
                if key in node:
                    child = node[key]
                    if isinstance(child, list):
                        for sub in child:
                            _collect_lines(sub, indent + 2)
                    else:
                        _collect_lines(child, indent + 2)
        else:
            lines.append(' ' * indent + str(node))

    _collect_lines(node)

    # Guardar en archivo
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))

    print(f"\n✅ Árbol sintáctico guardado en: {filename}")

# ======================
# 5. MAIN
# ======================

if __name__ == "__main__":
    token_list = read_tokens_from_file("tokens.txt")    # Leer archivo de tokens
    lexer = ManualLexer(token_list)                     # Simular lexer manual
    parser = yacc.yacc()                                # Crear parser

    result = parser.parse(lexer=lexer, tokenfunc=lexer.token)                  # Ejecutar parser
    print("\nÁrbol sintáctico:")
    print_tree(result)

    # Guardar en archivo
    save_tree_to_file(result, "arbol_sintactico.txt")
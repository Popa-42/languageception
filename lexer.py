import ply.lex as lex

tokens = (
    'STRING',
    'INT',
    'FLOAT',
    'ARRAY',
    'ID',
    'ASSIGN',
    'SEMICOLON',
    'COMMA',
    'LBRACKET',
    'RBRACKET',
    'COMMENT',
)

t_STRING = r'"[^"]*"'
t_INT = r'\bInt\b'
t_FLOAT = r'\bFloat\b'
t_ARRAY = r'\bArray\b'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Ignore whitespace
T_ignore = ' \t'


def t_COMMENT(t):
    r'\#\#\#.*?\#\#\#'
    pass  # Comments are ignored


# Rule to recognize variable assignments
def t_VARIABLE_ASSIGNMENT(t):
    r'\b(Int|Float|String)\b\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*((("[^"]*")|\d+(_\d+)*(\.\d+)?)\s*)\;'
    t.value = t.value.replace(";", "").replace("_", "").strip()
    t.type = 'ID'
    return t


# Rule to recognize array definitions
def t_ARRAY_DEFINITION(t):
    r'\b(Array)\b\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*\[\s*([a-zA-Z0-9_."]+\s*(,\s*[a-zA-Z0-9_."]+\s*)*)?\s*\]\s*;'
    print(t.value)
    t.value = t.value.replace("Array", "").replace("=", "").replace("[", "").replace("]", "").replace(";", "").replace("\n", "").replace("\t", "").strip()
    t.type = 'ARRAY'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()

text = '''
String text = "Dies ist ein Text.";
Int zahl = 42;
Int grossezahl = 100_000_000;
Float nochnezahl = 420.69;
Array liste = [
    1, 2, 3.141,
    "hallo",
    zahl, nochnezahl
];

# Einzelner Kommentar
###
Block-
Kommentar
###

# Simple Mathematik
Int zahl1 = 1;
'''

lexer.input(text)

while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

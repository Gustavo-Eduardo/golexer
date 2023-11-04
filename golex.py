import ply.lex as lex

# List of token names.

tokens = (
    # Gustavo
    'L_SQ_BRACKET',
    'R_SQ_BRACKET',
    'DOT',
    'COMMA',
    'COLON',
    'SEMI_COLON',
    'ASSIGN',
    'SHORT_ASSIGN',
    'CONSTANT',
    'VARIABLE',
    'IF',
    'ELSE',
    'FUNCTION',
    'RETURN',
    'FOR',
    'CONTINUE',
    'SWITCH',
    'BREAK',
    'CASE',
)

# Regular expression rules for simple tokens

# Gustavo
t_L_SQ_BRACKET = r'\['
t_R_SQ_BRACKET = r']'
t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'
t_SEMI_COLON = r';'
t_ASSIGN = r'='
t_SHORT_ASSIGN = r':='
t_CONSTANT = r'const'
t_VARIABLE = r'var'
t_IF = r'if'
t_ELSE = r'else'
t_FUNCTION = r'func'
t_RETURN = r'return'
t_FOR = r'for'
t_CONTINUE = r'continue'
t_SWITCH = r'switch'
t_BREAK = r'break'
t_CASE = r'case'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Input tests
data = ''' 
 const a = 32
'''

lexer.input(data)

#Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


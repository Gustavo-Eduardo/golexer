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

     #Guido
    'SLASH',
    'INIT_COMMENT',
    'END_COMMENT',
    'PLUS',
    'MINUS',
    'DOUBLE_SLASH',
    'PERCENT',
    'OP_AND',
    'OP_NEGATIVE',
    'NOT_EQUAL',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'L_PARENTHESIS',
    'R_PARENTHESIS',
    'L_BRACKET',
    'R_BRACKET',
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

#Guido Flores
t_SLASH = r'/'
t_INIT_COMMENT = r'/[*]'
t_END_COMMENT = r'[*]/'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DOUBLE_SLASH = r'//'
t_PERCENT = r'%'
t_OP_AND = r'&&'
t_OP_NEGATIVE = r'!'
t_NOT_EQUAL = r'!='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_L_BRACKET = r'{'
t_R_BRACKET = r'}'

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
#Guido
lexer2 = lex.lex()

# Input tests
data = ''' 
 const a = 32
'''
#Guido Flores
data2 = '''
    //comentario
    /*Texto*/
    /Texto2

    for i in range(0,12):
        if (i <= 5){
            i = i + 7
            }
        if (i >= 6){
            i = i - 2
            }
        if (i != 0){
            i = i % 2
        }
        if(i < 1 && i > 0){
            i = 0
        }         
''' 

lexer.input(data)
#Guido Flores
lexer2.input(data2)

#Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

#Guido
while True:
    tok2 = lexer2.token()
    if not tok2:
        break
    print(tok2)    



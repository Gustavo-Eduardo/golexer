
import ply.lex as lex


reservadas = {
  'if' : 'IF',
  'println' : 'PRINTLN',
  'printf' : 'PRINTF',
  'scan' : 'SCAN',
  'scanln' : 'SCANLN',
  'scanf' : 'SCANF',
  'else' : 'ELSE',
  'for' : 'FOR',
  'true' : 'TRUE',
  'false' : 'FALSE',
  'const':'CONSTANT',
  'var':'VARIABLE',
  'func':'FUNCTION',
  'return':'RETURN',
  'continue':'CONTINUE',
  'switch':'SWITCH',
  'break':'BREAK',
  'case':'CASE',
  'uint8':'UINT8',
  'uint16':'UINT16',
  'uint32':'UINT32',
  'uint64':'UINT64',
  'int8':'INT8',
  'int16':'INT16',
  'int32':'INT32',
  'int64':'INT64',
  'float32':'FLOAT32',
  'float64':'FLOAT64',
  'complex64':'COMPLEX64',
  'complex128':'COMPLEX128',
  'bool':'BOOL',
  'string':'STRING',
  'struct':'STRUCT',
}
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
     #Guido
    'SLASH',
    'INIT_COMMENT',
    'END_COMMENT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DOUBLE_SLASH',
    'PERCENT',
    'OP_AND',
    'OP_OR',
    'OP_NEGATIVE',
    'NOT_EQUAL',
    'EQUAL',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'L_PARENTHESIS',
    'R_PARENTHESIS',
    'L_BRACKET',
    'R_BRACKET',
    'NUMBER',
    'QUOTE',
    'FLOAT',
    'STR',

    # Gabriel    
    'IDENTIFICADOR',
    'AMPERSAND',
)+tuple(reservadas.values())

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
#Guido Flores
t_SLASH = r'/'
t_INIT_COMMENT = r'/[*]'
t_END_COMMENT = r'[*]/'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DOUBLE_SLASH = r'//'
t_PERCENT = r'%'
t_OP_AND = r'&&'
t_OP_OR = r'[|][|]'
t_OP_NEGATIVE = r'!'
t_NOT_EQUAL = r'!='
t_EQUAL = r'=='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_L_BRACKET = r'{'
t_R_BRACKET = r'}'
t_NUMBER = r'[0-9]+'
t_QUOTE = r'"'
t_FLOAT = r'[0-9]+[.][0.9]+'
t_AMPERSAND = r'&'

def t_IDENTIFICADOR(t):
  r'[a-zA-Z_]\w*'
  t.type = reservadas.get(t.value, 'IDENTIFICADOR')
  return t

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
# Gabriel
lexer3 = lex.lex()

# Input tests
data = ''' 
 const a = 32
'''
#Guido Flores
data2 = '''
    func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}
''' 

# Gabriel Castro
data3 = '''
    uint8 a = 32 
    uint16 b = 32
    uint32 c = 32
    uint64 d = 32
    int8 a = 32
    int16 b = 32
    int32 c = 32
    int64 d = 32
    float32 a = 32
    float64 b = 32
    complex64 a = 32
    complex128 b = 32
    bool a = true
    bool b = false
    string a = "texto"
    string b = "texto2"
    struct s1 {
    uint8 a = 32
    uint16 b = 32
    uint32 c = 32
    uint64 d = 32
    }
    '''

lexer.input(data)
#Guido Flores
lexer2.input(data2)
#Gabriel Castro
lexer3.input(data3)

'''
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

#Gabriel
while True:
    tok3 = lexer3.token()
    if not tok3:
        break
    print(tok3)
'''

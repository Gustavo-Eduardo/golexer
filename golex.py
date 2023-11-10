import ply.lex as lex


reservadas = {
  'if' : 'IF',
  'println' : 'PRINTLN',
  'printf' : 'PRINTF',
  'else' : 'ELSE',
  'for' : 'FOR',
  'True' : 'TRUE',
  'False' : 'FALSE',
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
    'TIMES',
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
    'NUMBER',
    'QUOTE',
    'PRINTLN',
    'PRINTF',
    'FLOAT',
    'STR',

    # Gabriel
    'UINT8',
    'UINT16',
    'UINT32',
    'UINT64',
    'INT8',
    'INT16',
    'INT32',
    'INT64',
    'FLOAT32',
    'FLOAT64',
    'COMPLEX64',
    'COMPLEX128',
    'BOOL',
    'STRING',
    'TRUE',
    'FALSE',
    'STRUCT',
    'IDENTIFICADOR' 
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
t_TIMES = r'\*'
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
t_NUMBER = r'[0-9]+'
t_QUOTE = r'"'
t_PRINTLN = r'println'
t_PRINTF = r'printf'
t_FLOAT = r'[0-9]+[.][0.9]+'

# Gabriel
t_UINT8 = r'uint8'
t_UINT16 = r'uint16'
t_UINT32 = r'uint32'
t_UINT64 = r'uint64'
t_INT8 = r'int8'
t_INT16 = r'int16'
t_INT32 = r'int32'
t_INT64 = r'int64'
t_FLOAT32 = r'float32'
t_FLOAT64 = r'float64'
t_COMPLEX64 = r'complex64'
t_COMPLEX128 = r'complex128'
t_BOOL = r'bool'
t_STRING = r'string'
t_TRUE = r'true'
t_FALSE = r'false'
t_STRUCT = r'struct'

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
    //comentario
    /*Texto*/
    /Texto2

    for i in range(0,12):
        if (i <= 5){
            i = i + 7
            }
        if (i >= 6){
            i = i - 2 * 4
            }
        if (i != 0){
            i = i % 2
        }
        if(i < 1 && i > 0){
            i = 0
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


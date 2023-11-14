import ply.yacc as yacc
from golex import tokens

def p_program(p):
  '''program : statement_list
  '''

def p_statement_list(p):
  '''statement_list : statement 
              | statement statement_list
  '''

def p_statement(p):
  '''statement : print
                | declaration
                | function_declaration
                | input
  '''

#Guido Flores

def p_print(p):
  '''print : printer L_PARENTHESIS valor R_PARENTHESIS 
  '''

def p_valor(p):
  '''valor : NUMBER 
            | IDENTIFICADOR 
            | FLOAT
            | bool
            | str
  '''
def p_string(p):
  '''str : QUOTE IDENTIFICADOR QUOTE
  '''

def p_bool(p):
  '''bool : TRUE
          | FALSE
  '''
  
def p_printer(p):
  '''printer : PRINTLN
              | PRINTF
  '''
  
# Gustavo Lopez

def p_identifier_list(p):
  '''identifier_list : IDENTIFICADOR
  | IDENTIFICADOR COMMA identifier_list
  '''

def p_values_list(p):
  '''values_list : valor
  | valor COMMA values_list
  '''

def p_type(p):
  '''type : UINT8
  | UINT16
  | UINT32
  | UINT64
  | INT8
  | INT16
  | INT32
  | INT64
  | FLOAT32
  | FLOAT64
  | COMPLEX64
  | COMPLEX128
  | BOOL
  | STRING 
  | STRUCT 
  '''

def p_constant_declaration(p):
  '''constant_declaration : CONSTANT identifier_list type ASSIGN values_list
  | CONSTANT identifier_list ASSIGN values_list
  '''

def p_variable_declaration(p):
  '''variable_declaration : VARIABLE identifier_list type ASSIGN values_list
  | VARIABLE identifier_list ASSIGN values_list
  | VARIABLE identifier_list type
  | VARIABLE identifier_list
  '''

def p_short_variable_declaration(p):
  '''short_variable_declaration : identifier_list SHORT_ASSIGN values_list
  | identifier_list type SHORT_ASSIGN values_list
  '''

def p_struct_declaration(p):
  '''struct_declaration : STRUCT L_BRACKET R_BRACKET
                        | STRUCT L_BRACKET field_declaration R_BRACKET
  '''

def p_field_declaration(p):
  '''field_declaration : identifier_list type
                       | identifier_list type str
  '''

def p_declaration(p):
  '''declaration : constant_declaration
  | variable_declaration
  | short_variable_declaration
  | struct_declaration
  '''

def p_parameter(p):
  '''parameter : IDENTIFICADOR type
  | IDENTIFICADOR
  '''

def p_parameter_list(p):
  '''parameter_list : parameter
  | parameter COMMA parameter_list
  '''

def p_function_declaration(p):
  '''function_declaration : FUNCTION IDENTIFICADOR L_PARENTHESIS parameter_list R_PARENTHESIS L_BRACKET statement_list R_BRACKET
  '''

def p_input(p):
  '''input : SCAN L_PARENTHESIS mem_address R_PARENTHESIS
           | SCANLN L_PARENTHESIS mem_address_list R_PARENTHESIS
           | SCANF L_PARENTHESIS str COMMA mem_address_list R_PARENTHESIS
  '''

def p_mem_address(p):
  '''mem_address : AMPERSAND IDENTIFICADOR
  '''

def p_mem_address_list(p):
  '''mem_address_list : mem_address
                      | mem_adress COMMA mem_adress_list
  '''

def p_error(p):
  if p:
    print("Syntax error at token", p)
  else:
    print("Syntax error at EOF")

parser = yacc.yacc()


while True:
   try:
       s = input('esp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if result != None:
    print(result)

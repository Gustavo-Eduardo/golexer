import ply.yacc as yacc
from lexico import tokens

def p_program(p):
  '''program : statement 
              | statement program
  
  '''

def p_statement(p):
  '''statement : print
                | assignment
  '''

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
  
def p_assigment(p):
  '''assignment : IDENTIFICADOR ASSIGN valor
  '''
  

def p_error(p):
  print("Error sintáctico")

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

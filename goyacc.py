import ply.yacc as yacc
from golex import tokens

def p_program(p):
  '''program : statement_list
              | operation
              | conditional_statement
  '''
  p[0] = "No errors found"

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
def p_str(p):
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


def p_arithmetic_operator_both(p):
  '''arithmetic_operator_both : PLUS
                              | MINUS
                              | TIMES
                              | SLASH
  '''

def p_float_value(p):
  '''float_value : NUMBER DOT NUMBER
  '''

def p_arithmetic_value(p):
  '''arithmetic_value : NUMBER
                      | float_value
  '''

def p_operation_sum_numbers(p):
  '''operation_sum_numbers : arithmetic_value PLUS arithmetic_value 
                            | arithmetic_value PLUS operation_sum_numbers
  '''

def p_operation_sum_str(p):
  '''operation_sum_str : str PLUS str 
                        | str PLUS operation_sum_str
  '''

def p_operation_minus(p):
  '''operation_minus : arithmetic_value MINUS arithmetic_value 
                      | arithmetic_value MINUS operation_minus
  '''  

def p_operation_multi(p):
  '''operation_multi : arithmetic_value TIMES arithmetic_value 
                      | arithmetic_value TIMES operation_multi
  '''

def p_operation_div(p):
  '''operation_div : arithmetic_value SLASH arithmetic_value 
                    | arithmetic_value SLASH operation_div
  '''  

def p_operation_percent(p):
  '''operation_percent : NUMBER PERCENT NUMBER 
                        | NUMBER PERCENT operation_percent 
  '''  

'''
def p_operand(p):
    operand : valor
  '''


def p_number_operation(p):
  '''number_operation : operation_sum_numbers
                      | operation_minus
                      | operation_multi
                      | operation_div
                      | operation_sum_str                      
                      | arithmetic_value arithmetic_operator_both number_operation
                      | number_operation arithmetic_operator_both arithmetic_value
  '''
def p_operation(p):
  '''operation : number_operation 
                | operation_percent
  '''


def p_conditional_statement(p):
  '''conditional_statement : conditional condition
                            | conditional united_condition
  '''

def p_conditional(p):
  '''conditional : IF
  '''

def p_op_conditional(p):
  '''op_conditional : NOT_EQUAL
                    | LESS_THAN
                    | GREATER_THAN
                    | LESS_EQUAL
                    | GREATER_EQUAL
                    | EQUAL
  '''

def p_condition(p):
  '''condition : IDENTIFICADOR op_conditional IDENTIFICADOR
                | IDENTIFICADOR op_conditional valor
                | valor op_conditional IDENTIFICADOR
                | valor op_conditional valor
  '''

def p_conector(p):
  '''conector : OP_AND
              | OP_OR
  '''
  
def p_united_condition(p):
  '''united_condition : condition conector condition 
                      | united_condition conector condition
                      | united_condition conector united_condition
                      | condition conector united_condition
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
                      | mem_address COMMA mem_address_list
  '''

#Funcion para detección de errores
def p_error(p):
  if p:
    raise Exception("Syntax error at token" + p.value)
    return "Syntax error at token" + " " + p.value
  else:
    raise Exception("Syntax error at EOF")

parser = yacc.yacc()


# # Funcion para analizar el codigo desde la API
# def analize(code: str):
#   result = parser.parse(code)
#   if result != None:
#     return result

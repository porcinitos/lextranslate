tablaDeErrores  = ""
tablaDeSimbolos = ""

def guardarError(t,tipo):
  global tablaDeErrores
  tablaDeErrores += ":: "+tipo+"('%s',%s,%s)\n" % (t.value, t.lineno,     t.lexpos)

def lista_a_regex(lista):
  expresion = ''
  for elemento in lista: expresion = expresion + elemento + '|'
  expresion = expresion[0:-1]
  return expresion

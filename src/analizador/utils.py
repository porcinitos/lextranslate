tablaErrores  = ""
tablaSimbolos = ""

def guardarError(t,tipo):
  global tablaErrores
  tablaErrores += tipo +"('%s',%s,%s)\n" % (t.value, t.lineno, t.lexpos)

def guardarToken(t):
  global tablaSimbolos
  tablaSimbolos += "Simbolo (%s,%s)\n" % (t.type,t.value)

def guardarDOF():
  global tablaErrores
  tablaErrores += "No existente"

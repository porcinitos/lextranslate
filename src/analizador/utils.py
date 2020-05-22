tablaErrores  = ""
tablaSimbolos = ""

def guardarError(t,tipo):
  global tablaErrores
  tablaErrores += tipo+"('%s',%s,%s)\n" % (t.value, t.lineno,     t.lexpos)

def guardarToken(t):
  global tablaSimbolos
  tablaSimbolos += "Simbolo (%s,%s,%s)\n" % (id,t.type,t.value)


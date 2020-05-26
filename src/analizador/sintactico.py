from lexer import tokens
import utils as U

import ply.yacc as yacc

def p_Programa(p):
    '''
    Programa : Oraciones
    '''

def p_Oraciones(p):
    '''
    Oraciones : Oracion
              | Oraciones Oracion
    '''

def p_Oracion(p):
    '''
    Oracion : PresenteSimple
            | PresenteParticipio
    '''

def p_PresenteSimple(p):
    '''
    PresenteSimple : PresenteSimpleStruct Sustantivo Signo_Punto
                   | PresenteSimpleStruct Signo_Punto
                   | PresenteSimpleStruct Preposicion VerboPresentePrimeraPersona AdverbioLugar Articulos Sustantivo Signo_Punto
                   | PresenteSimpleStruct Preposicion VerboPresentePrimeraPersona Sustantivo Signo_Punto
    '''
def p_PresenteSimpleStruct(p):
    '''
    PresenteSimpleStruct : PronombrePrimeraPersona VerboPresentePrimeraPersona
                         | PronombreTerceraPersona VerboPresenteTerceraPersona
                         | Sustantivo VerboPresenteTerceraPersona
                         | AdjetivosSujeto Sustantivo VerboPresenteTerceraPersona
    '''

def p_PresenteParticipio(p):
    '''
    PresenteParticipio : VerboPresenteParticipio Sustantivo Signo_Punto
    '''

def p_PasadoParticipio(p):
    '''
    PasadoParticipio :
    '''

def p_FuturoParticipio(p):
    '''
    FuturoParticipio :
    '''

def p_PresenteAdmirativo(p):
    '''
    PresenteAdmirativo :
    '''


def p_PresenteInterrogativo(p):
    '''
    PresenteInterrogativo :
    '''


def p_Articulos(p):
    '''
    Articulos : ArticuloDefinido
              | ArticuloIndefinido
    '''

def p_AdjetivosSujeto(p):
    '''
    AdjetivosSujeto : AdjetivoPosesivo
                    | AdjetivoDemostrativo
                    | AdjetivoNumeralCardinal
    '''

def p_Empty(p):
    '''
    Empty :
    '''
    pass

def p_error(p):
  if (p): U.guardarError(p,"Error Sintactico")
  else: U.guardarDOF()

def parsear(texto):
    parser = yacc.yacc()
    parser.parse(texto, tracking=False)


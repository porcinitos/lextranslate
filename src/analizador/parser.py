from lexer import *
import utils as U

def p_Programa(p):
    '''
    Programa: Oraciones
    '''

def p_Oraciones(p):
    '''
    Oraciones: Oracion
             | Oraciones Oracion
    '''

def p_Oracion(p):
    '''
    Oracion: PresenteSimple
           | PresenteParticipio
           | PasadoParticipio
           | FuturoParticipio
           | Dubitativa
           | Admirativa
    '''

def p_PresenteSimple(p):
    '''
    PresenteSimple: Sujeto VerboPresenteSimple sustantivo signo_punto
    '''

def p_PresenteParticipio(p):
    '''
    PresenteParticipio: Sujeto VerboPresenteParticipio sustantivo signo_punto


    '''

def p_Sujeto(p):
    '''
    Sujeto: Pronombres
          | Sustantivo
          | AdjetivosSujeto Sustantivo

    '''

def p_Pronombres(p):
    '''
    Pronombres: PronombresPersonales
              | PronombreDemostrativo
              | PronombreDemostrativo
              | PronombreInterrogativo
              | PronombreObjeto
              | PronombrePosesivo

    '''

def p_Articulos(p):
    '''
    Articulos: ArticuloDefinido
             | ArticuloIndefinido
    '''

def p_AdjetivosSujeto(p):
    '''
    AdjetivosSujeto: AdjetivoPosesivo
                   | AdjetivoDemostrativo
                   | AdjetivoNumeralCardinal
    '''

def p_Empty(p):
    '''
    Empty
    '''
    pass

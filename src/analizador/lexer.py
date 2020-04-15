import ply.lex as lex 
import re 
import codecs
import os
import sys 
import utils as U




PronombresPersonales = ['I','you','we','they','she','he']  

AdjetivoDemostrativo = ['this','that','these','those']

PronombreObjeto = ['me','you','him','her','it','us','them']

PronombrePosesivo = ['mine', 'yours', 'his', 'hers', 'ours', 'theirs']

PronombreInterrogativo = ['what', 'where', 'who', 'why', 'when', 'how', 'much', 'many', 'whose']

VerboToBe = ['am','is','are']

AdjetivoPosesivo = ['my', 'your' ,'his' ,'her' ,'its' ,'our', 'their']

AdjetivoCalificativo = ['absent','minded','adventurous','affectionate','artistic','athletic','attractive','big',
'boring','cautious','stingy','crazy','curious','fat','funny','generous','handsome','honest','impatient','intelligent','interesting',
'friendly','lazy','mean','nice','organized','clubbable','patient','polite','popular','famed','pop','pretty','serious','short','shy',
'sincere','skinny','small','strange','strict','tall','thin','ugly','unorganized','worker','brave','dirty','confident','ecstatic',
'energetic','afraid','ambitious','arrogant','ashamed','bad','cantankerous','careful','careless','conceited','confused','coward','cruel',
'disappointed','disciplined','distressed','drunk','envious','quick','fast','flirtatious','good','gullible','healthy','jealous','lonely','Modest',
'naughty','old','pessimistic','poor','possesive','practical','proud','rich','sad','sane','sick','slow','sober','strong','stubborn',
'stupid','sympathetic','trustworthy','weak','worried','young']

AdjetivoIndefinido = ['bad','worse','worst','ill','badly','far',' farther','farthest','further','furthest','better','best','well','late',
'later','latest','little','less','least','many','more','most','much','some']

ArticuloIndefinido = ['a','an']

PronombreDemostrativo = ['such','none']

AdverbioCantidad = ['almost','enough','entirely','even','failry','hardly','lots','less','much','partially','pretty','rather','quite','scarcely','so','too','very','way']

AdjetivodeModo = ['slow','easy','simple','careful','natural','happy','clear','hard']

AdverbiodeAfirmacion = ['certainly','clearly','indeed','naturally','obviously','surely','yes','definitely','obviously','really','truly','undoubtedly']

AdverbiodeNegacion = ['no','not','never','nowhere']

AdverbiodeDuda = ['probably','maybe','perhaps','likely']

PreposiciondeLugar = ['above','across','along','around','against','at','behind','below','beneath','by','in','inside','near','on','upon','opposite','outside','over','round','under','underneath']

PreposiciondeTiempo = ['about','after','around','during','for','over','past','since','to','until','within']

PreposiciondeMovimiento = ['across','after','along','around','by','down','into','past','off','onto','to','from','toward','under','up']

ConjugacionCoordinante = ['and','but','however','so','or','then','therefore','yet']

ConjugacionSubordinantes = ['although','as','after','before','if','since','until']

Interjeccion = ['wow','yuck','ouch','uh','oops','hey','yeah','eh']

Simbolos = {
        "," : "Signo_Coma " ,
        "." : "Signo_Punto " ,
        ":" : "Signo_dos_puntos " ,
        ";" : "Signo_puntoycoma " ,
        "'" : "Signo_comilla_simple " ,
        "´" : "Signo_apostrofe " ,
        "(" : "Signo_parentecis_abierto " ,
        ")" : "Signo_parentecis_cerrado " ,
        "!" : "Signo_exclamacion_cerredo " ,
        "¡" : "Signo_exclamacion_abierto " ,
        "¿" : "Signo_interrogacion_abierto " ,
        "?" : "Signo_interrogacion_cerrado " ,
        "/" : "Signo_Diagonal"
        '"' : "Signo_comillas"

        }

Tokens = ['PronombresPersonales','AdjetivoDemostrativo','PronombreObjeto','PronombrePosesivo','PronombreInterrogativo',
'VerboToBe','AdjetivoPosesivo','AdjetivoCalificativo','AdjetivoIndefinido','ArticuloIndefinido','PronombreDemostrativo',
'AdverbioCantidad','AdjetivodeModo','AdverbiodeAfirmacion','AdverbiodeNegacion','AdverbiodeDuda','PreposiciondeLugar',
'PreposiciondeTiempo','ConjugacionCoordinante','PreposiciondeMovimiento','ConjugacionSubordinantes','Interjeccion','Apostrofe',
'SignoInterrogacionA','SignoInterrogacionC','SignoExclamacionA','SignoExclamacionA','coma','punto','dospuntos','puntoycoma','Comillas', 'ParentesisA',
'ParentesisC'] +[*Simbolos.values()]


def t_Sujeto(t):
     '''
     [a-zA-z]+
     ''' 
     if (t.value in PronombresPersonales): t.type = "PronombresPersonales" 
     return t

def t_Simbolos(t):
  '''
  
  ''' 
  if (t.value in [*Simbolos.keys()]): t.type = Simbolos[t.value]
  else: t_error(t)
        

t_Apostrofe = r'´'
t_SignoInterrogacionA = r'¿'
t_SignoInterrogacionC = r'?'
t_SignoExclamacionA = r'¡'
t_SignoExclamacionC = r'!'
t_coma = r','
t_punto = r'.'
t_dospuntos = r':'
t_puntoycoma = r';'
t_Comillas = r'"'
t_ParentesisA = r'('
t_ParentesisC = r')'

def t_error(t):
    print("Error lexico '%s' " % t.value[0])

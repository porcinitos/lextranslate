import ply.lex as lex
import utils as U

Sustantivos = []

AdjetivoPosesivo = ['my', 'your' ,'his' ,'her' ,'its' ,'our', 'their']

AdjetivoDemostrativo = ['this','that','these','those']

AdjetivoCalificativo = ['absent','minded','adventurous','affectionate','artistic','athletic','attractive','big',
'boring','cautious','stingy','crazy','curious','fat','funny','generous','handsome','honest','impatient','intelligent','interesting',
'friendly','lazy','mean','nice','organized','clubbable','patient','polite','popular','famed','pop','pretty','serious','short','shy',
'sincere','skinny','small','strange','strict','tall','thin','ugly','unorganized','worker','brave','dirty','confident','ecstatic',
'energetic','afraid','ambitious','arrogant','ashamed','bad','cantankerous','careful','careless','conceited','confused','coward','cruel',
'disappointed','disciplined','distressed','drunk','envious','quick','fast','flirtatious','good','gullible','healthy','jealous','lonely','Modest',
'naughty','old','pessimistic','poor','possesive','practical','proud','rich','sad','sane','sick','slow','sober','strong','stubborn',
'stupid','sympathetic','trustworthy','weak','worried','young']

AdjetivoNumeralCardinal = []

AdjetivoNumeralOrdinal = []

AdjetivoIndefinido = ['bad','worse','worst','ill','badly','far',' farther','farthest','further','furthest','better','best','well','late',
'later','latest','little','less','least','many','more','most','much','some']

ArticuloDefinido = []

ArticuloIndefinido = ['a','an']

PronombresPersonales = ['I','you','we','they','she','he']

PronombresNumerales= []

PronombreDemostrativo = ['such','none']

PronombreInterrogativo = ['what', 'where', 'who', 'why', 'when', 'how', 'much', 'many', 'whose']

PronombreObjeto = ['me','you','him','her','it','us','them']

PronombrePosesivo = ['mine', 'yours', 'his', 'hers', 'ours', 'theirs']

VerboToBe = ['am','is','are']

AdverbioTiempo = []

AdverbioLugar= []

AdverbioCantidad = ['almost','enough','entirely','even','failry','hardly','lots','less','much','partially','pretty','rather','quite','scarcely','so','too','very','way']

AdverbioModo= []

AdverbioAfirmacion = ['certainly','clearly','indeed','naturally','obviously','surely','yes','definitely','obviously','really','truly','undoubtedly']

AdverbioNegacion = ['no','not','never','nowhere']

AdverbioDuda = ['probably','maybe','perhaps','likely']

AdverbioModo= ['slow','easy','simple','careful','natural','happy','clear','hard']

PreposicionTiempo = ['about','after','around','during','for','over','past','since','to','until','within']

PreposicionMovimiento = ['across','after','along','around','by','down','into','past','off','onto','to','from','toward','under','up']

ConjugacionCoordinante = ['and','but','however','so','or','then','therefore','yet']

ConjugacionSubordinantes = ['although','as','after','before','if','since','until']

Interjeccion = ['wow','yuck','ouch','uh','oops','hey','yeah','eh']

Contracciones = []

Simbolos = {
        "," : "Signo_Coma" ,
        "." : "Signo_Punto" ,
        ":" : "Signo_dos_puntos" ,
        ";" : "Signo_puntoycoma" ,
        "'" : "Signo_comilla_simple" ,
        "´" : "Signo_apostrofe" ,
        "(" : "Signo_parentecis_abierto" ,
        ")" : "Signo_parentecis_cerrado" ,
        "!" : "Signo_exclamacion_cerredo" ,
        "¡" : "Signo_exclamacion_abierto" ,
        "¿" : "Signo_interrogacion_abierto" ,
        "?" : "Signo_interrogacion_cerrado" ,
        "/" : "Signo_Diagonal",
        '{' : "Signo_Abrir_Llave",
        '}' : "Signo_Cerrar_Llave",
        '-' : "Signo_guion",
        '_' : "Signo_guion_bajo",
        }

tokens = ['Sujeto','PronombresPersonales','AdjetivoDemostrativo','PronombreObjeto','PronombrePosesivo','PronombreInterrogativo',
'VerboToBe','AdjetivoPosesivo','AdjetivoCalificativo','AdjetivoIndefinido','ArticuloDefinido','ArticuloIndefinido','PronombreDemostrativo',
'AdverbioCantidad','AdjetivodeModo','AdverbiodeAfirmacion','AdverbiodeNegacion','AdverbiodeDuda','PreposiciondeLugar',
'PreposiciondeTiempo','ConjugacionCoordinante','PreposiciondeMovimiento','ConjugacionSubordinantes','Interjeccion'] +[*Simbolos.values()]


def t_Sujeto(t):
  '''
  [a-zA-z]+
  '''
  if (t.value in PronombresPersonales): t.type = "PronombresPersonales"
  elif (t.value in AdjetivoDemostrativo): t.type = "AdjetivoDemostrativo"
  elif (t.value in PronombreObjeto): t.type = "PronombreObjeto"
  elif (t.value in PronombrePosesivo): t.type = "PronombrePosesivo"
  elif (t.value in PronombreInterrogativo): t.type = "PronombreInterrogativo"
  elif (t.value in VerboToBe): t.type = "VerboToBe"
  elif (t.value in AdjetivoPosesivo): t.type = "AdjetivoPosesivo"
  elif (t.value in AdjetivoCalificativo): t.type = "AdjetivoCalificativo"
  elif (t.value in AdjetivoIndefinido): t.type = "AdjetivoIndefinido"
  elif (t.value in ArticuloIndefinido): t.type = "ArticuloIndefinido"
  elif (t.value in PronombreDemostrativo): t.type = "PronombreDemostrativo"
  elif (t.value in AdverbioCantidad): t.type = "AdverbioCantidad"
  elif (t.value in AdjetivodeModo): t.type = "AdjetivodeModo"
  elif (t.value in AdverbioAfirmacion): t.type = "AdverbiodeAfirmacion"
  elif (t.value in AdverbioNegacion): t.type = "AdverbiodeNegacion"
  elif (t.value in AdverbioDuda): t.type = "AdverbiodeDuda"
  elif (t.value in PreposiciondeLugar): t.type = "PreposiciondeLugar"
  elif (t.value in PreposiciondeTiempo): t.type = "PreposiciondeTiempo"
  elif (t.value in ConjugacionCoordinante): t.type = "ConjugacionCoordinante"
  elif (t.value in PreposiciondeMovimiento): t.type = "PreposiciondeMovimiento"
  elif (t.value in ConjugacionSubordinantes): t.type = "ConjugacionSubordinantes"
  elif (t.value in Interjeccion): t.type = "Interjeccion"
  return t


def t_Simbolos(t):
  '''
  [.|,|\|!|¡|¿|?|&|;|:|{|}|-|_|(|)|…|'|´]
  '''
  if (t.value in [*Simbolos.keys()]): t.type = Simbolos[t.value]
  return t

t_ignore  = " \t"

def t_error(t):
    print("Error lexico '%s' " % t.value[0])


def scan(txt):
  analizer = lex.lex()
  analizer.input(txt)
  while True:
    tok = analizer.token()
    if not tok : break
    print(":: %s \n" % tok)

scan("this is my favorite game")

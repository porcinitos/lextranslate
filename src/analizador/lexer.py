import ply.lex as lex 
import re 
import codecs
import os
import sys 

u = utils()

Tokens = ['PronombresPerasonales','AdjetivoDemostrativo','PronombreObjeto','PronombrePosesivo','PronombreInterrogativo',
'VerboToBe','AdjetivoPosesivo','AdjetivoCalificativo','AdjetivoIndefinido','ArticuloIndefinido','PronombreDemostrativo',
'AdverbioCantidad','AdjetivodeModo','AdverbiodeAfirmacion','AdverbiodeNegacion','AdverbiodeDuda','PreposiciondeLugar',
'PreposiciondeTiempo','ConjugacionCoordinante','PreposiciondeMovimiento','ConjugacionSubordinantes','Interjeccion','Apostrofe',
'SignoInterrogacionA','SignoInterrogacionC','SignoExclamacionA','SignoExclamacionA','coma','punto','dospuntos','puntoycoma','Comillas', 'ParentesisA',
'ParentesisC']


PronombresPersonales = ['I','You','We','They','She','He']  

AdjetivoDemostrativo = ['this','that','these','those']

PronombreObjeto = ['me','you','him','her','it','us','them']

PronombrePosesivo = ['mine', 'yours', 'his', 'hers', 'ours', 'theirs']

PronombreInterrogativo = ['what', 'where', 'who', 'why', 'when', 'how', 'much', 'many', 'whose']

VerboToBe = ['am','is','are']

AdjetivoPosesivo = ['my', 'your' ,'his' ,'her' ,'its' ,'our', 'their']

AdjetivoCalificativo = ['Absent','minded','Adventurous','Affectionate','Artistic','Athletic','Attractive','Big',
'Boring','Cautious','Stingy','Crazy','Curious','Fat','Funny','Generous','Handsome','Honest','Impatient','Intelligent','Interesting',
'Friendly','Lazy','Mean','Nice','Organized','Clubbable','Patient','Polite','Popular','famed','Pop','Pretty','Serious','Short','Shy',
'Sincere','Skinny','Small','Strange','Strict','Tall','Thin','Ugly','Unorganized','Worker','Brave','Dirty','Confident','Ecstatic',
'Energetic','Afraid','Ambitious','Arrogant','Ashamed','Bad','Cantankerous','Careful','Careless','Conceited','Confused','Coward','Cruel',
'Disappointed','Disciplined','Distressed','Drunk','Envious','quick','Fast','Flirtatious','Good','Gullible','Healthy','Jealous','Lonely','Modest',
'Naughty','Old','Pessimistic','Poor','Possesive','Practical','Proud','Rich','Sad','Sane','Sick','Slow','Sober','Strong','Stubborn',
'Stupid','Sympathetic','Trustworthy','Weak','Worried','Young']

AdjetivoIndefinido = ['Bad','worse','worst','ill','Badly','far',' farther','farthest','further','furthest','better','best','well','late',
'later','latest','little','less','least','many','more','most','much','some']

ArticuloIndefinido = ['a','an']

PronombreDemostrativo = ['such','none']

AdverbioCantidad = ['Almost','Enough','Entirely','Even','Failry','Hardly','Lots','Less','Much','Partially','Pretty','Rather','Quite','Scarcely','So','Too','Very','Way']

AdjetivodeModo = ['Slow','Easy','Simple','Careful','Natural','Happy','Clear','Hard']

AdverbiodeAfirmacion = ['certainly','clearly','indeed','naturally','obviously','surely','yes','definitely','obviously','really','truly','Undoubtedly']

AdverbiodeNegacion = ['no','not','never','nowhere']

AdverbiodeDuda = ['probably','maybe','perhaps','likely']

PreposiciondeLugar = ['above','across','along','around','against','at','behind','below','beneath','by','in','inside','near','on','upon','opposite','outside','over','round','under','underneath']

PreposiciondeTiempo = ['about','after','around','during','for','over','past','since','to','until','within']

PreposiciondeMovimiento = ['across','after','along','around','by','down','into','past','off','onto','to','from','toward','under','up']

ConjugacionCoordinante = ['And','But','however','so','or','then','therefore','yet']

ConjugacionSubordinantes = ['Although','As','After','Before','If','Since','Until']

Interjeccion = ['wow','yuck','ouch','uh','oops','hey','yeah','eh']


u.lista_a_regex(PronombresPersonales)
u.lista_a_regex(AdjetivoDemostrativo)
u.lista_a_regex(PronombreObjeto)
u.lista_a_regex(PronombrePosesivo)
u.lista_a_regex(PronombreInterrogativo)
u.lista_a_regex(VerboToBe)
u.lista_a_regex(AdjetivoPosesivo)
u.lista_a_regex(AdjetivoCalificativo)
u.lista_a_regex(AdjetivoIndefinido)
u.lista_a_regex(ArticuloIndefinido)
u.lista_a_regex(PronombreDemostrativo)
u.lista_a_regex(AdverbioCantidad)
u.lista_a_regex(AdjetivodeModo)
u.lista_a_regex(AdverbiodeAfirmacion)
u.lista_a_regex(AdverbiodeNegacion)
u.lista_a_regex(AdverbiodeDuda)
u.lista_a_regex(PreposiciondeLugar)
u.lista_a_regex(PreposiciondeTiempo)
u.lista_a_regex(PreposiciondeMovimiento)
u.lista_a_regex(ConjugacionCoordinante)
u.lista_a_regex(ConjugacionSubordinantes)
u.lista_a_regex(Interjeccion)

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
    print "Error lexico '%s' " % t.value[0]
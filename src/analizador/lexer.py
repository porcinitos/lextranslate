import ply.lex as lex
import utils as U

AdjetivoPosesivo = ['my', 'your' ,'his' ,'her' ,'its' ,'our', 'their']

AdjetivoDemostrativo = ['this','that','these','those']

AdjetivoCalificativo = ['absent','minded','adventurous','affectionate','artistic','athletic','attractive','big',
'boring','cautious','stingy','crazy','curious','fat','funny','generous','handsome','honest','impatient','intelligent','interesting',
'friendly','lazy','mean','nice','organized','clubbable','patient','polite','popular','famed','pop','pretty','serious','short','shy',
'sincere','skinny','small','strange','strict','tall','thin','ugly','unorganized','worker','brave','dirty','confident','ecstatic',
'energetic','afraid','ambitious','arrogant','ashamed','bad','cantankerous','careful','careless','conceited','confused','coward','cruel',
'disappointed','disciplined','distressed','drunk','envious','quick','fast','flirtatious','good','gullible','healthy','jealous','lonely','Modest','naughty','old','pessimistic','poor','possesive','practical','proud','rich','sad','sane','sick','slow','sober','strong','stubborn',
'stupid','sympathetic','trustworthy','weak','worried','young']

AdjetivoNumeralCardinal = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty-one","twenty-two","twenty-three","twenty-four","twenty-five","twenty-six","twenty-seven","twenty-eight","twenty-nine","thirty","thirty-one","thirty-two","thirty-three","thirty-four","thirty-five","thirty-six","thirty-seven","thirty-eight","thirty-nine","forty","forty-one","forty-two","forty-three","forty-four","forty-five","forty-six","forty-seven","forty-eight","forty-nine","fifty","fifty-one","fifty-two","fifty-three","fifty-four","fifty-five","fifty-six","fifty-seven","fifty-eight","fifty-nine","sixty","sixty-one","sixty-two","sixty-three","sixty-four","sixty-five","sixty-six","sixty-seven","sixty-eight","sixty-nine","seventy","seventy-one","seventy-two","seventy-three","seventy-four","seventy-five","seventy-six","seventy-seven","seventy-eight","seventy-nine","eighty","eighty-one","eighty-two","eighty-three","eighty-four","eighty-five","eighty-six","eighty-seven","eighty-eight","eighty-nine","ninety","ninety-one","ninety-two","ninety-three","ninety-four","ninety-five","ninety-six","ninety-seven","ninety-eight","ninety-nine","one","hundred"]

AdjetivoNumeralOrdinal = ["first","seconds","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth","thirteenth","fourteenth","fifteenth","sixteenth","seventeenth","eighteenth","nineteenth","twentieth","twentyninth","thirtieth","thirtyfirst","thirtysecond","thirtythird","thirtyfourth","thirtyfifth","thirtysixth","thirtyseventh","thirtyeighth","thirtyninth","fortieth","fortyfirst","fortysecond","fortythird","fortyfourth","fortyfifth","fortysixth","fortyseventh","fortyeighth","fortyninth","fiftieth","fiftyfirst","fiftysecond","fiftythird","fiftyfourth","fiftyfifth","fiftysixth","fiftyseventh","fiftyeighth","fiftyninth","sixtieth","sixtyfirst","sixtysecond","sixtythird","sixtyfourth","sixtyfifth","sixtysixth","sixtyseventh","sixtyeighth","sixtyninth","seventieth","seventyfirst","seventysecond","seventythird","seventyfourth","seventyfifth","seventysixth","seventyseventh","seventyeighth","seventyninth","eightieth","eightyfirst","eightysecond","eightythird","eightyfourth","eightyfifth","eightysixth","eightyseventh","eightyeighth","eightyninth","ninetieth","ninetyfirst","ninetysecond","ninetythird","ninetyfourth","ninetyfifth","ninetysixth","ninetyseventh","ninetyeighth","ninetyninth","hundredth"]

AdjetivoIndefinido = ['bad','worse','worst','ill','badly','far',' farther','farthest','further','furthest','better','best','well','late',
'later','latest','little','less','least','many','more','most','much','some']

ArticuloDefinido = ["the"]

ArticuloIndefinido = ['a','an']

PronombresPersonales = ['i','you','we','they','she','he']

PronombreDemostrativo = ['such','none']

PronombreInterrogativo = ['what', 'where', 'who', 'why', 'when', 'how', 'much', 'many', 'whose']

PronombreObjeto = ['me','you','him','her','it','us','them']

PronombrePosesivo = ['mine', 'yours', 'his', 'hers', 'ours', 'theirs']

VerboToBe = ['am','is','are']

VerboPresente = ["like","answer","arrive","ask","be ","borrow","break ","buy ","catch ","clean","climb","collect","come ","compose","cook","cut ","dance","describe","discover","do ","drink ","drive ","eat ","enjoy","fall ","feel ","find ","fly ","forget ","give ","go ","happen","have ","help","hurt ","invent","invite","kill","know ","lend","leave ","lie ","like","live","look","love","make ","meet","miss","open","pack","pay ","phone","play","prefer","prepare","push","put ","rain","read ","remember","rent","rescue","return","ring ","save","say ","search","see ","sell ","sit ","skate","ski","sleep ","smell","speak","spend ","start","stay","stop","study","survive","swim ","take ","talk","teach","tell","think","throw","touch","try","understand","use","visit","wait","walk","want","wash","watch","wear ","work","write"]

VerboPresenteParticipio = ["liking","answering","arriving","asking","been","borrowing","breaking","buying","catching","cleaning","climbing","collecting","comeing","composeing","cooking","cuting","dancing","describing","discovering","doing","drinking","driving","eating","enjoying","falling","feeling","finding","flying","forgetting","giving","going","happening","having","helping","hurting","inventing","inviteing","killing","knowing","lending","leaveing","lying","liking","living","looking","loving","making","meeting","missing","opening","packing","paying","phoning","playing","prefering","preparing","pushing","puting","raining","reading","remembering","renting","rescuing","returning","ringing","saving","saying","searching","seeing","selling","sitting","skating","skiing","sleeping","smelling","speaking","spending","starting","staying","stoping","studying","surviveing","swimming","taking","talking","teaching","telling","thinking","throwing","touching","trying","understanding","using","visiting","waiting","walking","wanting","washing","watching","wearing","working","writeing"]

VerboPasado = ["liked","answered","arrived","asked","was","were","borrowed","broke","bought","caught","cleaned","climbed","collected","came","composed","cooked","cut","danced","described","discovered","did","drank","drove","ate","enjoyed","fell","felt","found","flew","forgot","gave","went","happened","had","helped","hurt","invented","invited","killed","knew","lent","left","lay","liked","lived","looked","loved","made","met","missed","opened","packed","paid","phoned","played","preferred","prepared","pushed","put","rained","read","remembered","rented","rescued","returned","rang","saved","said","searched","saw","sold","sat","skated","skied","slept","smelled","spoke","spent","started","stayed","stopped","studied","survived","swam","took","talked","taught","told","thought","threw","touched","tried","understood","used","visited","waited","walked","wanted","washed","watched","wore","worked","wrote"]

VerboPasadoParticipio = ["been","broken","come","done","drunk","driven","eaten","fallen","flown","fallen","flown","gone","known","lain","rung","seen","spoken","swum","taken","thrown","worn","written"]

AdverbioTiempo = ["currently","next","normally","now","meanwhile","never","last","night","eternally","occasionally","previously","finally","later","before","frequently","formerly","today","soon","regularly","initially","on","time","still","immediately","just","yesterday","instantly","recently","constantly","never","always","simultaneously","then","simultaneously","when","tomorrow","afternoon","While","early","after","momentarily","already"]

AdverbioLugar= ["through","here","where","bottom","up","in","back","here","above","out","low","","front","there","close","between","edge","next","there","away","there","below","around","behind","about"]

AdverbioCantidad = ['almost','enough','entirely','even','failry','hardly','lots','less','much','partially','pretty','rather','quite','scarcely','so','too','very','way']

AdverbioModo= ['slow','easy','simple','careful','natural','happy','clear','hard']

AdverbioAfirmacion = ['certainly','clearly','indeed','naturally','obviously','surely','yes','definitely','obviously','really','truly','undoubtedly']

AdverbioNegacion = ['no','not','never','nowhere']

AdverbioDuda = ['probably','maybe','perhaps','likely']

Preposicion = ["to","before","low","fits","with","against","of","since","in","between","toward","until","for","by","according","without","on","after"]

ConjuncionCoordinante = ['and','but','however','so','or','then','therefore','yet']

ConjuncionSubordinantes = ['although','as','after','before','if','since','until', 'because','though','whereas','while','nevertheless','only','whether']

Interjeccion = ['wow','yuck','ouch','uh','oops','hey','yeah','eh']

Contraccion = ["aight","ain't","amn't","aren't","can't","'cause","could've","couldn't","couldn't've","daren't","daresn't","dasn't","didn't","doesn't","don't","d'ye","e'er","everybody's","everyone's","finna","g'day","gimme","giv'n","gonna","gon't","gotta","hadn't","had've","hasn't","haven't","he'd","he'dn't've'd","he'll","he's","he've","how'd","howdy","how'll","how're","how's","I'd","I'd've","I'll","I'm","I'm'a","I'm'o","innit","I've","isn't","it'd","it'll","it's","let's","ma'am","mayn't","may've","methinks","mightn't","might've","mustn't","mustn't've","must've","needn't","ne'er","o'clock","o'er","ol'","oughtn't","'s","shalln't","shan't","she'd","she'll","she's","should've","shouldn't","shouldn't've","somebody's","someone's","something's","so're","that'll","that're","that's","that'd","there'd","there'll","there're","there's","these're","these've","they'd","they'll","they're","they've","this's","those're","those've","'tis","to've","'twas","wanna","wasn't","we'd","we'd've","we'll","we're","we've","weren't","what'd","what'll","what're","what's","what've","when's","where'd","where'll","where're","where's","where've","which'd","which'll","which're","which's","which've","who'd","who'd've","who'll","who're","who's","who've","why'd","why're","why's","willn't","won't","wonnot","would've","wouldn't","wouldn't've","y'all","y'all'd've","y'all'dn't've'd","y'all're","you'd","you'll","you're","you've","noun's"]

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

tokens = ['Sustantivo','AdjetivoPosesivo','AdjetivoDemostrativo','AdjetivoCalificativo','AdjetivoNumeralCardinal','AdjetivoNumeralOrdinal','AdjetivoIndefinido','ArticuloDefinido','ArticuloIndefinido','PronombresPersonales','PronombreDemostrativo','PronombreInterrogativo','PronombrePosesivo','PronombreObjeto','VerboToBe', 'VerboPresente', 'VerboPresenteParticipio', 'VerboPasado', 'VerboPasadoParticipio','AdverbioTiempo','AdverbioLugar','AdverbioCantidad','AdverbioModo','AdverbioAfirmacion','AdverbioNegacion','AdverbioDuda','Preposicion', 'ConjuncionCoordinante','ConjuncionSubordinantes','Interjeccion','Contraccion'] +[*Simbolos.values()]


def t_Sustantivo(t):
  '''
  [a-zA-z]+
  '''
  t.value = t.value.lower()
  if   (t.value in AdjetivoPosesivo): t.type = "AdjetivoPosesivo"
  elif (t.value in AdjetivoDemostrativo): t.type = "AdjetivoDemostrativo"
  elif (t.value in AdjetivoCalificativo): t.type = "AdjetivoCalificativo"
  elif (t.value in AdjetivoNumeralCardinal): t.type = "AdjetivoNumeralCardinal"
  elif (t.value in AdjetivoNumeralOrdinal): t.type = "AdjetivoNumeralOrdinal"
  elif (t.value in AdjetivoIndefinido): t.type = "AdjetivoIndefinido"
  elif (t.value in ArticuloDefinido): t.type = "ArticuloDefinido"
  elif (t.value in ArticuloIndefinido): t.type = "ArticuloIndefinido"
  elif (t.value in PronombresPersonales): t.type = "PronombresPersonales"
  elif (t.value in PronombreDemostrativo): t.type = "PronombreDemostrativo"
  elif (t.value in PronombreInterrogativo): t.type = "PronombreInterrogativo"
  elif (t.value in PronombreObjeto): t.type = "PronombreObjeto"
  elif (t.value in PronombrePosesivo): t.type = "PronombrePosesivo"
  elif (t.value in VerboToBe): t.type = "VerboToBe"
  elif (t.value in VerboPresente): t.type = "VerboPresente"
  elif (t.value in VerboPresenteParticipio): t.type = "VerboPresenteParticipio"
  elif (t.value in VerboPasado): t.type = "VerboPasado"
  elif (t.value in VerboPasadoParticipio): t.type = "VerboPasadoParticipio"
  elif (t.value in AdverbioTiempo): t.type = "AdverbioTiempo"
  elif (t.value in AdverbioLugar): t.type = "AdverbioLugar"
  elif (t.value in AdverbioCantidad): t.type = "AdverbioCantidad"
  elif (t.value in AdverbioModo): t.type = "AdverbioModo"
  elif (t.value in AdverbioAfirmacion): t.type = "AdverbioAfirmacion"
  elif (t.value in AdverbioNegacion): t.type = "AdverbioNegacion"
  elif (t.value in AdverbioDuda): t.type = "AdverbioDuda"
  elif (t.value in Preposicion): t.type = "Preposicion"
  elif (t.value in ConjuncionCoordinante): t.type = "ConjuncionCoordinante"
  elif (t.value in ConjuncionSubordinantes): t.type = "ConjuncionSubordinantes"
  elif (t.value in Preposicion): t.type = "Preposicion"
  elif (t.value in Interjeccion): t.type = "Interjeccion"
  elif (t.value in Contraccion): t.type = "Contraccion"
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

scan("I like to play with my girlfriend")

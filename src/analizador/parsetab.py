
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AdjetivoCalificativo AdjetivoDemostrativo AdjetivoIndefinido AdjetivoNumeralCardinal AdjetivoNumeralOrdinal AdjetivoPosesivo AdverbioAfirmacion AdverbioCantidad AdverbioDuda AdverbioLugar AdverbioModo AdverbioNegacion AdverbioTiempo ArticuloDefinido ArticuloIndefinido ConjuncionCoordinante ConjuncionSubordinantes Contraccion Interjeccion Preposicion PronombreDemostrativo PronombreInterrogativo PronombreObjeto PronombrePosesivo PronombrePrimeraPersona PronombreTerceraPersona Signo_Abrir_Llave Signo_Cerrar_Llave Signo_Coma Signo_Diagonal Signo_Punto Signo_apostrofe Signo_comilla_simple Signo_dos_puntos Signo_exclamacion_abierto Signo_exclamacion_cerredo Signo_guion Signo_guion_bajo Signo_interrogacion_abierto Signo_interrogacion_cerrado Signo_parentecis_abierto Signo_parentecis_cerrado Signo_puntoycoma Sustantivo VerboPasado VerboPasadoParticipio VerboPresenteParticipio VerboPresentePrimeraPersona VerboPresenteTerceraPersona VerboToBe\n    Programa : Oraciones\n    \n    Oraciones : Oracion\n              | Oraciones Oracion\n    \n    Oracion : PresenteSimple\n            | PresenteParticipio\n    \n    PresenteSimple : PresenteSimpleStruct Sustantivo Signo_Punto\n                   | PresenteSimpleStruct Signo_Punto\n                   | PresenteSimpleStruct Preposicion VerboPresentePrimeraPersona AdverbioLugar Articulos Sustantivo Signo_Punto\n                   | PresenteSimpleStruct Preposicion VerboPresentePrimeraPersona Sustantivo Signo_Punto\n    \n    PresenteSimpleStruct : PronombrePrimeraPersona VerboPresentePrimeraPersona\n                         | PronombreTerceraPersona VerboPresenteTerceraPersona\n                         | Sustantivo VerboPresenteTerceraPersona\n                         | AdjetivosSujeto Sustantivo VerboPresenteTerceraPersona\n    \n    PresenteParticipio : VerboPresenteParticipio Sustantivo Signo_Punto\n    \n    PasadoParticipio :\n    \n    FuturoParticipio :\n    \n    PresenteAdmirativo :\n    \n    PresenteInterrogativo :\n    \n    Articulos : ArticuloDefinido\n              | ArticuloIndefinido\n    \n    AdjetivosSujeto : AdjetivoPosesivo\n                    | AdjetivoDemostrativo\n                    | AdjetivoNumeralCardinal\n    \n    Empty :\n    '
    
_lr_action_items = {'VerboPresenteParticipio':([0,2,3,4,5,15,17,24,26,33,35,],[8,8,-2,-4,-5,-3,-7,-6,-14,-9,-8,]),'PronombrePrimeraPersona':([0,2,3,4,5,15,17,24,26,33,35,],[9,9,-2,-4,-5,-3,-7,-6,-14,-9,-8,]),'PronombreTerceraPersona':([0,2,3,4,5,15,17,24,26,33,35,],[10,10,-2,-4,-5,-3,-7,-6,-14,-9,-8,]),'Sustantivo':([0,2,3,4,5,6,8,11,12,13,14,15,17,19,21,22,24,25,26,27,30,31,32,33,35,],[7,7,-2,-4,-5,16,20,23,-21,-22,-23,-3,-7,-12,-10,-11,-6,29,-14,-13,34,-19,-20,-9,-8,]),'AdjetivoPosesivo':([0,2,3,4,5,15,17,24,26,33,35,],[12,12,-2,-4,-5,-3,-7,-6,-14,-9,-8,]),'AdjetivoDemostrativo':([0,2,3,4,5,15,17,24,26,33,35,],[13,13,-2,-4,-5,-3,-7,-6,-14,-9,-8,]),'AdjetivoNumeralCardinal':([0,2,3,4,5,15,17,24,26,33,35,],[14,14,-2,-4,-5,-3,-7,-6,-14,-9,-8,]),'$end':([1,2,3,4,5,15,17,24,26,33,35,],[0,-1,-2,-4,-5,-3,-7,-6,-14,-9,-8,]),'Signo_Punto':([6,16,19,20,21,22,27,29,34,],[17,24,-12,26,-10,-11,-13,33,35,]),'Preposicion':([6,19,21,22,27,],[18,-12,-10,-11,-13,]),'VerboPresenteTerceraPersona':([7,10,23,],[19,22,27,]),'VerboPresentePrimeraPersona':([9,18,],[21,25,]),'AdverbioLugar':([25,],[28,]),'ArticuloDefinido':([28,],[31,]),'ArticuloIndefinido':([28,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Oraciones':([0,],[2,]),'Oracion':([0,2,],[3,15,]),'PresenteSimple':([0,2,],[4,4,]),'PresenteParticipio':([0,2,],[5,5,]),'PresenteSimpleStruct':([0,2,],[6,6,]),'AdjetivosSujeto':([0,2,],[11,11,]),'Articulos':([28,],[30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Oraciones','Programa',1,'p_Programa','sintactico.py',8),
  ('Oraciones -> Oracion','Oraciones',1,'p_Oraciones','sintactico.py',13),
  ('Oraciones -> Oraciones Oracion','Oraciones',2,'p_Oraciones','sintactico.py',14),
  ('Oracion -> PresenteSimple','Oracion',1,'p_Oracion','sintactico.py',19),
  ('Oracion -> PresenteParticipio','Oracion',1,'p_Oracion','sintactico.py',20),
  ('PresenteSimple -> PresenteSimpleStruct Sustantivo Signo_Punto','PresenteSimple',3,'p_PresenteSimple','sintactico.py',25),
  ('PresenteSimple -> PresenteSimpleStruct Signo_Punto','PresenteSimple',2,'p_PresenteSimple','sintactico.py',26),
  ('PresenteSimple -> PresenteSimpleStruct Preposicion VerboPresentePrimeraPersona AdverbioLugar Articulos Sustantivo Signo_Punto','PresenteSimple',7,'p_PresenteSimple','sintactico.py',27),
  ('PresenteSimple -> PresenteSimpleStruct Preposicion VerboPresentePrimeraPersona Sustantivo Signo_Punto','PresenteSimple',5,'p_PresenteSimple','sintactico.py',28),
  ('PresenteSimpleStruct -> PronombrePrimeraPersona VerboPresentePrimeraPersona','PresenteSimpleStruct',2,'p_PresenteSimpleStruct','sintactico.py',32),
  ('PresenteSimpleStruct -> PronombreTerceraPersona VerboPresenteTerceraPersona','PresenteSimpleStruct',2,'p_PresenteSimpleStruct','sintactico.py',33),
  ('PresenteSimpleStruct -> Sustantivo VerboPresenteTerceraPersona','PresenteSimpleStruct',2,'p_PresenteSimpleStruct','sintactico.py',34),
  ('PresenteSimpleStruct -> AdjetivosSujeto Sustantivo VerboPresenteTerceraPersona','PresenteSimpleStruct',3,'p_PresenteSimpleStruct','sintactico.py',35),
  ('PresenteParticipio -> VerboPresenteParticipio Sustantivo Signo_Punto','PresenteParticipio',3,'p_PresenteParticipio','sintactico.py',40),
  ('PasadoParticipio -> <empty>','PasadoParticipio',0,'p_PasadoParticipio','sintactico.py',45),
  ('FuturoParticipio -> <empty>','FuturoParticipio',0,'p_FuturoParticipio','sintactico.py',50),
  ('PresenteAdmirativo -> <empty>','PresenteAdmirativo',0,'p_PresenteAdmirativo','sintactico.py',55),
  ('PresenteInterrogativo -> <empty>','PresenteInterrogativo',0,'p_PresenteInterrogativo','sintactico.py',61),
  ('Articulos -> ArticuloDefinido','Articulos',1,'p_Articulos','sintactico.py',67),
  ('Articulos -> ArticuloIndefinido','Articulos',1,'p_Articulos','sintactico.py',68),
  ('AdjetivosSujeto -> AdjetivoPosesivo','AdjetivosSujeto',1,'p_AdjetivosSujeto','sintactico.py',73),
  ('AdjetivosSujeto -> AdjetivoDemostrativo','AdjetivosSujeto',1,'p_AdjetivosSujeto','sintactico.py',74),
  ('AdjetivosSujeto -> AdjetivoNumeralCardinal','AdjetivosSujeto',1,'p_AdjetivosSujeto','sintactico.py',75),
  ('Empty -> <empty>','Empty',0,'p_Empty','sintactico.py',80),
]

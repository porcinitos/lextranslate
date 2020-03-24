import eel
import os
import easygui as gui
from gtts import gTTS
from platform import system

@eel.expose
def cargar_archivo():
  path = gui.fileopenbox(title="Seleccion", filetypes=["*.txt","*.md"])
  with open(path,"r") as content_file:
    content = content_file.read()
  eel.mostrarArchivo(content)

@eel.expose
def hablar(texto,lengua):
  audioname = "voice.wav"
  tts = gTTS(text=texto, lang = "es" if lengua == 0 else "en")
  print("es" if lengua == 0 else "en")
  tts.save(audioname)
  if (system() == "Linux"):
   os.system("mpg123 " + audioname)
  else:
    from winsound import PlaySound, SND_FILENAME
    PlaySound(audioname, SND_FILENAME)
  os.remove(audioname)

@eel.expose
def analizar(texto):
  #ejecutamos los analisis
  # obtenemos las variables desde utils
  tabla_simbolos = "LexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)"
  # tabla_errores ="LexToken(error,15,2)"
  tabla_errores =""
  traduccion = "tepo tepo"
  if len(tabla_simbolos) > 0:
    eel.mostrarTabla('{"tabla":"%r","tipo":"simbolos"}' % tabla_simbolos)
  if len(tabla_errores) > 0:
    eel.mostrarTabla('{"tabla":"%r","tipo":"errores"}'  % tabla_errores)
    eel.mostrarErrorTraduccion()
  else:
    # traduccir va vos
    eel.mostrarTraduccion(traduccion)
def __init__():
  eel.init('./gui')
  eel.start('index.html', size = (1020, 540), mode='chrome' )

if __name__ == "__main__":
  __init__()

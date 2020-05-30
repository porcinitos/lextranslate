from sys import path
path.append("./analizador")
import utils as U
import lexer
import sintactico

import eel
import os
import easygui as gui
from gtts import gTTS
from platform import system
from langdetect import detect
from translate import Translator

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

def traducir(texto, to):
  print("to -> " + to)
  translator = Translator(to_lang=to)
  return translator.translate(texto)

@eel.expose
def analizar(texto,lang):
  print(detect(texto)+ " " + lang)
  if (detect(texto) == lang):
    traduccion = traducir(texto, "en" if lang == "es" else "es")
    lexer.scan(texto)
    sintactico.parsear(texto)
  else:
    U.tablaErrores += "Lengua incorrecta"

  if len(U.tablaSimbolos) > 0:
    eel.mostrarTabla(U.tablaSimbolos,'simbolo')
  if len(U.tablaErrores) > 0:
    eel.mostrarTabla(U.tablaErrores,'errores')
    eel.mostrarErrorTraduccion()
  else:
    eel.mostrarTraduccion(traduccion)
  U.tablaSimbolos =""
  U.tablaErrores=""


def __init__():
  eel.init('./gui')
  eel.start('index.html', size = (1020, 540), mode='chrome' )

if __name__ == "__main__":
  __init__()

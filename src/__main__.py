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
  tts = gTTS(text=texto, lang = lengua)
  tts.save(audioname)
  if (system() == "Linux"):
   os.system("mpg123 " + audioname)
  os.remove(audioname)

def traducir(texto,froml, to):
  print("to -> " + to)
  translator = Translator(from_lang=froml,to_lang=to)
  return translator.translate(texto)

@eel.expose
def analizar(texto,lang):
  print(texto)
  print(detect(texto) + " " + lang)
  traduccion = ""
  if (detect(texto)  == lang or lang == "en" ):
    if lang == "es":
      traduccion = traducir(texto, lang, "en")
      print(traduccion)
      U.tablaSimbolos += "Analisis únicamente disponible en ingles"
    else:
      traduccion = traducir(texto, lang, "es")
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

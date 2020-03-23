import eel
import os
from gtts import gTTS
from platform import system

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


def __init__():
  eel.init('./gui')
  eel.start('index.html', size = (1020, 540), mode='chrome' )

if __name__ == "__main__":
  __init__()

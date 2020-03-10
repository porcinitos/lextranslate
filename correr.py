## necesita instalar python
## 
from platform import system
from subprocess import run
from os import chdir

sys = system()

print(":: Corriendo en " + sys)
if sys == 'Linux':
  chdir("./src")
elif sys == 'Windows':
  chdir("\src")

try: run("pipenv run python __main__.py".split(" "))
except: print("No se ha podido correr, verifica el archivo install.info")

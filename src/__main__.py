import eel

@eel.expose
def python_funct():
  print("hola desde python")


def __init__():
  eel.init('./gui')
  eel.start('index.html', size = (1020, 540), mode='chrome' )

if __name__ == "__main__":
  __init__()

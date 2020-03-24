import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

ruta = filedialog.askopenfilename()

print(ruta)

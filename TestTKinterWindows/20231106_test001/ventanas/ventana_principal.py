# ventanas/ventana_principal.py

import tkinter as tk

class VentanaPrincipal(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Ventana Principal")
    tk.Label(self, text = "Ventana Principal").pack(padx = 10, pady = 10)
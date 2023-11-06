# ventanas/ventana_principal.py
import tkinter as tk
from .ventana_secundaria import VentanaSecundaria

class VentanaPrincipal(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Ventana Principal")

    self.label = tk.Label(self, text = "texto original")
    self.label.pack(pady = 20)

    btn_abrir = tk.Button(self, text = "Abrir ventana secundaria", command = self.abrir_ventana_secundaria )
    btn_abrir.pack()

  def abrir_ventana_secundaria(self):
    VentanaSecundaria(master=self)
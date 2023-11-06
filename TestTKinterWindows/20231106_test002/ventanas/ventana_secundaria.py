# ventanas/ventana_secundaria.py
import tkinter as tk

class VentanaSecundaria(tk.Toplevel):
  def __init__(self, master = None):
    super().__init__(master)
    self.master = master
    self.title ( "Ventana Secundaria" )

    btn_cambiar = tk.Button( self, text = "Cambiar texto de Ventana principal", command = self.cambiar_texto_principal ) 
    btn_cambiar.pack(pady = 20)

  def cambiar_texto_principal(self):
    self.master.label.config(text = "Texto cambiado desde ventana secundaria" )
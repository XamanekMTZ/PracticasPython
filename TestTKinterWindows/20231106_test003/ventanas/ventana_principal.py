# ventanas/ventana_principal.py

import tkinter as tk

class VentanaPrincipal(tk.Tk):
  def __init__(self, info_usuario = None):
    super().__init__()
    self.title("Ventana Principal")
    mensaje = f"Bienvenido {info_usuario['nombre']} a la ventana principal"
    tk.Label(self, text = mensaje).pack(padx = 10, pady = 10)

    permisos_label = tk.Label(self, text="Tus permisos son: ")
    permisos_label.pack(pady = 10)

    for permiso in info_usuario['permisos']:
      tk.Label(self, text = permiso).pack()

    tk.Label(self, text = f"Último login: {info_usuario['ultimo_login']}").pack(pady = 20)
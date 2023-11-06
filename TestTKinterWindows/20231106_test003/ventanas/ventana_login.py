# ventanas/ventana_login.py

import tkinter as tk
from .ventana_principal import VentanaPrincipal

class VentanaLogin(tk.Toplevel):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.title("Login")

    self.label_usuario = tk.Label(self, text="Usuario")
    self.label_usuario.grid(row = 0, column = 0, padx = 10, pady = 10)

    self.entry_usuario = tk.Entry(self)
    self.entry_usuario.grid( row = 0, column = 1, padx = 10, pady = 10)

    self.label_contrasena = tk.Label(self, text="Contraseña")
    self.label_contrasena.grid(row = 1, column = 0, padx = 10, pady = 10)

    self.entry_contrasena = tk.Entry(self, show = "*")
    self.entry_contrasena.grid( row = 1, column = 1, padx = 10, pady = 10)

    self.btn_login = tk.Button(self, text="Login", command = self.verificar_credenciales)
    self.btn_login.grid( row = 2, column = 0, columnspan=2, pady = 10)


  def verificar_credenciales(self):
    usuario = self.entry_usuario.get()
    contrasena = self.entry_contrasena.get()

    if usuario == "admin" and contrasena == "1234":
      info_usuario = {
        "nombre": usuario,
        "permisos": ["crear", "editar", "eliminar"],
        "ultimo_login": "2023-11-01"
      }
      self.destroy()
      VentanaPrincipal(info_usuario = info_usuario)
    else:
      tk.messagebox.showerror("Error", "Usuario o contraseña incorrectos")
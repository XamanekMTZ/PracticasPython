from tkinter import *
from tkinter import ttk, font
import getpass

class Aplicacion():
  def __init__(self):
    self.raiz = Tk()
    self.raiz.title("Acceso")

    self.raiz.resizable(0,0)
    fuente = font.Font(weight='bold')

    self.marco = ttk.Frame(self.raiz, borderwidth=2, relief="raised", padding=(10,10))

    self.etiq1 = ttk.Label(self.marco, text="Usuario:", font=fuente, padding=(5,5))
    self.etiq2 = ttk.Label(self.marco, text="Contraseña:", font=fuente, padding=(5,5))

    self.usuario = StringVar()
    self.clave = StringVar()
    self.usuario.set(getpass.getuser())

    self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario, width=30)
    self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, width=30)
    self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
    self.boton1 = ttk.Button(self.marco, text="Aceptar", padding=(5,5), command=self.aceptar)
    self.boton2 = ttk.Button(self.marco, text="Cancelar", padding=(5,5), command=quit)

    self.marco.grid(column=0, row=0)
    self.etiq1.grid(column=0, row=0)
    self.ctext1.grid(column=1, row=0, columnspan=2)
    self.etiq2.grid(column=0, row=1)
    self.ctext2.grid(column=1, row=1, columnspan=2)
    self.separ1.grid(column=0, row=3, columnspan=3)
    self.boton1.grid(column=1, row=4)
    self.boton2.grid(column=2, row=4)

    self.ctext2.focus_set()
    self.raiz.mainloop()

  def aceptar(self):
    if self.clave.get() == 'tkinter':
      print("Acceso permitido")
      print("Usuario: ", self.ctext1.get())
      print("Contraseña: ", self.ctext2.get())
    else:
      print("Acceso denegado")
      self.clave.set("")
      self.ctext2.focus_set()

def main():
  mi_app = Aplicacion()
  return 0

if __name__ == '__main__':
  main()
    
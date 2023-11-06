# main.py
import tkinter as tk
from ventanas.ventana_login import VentanaLogin

if __name__ == "__main__":
  root = tk.Tk()
  root.withdraw()
  login = VentanaLogin(master = root)
  root.mainloop()
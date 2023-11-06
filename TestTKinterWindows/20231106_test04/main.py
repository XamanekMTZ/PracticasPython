import tkinter as tk

def on_resize(event):
  label.config(wraplength=event.width-10)
  label2.config(wraplength=event.width-10)

ventana = tk.Tk()
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
ventana.title("Mi ventana dinamica")
#ventana.geometry("800x600")
#ventana.minsize(400, 300)
ventana.minsize(1200, 720)
ventana.resizable(True, True)
ventana.geometry(f"{screen_width}x{screen_height}+0+0")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

label = tk.Label( ventana, text = "Este label se expande con la ventana y se ajusta al tamaño de la ventana.", bg = "lightgray", fg = "black", wraplength = 200)
#label.grid(row = 0, column = 0, sticky="nsew")
label.grid(row = 0, column = 0, sticky="nsew", padx = 20, pady = 20)

label2 = tk.Label( ventana, text = "Este label se expande con la ventana y se ajusta al tamaño de la ventana dos.", bg = "lightgray", fg = "black", wraplength = 200)
label2.grid(row = 0, column = 1, sticky = "nsew", padx = 20, pady = 20)

label.bind("<Configure>", on_resize)
label2.bind("<Configure>", on_resize)

ventana.mainloop()
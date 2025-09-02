import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title("Calculadora")
window.geometry("500x700")
window.config(bg="white")

# Botão suspenso menu 

mb = Menubutton(activebackground="lightblue",text="Menu",relief=RAISED)
mb.grid()
mb.menu = Menu(mb,tearoff=0)
mb["menu"] = mb.menu

Option = IntVar()
Config = IntVar()

mb.menu.add_checkbutton (label="Option", variable=Option)
mb.menu.add_checkbutton(label="Config", variable=Config)

# Tela calculadora



frame_num = tk.Frame(window)
frame_num.pack(pady=15)
tk.Label(frame_num, text="Digite o valor do produto:").pack(side=tk.LEFT,padx=(0,16))
entry_num = tk.Entry(frame_num)
entry_num.pack(side=tk.LEFT, fill=tk.X, expand=True)







#frame_visor = tk.Frame(window)
#frame_visor.place(x=125, y=50)
#entry_num = tk.Entry(frame_visor,font=("Arial",15), justify="right")
#entry_num.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2,expand=True)


window.mainloop()

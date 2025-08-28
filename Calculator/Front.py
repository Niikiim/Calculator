import tkinter as tk
from tkinter import *


window = Tk()
window.title("Calculadora")
window.geometry("500x700")
window.config(bg="white")


mb = Menubutton(activebackground="lightblue",text="Menu",relief=RAISED)
mb.grid()
mb.menu = Menu(mb,tearoff=0)
mb["menu"] = mb.menu

Option = IntVar()
Config = IntVar()

mb.menu.add_checkbutton (label="Option", variable=Option)
mb.menu.add_checkbutton(label="Config", variable=Config)




#frame_visor = tk.Frame(window)
#frame_visor.place(x=125, y=50)
#entry_num = tk.Entry(frame_visor,font=("Arial",15), justify="right")
#entry_num.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2,expand=True)


window.mainloop()

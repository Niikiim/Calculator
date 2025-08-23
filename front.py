import tkinter as tk

window = tk.Tk()
window.title = "Calculadora de desconto"
window.geometry("500x500")

frame_num = tk.Frame(window)
frame_num.pack(pady=15)
tk.Label(frame_num, text="Digite o valor do produto:").pack(side=tk.LEFT,padx=(0,16))


window.mainloop()

import tkinter as tk
from calculator import desconto

window = tk.Tk()
window.title = "Calculadora de desconto"
window.geometry("500x500")

frame_num = tk.Frame(window)
frame_num.pack(pady=15)
tk.Label(frame_num, text="Digite o valor do produto:").pack(side=tk.LEFT,padx=(0,16))
entry_num = tk.Entry(frame_num)
entry_num.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_desc = tk.Frame(window)
frame_desc.pack(pady=15)
tk.Label(frame_desc, text="Digite o valor do produto:").pack(side=tk.LEFT,padx=(0,16))
entry_num = tk.Entry(frame_desc)
entry_num.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_calc = tk.Frame(window)
frame_calc.pack(pady=15)
button_calc = tk.Button(frame_calc, text="Calcular desoconto", command=lambda:desconto)
button_calc.pack(side=tk.LEFT,padx=10)

window.mainloop()

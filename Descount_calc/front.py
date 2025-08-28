import tkinter as tk
from calculator import desconto

window = tk.Tk()
window.title = "Calculadora de desconto"
window.geometry("500x500")

def calcular():
    price = entry_num.get()
    desc = entry_desc.get()
    resultado = desconto(desc,price)
    label_result.config(text = resultado)


#Frame para colocar o preço
frame_num = tk.Frame(window)
frame_num.pack(pady=15)
tk.Label(frame_num, text="Digite o valor do produto:").pack(side=tk.LEFT,padx=(0,16))
entry_num = tk.Entry(frame_num)
entry_num.pack(side=tk.LEFT, fill=tk.X, expand=True)


#Frame para colocar o desconto
frame_desc = tk.Frame(window)
frame_desc.pack(pady=15)
tk.Label(frame_desc, text="Digite qual a porcentagem de desconto que será aplicada:").pack(side=tk.LEFT,padx=(0,16))
entry_desc = tk.Entry(frame_desc)
entry_desc.pack(side=tk.LEFT, fill=tk.X, expand=True)


#Frame Botão
frame_calc = tk.Frame(window)
frame_calc.pack(pady=15)
button_calc = tk.Button(frame_calc, text="Calcular desoconto", command=calcular)
button_calc.pack(side=tk.LEFT,padx=10)

#Resultado
label_result =  tk.Label(window, text="", fg="blue", font=("Arial",12))
label_result.pack(pady=20)

window.mainloop()

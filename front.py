import tkinter as tk
import calculator

window = tk.Tk
window.title = "Calculadora de desconto"
window.geometry("1000x1000")

frame_num = tk.frame(window)
frame_num.pack(pady=15)
tk.label(frame_num, text="Digite o valor do produto:").pack(side=tk.CENTER,padx=(0,16))




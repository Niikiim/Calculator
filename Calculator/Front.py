import tkinter as tk

window = tk.Tk()
window.title("Calculadora")
window.geometry("500x700")


frame_visor = tk.Frame(window)
frame_visor.pack(pady=50,padx=500)
frame_visor.place(x=50, width=400, height=100)
tk.Label(frame_visor).pack(side=tk.LEFT)
entry_num = tk.Entry(frame_visor)
entry_num.pack(side=tk.RIGHT,fill=tk.X, expand = True)




button_num0 = tk.Button(window)
button_num0.pack(pady=10,padx=10)
tk.Label(button_num0, text="0")
button_num0.pack(side=tk.LEFT,padx = 50)


window.mainloop()

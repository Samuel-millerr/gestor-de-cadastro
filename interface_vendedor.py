import tkinter as tk

vend = []
def inserir_vendedor():
    nome = case1.get()
    matri = case2.get()
    
    vend.append((nome, matri))

windon = tk.Tk() 

l1 = tk.Label(windon, text = "Insira os dados do vendedor: ")
l1.grid(row = 0, column = 0, pady = 2)

l2 = tk.Label(windon, text = "Nome do Vendedor:")
l2.grid(row = 1, column = 0, pady = 2)
case1 = tk.Entry(windon)
case1.grid(row = 1, column = 1, pady = 2)

l3 = tk.Label(windon, text = "Matrícula:")
l3.grid(row = 2, column = 0, pady = 2)
case2 = tk.Entry(windon)
case2.grid(row = 2, column = 1, pady = 2)

button = tk.Button(windon, text = "Inserir", command = inserir_vendedor)
button.grid(row = 3, column = 1, pady = 2)

windon.mainloop()


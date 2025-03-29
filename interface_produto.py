import tkinter as tk

prod = []

def inserir_produto():
    nomeProd = case1.get()
    valor = case2.get()
    categ = case3.get()
    
windon = tk.Tk()

l1 = tk.Label(windon, text = "Digite as informações do produto: ")
l1.grid(row = 0, column = 0, pady = 2)

l2 = tk.Label(windon, text = "Nome do Produto: ")
l2.grid(row = 1, column = 0, pady = 2)
case1 = tk.Entry(windon)
case1.grid(row = 1, column = 1, pady =2)

l3 = tk.Label(windon, text = "Valor:")
l3.grid(row = 2, column = 0, pady = 2)
case2 = tk.Entry(windon)
case2.grid(row = 2, column = 1, pady = 2)

l4 = tk.Label(windon, text = "Categoria:")
l4.grid(row = 3, column = 0, pady = 2)
case3 = tk.Entry(windon)
case3.grid(row = 3, column = 1, pady = 2)

button = tk.Button(windon, text = "Inserir", command = inserir_produto)
button.grid(row = 4, column = 1, pady = 2)


windon.mainloop()

    
    

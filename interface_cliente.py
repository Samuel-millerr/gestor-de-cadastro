import tkinter as tk

cliente = []

def inserir_cliente():
    nome_cliente = case1.get()
    data_nasc = case2.get()
    cpf = case3.get()
    origem = case4.get()
    score = case5.get()
    cliente.append((nome_cliente, data_nasc, cpf, origem, score))
    
windon = tk.Tk()
windon.title("Inserir dados do cliente")

l1 = tk.Label(windon, text = "Digite as informações do cliente a seguir:")
l1.grid(row = 0, column= 0,pady= 2)

l2 = tk.Label(windon, text = "Nome:")
l2.grid(row = 1, column=0, pady = 2)
case1 = tk.Entry(windon)
case1.grid(row = 1, column= 1, pady=2)

l3 = tk.Label(windon, text = "Data de Nascimento:")
l3.grid(row = 2, column=0, pady = 2)
case2 = tk.Entry(windon)
case2.grid(row=2, column=1, pady = 2)

l4 = tk.Label(windon, text = "CPF:")
l4.grid(row = 3, column = 0, pady = 2)
case3 = tk.Entry(windon)
case3.grid(row = 3, column = 1, pady = 2)

l5 = tk.Label(windon, text = "Origem:")
l5.grid(row = 4, column = 0, pady = 1)
case4 = tk.Entry(windon)
case4.grid(row = 4, column = 1, pady = 2)

l6 = tk.Label(windon, text = "Score:")
l6.grid(row = 5, column = 0, pady = 2)
case5 = tk.Entry(windon)
case5.grid(row = 5, column = 1, pady = 2)
           
button = tk.Button(windon, text = "Inserir", command = inserir_cliente)
button.grid(row = 6, column = 1, pady = 2)

windon.mainloop()
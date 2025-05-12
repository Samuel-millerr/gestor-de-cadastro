from tkinter import *
from tkinter import ttk
from cliente import mostrar_inter_cliente
from produto import mostrar_interface_produto
from vendedor import mostrar_interface_vendedor

window = Tk()
window.title("Cadastro")

frm = ttk.Frame(window, width=145, height=270, padding=5)
frm.grid(row=0, column=0)

l1 = ttk.Label(frm, text = "Essas são as três opções para inserir informações")
l1.grid(row = 0, column = 0, pady = 2)
button1 = ttk.Button(frm, text = "Cliente", command=mostrar_inter_cliente)
button1.grid(row = 1, column = 0, pady = 2)
button2 = ttk.Button(frm, text = "Produto", command=mostrar_interface_produto)
button2.grid(row = 2, column = 0, pady = 2)
button3 = ttk.Button(frm, text = "Vendedor", command=mostrar_interface_vendedor)
button3.grid(row = 3, column = 0, pady = 2)

window.resizable(False, False)
window.geometry("270x145")
window.mainloop()
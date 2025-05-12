from tkinter import *
from tkinter import ttk

def mostrar_interface_produto():
    window = Tk()
    window.title("Cadastro Produto")

    produto = []
    frm = ttk.Frame(window, width=250, height=330, padding=10)
    frm.grid(row=0, column=0)

    l1 = ttk.Label(frm, text="Digite as informações do produto: ")
    l1.grid(row=0, column=1, pady=2)

    l2 = ttk.Label(frm, text="Nome do Produto: ")
    l2.grid(row=1, column=0, pady=2)
    case1 = ttk.Entry(frm)
    case1.grid(row=1, column=1, pady=2)

    l3 = ttk.Label(frm, text="Valor:")
    l3.grid(row=2, column=0, pady=2)
    case2 = ttk.Entry(frm)
    case2.grid(row=2, column=1, pady=2)

    l4 = ttk.Label(frm, text="Categoria:")
    l4.grid(row=3, column=0, pady=2)
    case3 = ttk.Entry(frm)
    case3.grid(row=3, column=1, pady=2)

    button = ttk.Button(frm, text="Inserir")
    button.grid(row=4, column=1, pady=2)

    button = ttk.Button(frm, text="Adicionar ao Exel")
    button.grid(row=5, column=1, pady=2)

    space = ttk.Label(frm)
    space.grid(row=6, column=1)

    casex = ttk.Entry(frm)
    casex.grid(row=7, column=1, pady=2)

    button = ttk.Button(frm, text="Consultar")
    button.grid(row=8, column=1, pady=2)

    window.resizable(False,False)
    window.geometry("320x250")
    window.mainloop()
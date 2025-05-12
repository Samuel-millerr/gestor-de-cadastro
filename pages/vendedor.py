from tkinter import *
from tkinter import ttk

def mostrar_interface_vendedor():
    window = Tk()
    window.title("Cadastro Vendedor")

    frm = ttk.Frame(window, width=220, height=300, padding=10)
    frm.grid(row=0, column=0)

    l1 = ttk.Label(frm, text="Insira os dados do vendedor: ")
    l1.grid(row=0, column=1, pady=2)

    l2 = ttk.Label(frm, text="Nome do Vendedor:")
    l2.grid(row=1, column=0, pady=2)
    case1 = ttk.Entry(frm)
    case1.grid(row=1, column=1, pady=2)

    l3 = ttk.Label(frm, text="Matrícula:")
    l3.grid(row=2, column=0, pady=2)
    case2 = ttk.Entry(frm)
    case2.grid(row=2, column=1, pady=2)

    button = ttk.Button(frm, text="Inserir")
    button.grid(row=3, column=1, pady=2)

    button = ttk.Button(frm, text="Adicionar ao Exel")
    button.grid(row=4, column=1, pady=2)

    space = ttk.Label(frm)
    space.grid(row=5, column=1)

    casex = ttk.Entry(frm)
    casex.grid(row=6, column=1, pady=2)

    button = ttk.Button(frm, text="Consultar")
    button.grid(row=7, column=1, pady=2)

    window.resizable(False,False)
    window.geometry("300x220")
    window.mainloop()
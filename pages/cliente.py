from tkinter import *
from tkinter import ttk

def mostrar_inter_cliente():
    window = Tk()
    window.title("Cadastro Cliente")

    cliente = []
    frm = ttk.Frame(window, width=300, height=350, padding=10)
    frm.grid(row=0, column=0)

    l1 = ttk.Label(frm, text="Digite as informações do cliente a seguir:")
    l1.grid(row=0, column=1, pady=2)

    l2 = ttk.Label(frm, text="Nome:")
    l2.grid(row=1, column=0, pady=2)
    case1 = ttk.Entry(frm)
    case1.grid(row=1, column=1, pady=2)

    l3 = ttk.Label(frm, text="Data de Nascimento:")
    l3.grid(row=2, column=0, pady=2)
    case2 = ttk.Entry(frm)
    case2.grid(row=2, column=1, pady=2)

    l4 = ttk.Label(frm, text="CPF:")
    l4.grid(row=3, column=0, pady=2)
    case3 = ttk.Entry(frm)
    case3.grid(row=3, column=1, pady=2)

    l5 = ttk.Label(frm, text="Origem:")
    l5.grid(row=4, column=0, pady=1)
    case4 = ttk.Entry(frm)
    case4.grid(row=4, column=1, pady=2)

    l6 = ttk.Label(frm, text="Score:")
    l6.grid(row=5, column=0, pady=2)
    case5 = ttk.Entry(frm)
    case5.grid(row=5, column=1, pady=2)

    button = ttk.Button(frm, text="Inserir")
    button.grid(row=6, column=1, pady=2)

    button = ttk.Button(frm, text="Adicionar ao Exel")
    button.grid(row=7, column=1, pady=2)

    space = ttk.Label(frm)
    space.grid(row=8, column=1)

    casex = ttk.Entry(frm)
    casex.grid(row=9, column=1, pady=2)

    button = ttk.Button(frm, text="Consultar Cliente")
    button.grid(row=10, column=1, pady=2)

    window.resizable(False,False)
    window.geometry("350x300")
    window.mainloop()

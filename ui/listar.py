import tkinter as tk
from tkinter import ttk
from utils.db_helper import executar_query

def abrir_tela_listar():
    janela = tk.Toplevel()
    janela.title("Listar Produtos")
    janela.geometry("1000x600")

    tree = ttk.Treeview(janela, columns=("ID", "Nome", "Descrição", "Quantidade", "Preço"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Descrição", text="Descrição")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Preço", text="Preço")
    tree.pack(fill="both", expand=True)

    query = "SELECT * FROM produtos"
    produtos = executar_query(query)


    for produto in produtos:
        tree.insert("", "end", values=produto)
import tkinter as tk
from tkinter import messagebox
from utils.db_helper import executar_query

def excluir_produto(id_produto):
    query = "DELETE FROM produtos WHERE id = %s"
    valores = (id_produto,)
    executar_query(query, valores)
    messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

def abrir_tela_removerproduto():
    janela = tk.Toplevel()
    janela.title("Remover Produto")
    janela.geometry("400x300")

    tk.Label(janela, text="Id Produto").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()
    def salvar():
        nome = nome_entry.get()
        excluir_produto(nome)
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)
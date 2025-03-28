import tkinter as tk
from tkinter import messagebox
from utils.db_helper import executar_query

def adicionar_produto(nome, descricao, quantidade, preco):
    query = "INSERT INTO produtos (nome, descricao, quantidade, preco) VALUES (%s, %s, %s, %s)"
    valores = (nome, descricao, quantidade, preco)
    executar_query(query, valores)
    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

def abrir_tela_adicionar():
    janela = tk.Toplevel()
    janela.title("Adicionar Produto")
    janela.geometry("400x300")

    tk.Label(janela, text="Nome").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    tk.Label(janela, text="Descrição").pack()
    descricao_entry = tk.Entry(janela)
    descricao_entry.pack()

    tk.Label(janela, text="Quantidade").pack()
    quantidade_entry = tk.Entry(janela)
    quantidade_entry.pack()

    tk.Label(janela, text="Preço").pack()
    preco_entry = tk.Entry(janela)
    preco_entry.pack()

    def salvar():
        nome = nome_entry.get()
        descricao = descricao_entry.get()
        quantidade = int(quantidade_entry.get())
        preco = float(preco_entry.get())
        adicionar_produto(nome, descricao, quantidade, preco)
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

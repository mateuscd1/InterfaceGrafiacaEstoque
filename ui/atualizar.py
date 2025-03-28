import tkinter as tk
from tkinter import messagebox
from utils.db_helper import executar_query

def atualizar_produto(nome, descricao, quantidade, preco, id):
    query = "UPDATE produtos SET nome = %s, descricao = %s, quantidade = %s, preco = %s WHERE id = %s"
    valores = (nome, descricao, quantidade, preco, id)
    executar_query(query, valores)
    messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

def abrir_tela_adicionar(id):
    janela = tk.Toplevel()
    janela.title("Atualizar Produto")
    janela.geometry("400x300")

    tk.Label(janela, text="Nome novo").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    tk.Label(janela, text="Descrição a ser atualizada").pack()
    descricao_entry = tk.Entry(janela)
    descricao_entry.pack()

    tk.Label(janela, text="Quantidade nova").pack()
    quantidade_entry = tk.Entry(janela)
    quantidade_entry.pack()

    tk.Label(janela, text="Preço novo").pack()
    preco_entry = tk.Entry(janela)
    preco_entry.pack()

    def salvar():
        nome = nome_entry.get()
        descricao = descricao_entry.get()
        try:
            quantidade = int(quantidade_entry.get())
            preco = float(preco_entry.get())
            atualizar_produto(nome, descricao, quantidade, preco, id)
            janela.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro e preço deve ser um número decimal.")

    tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

def verificarId_AtualizarProduto():
    janela = tk.Toplevel()
    janela.title("Atualizar Produto")
    janela.geometry("400x300")

    tk.Label(janela, text="ID do Produto a ser atualizado").pack()
    id_entry = tk.Entry(janela)
    id_entry.pack()

    def verificar():
        id = id_entry.get()

        if not id.isdigit():
            messagebox.showerror("Erro", "ID inválido! Digite um número.")
            return
        
        query = "SELECT * FROM produtos WHERE id = %s"
        resultado = executar_query(query, (id,))

        if resultado:
            janela.destroy()
            messagebox.showinfo("Sucesso", "Produto encontrado na base de dados")
            abrir_tela_adicionar(id)
        else:
            messagebox.showinfo("Erro", "Produto não encontrado")

    tk.Button(janela, text="Verificar", command=verificar).pack(pady=10)

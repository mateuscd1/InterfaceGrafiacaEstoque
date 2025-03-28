import tkinter as tk
from ui.adicionar import abrir_tela_adicionar
from ui.listar import abrir_tela_listar
from ui.atualizar import verificarId_AtualizarProduto
from ui.remover import abrir_tela_removerproduto

def fechar_programa():
    root = tk.Tk()
    root.quit()  # Fecha a janela principal e encerra o programa

def main():
    root = tk.Tk()
    root.title("Sistema de Controle de Estoque")
    root.geometry("800x600")

    tk.Button(root, text="Adicionar Produto", command=abrir_tela_adicionar).pack(pady=10)
    tk.Button(root, text="Listar Produtos", command=abrir_tela_listar).pack(pady=10)
    tk.Button(root, text="Atualizar Produto", command=verificarId_AtualizarProduto).pack(pady=10)
    tk.Button(root, text="Remover Produto", command=abrir_tela_removerproduto).pack(pady=10)

   # Criar o botão "Fechar"
    btn_fechar = tk.Button(root, text="Fechar", command=fechar_programa, bg="red", fg="white")
    btn_fechar.pack(pady=20)

    # Iniciar o loop principal
    root.mainloop()

if __name__ == "__main__":
    main()

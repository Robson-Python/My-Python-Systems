import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


# Função para criar o banco de dados
def criar_banco():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              sobrenome TEXT NOT NULL,
              email TEXT NOT NULL,
              telefone TEXT NOT NULL)''')
    conexao.commit()
    conexao.close()


# Função para abrir janela consulta global
def abrir_tela_consulta():
    tela_consulta = tk.Tk()
    tela_consulta.title("Buscar todos os clientes")
    tela_consulta.geometry("600x400+50+50")
    def busca_cliente():
        conexao = sqlite3.connect('clientes.db')
        c = conexao.cursor()
        c.execute("SELECT * FROM clientes order by nome")
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
    tree = ttk.Treeview(tela_consulta)
    tree.grid(row=10, column=0, sticky='nsew')
    tree["columns"] = ("id", "nome", "sobrenome", "email", "telefone")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.heading("#0", text="", anchor=tk.W)
    tree.column("id", anchor=tk.W, width=120)
    tree.heading("id", text="Id", anchor=tk.W)
    tree.column("nome", anchor=tk.W, width=120)
    tree.heading("nome", text="Nome", anchor=tk.W)
    tree.column("sobrenome", anchor=tk.W, width=120)
    tree.heading("sobrenome", text="Sobrenome", anchor=tk.W)
    tree.column("email", anchor=tk.W, width=120)
    tree.heading("email", text="E-mail", anchor=tk.W)
    tree.column("telefone", anchor=tk.W, width=120)
    tree.heading("telefone", text="Telefone", anchor=tk.W)
    tk.Button(tela_consulta, text="Buscar Clientes", command=busca_cliente).grid(row=30, columnspan=1)
    tk.Button(tela_consulta, text="Fechar", command=tela_consulta.destroy).grid(row=31, columnspan=1)
    
        
# Função para adicionar um cliente
def adicionar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("INSERT INTO clientes (nome, sobrenome, email, telefone) VALUES (?, ?, ?, ?)",
              (entry_nome.get(), entry_sobrenome.get(), entry_email.get(), entry_telefone.get()))
    conexao.commit()
    conexao.close()
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso")
    limpar_campos()


#Função para excluir um cliente
def excluir_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("DELETE FROM clientes WHERE id =?", (entry_id.get(),))
    messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
    conexao.commit()
    conexao.close()
    limpar_campos()


#Função para atualizar um cliente
def atualiza_cliente():
     conexao = sqlite3.connect('clientes.db')
     c = conexao.cursor()
     c.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, telefone = ? WHERE id =?", 
               (entry_nome.get(), entry_sobrenome.get(), entry_email.get(), entry_telefone.get(), entry_id.get()))
     messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
     conexao.commit()
     conexao.close()
     limpar_campos()


#Função para selecionar o cliente
def selecionar_cliente():
     conexao = sqlite3.connect('clientes.db')
     c = conexao.cursor()
     c.execute("SELECT * FROM clientes WHERE nome = ?", (entry_nome.get(),))
     row = c.fetchone()
     conexao.close()
     if row:
        limpar_campos()
        entry_id.insert(0, row[0])
        entry_nome.insert(0, row[1])
        entry_sobrenome.insert(0, row[2])
        entry_email.insert(0, row[3])
        entry_telefone.insert(0, row[4])
        messagebox.showinfo("Sucesso", "Cliente encontrado!")
     else:
        limpar_campos()
        entry_nome.insert(0, "Not found")
        entry_sobrenome.insert(0, "Not found")
        entry_email.insert(0, "Not found")
        entry_telefone.insert(0, "Not found")
        messagebox.showerror("Erro", "Cliente não encontrado!")
     

# Funçãp para limpar os campos de entrada
def limpar_campos():
      entry_id.delete(0, tk.END)
      entry_nome.delete(0, tk.END)
      entry_sobrenome.delete(0, tk.END)
      entry_email.delete(0, tk.END)
      entry_telefone.delete(0, tk.END)


#Função para centralizar janela
def centralizar_janela(janela):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)
    janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')


# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("600x400+50+50")

    
# Labels e entradas
tk.Label(janela, text="Id").grid(row=0, column=0)
entry_id = tk.Entry(janela)
entry_id.grid(row=0, column=1)


tk.Label(janela, text="Nome").grid(row=1, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1)


tk.Label(janela, text="Sobrenome").grid(row=2, column=0)
entry_sobrenome = tk.Entry(janela)
entry_sobrenome.grid(row=2, column=1)


tk.Label(janela, text="E-mail").grid(row=3, column=0)
entry_email = tk.Entry(janela)
entry_email.grid(row=3, column=1)


tk.Label(janela, text="Telefone").grid(row=4, column=0)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=4, column=1)


# Botão para adicionar cliente
tk.Button(janela, text="Cadastrar", command=adicionar_cliente).grid(row=5, columnspan=1)

# Botão para atualizar cliente
tk.Button(janela, text="Atualizar", command=atualiza_cliente).grid(row=6, columnspan=1)

# Botão para selecionar cliente
tk.Button(janela, text="Selecionar", command=selecionar_cliente).grid(row=5, columnspan=2)

# Botão para Limpar campos
tk.Button(janela, text="Limpar", command=limpar_campos).grid(row=7, columnspan=1)


#Botão para excluir cliente
tk.Button(janela, text="Exlcuir", command=excluir_cliente).grid(row=6, columnspan=2)

#Botão para tela todos os clientes
tk.Button(janela, text="Buscar todos", command=abrir_tela_consulta).grid(row=8, columnspan=1)

# Fechar a janela
tk.Button(janela, text="Sair", command=janela.destroy).grid(row=7, columnspan=2)


# Inicializar banco de dados
criar_banco()


#Centralizar a janela
centralizar_janela(janela)


# Iniciar o loop da interface gráfica
janela.mainloop()
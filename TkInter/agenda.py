import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# Função para abrir novas janelas
def abrir_tela_cliente():
    tela_cliente = tk.Tk()
    tela_cliente.title("Cadastro de Clientes")
    tela_cliente.geometry("600x400+50+50")
    #tela_cliente = tk.Toplevel(principal)
    #tela_cliente.title("Cadastro de cliente")
    #ttk.Label(tela_cliente, text="Tela de Cadastro de Cliente").pack()


    #Tela clientes

    # Função para adicionar um cliente
    def adicionar_cliente():
        conexao = sqlite3.connect('agenda.db')
        c = conexao.cursor()
        c.execute("INSERT INTO clientes (nome, sobrenome, email, telefone) VALUES (?, ?, ?, ?)",
                 (entry_nome.get(), entry_sobrenome.get(), entry_email.get(), entry_telefone.get()))
        conexao.commit()
        conexao.close()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso")
        limpar_campos()

    #Função para excluir um cliente
    def excluir_cliente():
        conexao = sqlite3.connect('agenda.db')
        c = conexao.cursor()
        c.execute("DELETE FROM clientes WHERE id =?", (entry_id.get(),))
        messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        conexao.commit()
        conexao.close()
        limpar_campos()

    #Função para atualizar um cliente
    def atualiza_cliente():
        conexao = sqlite3.connect('agenda.db')
        c = conexao.cursor()
        c.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, telefone = ? WHERE id =?", 
                 (entry_nome.get(), entry_sobrenome.get(), entry_email.get(), entry_telefone.get(), entry_id.get()))
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        conexao.commit()
        conexao.close()
        limpar_campos()

    #Função para selecionar o cliente
    def selecionar_cliente():
        conexao = sqlite3.connect('agenda.db')
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

    # Labels e entradas
    tk.Label(tela_cliente, text="Id").grid(row=0, column=0)
    entry_id = tk.Entry(tela_cliente)
    entry_id.grid(row=0, column=1)

    tk.Label(tela_cliente, text="Nome").grid(row=1, column=0)
    entry_nome = tk.Entry(tela_cliente)
    entry_nome.grid(row=1, column=1)

    tk.Label(tela_cliente, text="Sobrenome").grid(row=2, column=0)
    entry_sobrenome = tk.Entry(tela_cliente)
    entry_sobrenome.grid(row=2, column=1)

    tk.Label(tela_cliente, text="E-mail").grid(row=3, column=0)
    entry_email = tk.Entry(tela_cliente)
    entry_email.grid(row=3, column=1)

    tk.Label(tela_cliente, text="Telefone").grid(row=4, column=0)
    entry_telefone = tk.Entry(tela_cliente)
    entry_telefone.grid(row=4, column=1)


    # Botão para adicionar cliente
    tk.Button(tela_cliente, text="Cadastrar", command=adicionar_cliente).grid(row=5, columnspan=1)

    # Botão para atualizar cliente
    tk.Button(tela_cliente, text="Atualizar", command=atualiza_cliente).grid(row=6, columnspan=1)

    # Botão para selecionar cliente
    tk.Button(tela_cliente, text="Selecionar", command=selecionar_cliente).grid(row=5, columnspan=2)

    # Botão para Limpar campos
    tk.Button(tela_cliente, text="Limpar", command=limpar_campos).grid(row=7, columnspan=1)

    #Botão para excluir cliente
    tk.Button(tela_cliente, text="Exlcuir", command=excluir_cliente).grid(row=6, columnspan=2)

    # Fechar a janela
    tk.Button(tela_cliente, text="Sair", command=tela_cliente.destroy).grid(row=7, columnspan=2)


def abrir_tela_evento():
    tela_evento = tk.Tk()
    tela_evento.title("Cadastro de Eventos")
    tela_evento.geometry("600x400+50+50")

    #Tela eventos

    # Função para adicionar evento
    def adicionar_evento():
        conexao = sqlite3.connect('agenda.db')
        c = conexao.cursor()
        c.execute("INSERT INTO eventos (nome_cli, evento, data, obs) VALUES (?, ?, ?, ?)",
                 (entry_nome.get(), entry_evento.get(), entry_data.get(), entry_obs.get()))
        conexao.commit()
        conexao.close()
        messagebox.showinfo("Sucesso", "Evento cadastrado com sucesso")
        limpar_campos()

    #Função para excluir um evento
    def excluir_evento():
        conexao = sqlite3.connect('agenda.db')
        c = conexao.cursor()
        c.execute("DELETE FROM eventos WHERE id =?", (entry_id.get(),))
        messagebox.showinfo("Sucesso", "Evento excluído com sucesso!")
        conexao.commit()
        conexao.close()
        limpar_campos()


    #Função para atualizar um evento
    def atualiza_evento():
        conexao = sqlite3.connect('agenda.db')
        c = conexao.cursor()
        c.execute("UPDATE eventos SET nome_cli = ?, evento = ?, data = ?, obs = ? WHERE id =?", 
                 (entry_nome.get(), entry_evento.get(), entry_data.get(), entry_obs.get(), entry_id.get()))
        messagebox.showinfo("Sucesso", "Evento atualizado com sucesso!")
        conexao.commit()
        conexao.close()
        limpar_campos()


    #Função para selecionar o evento
    def selecionar_evento():
        conexao = sqlite3.connect('agenda.db')
        c = conexao.cursor()
        c.execute("SELECT * FROM eventos WHERE nome_cli = ?", (entry_nome.get(),))
        row = c.fetchone()
        conexao.close()
        if row:
           limpar_campos()
           entry_id.insert(0, row[0])
           entry_nome.insert(0, row[1])
           entry_evento.insert(0, row[2])
           entry_data.insert(0, row[3])
           entry_obs.insert(0, row[4])
           messagebox.showinfo("Sucesso", "Evento encontrado!")
        else:
            limpar_campos()
            entry_nome.insert(0, "Not found")
            entry_evento.insert(0, "Not found")
            entry_data.insert(0, "Not found")
            entry_obs.insert(0, "Not found")
            messagebox.showerror("Erro", "Cliente não encontrado!")
    

    # Funçãp para limpar os campos de entrada
    def limpar_campos():
         entry_id.delete(0, tk.END)
         entry_nome.delete(0, tk.END)
         entry_evento.delete(0, tk.END)
         entry_data.delete(0, tk.END)
         entry_obs.delete(0, tk.END)

    # Labels e entradas
    tk.Label(tela_evento, text="Id").grid(row=0, column=0)
    entry_id = tk.Entry(tela_evento)
    entry_id.grid(row=0, column=1)

    tk.Label(tela_evento, text="Nome").grid(row=1, column=0)
    entry_nome = tk.Entry(tela_evento)
    entry_nome.grid(row=1, column=1)

    tk.Label(tela_evento, text="Evento").grid(row=2, column=0)
    entry_evento = tk.Entry(tela_evento)
    entry_evento.grid(row=2, column=1)


    tk.Label(tela_evento, text="Data").grid(row=3, column=0)
    entry_data = tk.Entry(tela_evento)
    entry_data.grid(row=3, column=1)


    tk.Label(tela_evento, text="Observação").grid(row=4, column=0)
    entry_obs = tk.Entry(tela_evento)
    entry_obs.grid(row=4, column=1)


    # Botão para adicionar cliente
    tk.Button(tela_evento, text="Cadastrar", command=adicionar_evento).grid(row=5, columnspan=1)

    # Botão para atualizar cliente
    tk.Button(tela_evento, text="Atualizar", command=atualiza_evento).grid(row=6, columnspan=1)

    # Botão para selecionar cliente
    tk.Button(tela_evento, text="Selecionar", command=selecionar_evento).grid(row=5, columnspan=2)

    # Botão para Limpar campos
    tk.Button(tela_evento, text="Limpar", command=limpar_campos).grid(row=7, columnspan=1)

    #Botão para excluir cliente
    tk.Button(tela_evento, text="Exlcuir", command=excluir_evento).grid(row=6, columnspan=2)

    # Fechar a janela
    tk.Button(tela_evento, text="Sair", command=tela_evento.destroy).grid(row=7, columnspan=2)


# Configuração da janela principal
principal = tk.Tk()
principal.title("Agenda")
principal.geometry("300x200")


# Botões da janela principal
ttk.Button(principal, text="Cadastro de Cliente", command=abrir_tela_cliente).pack(pady=10)
ttk.Button(principal, text="Cadastro de Eventos", command=abrir_tela_evento).pack(pady=10)
ttk.Button(principal, text="Fechar", command=principal.destroy).pack(pady=10)


#Comandos para congelar a tela
#tela_cliente.attributes('-topmost', True)
#tela_cliente.attributes('-topmost', False)


# Iniciar o loop principal
principal.mainloop()
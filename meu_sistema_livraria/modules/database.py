import sqlite3
from pathlib import Path

DB_FILE = Path("meu_sistema_livraria/data/livraria.db")

# Função para conexão com o banco de dados
def conectar_banco():
    return sqlite3.connect(DB_FILE)

# Função para criar as tabelas
def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        ano_publicacao INTEGER NOT NULL,
                        preco REAL NOT NULL
                      )''')
    conn.commit()
    conn.close()

# Função para adicionar um livro
def adicionar_livro(titulo, autor, ano_publicacao, preco):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO livros (titulo, autor, ano_publicacao, preco) 
                      VALUES (?, ?, ?, ?)''', (titulo, autor, ano_publicacao, preco))
    conn.commit()
    conn.close()
    print(f"Livro '{titulo}' adicionado com sucesso!")

# Função para exibir todos os livros
def exibir_livros():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    
    if livros:
        print("ID | Título | Autor | Ano | Preço")
        for livro in livros:
            print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]} | {livro[4]}")
    else:
        print("Nenhum livro cadastrado.")

# Função para atualizar o preço de um livro
def atualizar_preco(id_livro, novo_preco):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))
    conn.commit()
    conn.close()
    print(f"Preço do livro ID {id_livro} atualizado para {novo_preco}.")

# Função para remover um livro
def remover_livro(id_livro):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    conn.commit()
    conn.close()
    print(f"Livro com ID {id_livro} removido com sucesso.")

# Função para buscar livros por autor
def buscar_livros_por_autor(autor):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE autor LIKE ?", ('%' + autor + '%',))
    livros = cursor.fetchall()
    conn.close()
    
    if livros:
        print(f"Livros de {autor}:")
        for livro in livros:
            print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]} | {livro[4]}")
    else:
        print(f"Nenhum livro encontrado para o autor '{autor}'.")

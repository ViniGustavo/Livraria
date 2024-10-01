import csv
from pathlib import Path
from .database import conectar_banco

EXPORT_DIR = Path("meu_sistema_livraria/exports/")

# Função para exportar dados para CSV
def exportar_para_csv():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()

    csv_file = EXPORT_DIR / 'livros_exportados.csv'
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Título", "Autor", "Ano", "Preço"])
        writer.writerows(livros)
    
    print(f"Dados exportados para {csv_file}")

# Função para importar dados de CSV
def importar_de_csv(arquivo_csv):
    conn = conectar_banco()
    cursor = conn.cursor()

    with open(arquivo_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''INSERT INTO livros (titulo, autor, ano_publicacao, preco) 
                              VALUES (?, ?, ?, ?)''', (row['Título'], row['Autor'], int(row['Ano']), float(row['Preço'])))
    
    conn.commit()
    conn.close()
    print(f"Dados importados de {arquivo_csv}")

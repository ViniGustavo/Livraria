from .database import adicionar_livro, exibir_livros, atualizar_preco, remover_livro, buscar_livros_por_autor
from .file_manager import exportar_para_csv, importar_de_csv
from .backups import backup_banco

# Função para exibir o menu do sistema
def menu():
    while True:
        print("\nSistema de Gerenciamento de Livraria")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("7. Importar dados de CSV")
        print("8. Fazer backup do banco de dados")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de Publicação: "))
            preco = float(input("Preço: "))
            adicionar_livro(titulo, autor, ano, preco)
        elif escolha == '2':
            exibir_livros()
        elif escolha == '3':
            id_livro = int(input("ID do livro: "))
            novo_preco = float(input("Novo preço: "))
            atualizar_preco(id_livro, novo_preco)
        elif escolha == '4':
            id_livro = int(input("ID do livro a remover: "))
            remover_livro(id_livro)
        elif escolha == '5':
            autor = input("Nome do autor: ")
            buscar_livros_por_autor(autor)
        elif escolha == '6':
            exportar_para_csv()
        elif escolha == '7':
            arquivo_csv = input("Caminho do arquivo CSV: ")
            importar_de_csv(arquivo_csv)
        elif escolha == '8':
            backup_banco()
        elif escolha == '9':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

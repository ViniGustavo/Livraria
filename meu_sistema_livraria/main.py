from modules.menu import menu
from modules.database import criar_tabela
from pathlib import Path

# Configurações de diretórios
BACKUP_DIR = Path("meu_sistema_livraria/backups/")
DATA_DIR = Path("meu_sistema_livraria/data/")
EXPORT_DIR = Path("meu_sistema_livraria/exports/")

# Função para garantir que os diretórios existem
def inicializar_sistema():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True)

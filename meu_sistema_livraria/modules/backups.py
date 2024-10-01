import shutil
from pathlib import Path
from datetime import datetime
import os

BACKUP_DIR = Path("meu_sistema_livraria/backups/")
DB_FILE = Path("meu_sistema_livraria/data/livraria.db")

# Função para fazer backup do banco de dados
def backup_banco():
    if DB_FILE.exists():
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = BACKUP_DIR / f"backup_livraria_{timestamp}.db"
        shutil.copy(DB_FILE, backup_file)
        print(f"Backup realizado: {backup_file}")
        limpar_backups_antigos()

# Função para limpar backups antigos (mantém apenas os 5 mais recentes)
def limpar_backups_antigos():
    backups = sorted(BACKUP_DIR.glob("*.db"), key=os.path.getmtime, reverse=True)
    for backup in backups[5:]:
        backup.unlink()
        print(f"Backup antigo removido: {backup}")

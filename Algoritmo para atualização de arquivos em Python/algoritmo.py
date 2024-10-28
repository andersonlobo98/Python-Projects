import os
from pathlib import Path

# Obtém o diretório atual de trabalho
current_dir = Path(os.getcwd())
import_file = current_dir / "allow_list.txt"

with open(import_file, "r") as file:
    content = file.read()
print(content)



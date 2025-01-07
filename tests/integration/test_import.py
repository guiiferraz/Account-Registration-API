import sys
import os

# Adicionar o diretório raiz do projeto ao sys.path
# Aqui estamos subindo dois diretórios (para alcançar a raiz do projeto)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

# Agora, o Python conseguirá localizar os módulos dentro de `src`
from app import app
from utils.utils import FileHandler
from models.db_connector import db_session

# Agora, seu código pode rodar sem problemas
print("Módulos importados com sucesso!")

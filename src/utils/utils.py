import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

FILE_PATH = os.getenv('FILEPATH')

class FileHandler:
    def __init__(self):
        pass


    def read_excel(self):
        read = pd.read_excel(FILE_PATH)
        
        # for row in read.itertuples():
        #     print(row.Nome)
        #     print(row.Numero)

        return read

# teste = FileHandler()
# teste.read_excel()

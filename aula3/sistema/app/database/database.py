import json # biblioteca para lidar com arquivos JSON
from pathlib import Path # biblioteca para lidar com caminhos do WIN

class Bancofake:

    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()
        
    def _carregar(self): 
        # carrega dados do arquivo JSON, se existir. caso não exista, inicia com dados vazio
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            # abrindo arquivo no modo de leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as data:
                # salvando dados que já existem no arquivo
                # na variável dados
                self.dados = json.load(data)
        else:
            self._salvar()
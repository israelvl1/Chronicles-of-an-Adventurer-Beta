import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import json
from PyQt6.QtWidgets import QApplication
from Jogo import *
import Personagem
import Entrada
import ResultadoDado
import utils
from cores import TelaCores  # Importa a classe TelaCores
# Função para exibir a tela de seleção de cor
def exibir_tela_cores():
    app = QApplication(sys.argv)
    janela = TelaCores()

    # Conectar o sinal de fechamento da janela para garantir que o jogo inicie após o fechamento da tela
    janela.destroyed.connect(app.quit)  # Fechamento da janela vai sair do loop do Qt

    janela.show()
    app.exec()  # Inicia o loop de eventos, mas não faz o programa encerrar

# Exibe a tela de seleção de cor
exibir_tela_cores()

# Função para carregar a cor salva do arquivo de configuração
def carregar_cor():
    CONFIG_FILE = "config.json"
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f).get("cor", "0A")  # Retorna o código da cor ou "0A" por padrão
    return "0A"  # Retorna o valor padrão caso o arquivo não exista

# Obtém o código de cor
codigo_cor = carregar_cor()

# Se o sistema for Windows, altera a cor do console
if sys.platform.startswith("win"):
    os.system(f'color {codigo_cor}')  # Aplica a cor salva

# Inicia o jogo após a janela de cor ser fechada
jogar()

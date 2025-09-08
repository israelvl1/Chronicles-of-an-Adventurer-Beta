import sys
import os
import json
from PyQt6.QtWidgets import QApplication

# Adiciona diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Imports do seu projeto
import Jogo
import Personagem
import Entrada
import ResultadoDado
import utils
from cores import TelaCores  # Tela de seleção de cores

CONFIG_FILE = "config.json"

# Dicionário de conversão para ANSI (texto e fundo)
ansi_cores = {
    "0": "30", "1": "34", "2": "32", "3": "36", "4": "31", "5": "35",
    "6": "33", "7": "37", "8": "90", "9": "94", "A": "92", "B": "96",
    "C": "91", "D": "95", "E": "93", "F": "97"
}

# Função para carregar o código de cor salvo
def carregar_cor():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f).get("cor", "0A")
    return "0A"

# Função para aplicar a cor no terminal
def aplicar_cor_console(codigo_cor):
    if len(codigo_cor) != 2:
        return  # Código inválido
    texto = codigo_cor[0].upper()
    fundo = codigo_cor[1].upper()

    if sys.platform.startswith("win"):
        os.system(f"color {codigo_cor}")
    else:
        # ANSI: fundo precisa de código "4X", trocando "3" por "4" do texto
        ansi_texto = ansi_cores.get(texto, "37")
        ansi_fundo = ansi_cores.get(fundo, "40").replace("3", "4", 1)
        print(f"\033[{ansi_texto};{ansi_fundo}m", end="")

# Função para resetar cor no fim (opcional)
def resetar_cor():
    if not sys.platform.startswith("win"):
        print("\033[0m", end="")  # ANSI reset

# Exibe a janela gráfica de escolha de cores
def exibir_tela_cores():
    app = QApplication(sys.argv)
    janela = TelaCores()
    janela.destroyed.connect(app.quit)  # Quando fechar, encerra o loop
    janela.show()
    app.exec()

# Executa a tela de escolha
exibir_tela_cores()

# Aplica a cor salva após fechar a janela
codigo = carregar_cor()
aplicar_cor_console(codigo)

# Inicia o jogo
Jogo.jogar()

# Restaura a cor padrão no final (boa prática)
resetar_cor()

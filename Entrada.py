from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer
import sys
import time


class PerguntarDialog(QDialog):
    def __init__(self, texto_ascii1, texto_ascii2):
        super().__init__()
        self.setWindowTitle("Projeto RPG")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: black; color: lime;")
        self.resultado = None

        self.texto_ascii1 = texto_ascii1  # ⬅️ salvar como atributo
        self.texto_ascii2 = texto_ascii2  # ⬅️ salvar como atributo

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Mostrar primeira imagem
        self.label, self.timer = mostrar_primeira_imagem(self.layout, self.texto_ascii1)

        # Depois de 3 segundos, trocar para segunda imagem
        QTimer.singleShot(13000, self.trocar_para_segunda)

    def trocar_para_segunda(self):
        self.label, self.timer = trocar_imagem(self.layout, self.texto_ascii2)  # ⬅️ usar self.texto_ascii2
        QTimer.singleShot(5000, self.mostrar_botoes)
        
    def mostrar_botoes(self):
        botoes_layout = QHBoxLayout()

        btn_sim = QPushButton("Sim")
        btn_sim.setStyleSheet("background-color: black; color: lime;")
        btn_sim.clicked.connect(self.escolher_sim)
        botoes_layout.addWidget(btn_sim)

        btn_nao = QPushButton("Não")
        btn_nao.setStyleSheet("background-color: black; color: lime;")
        btn_nao.clicked.connect(self.escolher_nao)
        botoes_layout.addWidget(btn_nao)

        self.layout.addLayout(botoes_layout)

    def escolher_sim(self):
        self.resultado = "Sim"
        self.accept()

    def escolher_nao(self):
        self.resultado = "Não"
        self.accept()

    def closeEvent(self, event):
        # Se quiser impedir fechar com X, use event.ignore()
        event.accept()

def perguntar_qt(texto_ascii1, texto_ascii2):
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    dialog = PerguntarDialog(texto_ascii1, texto_ascii2)
    dialog.exec()
    return dialog.resultado


# Função para limpar todos os widgets dentro do frame (útil para trocar telas)
def limpar_tela(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.setParent(None)


def escrever_ascii(label, texto, index_tracker, timer):
    passo = 3  # número de letras por atualização (ajuste aqui para mais/menos)
    if index_tracker["index"] < len(texto):
        atual = label.text()
        fim = index_tracker["index"] + passo
        atual += texto[index_tracker["index"]:fim]
        label.setText(atual)
        index_tracker["index"] = fim
    else:
        timer.stop()

ascii1 = r"""
                                                                                                                                                                                     
                                                            .oPYo.  .oPYo. .oPYo.    ooooo .oPYo. o ooooo .oPYo.    .oPYo. .oPYo.  .oPYo.                                                             
                                                            8   `8  8    8 8    8    8     8.     8   8   8    8    8    8 8    8  8   `8                                                             
                                                           o8YooP' o8YooP' 8        o8oo   `boo   8   8   8    8   o8YooP' 8    8 o8YooP'                                                             
                                                            8   `b  8      8   oo    8     .P     8   8   8    8    8      8    8  8   `b                                                             
                                                            8    8  8      8    8    8     8      8   8   8    8    8      8    8  8    8                                                             
                                                            8    8  8      `YooP8    8     `YooP' 8   8   `YooP'    8      `YooP'  8    8                                                             
                                                            ..:::..:..::::::....8 :::..:::::.....:..::..:::.....::::..::::::.....::..:::..                                                            
                                                            ::::::::::::::::::::8 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::                                                            
                                                            ::::::::::::::::::::..::::::::::::::::::::::::::::::::::::::::::::::::::::::::                                                            
                                                                                                                                                                                                 
                                                               
                                              .%%%%%%...%%%%...%%%%%....%%%%...%%%%%%..%%...........%%..%%..%%%%%%..%%......%%%%%%..%%.......%%%%..
                                              ...%%....%%......%%..%%..%%..%%..%%......%%...........%%..%%....%%....%%......%%......%%......%%..%%.
                                              ...%%.....%%%%...%%%%%...%%%%%%..%%%%....%%...........%%..%%....%%....%%......%%%%....%%......%%%%%%.
                                              ...%%........%%..%%..%%..%%..%%..%%......%%............%%%%.....%%....%%......%%......%%......%%..%%.
                                              .%%%%%%...%%%%...%%..%%..%%..%%..%%%%%%..%%%%%%.........%%....%%%%%%..%%%%%%..%%%%%%..%%%%%%..%%..%%.
                                              .....................................................................................................
                      
                                                                                         @@@@@@@@@@@@@@@@                                
                                                                                       @@@@@@@@@@@@@@@@@@@@@@                            
                                                                                     @@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                                                                     @@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                                                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                                                                                   @@@@@@@@@@@@@@@@@@@@  @@@@@@@@                        
                                                                                   @@@@@@@@@@@@@@@@      @@@@@@@@                        
                                                                                   @@@@@@@@@@@@@@          @@@@@@                        
                                                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                                                                                     @@        @   @          @@                          
                                                                                     @@        @   @          @@                          
                                                                                     @@@@     @     @      @@@@                          
                                                                                     @@@@@@@@@       @@@@@@@@@                          
                                                                                       @@                  @@                            
                                                                                       @@@@              @@@@                            
                                                                                         @@              @@                              
                                                                                         @@@@@@      @@@@@@                                                                                   
                                                                                           @@@@@@@@@@@@@@                                
                                                                                           @@@@        @@                                
                                                                                           @@          @@                                
                                                                                       @@@@@@          @@@@@@                            
                                                                                 @@@@@@@@@@              @@@@@@@@@@                      
                                                                           @@@@@@@@@@@@@@                  @@@@@@@@@@@@@@                
                                                                       @@@@@@@@@@@@@@@@@@@@              @@@@@@@@@@@@@@@@@@@@            
                                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@        
                                                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@  @@  @@@@@@@@@@@@@@@@@@@@@@@@@@    
                                                               @@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@    @@    @@@@@@@@@@@@@@@@@@@@@@@@    
                                                               @@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@  @@@@@@    @@@@@@@@@@@@@@@@@@@@@@    
                                                               @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@    @@@@@@@@    @@@@@@@@@@@@@@@@@@@@    
                                                             @@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@    @@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@  
                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@  @@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@  
                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@  
                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
                                                         
    """
ascii2 = r"""
    
                                                    .%%%%%%..%%..%%..%%%%%%...%%%%...%%%%%%...%%%%...%%%%%...........%%%%%...%%%%%....%%%%....%%%%..
                                                    ...%%....%%%.%%....%%....%%..%%....%%....%%..%%..%%..%%..........%%..%%..%%..%%..%%......%%..%%.
                                                    ...%%....%%.%%%....%%....%%........%%....%%%%%%..%%%%%...........%%%%%...%%%%%...%%.%%%.....%%..
                                                    ...%%....%%..%%....%%....%%..%%....%%....%%..%%..%%..%%..........%%..%%..%%......%%..%%....%%...
                                                    .%%%%%%..%%..%%..%%%%%%...%%%%...%%%%%%..%%..%%..%%..%%..........%%..%%..%%.......%%%%.....%%...

                                                                                        .%%%%...%%%%%%..%%...%%.
                                                                                        %%........%%....%%%.%%%.
                                                                                        .%%%%.....%%....%%.%.%%.
                                                                                        ....%%....%%....%%...%%.
                                                                                        .%%%%...%%%%%%..%%...%%.

                                                                                            .%%%%...%%..%%. 
                                                                                            %%..%%..%%..%%. 
                                                                                            %%..%%..%%..%%. 
                                                                                            %%..%%..%%..%%. 
                                                                                            .%%%%....%%%%.. 

                                                                                        %%..%%...%%%%....%%%%.. 
                                                                                        %%%.%%..%%..%%..%%..%%. 
                                                                                        %%.%%%..%%%%%%..%%..%%. 
                                                                                        %%..%%..%%..%%..%%..%%. 
                                                                                        %%..%%..%%..%%...%%%%.. 
                                        
    """

ascii3 = r"""
                                                       
    .............................................................................................................................................................................................................                                                         
    .%%..%%.%%%%%%..%%%%..%%%%%%.%%%%%%........%%%%%..%%%%%...%%%%.................%%%%...%%%%.........%%%%%..%%%%%%.%%%%%...%%%%...%%%%..%%..%%..%%%%...%%%%..%%%%%%.%%..%%..%%%%.........%%%%%%.%%%%%%.%%...%%.
    .%%%.%%.%%.....%%.......%%...%%............%%..%%.%%..%%.%%...................%%..%%.%%............%%..%%.%%.....%%..%%.%%.....%%..%%.%%%.%%.%%..%%.%%.....%%.....%%%.%%.%%..............%%...%%.....%%%.%%%.
    .%%.%%%.%%%%....%%%%....%%...%%%%..........%%%%%..%%%%%..%%.%%%...%%..........%%..%%..%%%%.........%%%%%..%%%%...%%%%%...%%%%..%%..%%.%%.%%%.%%%%%%.%%.%%%.%%%%...%%.%%%..%%%%...........%%...%%%%...%%.%.%%.
    .%%..%%.%%.........%%...%%...%%............%%..%%.%%.....%%..%%...%%..........%%..%%.....%%........%%.....%%.....%%..%%.....%%.%%..%%.%%..%%.%%..%%.%%..%%.%%.....%%..%%.....%%..........%%...%%.....%%...%%.
    .%%..%%.%%%%%%..%%%%....%%...%%%%%%........%%..%%.%%......%%%%.....%...........%%%%...%%%%.........%%.....%%%%%%.%%..%%..%%%%...%%%%..%%..%%.%%..%%..%%%%..%%%%%%.%%..%%..%%%%...........%%...%%%%%%.%%...%%.
    .............................................................................................................................................................................................................
           .%%..%%.%%...%%.........%%%%..%%%%%%.%%..%%..%%%%.........%%%%%%.%%%%%%.%%..%%..%%%%.........%%%%%%........%%..%%..%%%%...%%%%.........%%..%%..%%%%..........%%%%..%%%%%...%%%%...%%%%...%%%%..       
           .%%..%%.%%%.%%%........%%.....%%......%%%%..%%..%%........%%.......%%....%%%%..%%..%%........%%............%%%.%%.%%..%%.%%..%%........%%..%%.%%..%%........%%..%%.%%..%%.%%..%%.%%..%%.%%..%%.       
           .%%..%%.%%.%.%%.........%%%%..%%%%.....%%...%%..%%........%%%%.....%%.....%%...%%..%%........%%%%..........%%.%%%.%%%%%%.%%..%%........%%%%%%.%%%%%%........%%..%%.%%%%%..%%.....%%%%%%.%%..%%.       
           .%%..%%.%%...%%............%%.%%......%%%%..%%..%%........%%.......%%....%%%%..%%..%%........%%............%%..%%.%%..%%.%%..%%........%%..%%.%%..%%........%%..%%.%%.....%%..%%.%%..%%.%%..%%.       
           ..%%%%..%%...%%.........%%%%..%%%%%%.%%..%%..%%%%.........%%.....%%%%%%.%%..%%..%%%%.........%%%%%%........%%..%%.%%..%%..%%%%.........%%..%%.%%..%%.........%%%%..%%......%%%%..%%..%%..%%%%..       
           ...............................................................................................................................................................................................       
                  ....%%%%%..%%%%%%......%%%%..%%.....%%%%%%.%%%%%%.%%%%%...%%%%..%%%%%................%%%%%..%%%%%%.%%%%%%.%%%%%%.%%%%%..%%%%%%.%%..%%.%%%%%%.%%%%%%........%%%%%..%%%%%%........               
                  ....%%..%%.%%.........%%..%%.%%.......%%...%%.....%%..%%.%%..%%.%%..%%...............%%..%%...%%...%%.....%%.....%%..%%.%%.....%%%.%%...%%...%%............%%..%%.%%............               
                  ....%%..%%.%%%%.......%%%%%%.%%.......%%...%%%%...%%%%%..%%%%%%.%%%%%....%%..........%%..%%...%%...%%%%...%%%%...%%%%%..%%%%...%%.%%%...%%...%%%%..........%%..%%.%%%%..........               
                  ....%%..%%.%%.........%%..%%.%%.......%%...%%.....%%..%%.%%..%%.%%..%%...%%..........%%..%%...%%...%%.....%%.....%%..%%.%%.....%%..%%...%%...%%............%%..%%.%%............               
                  ....%%%%%..%%%%%%.....%%..%%.%%%%%%...%%...%%%%%%.%%..%%.%%..%%.%%..%%....%..........%%%%%..%%%%%%.%%.....%%%%%%.%%..%%.%%%%%%.%%..%%...%%...%%%%%%........%%%%%..%%%%%%........               
                  ................................................................................................................................................................................               
                                                            .%%%%%..%%%%%...%%%%...%%%%...%%%%..%%..%%.........%%%%...%%%%..%%%%%%........%%%%%%.                                                                
                                                            .%%..%%.%%..%%.%%..%%.%%.....%%..%%.%%%.%%........%%..%%.%%.....%%...............%%..                                                                
                                                            .%%..%%.%%%%%..%%%%%%.%%.%%%.%%..%%.%%.%%%........%%%%%%.%%.%%%.%%%%............%%%..                                                                
                                                            .%%..%%.%%..%%.%%..%%.%%..%%.%%..%%.%%..%%........%%..%%.%%..%%.%%................%%.                                                                
                                                            .%%%%%..%%..%%.%%..%%..%%%%...%%%%..%%..%%........%%..%%..%%%%..%%%%%%........%%%%%..                                                                
                                                            .....................................................................................

    """
ascii4 = r"""

                                                            .%%%%%%.%%..%%........%%%%%%.%%%%%%.........%%%%..%%..%%.%%%%%%..%%%%..%%%%%%.%%%%%%.                                                         
                                                            .%%.....%%..%%..........%%...%%............%%..%%.%%..%%...%%...%%.....%%.......%%...                                                         
                                                            .%%%%...%%..%%..........%%...%%%%..........%%%%%%.%%..%%...%%....%%%%..%%%%.....%%...                                                         
                                                            .%%.....%%..%%..........%%...%%............%%..%%..%%%%....%%.......%%.%%.......%%...                                                         
                                                            .%%%%%%..%%%%...........%%...%%%%%%........%%..%%...%%...%%%%%%..%%%%..%%%%%%.%%%%%%.                                                         
                                                            .....................................................................................                                                         
    .%%..%%.%%%%%%..%%%%..%%%%%%.%%%%%%........%%%%%..%%%%%...%%%%.................%%%%...%%%%.........%%%%%..%%%%%%.%%%%%...%%%%...%%%%..%%..%%..%%%%...%%%%..%%%%%%.%%..%%..%%%%.........%%%%%%.%%%%%%.%%...%%.
    .%%%.%%.%%.....%%.......%%...%%............%%..%%.%%..%%.%%...................%%..%%.%%............%%..%%.%%.....%%..%%.%%.....%%..%%.%%%.%%.%%..%%.%%.....%%.....%%%.%%.%%..............%%...%%.....%%%.%%%.
    .%%.%%%.%%%%....%%%%....%%...%%%%..........%%%%%..%%%%%..%%.%%%...%%..........%%..%%..%%%%.........%%%%%..%%%%...%%%%%...%%%%..%%..%%.%%.%%%.%%%%%%.%%.%%%.%%%%...%%.%%%..%%%%...........%%...%%%%...%%.%.%%.
    .%%..%%.%%.........%%...%%...%%............%%..%%.%%.....%%..%%...%%..........%%..%%.....%%........%%.....%%.....%%..%%.....%%.%%..%%.%%..%%.%%..%%.%%..%%.%%.....%%..%%.....%%..........%%...%%.....%%...%%.
    .%%..%%.%%%%%%..%%%%....%%...%%%%%%........%%..%%.%%......%%%%.....%...........%%%%...%%%%.........%%.....%%%%%%.%%..%%..%%%%...%%%%..%%..%%.%%..%%..%%%%..%%%%%%.%%..%%..%%%%...........%%...%%%%%%.%%...%%.
    .............................................................................................................................................................................................................
           .%%..%%.%%...%%.........%%%%..%%%%%%.%%..%%..%%%%.........%%%%%%.%%%%%%.%%..%%..%%%%.........%%%%%%........%%..%%..%%%%...%%%%.........%%..%%..%%%%..........%%%%..%%%%%...%%%%...%%%%...%%%%..       
           .%%..%%.%%%.%%%........%%.....%%......%%%%..%%..%%........%%.......%%....%%%%..%%..%%........%%............%%%.%%.%%..%%.%%..%%........%%..%%.%%..%%........%%..%%.%%..%%.%%..%%.%%..%%.%%..%%.       
           .%%..%%.%%.%.%%.........%%%%..%%%%.....%%...%%..%%........%%%%.....%%.....%%...%%..%%........%%%%..........%%.%%%.%%%%%%.%%..%%........%%%%%%.%%%%%%........%%..%%.%%%%%..%%.....%%%%%%.%%..%%.       
           .%%..%%.%%...%%............%%.%%......%%%%..%%..%%........%%.......%%....%%%%..%%..%%........%%............%%..%%.%%..%%.%%..%%........%%..%%.%%..%%........%%..%%.%%.....%%..%%.%%..%%.%%..%%.       
           ..%%%%..%%...%%.........%%%%..%%%%%%.%%..%%..%%%%.........%%.....%%%%%%.%%..%%..%%%%.........%%%%%%........%%..%%.%%..%%..%%%%.........%%..%%.%%..%%.........%%%%..%%......%%%%..%%..%%..%%%%..       
           ...............................................................................................................................................................................................       
                .......%%%%%..%%%%%%.........%%%%..%%.....%%%%%%.%%%%%%.%%%%%...%%%%..%%%%%................%%%%%..%%%%%%.%%%%%%.%%%%%%.%%%%%..%%%%%%.%%..%%.%%%%%%.%%%%%%........%%%%%..%%%%%%........               
                .......%%..%%.%%............%%..%%.%%.......%%...%%.....%%..%%.%%..%%.%%..%%...............%%..%%...%%...%%.....%%.....%%..%%.%%.....%%%.%%...%%...%%............%%..%%.%%............               
                .......%%..%%.%%%%..........%%%%%%.%%.......%%...%%%%...%%%%%..%%%%%%.%%%%%....%%..........%%..%%...%%...%%%%...%%%%...%%%%%..%%%%...%%.%%%...%%...%%%%..........%%..%%.%%%%..........               
                .......%%..%%.%%............%%..%%.%%.......%%...%%.....%%..%%.%%..%%.%%..%%...%%..........%%..%%...%%...%%.....%%.....%%..%%.%%.....%%..%%...%%...%%............%%..%%.%%............               
                .......%%%%%..%%%%%%........%%..%%.%%%%%%...%%...%%%%%%.%%..%%.%%..%%.%%..%%....%..........%%%%%..%%%%%%.%%.....%%%%%%.%%..%%.%%%%%%.%%..%%...%%...%%%%%%........%%%%%..%%%%%%........               
                ......................................................................................................................................................................................               
                                                         .%%%%%..%%%%%...%%%%...%%%%...%%%%..%%..%%.........%%%%...%%%%..%%%%%%........%%%%%%.                                                                
                                                         .%%..%%.%%..%%.%%..%%.%%.....%%..%%.%%%.%%........%%..%%.%%.....%%...............%%..                                                                
                                                         .%%..%%.%%%%%..%%%%%%.%%.%%%.%%..%%.%%.%%%........%%%%%%.%%.%%%.%%%%............%%%..                                                                
                                                         .%%..%%.%%..%%.%%..%%.%%..%%.%%..%%.%%..%%........%%..%%.%%..%%.%%................%%.                                                                
                                                         .%%%%%..%%..%%.%%..%%..%%%%...%%%%..%%..%%........%%..%%..%%%%..%%%%%%........%%%%%..                                                                
                                                         .....................................................................................                                                                
        
    """

ascii5 = r"""
    
               ______   .______   .______       __    _______      ___       _______   ______                
              /  __  \  |   _  \  |   _  \     |  |  /  _____|    /   \     |       \ /  __  \               
             |  |  |  | |  |_)  | |  |_)  |    |  | |  |  __     /  ^  \    |  .--.  |  |  |  |              
             |  |  |  | |   _  <  |      /     |  | |  | |_ |   /  /_\  \   |  |  |  |  |  |  |              
             |  `--'  | |  |_)  | |  |\  \----.|  | |  |__| |  /  _____  \  |  '--'  |  `--'  |              
              \______/  |______/  | _| `._____||__|  \______| /__/     \__\ |_______/ \______/               
                                                                                                             
             .______     ______   .______                __    ______     _______      ___      .______      
             |   _  \   /  __  \  |   _  \              |  |  /  __  \   /  _____|    /   \     |   _  \     
             |  |_)  | |  |  |  | |  |_)  |             |  | |  |  |  | |  |  __     /  ^  \    |  |_)  |    
             |   ___/  |  |  |  | |      /        .--.  |  | |  |  |  | |  | |_ |   /  /_\  \   |      /     
             |  |      |  `--'  | |  |\  \----.   |  `--'  | |  `--'  | |  |__| |  /  _____  \  |  |\  \----.
             | _|       \______/  | _| `._____|    \______/   \______/   \______| /__/     \__\ | _| `._____|
                                                                                                                             

    
    """

# Mostrar a primeira imagem
def mostrar_primeira_imagem(layout, texto_ascii):
    label = QLabel()
    label.setFont(QFont("Courier", 5))
    label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    label.setStyleSheet("background-color: black; color: lime;")
    label.setText("")  # começa vazio

    layout.addWidget(label)

    index_tracker = {"index": 0}
    timer = QTimer()
    timer.timeout.connect(lambda: escrever_ascii(label, texto_ascii, index_tracker, timer))
    timer.start(1)  # atualiza a cada 3 ms (ajuste para o efeito desejado)

    return label, timer

    

# Trocar a imagem após o tempo
def trocar_imagem(layout, texto_ascii):
    limpar_tela(layout)  # Limpa o layout antes de trocar

    label = QLabel()
    label.setFont(QFont("Courier", 5))
    label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    label.setStyleSheet("background-color: black; color: lime;")
    label.setText("")

    layout.addWidget(label)

    index_tracker = {"index": 0}
    timer = QTimer()
    timer.timeout.connect(lambda: escrever_ascii(label, texto_ascii, index_tracker, timer))
    timer.start(3)

    return label, timer

# Função para impedir que o usuário feche a janela pelo botão X
def nao_fechar(event):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle("Atenção")
    msg.setText("Você não pode fechar esta janela agora.")
    msg.exec()

    event.ignore()  # Impede que a janela seja fechada

# Função para exibir uma janela com uma mensagem fixa (ex: imagem ASCII)
class DialogMensagemFixa(QDialog):
    def __init__(self, texto_ascii):
        super().__init__()
        self.setWindowTitle("Imagens ASCII")
        self.setFixedSize(1000, 300)
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        mostrar_terceira_imagem(layout, texto_ascii)

        self._fechamento_permitido = False
        QTimer.singleShot(8000, self.permitir_fechamento)

    def permitir_fechamento(self):
        self._fechamento_permitido = True
        self.accept()

    def closeEvent(self, event):
        if self._fechamento_permitido:
            event.accept()  # permite fechar
        else:
            event.ignore()  # bloqueia fechamento manual


class DialogMensagemFim(QDialog):
    def __init__(self, texto_ascii):
        super().__init__()
        self.setWindowTitle("Fim do Jogo")
        self.setFixedSize(1000, 300)
        self.setStyleSheet("background-color: black; color: lime;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        mostrar_fim(layout, texto_ascii)

        # Fecha automaticamente após 5 segundos (5000 ms)
        QTimer.singleShot(5000, self.accept)

    def closeEvent(self, event):
        # Se quiser impedir fechamento manual antes do tempo, descomente abaixo:
        # event.ignore()
        event.accept()

def exibir_mensagem_fim(texto_ascii):
    app = QApplication.instance()
    if not app:
        app = QApplication([])

    dialog = DialogMensagemFim(texto_ascii)
    dialog.exec()


class DialogMensagemErro(QDialog):
    def __init__(self, texto_ascii):
        super().__init__()
        self.setWindowTitle("Imagens ASCII - Erro")
        self.setFixedSize(900, 300)
        self.setStyleSheet("background-color: black; color: red;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        mostrar_erro_imagem(layout, texto_ascii)

        self._fechamento_permitido = False
        # Fecha automaticamente após 5 segundos (5000 ms)
        QTimer.singleShot(8000, self.permitir_fechamento)

    def permitir_fechamento(self):
        self._fechamento_permitido = True
        self.accept()

    def closeEvent(self, event):
        if self._fechamento_permitido:
            event.accept()
        else:
            event.ignore()

def exibir_mensagem_erro(texto_ascii):
    app = QApplication.instance()
    if not app:
        app = QApplication([])

    dialog = DialogMensagemErro(texto_ascii)
    dialog.exec()

        
def exibir_mensagem_fixa(texto_ascii):
    app = QApplication.instance()
    if not app:
        app = QApplication([])

    dialog = DialogMensagemFixa(texto_ascii)
    dialog.exec()  # mostra modal, bloqueia até fechar

# Mostrar a terceira imagem
def mostrar_terceira_imagem(layout, texto_ascii):
    label = QLabel()
    label.setFont(QFont("Courier", 5))
    label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    label.setStyleSheet("background-color: black; color: lime;")
    label.setText("")  # começa vazio

    layout.addWidget(label)

    index_tracker = {"index": 0}
    timer = QTimer()
    timer.timeout.connect(lambda: escrever_ascii(label, texto_ascii, index_tracker, timer))
    timer.start(1)  # atualiza a cada 3 ms (ajuste para o efeito desejado)

    return label
    
# Mostrar a terceira imagem
def mostrar_erro_imagem(layout, texto_ascii):
    label = QLabel()
    label.setFont(QFont("Courier", 5))
    label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    label.setStyleSheet("background-color: black; color: lime;")
    label.setText("")  # começa vazio

    layout.addWidget(label)

    index_tracker = {"index": 0}
    timer = QTimer()
    timer.timeout.connect(lambda: escrever_ascii(label, texto_ascii, index_tracker, timer))
    timer.start(1)  # atualiza a cada 3 ms (ajuste para o efeito desejado)

    return label
    
# Mostrar a terceira imagem
def mostrar_fim(layout, texto_ascii):
    label = QLabel()
    label.setFont(QFont("Courier", 5))
    label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    label.setStyleSheet("background-color: black; color: lime;")
    label.setText("")  # começa vazio

    layout.addWidget(label)

    index_tracker = {"index": 0}
    timer = QTimer()
    timer.timeout.connect(lambda: escrever_ascii(label, texto_ascii, index_tracker, timer))
    timer.start(1)  # atualiza a cada 3 ms (ajuste para o efeito desejado)

    return label
    

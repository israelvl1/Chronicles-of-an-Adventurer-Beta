from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt, QTimer, QByteArray
import sys
import time
icone_base64 = """,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"""

class PerguntarDialog(QDialog):
    def __init__(self, texto_ascii1, texto_ascii2):
        super().__init__()
        self.setWindowTitle("Projeto RPG")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: black; color: lime;")
        self.resultado = None

        pixmap.loadFromData(QByteArray.fromBase64(icone_base64))
        self.setWindowIcon(QIcon(pixmap))

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

        pixmap.loadFromData(QByteArray.fromBase64(icone_base64))
        self.setWindowIcon(QIcon(pixmap))

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

        pixmap.loadFromData(QByteArray.fromBase64(icone_base64))
        self.setWindowIcon(QIcon(pixmap))

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

        pixmap.loadFromData(QByteArray.fromBase64(icone_base64))
        self.setWindowIcon(QIcon(pixmap))

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
    

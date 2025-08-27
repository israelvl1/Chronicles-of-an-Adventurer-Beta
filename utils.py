import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QSurfaceFormat

# Cria um objeto de configuração de formato de superfície (para definir como o OpenGL será usado)
fmt = QSurfaceFormat()

# Define que o tipo de renderização será com OpenGL
fmt.setRenderableType(QSurfaceFormat.RenderableType.OpenGL)

# Define o perfil de compatibilidade do OpenGL (não usa o modo "core")
fmt.setProfile(QSurfaceFormat.OpenGLContextProfile.CompatibilityProfile)  # <- modo compatível com versões antigas

# Define a versão do OpenGL que será usada (aqui, 2.1)
fmt.setVersion(2, 1)  # ou 2.0, dependendo do seu driver de vídeo

# Define o uso de double buffering (evita flickering e melhora desempenho visual)
fmt.setSwapBehavior(QSurfaceFormat.SwapBehavior.DoubleBuffer)

# Define o tamanho do depth buffer (usado para profundidade 3D, 24 bits aqui)
fmt.setDepthBufferSize(24)

# Aplica esse formato como padrão para qualquer contexto OpenGL criado
QSurfaceFormat.setDefaultFormat(fmt)

# Função para garantir que exista uma instância de QApplication (necessária para apps PyQt)
def garantir_qt_app():
    app = QApplication.instance()  # Verifica se já existe uma instância
    if not app:
        app = QApplication(sys.argv)  # Cria uma nova se não existir
    return app  # Retorna a instância da aplicação

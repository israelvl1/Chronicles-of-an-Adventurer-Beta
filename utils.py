import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QSurfaceFormat

fmt = QSurfaceFormat()
fmt.setRenderableType(QSurfaceFormat.RenderableType.OpenGL)
fmt.setProfile(QSurfaceFormat.OpenGLContextProfile.CompatibilityProfile)  # <- aqui!
fmt.setVersion(2, 1)  # ou 2.0, dependendo do seu driver
fmt.setSwapBehavior(QSurfaceFormat.SwapBehavior.DoubleBuffer)
fmt.setDepthBufferSize(24)

QSurfaceFormat.setDefaultFormat(fmt)
def garantir_qt_app():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    return app

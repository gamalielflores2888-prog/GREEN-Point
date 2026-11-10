import sys
from PyQt5.QtWidgets import QApplication
from ventana import GreenPoint

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GreenPoint()
    ventana.show()
    sys.exit(app.exec_())
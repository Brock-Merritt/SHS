import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("PyPlater")
        self.setGeometry(350,100, 700,500)


app = QApplication([sys.argv])
window = Window()
window.show()
sys.exit(app.exec_())
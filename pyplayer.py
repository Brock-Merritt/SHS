import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QStyle
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("PyPlayer")
        self.setGeometry(350,100, 700,500)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.blue)
        self.setPalette(p)

        self.create_player()

    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videowidget = QVideoWidget()

        self.openBtn = QPushButton('open video')

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)

        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)

        vbox = QVBoxLayout()

        vbox.addLayout(hbox)

        self.setLayout(vbox)





app = QApplication([sys.argv])
window = Window()
window.show()
sys.exit(app.exec_())



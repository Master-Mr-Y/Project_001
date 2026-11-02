from PySide6.QtWidgets import QApplication,QWidget, QLabel, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys
app = QApplication(sys.argv)
window = QWidget()
 
window.resize(1000,500)

image = QLabel(window)


pixmap = QPixmap("../assets/logo.png")

image.setPixmap(pixmap)

image.setScaledContents(True)

image.resize(50,50)
 

window.show()
sys.exit(app.exec())
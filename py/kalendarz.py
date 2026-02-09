import sys
import pyQt5.QtWidgets
# from layout_colorWidget import color

# from PyQt5.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __def__(self):
        super().__init__()

        self.setWindowTitle("calendarz")

        self.label = QLabel()
        
app = QAppLication(sys.arry)
window = MainWindow()
window.show()
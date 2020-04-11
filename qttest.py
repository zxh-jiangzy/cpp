import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
import untitled

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

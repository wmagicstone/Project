from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import ytbui
from functools import partial
import InternalRun

if __name__ == '__main__':
    directory = '1'
    app = QApplication(sys.argv)
    MainWindows = QMainWindow()
    ui = ytbui.Ui_MainWindow()
    ui.setupUi(MainWindows)
    MainWindows.show()
    ui.pushButton_2.clicked.connect(partial(InternalRun.selectDialog, MainWindows, ui))
    ui.pushButton.clicked.connect(partial(InternalRun.final, ui))
    sys.exit(app.exec())

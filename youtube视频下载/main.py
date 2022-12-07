from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import ytbui
from pytube import YouTube
from functools import partial


def download_url(ui):
    download_url_content = ui.lineEdit.text()
    return download_url_content


def down_dir(ui):
    down_dir_path = ui.lineEdit_2.text()
    return down_dir_path


def downloadvideo(url, dirpath):
    yt = YouTube(url)
    yd = yt.streams.get_highest_resolution()
    yd.download(dirpath)
    print('true')


def final():
    url = download_url(ui)
    dir = down_dir(ui)
    downloadvideo(url, dir)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindows = QMainWindow()
    ui = ytbui.Ui_MainWindow()
    ui.setupUi(MainWindows)
    MainWindows.show()
    ui.pushButton.clicked.connect(final)
    sys.exit(app.exec())

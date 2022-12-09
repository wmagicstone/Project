from PyQt5.QtWidgets import QFileDialog
from pytube import YouTube

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


def selectDialog(mainwindow, ui):
    directory = QFileDialog.getExistingDirectory(mainwindow, '选择目录', '/path/to/default/directory')
    ui.lineEdit_2.setText(directory)


def final(ui):
    url = download_url(ui)
    dir = down_dir(ui)
    downloadvideo(url, dir)


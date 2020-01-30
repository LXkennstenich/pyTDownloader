from __future__ import unicode_literals
import os
from PyQt5 import uic, QtWidgets
import youtube_dl


class MainWindow(QtWidgets.QMainWindow):
    """
    Hauptfenster

    """

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + '/gui/main_window.ui', self)
        self.completed_downloads_listWidget = self.findChild(QtWidgets.QListWidget, "completed_downloads_listWidget")
        self.current_download_label = self.findChild(QtWidgets.QLabel, "current_download_label")
        self.download_pushButton = self.findChild(QtWidgets.QPushButton, "download_pushButton")
        self.progressBar = self.findChild(QtWidgets.QProgressBar, "progressBar")
        self.quality_comboBox = self.findChild(QtWidgets.QComboBox, "quality_comboBox")
        self.video_url_lineEdit = self.findChild(QtWidgets.QLineEdit, "video_url_lineEdit")
        self.video_url_lineEdit.textChanged.connect(self.video_url_lineEdit_finished)
        self.download_pushButton.clicked.connect(self.download_pushButton_clicked)

    def video_url_lineEdit_finished(self):
        print("hole video infos")

    def download_pushButton_clicked(self):
        url = self.video_url_lineEdit.text()
        with youtube_dl.YoutubeDL() as ydl:
            print("downloading")
            ydl.add_progress_hook(self.progress)
            ydl.download([url])

    def progress(self, progress):
        print(progress)

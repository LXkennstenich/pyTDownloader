from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal
import os


class SyncFilesThread(QThread):
    """
    thread for fetching information about a video

    """

    url = ""
    file_list = []
    files = pyqtSignal(list)

    def __init__(self):
        """
        init function

        """
        QThread.__init__(self)

    def __del__(self):
        """
        stops the thread

        :return: None
        :rtype: None
        """
        self.wait()

    def run(self):
        while True:
            self.file_list.clear()
            for entry in os.scandir(os.curdir + '/PyTDownloader'):
                self.file_list.append(entry)
            self.files.emit(self.file_list)
            sleep(1)

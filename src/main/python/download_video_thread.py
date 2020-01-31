import youtube_dl
from PyQt5.QtCore import QThread, pyqtSignal


class Download_Video_Thread(QThread):
    url = ""
    download_progress = pyqtSignal(dict)
    format = None

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def progress(self, progress):
        """
        Emit a signal to the main window for updating the user interface

        :param progress: The Progress Dictionary
        :type progress: dict
        :return: None
        :rtype: None
        """
        self.download_progress.emit(progress)

    def run(self):
        """

        :return:
        :rtype:
        """
        if self.url is not None:
            download_options = {
                'format': self.format
            }
            with youtube_dl.YoutubeDL(download_options) as ydl:
                ydl.add_progress_hook(self.progress)
                ydl.download([self.url])

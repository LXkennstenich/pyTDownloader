import os

import youtube_dl
from PyQt5.QtCore import QThread, pyqtSignal


class DownloadVideoThread(QThread):
    """
    Thread for downloading task
    Let the UI feel responsive while doing work :P
    """

    url = ""
    download_progress = pyqtSignal(dict)
    format = None
    audio_only = False

    def __init__(self):
        """
        init the parent model
        """
        QThread.__init__(self)

    def __del__(self):
        """
        stops the thread

        :return: None
        :rtype: None
        """
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

    def generate_output_template(self):
        return os.curdir + '/PyQt_YTDownloader/%(title)s.%(ext)s'

    def run(self):
        """
        Will be executed while the thread runs

        :return: None
        :rtype: None
        """
        if self.url is not None:
            format_string = self.format
            download_options = {
                'outtmpl': self.generate_output_template(),
                'quiet': True,
                'format': format_string
            }
            with youtube_dl.YoutubeDL(download_options) as ydl:
                ydl.add_progress_hook(self.progress)
                ydl.download([self.url])

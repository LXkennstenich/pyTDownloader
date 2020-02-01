from PyQt5.QtCore import QThread, pyqtSignal
import youtube_dl


class Info_Thread(QThread):
    """
    thread for fetching information about a video

    """
    
    url = ""
    add_quality_item = pyqtSignal(str, str)

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
        """
        fetches information about the video and creates listwidget-items and emits a
        signal to tell the mainwindow to add the item to the listwidget

        :return: None
        :rtype: None
        """
        info_list = []
        download_options = {
            'quiet': True  # disable verbose output in console
        }
        with youtube_dl.YoutubeDL(download_options) as ydl:
            info_list = ydl.extract_info(self.url, download=False)

        for key in info_list:
            if key == "formats":
                format_list = info_list[key]
                for format_dict in format_list:
                    quality_string = None
                    if format_dict["format_note"] == "tiny":
                        quality_string = "Audio Only - " + format_dict["ext"]
                    elif format_dict["fps"] is not None:
                        quality_string = format_dict["format_note"] + " - " + format_dict["ext"]
                    if quality_string is not None:
                        self.add_quality_item.emit(quality_string, format_dict["format_id"])

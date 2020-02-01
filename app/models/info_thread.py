from PyQt5.QtCore import QThread, pyqtSignal
import youtube_dl


class Info_Thread(QThread):
    url = ""
    add_quality_item = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        info_list = []
        with youtube_dl.YoutubeDL() as ydl:
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

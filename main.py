import sys
from PyQt5.QtWidgets import QApplication
import asyncio

from app.models.main_window import MainWindow

app = QApplication(sys.argv)


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.show()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(sys.exit(app.exec())))

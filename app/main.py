from PyQt5.QtWidgets import QApplication
import sys
from app.gui.main_window import MainWindow

if __name__ == '__main__':
    application = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec())

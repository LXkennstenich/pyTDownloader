from PyQt5.QtWidgets import QApplication
import sys
from app.gui.main_window import MainWindow

app = QApplication(sys.argv)

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

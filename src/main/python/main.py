from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()
    from main_window import MainWindow

    main_window = MainWindow()
    main_window.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

import sys
from PySide6.QtWidgets import QMainWindow,QPushButton,QApplication,QWidget,QHBoxLayout


class CloseWin(QMainWindow):
    def __init__(self):
        super(CloseWin, self).__init__()
        self.setWindowTitle('关闭窗口')
        self.cl_btu = QPushButton('关闭窗口')
        self.cl_btu.clicked.connect(self.onButtonClick)
        layout = QHBoxLayout()
        layout.addWidget(self.cl_btu)       # 放置按钮

        main_frame = QWidget()              # 建立QWidget实例
        main_frame.setLayout(layout)        # 放置层
        self.setCentralWidget(main_frame)
        # self.setCentralWidget(self.cl_btu)  # 放置按钮

    def onButtonClick(self):
        sender = self.sender()
        print(sender.text()+'  被按下')
        qApp = QApplication.instance()
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CloseWin()
    win.show()
    sys.exit(app.exec())
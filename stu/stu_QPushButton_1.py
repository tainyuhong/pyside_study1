import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        layout = QVBoxLayout()
        # 普通按钮
        self.btn1 = QPushButton('按钮1')
        self.btn1.setChecked(True)
        self.btn1.toggle()
        layout.addWidget(self.btn1)
        self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))     # 通过lambda给槽函数传入值
        self.btn1.clicked.connect(self.btnstate)    # 指定按钮点击信号发射到槽函数btnstate()
        # 带图标的按钮
        self.btn2 = QPushButton('图片按钮')
        self.btn2.setIcon(QIcon(QPixmap('img/3.ico')))
        self.btn2.setChecked(True)
        self.btn2.clicked.connect(lambda: self.whichbtn(self.btn2))
        layout.addWidget(self.btn2)
        # 不可用状态按钮
        self.btn3 = QPushButton('不可用按钮')
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)
        # 快捷键按钮
        self.btn4 = QPushButton('下载&D')
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda: self.whichbtn(self.btn4))
        layout.addWidget(self.btn4)
        self.btn4.clicked.connect(self.btnstate)

        self.setWindowTitle('标题Demo')
        self.setLayout(layout)

    # 定义一个按钮点击事件
    def btnstate(self):
        if self.btn1.isChecked():
            print("按钮被按了")
        else:
            print('按钮被释放了')

    # 显示点击按钮名称
    def whichbtn(self, btn):
        print("点击按钮", btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec())

import sys
from PySide6.QtGui import  *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class RadioDemo(QWidget):
    def __init__(self):
        super(RadioDemo, self).__init__()
        layout = QVBoxLayout()

        # 添加单选按钮
        self.btn1 = QRadioButton('语文')
        # self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda :self.display_select(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2 = QRadioButton('数学')
        self.btn2.toggled.connect(lambda :self.display_select(self.btn2))
        layout.addWidget(self.btn2)

        self.btn3 = QRadioButton('英语')
        self.btn3.toggled.connect(lambda :self.display_select(self.btn3))

        layout.addWidget(self.btn3)

        self.setLayout(layout)

    def display_select(self,btn):
        # 如果按钮为被选定状态，则显示按钮选项
        if btn.isChecked() == True:
            print(btn.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = RadioDemo()
    radio_win.show()
    sys.exit(app.exec())
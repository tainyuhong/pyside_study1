import sys
from PySide6.QtGui import  *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class CheckBoxDemo(QWidget):
    def __init__(self):
        super(CheckBoxDemo, self).__init__()
        # 组合框
        groupBox = QGroupBox("复选框1")
        groupBox.setFlat(False)

        groupBox1 = QGroupBox("复选框2")
        groupBox1.setFlat(False)

        # 添加多选按钮到组合框中
        layout = QHBoxLayout()      # 组合框1中布局
        self.check_btn1 = QCheckBox('语文')
        self.check_btn1.toggled.connect(lambda :self.display_select(self.check_btn1))
        layout.addWidget(self.check_btn1)

        self.check_btn2 = QCheckBox('数学')
        self.check_btn2.toggled.connect(lambda :self.display_select(self.check_btn2))
        layout.addWidget(self.check_btn2)

        self.check_btn3 = QCheckBox('英语')
        self.check_btn3.toggled.connect(lambda :self.display_select(self.check_btn3))
        layout.addWidget(self.check_btn3)

        # 组合框2中按钮内容
        layout2 = QHBoxLayout()  # 组合框1中布局
        self.check_btn4 = QCheckBox('语文')
        self.check_btn4.toggled.connect(lambda: self.display_select(self.check_btn4))
        layout2.addWidget(self.check_btn4)

        self.check_btn5 = QCheckBox('数学')
        self.check_btn5.toggled.connect(lambda: self.display_select(self.check_btn5))
        layout2.addWidget(self.check_btn5)

        groupBox.setLayout(layout)
        groupBox1.setLayout(layout2)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox1)
        self.setLayout(mainLayout)
        self.setWindowTitle('复选框示例')

    def display_select(self,btn):
        # 如果按钮为被选定状态，则显示按钮选项
        if btn.isChecked() == True:
            print(btn.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = CheckBoxDemo()
    radio_win.show()
    sys.exit(app.exec())
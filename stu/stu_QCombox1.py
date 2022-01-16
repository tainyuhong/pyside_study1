import sys
from PySide6.QtGui import  *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class ComBoxDemo(QWidget):
    def __init__(self):
        super(ComBoxDemo, self).__init__()
        self.setWindowTitle('组合框实例')
        mainLayout = QHBoxLayout()
        self.lb1 = QLabel("开发语言")
        self.combox1 = QComboBox()       # 创建组合框实例
        self.combox1.addItems(['Java','C','C++'])    # 添加多个选项
        self.combox1.addItem('Python')       # 添加一个选项
        # self.combox1.currentIndexChanged.connect(self.selectionchange)    # 下拉菜单索引发生改变时触发槽函数
        self.combox1.activated.connect(self.selectionchange)        # 下拉菜单选项发生改变时触发槽函数，与上产生的效果相同
        mainLayout.addWidget(self.lb1)
        mainLayout.addWidget(self.combox1)
        self.setLayout(mainLayout)

    # 选项变更
    def selectionchange(self,i):
        self.lb1.setText(self.combox1.currentText())
        print('选项值为：',self.combox1.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = ComBoxDemo()
    radio_win.show()
    sys.exit(app.exec())
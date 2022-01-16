import sys
from PySide6.QtGui import  *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class sbinboxDemo(QWidget):
    def __init__(self):
        super(sbinboxDemo, self).__init__()
        self.setWindowTitle('计数器使用实例')
        mainLayout = QVBoxLayout()
        self.lb1 = QLabel("计数器当值值：")
        self.sp = QSpinBox()       # 创建计数器实例
        self.sp.setRange(0,99)
        self.sp.setSingleStep(2)
        self.sp.valueChanged.connect(self.selectionchange)
        mainLayout.addWidget(self.lb1)
        mainLayout.addWidget(self.sp)
        self.setLayout(mainLayout)

    # 读取计数器值
    def selectionchange(self,i):
        self.lb1.setText('计数器当值值：'+str(self.sp.value()))
        print('选项值为：', self.sp.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = sbinboxDemo()
    radio_win.show()
    sys.exit(app.exec())
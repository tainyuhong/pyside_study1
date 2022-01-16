import sys
from PySide6.QtGui import  *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class sbinboxDemo(QWidget):
    def __init__(self):
        super(sbinboxDemo, self).__init__()
        self.setWindowTitle('Pyside6滑块使用实例')
        mainLayout = QVBoxLayout()
        self.lb1 = QLabel("滑块当值值：")
        self.slider = QSlider(Qt.Horizontal)       # 创建计数器实例
        self.slider.setRange(0, 100)    # 设置滑动值范围
        self.slider.setSingleStep(1)       # 设置步长，只能为整数
        self.slider.setTickPosition(QSlider.TicksBelow)   # 设置滑块刻度显示在下方，默认不显示刻度
        self.slider.valueChanged.connect(self.selectionchange)      # 当触发信号valueChanged时调用槽函数selectionchange
        self.slider.setTickInterval(5)      # 设置刻度间隔
        mainLayout.addWidget(self.lb1)
        mainLayout.addWidget(self.slider)
        self.setLayout(mainLayout)

    # 读取计数器值
    def selectionchange(self,i):
        self.lb1.setText('计数器当值值：' + str(self.slider.value()))
        print('选项值为：', self.slider.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = sbinboxDemo()
    radio_win.show()
    sys.exit(app.exec())
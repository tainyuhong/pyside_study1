import sys
from PySide6.QtWidgets import QWidget,QApplication,QFormLayout,QLineEdit
from PySide6.QtGui import QIntValidator,QDoubleValidator,QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIcon

# 输入掩码案例
class Winform(QWidget):
    def __init__(self):
        super(Winform, self).__init__()
        self.initUI()

        flo = QFormLayout()     # 添加表单布局
        e1 = QLineEdit()
        e2 = QLineEdit()
        e3 = QLineEdit()
        e4 = QLineEdit()
        e5 = QLineEdit()
        e6 = QLineEdit()

        e1.setValidator(QIntValidator())        # 设置成只允许输入数字
        e3.setInputMask('000.000.000.000;_')     # 设置掩码格式

        # 将QLineEdit添加到表单布局
        flo.addRow('integer validator整数', e1)
        flo.addRow('Double validator浮点数', e2)
        flo.addRow('Input Mask子网掩码', e3)
        flo.addRow('Text changed文本', e4)
        flo.addRow('Password密码', e5)
        flo.addRow('Read only只读', e6)

        self.setLayout(flo)
    # 初始化窗口
    def initUI(self):
        self.setGeometry(200,300,400,150)
        self.setWindowTitle('QLineEdit综合实例')
        self.setWindowIcon(QIcon('img/74.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Winform()
    icon.show()
    sys.exit(app.exec())
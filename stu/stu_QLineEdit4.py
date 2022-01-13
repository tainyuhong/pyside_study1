import sys
from PySide6.QtWidgets import QWidget,QApplication,QFormLayout,QLineEdit
from PySide6.QtGui import QIntValidator,QDoubleValidator,QRegularExpressionValidator
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

# 综合案例
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

        # 1、允许输入整数
        # 2、限制输入小数点后2位
        # 3、输入子网掩码
        # 4、文本格式。需要发射信号textChanged，连接到槽函数display_text()
        # 5、显示密码，发射editingfinished信号连接到槽函数enterPress()
        # 6、显示一个默认的文本，不能编辑

        e1.setValidator(QIntValidator())        # 设置成只允许输入数字
        e2.setValidator(QDoubleValidator(0,99,2))   # 设置为只允许输入浮点数
        e3.setInputMask('000.000.000.000;_')     # 设置掩码格式
        e5.setEchoMode(QLineEdit.Password)      # 设置为显示密码字符
        e5.editingFinished.connect(self.print_pass)
        e6.setReadOnly(True)        # 设置为只读


        e4.textChanged.connect(self.display_text)


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

    def display_text(self,text):
        print('输入：',text)

    def print_pass(self):
        print('输入了密码')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Winform()
    icon.show()
    sys.exit(app.exec())
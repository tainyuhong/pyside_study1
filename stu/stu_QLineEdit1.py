import sys
from PySide6.QtWidgets import QWidget,QApplication,QFormLayout,QLineEdit
from PySide6.QtGui import QIcon

# 创建一个Icon类，继承QWidget类
class Winform(QWidget):
    def __init__(self):
        super(Winform, self).__init__()
        self.initUI()

        flo = QFormLayout()     # 添加表单布局
        pNormal_L = QLineEdit()
        pNoEcho_L = QLineEdit()
        pPassword_l = QLineEdit()
        pPasswordEchoL = QLineEdit()

        # 将QLineEdit添加到表单布局
        flo.addRow('Normal',pNormal_L)
        flo.addRow('NoEcho',pNoEcho_L)
        flo.addRow('Password',pPassword_l)
        flo.addRow('PasswordEchoOnEdit',pPasswordEchoL)

        # 设置文本框悬浮文本显示
        pNormal_L.setPlaceholderText(('Normal'))
        pNoEcho_L.setPlaceholderText(('NoEcho'))
        pPassword_l.setPlaceholderText(('Password'))
        pPasswordEchoL.setPlaceholderText(('PasswordEchoOnEdit'))

        # 设置显示效果
        pNormal_L.setEchoMode((QLineEdit.Normal))
        pNoEcho_L.setEchoMode((QLineEdit.NoEcho))
        pPassword_l.setEchoMode((QLineEdit.Password))
        pPasswordEchoL.setEchoMode((QLineEdit.PasswordEchoOnEdit))

        self.setLayout(flo)
    # 初始化窗口
    def initUI(self):
        self.setGeometry(200,300,400,150)
        self.setWindowTitle('QLineEdit例子')
        self.setWindowIcon(QIcon('img/74.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Winform()
    icon.show()
    sys.exit(app.exec())
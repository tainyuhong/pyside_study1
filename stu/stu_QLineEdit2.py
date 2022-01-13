import sys
from PySide6.QtWidgets import QWidget,QApplication,QFormLayout,QLineEdit
from PySide6.QtGui import QIntValidator,QDoubleValidator,QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIcon

# 密码验证器
class Winform(QWidget):
    def __init__(self):
        super(Winform, self).__init__()
        self.initUI()

        flo = QFormLayout()     # 添加表单布局
        pIntLineEdit = QLineEdit()
        pDoubleLineEdit = QLineEdit()
        pValidatorLineEdit = QLineEdit()

        # 将QLineEdit添加到表单布局
        flo.addRow('整型', pIntLineEdit)
        flo.addRow('浮点型', pDoubleLineEdit)
        flo.addRow('字母和数字', pValidatorLineEdit)

        # 设置文本框悬浮文本显示
        pIntLineEdit.setPlaceholderText(('整型'))
        pDoubleLineEdit.setPlaceholderText(('浮点型'))
        pValidatorLineEdit.setPlaceholderText(('字母和数字'))

        # 设置显示效果
        pIntValidator = QIntValidator(self)     # 设置为整型
        pIntValidator.setRange(1,99)            # 设置范围为1-99
        pIntLineEdit.setValidator(pIntValidator)    # 设置验证规则为整型

        pDoubleValidator = QDoubleValidator(self)  # 设置为浮点型
        pDoubleValidator.setRange(-360,360)  # 设置范围为【-360，360】
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)  # 设置符号
        pDoubleValidator.setDecimals(2)
        pDoubleLineEdit.setValidator(pDoubleValidator)      # 设置验证规则为浮点型

        # 字母或数字
        reg = QRegularExpression('[a-zA-Z0-9]+$')
        pValidator = QRegularExpressionValidator(self)  # 设置为字母或数字
        pValidator.setRegularExpression(reg)  # 设置范围为正则表达式中字母
        pValidatorLineEdit.setValidator(pValidator)  # 设置验证规则为整型

        self.setLayout(flo)
    # 初始化窗口
    def initUI(self):
        self.setGeometry(200,300,400,150)
        self.setWindowTitle('密码验证器')
        self.setWindowIcon(QIcon('img/74.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Winform()
    icon.show()
    sys.exit(app.exec())
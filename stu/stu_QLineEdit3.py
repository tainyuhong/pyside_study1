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
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDATELineEdit = QLineEdit()
        plicenseLineEdit = QLineEdit()

        # 设置掩码格式
        pIPLineEdit.setInputMask('000.000.000.000')
        pMACLineEdit.setInputMask('HH:HH:HH:HH:HH:HH:HH:HH')
        pDATELineEdit.setInputMask('0000-00-00')
        plicenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA')

        # 将QLineEdit添加到表单布局
        flo.addRow('IP', pIPLineEdit)
        flo.addRow('MAC', pMACLineEdit)
        flo.addRow('日期', pDATELineEdit)
        flo.addRow('许可号', plicenseLineEdit)

        self.setLayout(flo)
    # 初始化窗口
    def initUI(self):
        self.setGeometry(200,300,400,150)
        self.setWindowTitle('掩码输入实例')
        self.setWindowIcon(QIcon('img/74.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Winform()
    icon.show()
    sys.exit(app.exec())
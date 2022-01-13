import sys
from PySide6.QtWidgets import QWidget,QApplication,QToolTip,QLabel,QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont,QIcon,QPixmap,QPalette

# 创建一个Icon类，继承QWidget类
class Winform(QWidget):
    def __init__(self):
        super(Winform, self).__init__()
        self.initUI()
        # 创建标签实例
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 初始化标签杆件
        label1.setText('这是一个文本标签')
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python Gui应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('tuzi.bmp'))

        label4.setText("<a href='#'>http://www.baidu.com</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        # 创建一个布局，将标签添加至其中
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)
        vbox.addStretch()

        self.setLayout(vbox)

        label1.setOpenExternalLinks(True)

    # 初始化窗口
    def initUI(self):
        QToolTip.setFont(QFont('Arial', 10))
        self.setToolTip('这是一个<b>气泡提示</b>')
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('气泡提示')
        self.setWindowIcon(QIcon('img/74.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Winform()
    icon.show()
    sys.exit(app.exec())
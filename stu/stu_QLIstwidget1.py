import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ListWidget(QListWidget):
    def clicked(self,item):
        QMessageBox.information(self,'ListWidget','你选择了：'+ item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    listwidget = ListWidget()
    listwidget.resize(300,120)
    listwidget.addItems(['条目1','条目2','条目3','条目4','条目5'])
    listwidget.setWindowTitle('ListWidget使用实例')
    listwidget.itemClicked.connect(listwidget.clicked)
    listwidget.show()
    sys.exit(app.exec())
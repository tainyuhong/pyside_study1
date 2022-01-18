import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = QDir()
    treeview1 = QTreeView()  # 创建QTreeView实例
    treeview1.setModel(model)
    treeview1.setWindowTitle('QTreeView实例')
    treeview1.resize(640,480)
    treeview1.show()
    sys.exit(app.exec())

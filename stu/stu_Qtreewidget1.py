import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *



class TreewidgetDome(QWidget):
    def __init__(self):
        super(TreewidgetDome, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTreeWidget案例')
        self.resize(400, 300)
        conLayout = QHBoxLayout()
        treeWidget = QTreeWidget()  # 创建树形实例
        treeWidget.setColumnCount(2)    # 设置列类
        treeWidget.setColumnWidth(0, 160)  # 设置第一列的宽度
        # treeWidget.setColumnWidth(0, 100)  # 设置第二列的宽度
        treeWidget.setHeaderLabels(['机房','机柜'])    # 设置表头，不设置时默认显示数字
        # 设置根节点
        root = QTreeWidgetItem(treeWidget)
        root.setText(0,'同城灾备中心')
        root.setIcon(0,QIcon('img/007.gif'))    # 设置根节点图标

        # 设置子节点1
        ch1 = QTreeWidgetItem(root)
        ch1.setText(0,'ZB-1')
        ch1.setText(1,'A01')

        # 设置子节点2
        ch2 = QTreeWidgetItem(root)
        ch2.setText(0, 'ZB-2')
        ch2.setText(1, 'C01')

        # 设置子节点3
        ch1 = QTreeWidgetItem(ch2)
        ch1.setText(0, 'A01')
        ch1.setText(1, '1U')

        treeWidget.expandAll()  # 全部展开

        conLayout.addWidget(treeWidget)
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TreewidgetDome()
    example.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class tableViewDemo(QWidget):
    def __init__(self):
        super(tableViewDemo, self).__init__()

        self.setWindowTitle('Pyside6  QTableView表视图使用实例')
        self.resize(700,400)
        self.model = QStandardItemModel(4,4)        # 创建表实例4行4列
        self.model.setHorizontalHeaderLabels(['第一列','第二列','第三列','第四列'])     # 设置表列名
        for row in  range(4):
            for col in range(4):
                item = QStandardItem('第{}行第{}列'.format(row+1,col+1))
                self.model.setItem(row,col,item)
        self.tableView=QTableView()
        self.tableView.setModel(self.model)
        # self.tableView.horizontalHeader().setStretchLastSection(True)       # 最后一列填充剩下空间
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)     # 所有列自动拉伸充满界面
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.tableView)
        self.setLayout(mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = tableViewDemo()
    radio_win.show()
    sys.exit(app.exec())
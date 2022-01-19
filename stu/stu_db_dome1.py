import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel,QSqlQueryModel

class db_page(QWidget):
    def __init__(self):
        super(db_page, self).__init__()
        operatorLayout = QHBoxLayout()
        self.preBtn = QPushButton('前一页')
        self.nextBtn = QPushButton('下一页')
        self.switchbtn = QPushButton('Go')
        self.switchLe = QLineEdit()         # 输入页数文本框
        self.switchLe.setFixedWidth(40)
        switchpage = QLabel('转到第')
        page = QLabel('页')

        operatorLayout.addWidget(self.preBtn)       # 上一面
        operatorLayout.addWidget(self.nextBtn)       # 下一面
        operatorLayout.addWidget(switchpage)        # 转到第
        operatorLayout.addWidget(self.switchLe)     # 输入页数文本框
        operatorLayout.addWidget(page)              # 页
        operatorLayout.addWidget(self.switchbtn)       # 跳转执行按钮
        operatorLayout.addWidget(QSplitter())

        # 创建表格
        self.tableview1 = QTableView()
        self.tableview1.horizontalHeader().setStretchLastSection(True)
        self.tableview1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 创建状态栏
        statusbar = QStatusBar()
        statuslay = QHBoxLayout()
        statuslay.addWidget(statusbar)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.tableview1)
        self.setTableView()
        mainLayout.addLayout(operatorLayout)

        mainLayout.addLayout(statuslay)

        self.setLayout(mainLayout)
        self.setWindowTitle('分页查询实例')
        self.resize(430,450)

    def setTableView(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('testdb.db')
        self.db.open()
        print('数据库连接成功')
        self.queryMode = QSqlQueryModel()
        self.recordQuery(0)
        self.tableview1.setModel(self.queryMode)
        self.queryMode.setHeaderData(0,Qt.Horizontal,'编号')
        self.queryMode.setHeaderData(1,Qt.Horizontal,'姓名')
        self.queryMode.setHeaderData(2,Qt.Horizontal,'性别')
        self.queryMode.setHeaderData(3,Qt.Horizontal,'年龄')
        self.queryMode.setHeaderData(4,Qt.Horizontal,'院系')

    def recordQuery(self,limitIndex):
        # szQuery = "select * from student "
        szQuery = ("select * from student limit {},{}" .format(limitIndex,5))
        data = self.queryMode.setQuery(szQuery)
        print('data',data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    page_demo = db_page()
    page_demo.show()
    sys.exit(app.exec())
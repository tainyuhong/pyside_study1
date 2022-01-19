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
        self.switchLe.setValidator(QIntValidator() )  # 限制只允许输入整数
        self.switchLe.setFixedWidth(40)
        switchpage = QLabel('转到第')
        page = QLabel('页')
        # 初始化当前页、总页数、每页显示记录数
        self.currentPage = 1
        self.totalPage = 0
        self.totalRecrodCount =0
        self.PageRecordCount = 6
        self.table_labels = ['编号','姓名','性别','年龄','院系']  # 表头名称

        operatorLayout.addWidget(self.preBtn)       # 上一面
        operatorLayout.addWidget(self.nextBtn)       # 下一面
        operatorLayout.addWidget(switchpage)        # 转到第
        operatorLayout.addWidget(self.switchLe)     # 输入页数文本框
        operatorLayout.addWidget(page)              # 页
        operatorLayout.addWidget(self.switchbtn)       # 跳转执行按钮
        operatorLayout.addWidget(QSplitter())

        # 定义按钮事件
        self.nextBtn.clicked.connect(self.nextPage)     # 定义下一页按钮事件
        self.preBtn.clicked.connect(self.upPage)        # 定义上一页按钮事件
        self.switchbtn.clicked.connect(self.switchpage)        # 定义跳转到页按钮事件

        # 创建表格
        self.tableview1 = QTableView()
        self.tableview1.horizontalHeader().setStretchLastSection(True)
        self.tableview1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 创建状态栏
        self.statusbar = QStatusBar()
        self.statusbar.showMessage('准备就绪')
        statuslay = QHBoxLayout()
        statuslay.addWidget(self.statusbar)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.tableview1)
        self.setTableView()
        mainLayout.addLayout(operatorLayout)

        mainLayout.addLayout(statuslay)

        self.setLayout(mainLayout)
        self.setWindowTitle('分页查询实例')
        self.resize(430,450)
    def closeEvent(self, event):
        # 关闭数据库
        self.db.close()

    # 连接数据库，并初始化表头信息，初始化表格数据
    def setTableView(self):
        # 连接sqlite数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('testdb.db')
        self.db.open()
        print('数据库连接成功')
        # 声明查询模型
        self.queryMode = QSqlQueryModel()
        self.total_info()
        self.statusbar.showMessage('总共 【{}】 页，共 【{}】 条记录。'.format(self.totalPage,self.totalRecrodCount))
        # 从第1条记录开始查询，第一条索引为0
        self.recordQuery(0)
        # 设置表视图模型为QSqlQueryModel
        self.tableview1.setModel(self.queryMode)
        # 设置表视图的列名
        for col,label in enumerate(self.table_labels):
            self.queryMode.setHeaderData(col, Qt.Horizontal, label)
        # self.queryMode.setHeaderData(0,Qt.Horizontal,'编号')
        # self.queryMode.setHeaderData(1,Qt.Horizontal,'姓名')
        # self.queryMode.setHeaderData(2,Qt.Horizontal,'性别')
        # self.queryMode.setHeaderData(3,Qt.Horizontal,'年龄')
        # self.queryMode.setHeaderData(4,Qt.Horizontal,'院系')

    # 获取总记录数及总页数
    def total_info(self):
        # 获取要查询的表中总记录数及页数判断
        sql = "select * from student"
        self.queryMode.setQuery(sql)
        # print('总data', self.queryMode.rowCount())
        self.totalRecrodCount = self.queryMode.rowCount()
        if self.totalRecrodCount % self.PageRecordCount == 0:
            self.totalPage = (self.totalRecrodCount // self.PageRecordCount)
        else:
            self.totalPage = (self.totalRecrodCount // self.PageRecordCount) +1
        # print('总页数',self.totalPage)
        return self.totalRecrodCount,self.totalPage

    # 定义查询记录语句
    def recordQuery(self,limitIndex):
        szQuery = ("select * from student limit {},{}" .format(limitIndex,self.PageRecordCount))       # limitIndex:索引开始点；5为每页5条记录
        # 执行查询SQL
        self.queryMode.setQuery(szQuery)

    # 下一页查询事件
    def nextPage(self):
        if self.currentPage < self.totalPage:
            limiIndex = (self.currentPage)*self.PageRecordCount   # 获取当前索引号
            self.recordQuery(limiIndex)
            self.currentPage += 1
            # print('向后--当前页', self.currentPage)
        else:
            print('已是最后一页')
            return

    # 上一页查询事件
    def upPage(self):
        limiIndex = (self.currentPage-2)*self.PageRecordCount   # 获取当前索引号

        self.currentPage -= 1
        if limiIndex >= 0:
            self.recordQuery(limiIndex)
            # print('向前--当前页', self.currentPage)
            # print('limiIndex:',limiIndex)
        else:
            print('已是第一页了' )
            self.currentPage = 1    # 当索引小于0时，设置默认当前页为第一页
            # print('向前--当前页', self.currentPage)
            return

    # 跳转到指定的页
    def switchpage(self):
        page = self.switchLe.text()
        if page == '':
            QMessageBox.information(self,'提示','请输入跳转页数')
            return
        elif int(page) > 0:
            page = int(page)
            limiIndex = (page-1) * self.PageRecordCount  # 获取当前索引号
            # print(limiIndex)
            self.currentPage = page
            self.recordQuery(limiIndex)
        else:
            QMessageBox.information(self, '提示', '请输入正确的跳转页数')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    page_demo = db_page()
    page_demo.show()
    sys.exit(app.exec())
from PySide6.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel,QSqlQueryModel
from PySide6.QtCore import *

class DataGrid():
    def __init__(self):
        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 总数页文本
        self.totalPageLabel = None
        # 当前页文本
        self.currentPageLabel = None
        # 转到页输入框
        self.switchPageLineEdit = None
        # 前一页按钮
        self.prevButton = None
        # 后一页按钮
        self.nextButton = None
        # 转到页按钮
        self.switchPageButton = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecrodCount = 0
        # 每页显示记录数
        self.PageRecordCount = 5
        self.db = None
        self.table_labels = []

    # 关闭数据库事件
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
        # self.statusbar.showMessage('总共 【{}】 页，共 【{}】 条记录。'.format(self.totalPage, self.totalRecrodCount))
        # 从第1条记录开始查询，第一条索引为0
        self.recordQuery(0)
        # 设置表视图模型为QSqlQueryModel
        self.tableview1.setModel(self.queryMode)
        # 设置表视图的列名
        for col, label in enumerate(self.table_labels):
            self.queryMode.setHeaderData(col, Qt.Horizontal, label)

    # 获取总记录数及总页数
    def total_info(self):
        # 获取要查询的表中总记录数及页数判断
        sql = "select * from student"
        self.queryMode.setQuery(sql)
        print('总data', self.queryMode.rowCount())
        self.totalRecrodCount = self.queryMode.rowCount()
        if self.totalRecrodCount % self.PageRecordCount == 0:
            self.totalPage = (self.totalRecrodCount // self.PageRecordCount)
        else:
            self.totalPage = (self.totalRecrodCount // self.PageRecordCount) + 1
        print('总页数',self.totalPage)
        return self.totalRecrodCount, self.totalPage

    # 定义查询记录语句
    def recordQuery(self, limitIndex):
        szQuery = ("select * from student limit {},{}".format(limitIndex,
                                                              self.PageRecordCount))  # limitIndex:索引开始点；5为每页5条记录
        # 执行查询SQL
        self.queryMode.setQuery(szQuery)

    # 下一页查询事件
    def nextPage(self):
        if self.currentPage < self.totalPage:
            limiIndex = (self.currentPage) * self.PageRecordCount  # 获取当前索引号
            self.recordQuery(limiIndex)
            self.currentPage += 1
            # print('向后--当前页', self.currentPage)
        else:
            print('已是最后一页')
            return

    # 上一页查询事件
    def upPage(self):
        limiIndex = (self.currentPage - 2) * self.PageRecordCount  # 获取当前索引号
        self.currentPage -= 1
        if limiIndex >= 0:
            self.recordQuery(limiIndex)
            # print('向前--当前页', self.currentPage)
            # print('limiIndex:',limiIndex)
        else:
            print('已是第一页了')
            self.currentPage = 1  # 当索引小于0时，设置默认当前页为第一页
            # print('向前--当前页', self.currentPage)
            return

    # 跳转到指定的页
    def switchpage(self):
        page = self.switchPageLineEdit.text()
        if page == '':
            # QMessageBox.information(self, '提示', '请输入跳转页数')
            return
        elif int(page) > 0:
            page = int(page)
            limiIndex = (page - 1) * self.PageRecordCount  # 获取当前索引号
            # print(limiIndex)
            self.currentPage = page
            self.recordQuery(limiIndex)
        else:
            # QMessageBox.information(self, '提示', '请输入正确的跳转页数')
            print('请输入正确的跳转页数')


if __name__ == '__main__':
    db = DataGrid()
    d = db.total_info
    print(d)
    print(db.totalRecrodCount)
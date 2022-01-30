import sys
from PySide6 import QtWidgets, QtGui, QtCore
from MachineSelect import *
from db_handler import *


class Ui_MachineSelect(QtWidgets.QMainWindow, Ui_MachineSelect):
    def __init__(self, parent=None):
        super(Ui_MachineSelect, self).__init__(parent)
        self.setupUi(self)
        # 设置表格相关信息
        self.select_table.setHorizontalHeaderLabels(
            ['ID', '机房', '机柜', 'U位', 'U数', '设备类型', '设备品牌', '设备型号', '设备序列号', '设备名称', '设备IP', '设备管理员'])
        self.select_table.setStyleSheet("alternate-background-color: SkyBlue;background-color: Azure;")  # 设置行的交替显示背景颜色

        # 初始化定义分页信息
        # self.pre_page = None
        # self.next_page = None
        # self.first_page = None
        # self.last_page = None
        # self.total_page_lb = '总页数   '
        self.current_page = 1
        self.select_values = []  # 查询条件值

        # self.firstPage()      # 默认打开页面先查询并显示第一页数据
        # self.data_sql = '''  '''
        self.select_btn.clicked.connect(self.get_input_data)  # 按条件进行查询
        # 分页查询按钮事件
        if self.go_btn.clicked.connect(lambda: self.goToPage(self.data_sql, self.select_values[:-1])):  # 定义转到按钮点击事件
            self.db = DBMysql()     # 点击按钮时创建数据库连接对象
        self.next_btn.clicked.connect(lambda: self.nextPage(self.data_sql, self.select_values[:-1]))  # 定义下一页按钮事件
        self.pre_btn.clicked.connect(lambda: self.prePage(self.data_sql, self.select_values[:-1]))  # 定义上一页按钮事件
        self.home_btn.clicked.connect(lambda: self.firstPage(self.data_sql, self.select_values[:-1]))  # # 定义首页按钮事件
        self.last_btn.clicked.connect(lambda: self.lastPage(self.data_sql, self.select_values[:-1]))  # 定义最后一页事件

    # 根据查询进行查询获取数据
    def get_input_data(self):
        # room = self.room.text()
        # cabinet = self.cabinet.text()
        # machine_name = self.machine_name.text()
        # mg_ip = self.mg_ip.text()
        # print(room, mg_ip, cabinet, machine_name)

        # 根据条件查询设备
        sel_values = []  # 用于保存获取的查询条件列表
        sql = '''select * from machine_list  where 1 = 1 '''

        # 判断并组合查询SQL
        if self.room.text() != '':
            sql = sql + ' and room_name= %s'
            sel_values.append(self.room.text())
        if self.mg_ip.text() != '':
            sql = sql + ' and mg_ip=%s'
            sel_values.append(self.mg_ip.text())
        if self.cabinet.text() != '':
            sql = sql + ' and cab_name=%s'
            sel_values.append(self.cabinet.text())
        if self.machine_name.text() != '':
            sql = sql + ' and machine_name=%s'
            sel_values.append(self.machine_name.text())
        self.data_sql = sql  # 获取按条件查询的sql语句
        self.select_values = sel_values  # 获取查询条件值
        # print('查询条件',sel_values)
        # print('查询SQL',self.data_sql)
        self.recordQuery(self.data_sql, 0, self.select_values)  # 按查询查询记录
        # print('总页数', self.totalPage)
        self.current_page = 1
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数

    # 获取要查询的总页数
    def page_record(self, sql, values):
        # 连接数据库并显示数据至页面
        # print('总页数条件：', values)
        # print('总页数SQL：', sql)
        data = self.db.query_single(self.data_sql, values)  # 获取查询的数据，返回格式为一个内嵌的2元组，格式：（总记录数，数据内容）
        # print('数据条数：',len(data))
        total_record = len(data)  # 查询到的数据总记录条数
        if total_record % 15 == 0:
            self.totalPage = (total_record // 15)
            self.total_page_lb.setText('总页数：{}页'.format(self.totalPage, total_record))  # 分页显示数据
        else:
            self.totalPage = (total_record // 15) + 1
            self.total_page_lb.setText('总页数：{}页'.format(self.totalPage, total_record))  # 分页显示数据
        # print('总页数',self.totalPage)
        return self.totalPage

    # 定义查询记录并显示数据
    def recordQuery(self, sql, limiIndex, sql_args=None):
        '''
        定义查询记录并显示数据
        :param sql:     不带分页功能的查询语句
        :param limiIndex:   sql索引记录开始点
        :param sql_args:    传入sql的参数
        :return:
        '''
        sql_page = sql + ' limit %s,15 '  # 定义分页查询SQL
        # print('sql_page',sql_page)
        # print('limiIndex',limiIndex)
        if sql_args is None:
            page_data = self.db.query_single(sql_page, limiIndex)  # 每页数据内容
        else:
            sql_args.append(limiIndex)  # 将索引记录放入SQL传入的参数列表中
            page_data = self.db.query_single(sql_page, sql_args)  # 每页数据内容
        self.select_table.clearContents()  # 清除所有内容
        for i in range(len(page_data)):
            for _ in range(12):
                if page_data[i][_] is None:
                    self.select_table.setItem(i, _, QTableWidgetItem(''))  # 显示单元格数据
                else:
                    self.select_table.setItem(i, _, QTableWidgetItem(str(page_data[i][_])))  # 显示单元格数据
        self.select_table.resizeColumnsToContents()  # 自适应列宽
        # print('self.select_values',self.select_values)
        self.page_record(self.data_sql, self.select_values[:-1])  # 显示总页数 self.select_values最除索引记录的所有参数

    # 转到指定页事件
    def goToPage(self, sql, sql_args):
        if self.page_input_le.text() != '' and int(self.page_input_le.text()) <= self.totalPage and int(
                self.page_input_le.text()) > 0:
            self.current_page = int(self.page_input_le.text())  # 获取输入的查询页数
            limiIndex = (int(self.page_input_le.text()) - 1) * 15  # 定位查询开始记录索引点
            sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
            self.recordQuery(sql, sql_args)  # 查询数据并进行显示
            self.page_input_le.setText('')
            self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
            if self.current_page == self.totalPage:
                self.pre_btn.setDisabled(False)  # 当为第一页时，按钮可用
                self.next_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
                self.home_btn.setDisabled(False)  # 当为最后一页时，按钮可用
                self.last_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
            elif self.current_page == 1:  # 当索引小于0时，设置默认当前页为第一页
                self.pre_btn.setDisabled(True)  # 当为第一页时，上一页按钮不可用
                self.next_btn.setDisabled(False)  # 当为第一页时，下一页按钮可用
                self.home_btn.setDisabled(True)  # 当为第一页时，首页按钮不可用
                self.last_btn.setDisabled(False)  # 当为第一页时，最后一页按钮不可用
            else:
                self.pre_btn.setDisabled(False)  # 上一页按钮可用
                self.next_btn.setDisabled(False)  # 下一页按钮可用
                self.home_btn.setDisabled(False)  # 首页按钮可用
                self.last_btn.setDisabled(False)  # 最后一页按钮可用

        else:
            QtWidgets.QMessageBox.information(self, '提示', '请输入正确的跳转页数')

    # 下一页查询事件
    def nextPage(self, sql, sql_args):
        # print('self.currentPage',self.current_page)
        # print('self.totalPage',self.totalPage)
        if self.current_page < self.totalPage:
            limiIndex = self.current_page * 15  # 获取当前索引号
            sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
            self.recordQuery(sql, sql_args)  # 传入值进行查询
            # print('当前页：',self.current_page)
            self.pre_btn.setDisabled(False)  # 上一页按钮可用
            self.next_btn.setDisabled(False)  # 下一页按钮可用
            self.home_btn.setDisabled(False)  # 首页按钮可用
            self.last_btn.setDisabled(False)  # 最后一页按钮可用
            # print('向后--当前页', self.currentPage)
        else:
            # print('已是最后一页')
            self.pre_btn.setDisabled(False)  # 当为第一页时，按钮可用
            self.next_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
            self.home_btn.setDisabled(False)  # 当为最后一页时，按钮可用
            self.last_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
            return
        self.current_page += 1
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        # print('当前页：', self.current_page)

    # 上一页查询事件
    def prePage(self, sql, sql_args):
        limiIndex = (self.current_page - 2) * 15  # 获取当前索引号
        self.current_page -= 1
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        if limiIndex >= 0:
            sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
            self.recordQuery(sql, sql_args)
            # print('向前--当前页', self.current_page)
            # print('limiIndex:',limiIndex)
            self.pre_btn.setDisabled(False)
            self.next_btn.setDisabled(False)
            self.home_btn.setDisabled(False)
            self.last_btn.setDisabled(False)
        else:
            # print('已是第一页了')
            self.current_page = 1  # 当索引小于0时，设置默认当前页为第一页
            # print('向前--当前页', self.current_page)
            self.pre_btn.setDisabled(True)  # 当为第一页时，上一页按钮不可用
            self.next_btn.setDisabled(False)  # 当为第一页时，下一页按钮可用
            self.home_btn.setDisabled(True)  # 当为第一页时，首页按钮不可用
            self.last_btn.setDisabled(False)  # 当为第一页时，最后一页按钮不可用
            return

    # 首页查询事件
    def firstPage(self, sql, sql_args):
        limiIndex = 0  # 获取当前索引号
        sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
        self.recordQuery(sql, sql_args)
        self.current_page = 1  # 当索引小于0时，设置默认当前页为第一页
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        self.pre_btn.setDisabled(True)  # 当为第一页时，上一页按钮不可用
        self.next_btn.setDisabled(False)  # 当为第一页时，下一页按钮可用
        self.home_btn.setDisabled(True)  # 当为第一页时，首页按钮不可用
        self.last_btn.setDisabled(False)  # 当为第一页时，最后一页按钮不可用

    # 最后一页查询事件
    def lastPage(self, sql, sql_args):
        # print('最后一页',self.totalPage)
        limiIndex = (self.totalPage - 1) * 15  # 获取当前索引号
        sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
        self.recordQuery(sql, sql_args)
        self.current_page = self.totalPage
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        self.pre_btn.setDisabled(False)  # 当为第一页时，按钮可用
        self.next_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
        self.home_btn.setDisabled(False)  # 当为最后一页时，按钮可用
        self.last_btn.setDisabled(True)  # 当为最后一页时，按钮不可用


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MachineSelect()
    mainWindow.show()
    sys.exit(app.exec())

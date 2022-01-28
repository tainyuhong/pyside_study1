import sys
from PySide6 import QtWidgets,QtGui,QtCore
from MachineSelect import *
from db_handler import *


data_sql = ''' select * from machine_list  where 1=1 '''

class Ui_MachineSelect(QtWidgets.QMainWindow,Ui_MachineSelect):
    def __init__(self,parent=None):
        super(Ui_MachineSelect,self).__init__(parent)
        self.setupUi(self)
        # self.resize(1150,750)
        self.db= DBMysql()


        # 设置表格相关信息
        self.select_table.setHorizontalHeaderLabels(['ID','机房','机柜','U位','U数','设备类型','设备品牌','设备型号','设备序列号','设备名称','设备IP','设备管理员'])
        self.select_table.setStyleSheet("alternate-background-color: SkyBlue;background-color: Azure;")  # 设置行的交替显示背景颜色
        # self.select_table.resizeRowsToContents()        # 自适应行高
        # self.select_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    # # 自适应伸缩模式

        # 初始化定义分页信息
        # self.pre_page = None
        self.next_page = None
        self.first_page = None
        self.last_page = None
        # self.total_page_lb = '总页数   '
        self.current_page = 1

        self.firstPage()      # 默认打开页面先查询并显示第一页数据

        self.select_btn.clicked.connect(self.get_input_data)  # 按条件进行查询
        # 分页查询按钮事件
        self.go_btn.clicked.connect(self.goToPage)      # 定义转到按钮点击事件
        self.next_btn.clicked.connect(self.nextPage)        # 定义下一页按钮事件
        self.pre_btn.clicked.connect(self.prePage)     # 定义上一页按钮事件
        self.home_btn.clicked.connect(self.firstPage)    # # 定义首页按钮事件
        self.last_btn.clicked.connect(self.lastPage)        # 定义最后一页事件

    # 获取数据
    def get_input_data(self):
        room = self.room.text()
        cabinet = self.cabinet.text()
        machine_name = self.machine_name.text()
        mg_ip = self.mg_ip.text()
        print(room,mg_ip,cabinet,machine_name)

        select_sql = ''' select * from machine_list  where 1=1 '''
        # 根据条件查询设备
        select_values = []

        # 判断并组合查询SQL
        if self.room.text() != '':
            select_sql = select_sql + 'and room_name= %s'
            select_values.append(self.room.text())
        if self.mg_ip.text() != '':
            select_sql = select_sql + ' and cab_name=%s'
            select_values.append(self.mg_ip.text())
        if self.cabinet.text() != '':
            select_sql = select_sql + ' and start_position=%s'
            select_values.append(self.cabinet.text())
        if self.machine_name.text() != '':
            select_sql = select_sql + ' and machine_name=%s'
            select_values.append(self.machine_name.text())
        # tmp = self.db.query_single(data_sql, select_values)
        print('查询条件',select_values)
        print('查询SQL',select_sql)
        self.db.query_single(select_sql,select_values)

    # 获取要查询的总页数
    def page_record(self):
        # 连接数据库并显示数据至页面
        data = self.db.query_single(data_sql)     # 获取查询的数据，返回格式为一个内嵌的2元组，格式：（总记录数，数据内容）
        # print('数据条数：',len(data))
        total_record = len(data)  # 查询到的数据总记录条数
        if total_record % 15 == 0:
            self.totalPage = (total_record // 15)
            self.total_page_lb.setText('总页数：{}页'.format(self.totalPage, total_record))  # 分页显示数据
        else:
            self.totalPage = (total_record // 15) + 1
            self.total_page_lb.setText('总页数：{}页'.format(self.totalPage, total_record))  # 分页显示数据
        # print('总页数',totalPage)
        return self.totalPage

    # 定义查询记录并显示数据
    def recordQuery(self,sql,limiIndex,args=None):
        sql_page = sql + ' limit %s,15 '        # 定义分页查询SQL

        page_data = self.db.query_single(sql_page,limiIndex)      # 每页数据内容
        # print(page_data)
        self.select_table.clearContents()       # 清除所有内容
        for i in range(len(page_data)):
            for _ in range(12):
                if page_data[i][_] is None:
                    self.select_table.setItem(i, _, QTableWidgetItem(''))  # 显示单元格数据
                else:
                    self.select_table.setItem(i, _, QTableWidgetItem(str(page_data[i][_])))  # 显示单元格数据
        self.select_table.resizeColumnsToContents()  # 自适应列宽
        self.page_record()  # 显示总页数

    # 转到指定页事件
    def goToPage(self):
        if self.page_input_le.text() != '' and int(self.page_input_le.text()) <= self.totalPage:
            self.current_page = int(self.page_input_le.text())      # 获取输入的查询页数
            limiIndex = (int(self.page_input_le.text()) - 1) * 15  # 定位查询开始记录索引点
            self.recordQuery(data_sql,limiIndex)             # 查询数据并进行显示
            self.page_input_le.setText('')
            self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))      # 显示当前页数
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
    def nextPage(self):
        # print('self.currentPage',self.current_page)
        # print('self.totalPage',self.totalPage)
        if self.current_page < self.totalPage:
            limiIndex = self.current_page * 15  # 获取当前索引号
            self.recordQuery(data_sql,limiIndex)
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
    def prePage(self):
        limiIndex = (self.current_page - 2) * 15  # 获取当前索引号
        self.current_page -= 1
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        if limiIndex >= 0:
            self.recordQuery(data_sql,limiIndex)
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
    def firstPage(self):
        limiIndex = 0  # 获取当前索引号
        self.recordQuery(data_sql,limiIndex)
        self.current_page = 1       # 当索引小于0时，设置默认当前页为第一页
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        self.pre_btn.setDisabled(True)  # 当为第一页时，上一页按钮不可用
        self.next_btn.setDisabled(False)  # 当为第一页时，下一页按钮可用
        self.home_btn.setDisabled(True)  # 当为第一页时，首页按钮不可用
        self.last_btn.setDisabled(False)  # 当为第一页时，最后一页按钮不可用

    # 最后一页查询事件
    def lastPage(self):
        # print('最后一页',self.totalPage)
        limiIndex = (self.totalPage-1) * 15  # 获取当前索引号
        # print('当前索引：',limiIndex)
        self.recordQuery(data_sql,limiIndex)
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


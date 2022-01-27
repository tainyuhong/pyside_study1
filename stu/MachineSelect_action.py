import sys
from PySide6 import QtWidgets,QtGui,QtCore
from MachineSelect import *
from db_handler import *


data_sql = ''' select * from machine_list '''
# sql_page = ''' select * from machine_list limit %s,15;'''

class Ui_MachineSelect(QtWidgets.QMainWindow,Ui_MachineSelect):
    def __init__(self,parent=None):
        super(Ui_MachineSelect,self).__init__(parent)
        self.setupUi(self)
        # self.resize(1150,750)
        self.db= DBMysql()


        # 设置表格相关信息
        self.select_table.setHorizontalHeaderLabels(['ID','机房','机柜','U位','U数','设备类型','设备品牌','设备型号','设备序列号','设备名称','设备IP','设备管理员'])
        self.select_table.setStyleSheet("alternate-background-color: LightBLue;background-color: white;")  # 设置行的交替显示背景颜色
        # self.select_table.resizeRowsToContents()        # 自适应行高
        # self.select_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    # # 自适应伸缩模式

        # 初始化定义分页信息
        # self.pre_page = None
        self.next_page = None
        self.first_page = None
        self.last_page = None
        # self.total_page_lb = '总页数   '
        self.current_page = 1

        self.page_record()      # 显示总共页数及总记录数

        self.select_btn.clicked.connect(self.get_input_data)  # 按条件进行查询
        # 分页查询按钮事件
        self.go_btn.clicked.connect(self.recordQuery)      # 定义转到按钮点击事件
        self.next_btn.clicked.connect(self.nextPage)        # 定义下一页按钮事件
        self.pre_btn.clicked.connect(self.prePage)     # 定义上一页按钮事件
        self..clicked.connect(self.firstPage)    # # 定义首页按钮事件

    # 获取数据
    def get_input_data(self):
        room = self.room.text()
        cabinet = self.cabinet.text()
        machine_name = self.machine_name.text()
        mg_ip = self.mg_ip.text()
        print(room,cabinet,mg_ip,machine_name)
        return room,cabinet,mg_ip,machine_name

    # 获取要查询的总页数
    def page_record(self):
        # 连接数据库并显示数据至页面
        data = self.db.query_single(data_sql)     # 获取查询的数据，返回格式为一个内嵌的2元组，格式：（总记录数，数据内容）
        print('数据条数：',len(data))
        total_record = len(data)  # 查询到的数据总记录条数
        if total_record % 15 == 0:
            self.totalPage = (total_record // 15)
            self.total_page_lb.setText('总页数：{}页，总记录{}条'.format(self.totalPage, total_record))  # 分页显示数据
        else:
            self.totalPage = (total_record // 15) + 1
            self.total_page_lb.setText('总页数：{}页，总记录{}条'.format(self.totalPage, total_record))  # 分页显示数据
        # print('总页数',totalPage)
        return self.totalPage

    # 分页显示数据查询并显示
    # def page_btn(self):

    # 定义查询记录并显示数据
    def recordQuery(self,limiIndex):
        sql_page = data_sql + ' limit %s,15 '        # 定义分页查询SQL
        # print(self.page_input_le.text())
        # self.current_page = int(self.page_input_le.text())
        # print('当前页：', self.current_page)
        # num = (int(self.page_input_le.text())-1)*15     # 定义每页开始记录数
        page_data = self.db.query_single(sql_page,limiIndex)      # 每页数据内容
        print(page_data)
        row_num = len(page_data)  # 获取行数
        for i in range(row_num):
            for _ in range(12):
                if page_data[i][_] is None:
                    self.select_table.setItem(i, _, QTableWidgetItem(''))  # 显示单元格数据
                else:
                    self.select_table.setItem(i, _, QTableWidgetItem(str(page_data[i][_])))  # 显示单元格数据
        self.select_table.resizeColumnsToContents()  # 自适应列宽
        # self.total_page_lb.setText('总页数：【{}】页'.format(1))

    # 下一页查询事件
    def nextPage(self):
        print('self.currentPage',self.current_page)
        print('self.totalPage',self.totalPage)
        if self.current_page < self.totalPage:
            limiIndex = self.current_page * 15  # 获取当前索引号
            self.recordQuery(limiIndex)
            print('当前页：',self.current_page)

            # print('向后--当前页', self.currentPage)
        else:
            print('已是最后一页')
            return
        self.current_page += 1
        print('当前页：', self.current_page)

    # 上一页查询事件
    def prePage(self):
        limiIndex = (self.current_page - 2) * 15  # 获取当前索引号
        self.current_page -= 1
        if limiIndex >= 0:
            self.recordQuery(limiIndex)
            print('向前--当前页', self.current_page)
            print('limiIndex:',limiIndex)
        else:
            print('已是第一页了')
            self.current_page = 1  # 当索引小于0时，设置默认当前页为第一页
            print('向前--当前页', self.current_page)
            return

    # 首页查询事件
    def firstPage(self):
        limiIndex = 0  # 获取当前索引号
        self.recordQuery(limiIndex)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MachineSelect()
    mainWindow.show()
    sys.exit(app.exec())


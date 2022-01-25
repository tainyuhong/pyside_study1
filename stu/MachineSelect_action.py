from PySide6 import QtWidgets,QtGui,QtCore
from MachineSelect import *
from db_handler import *


class Ui_MachineSelect(QtWidgets.QMainWindow,Ui_MachineSelect):
    def __init__(self,parent=None):
        super(Ui_MachineSelect,self).__init__(parent)
        self.setupUi(self)
        self.resize(1150,750)
        self.select_btn.clicked.connect(self.get_input_data)
        self.select_table.setHorizontalHeaderLabels(['ID','机房','机柜','U位','U数','设备类型','设备品牌','设备型号','设备序列号','设备名称','设备IP','设备管理员'])
        # self.select_table.resizeColumnsToContents()       # 自适应列宽
        self.select_table.resizeRowsToContents()        # 自适应行高
        self.select_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        print(self.get_table_data())

    # 获取数据
    def get_input_data(self):
        room = self.room.text()
        cabinet = self.cabinet.text()
        machine_name = self.machine_name.text()
        mg_ip = self.mg_ip.text()
        print(room,cabinet,mg_ip,machine_name)
        return room,cabinet,mg_ip,machine_name

    # 获取表格数据
    def get_table_data(self):
        sql = ''' select * from machine_list '''
        db = DBMysql()
        data = db.query(sql)
        print(data)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MachineSelect()
    mainWindow.show()
    sys.exit(app.exec())


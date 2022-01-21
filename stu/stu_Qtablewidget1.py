import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

data = (['1', '张三', '男'], ['2', '张四', '男'], ['3', '王五', '男'], ['4', '虎妞', '女'], ['5', '刘明', '男'], ['1', '张三', '男'],
        ['2', '张四', '男'], ['3', '王五', '男'], ['4', '虎妞1', '女'], ['5', '刘1明', '男'])


class TableDome(QWidget):
    def __init__(self):
        super(TableDome, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget案例')
        self.resize(400, 300)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()  # 创建表格实例
        tableWidget.setRowCount(15)  # 初始化表格5行
        tableWidget.setColumnCount(3)  # 3列
        tableWidget.setShowGrid(True)  # 设置显示网格线
        tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '性别'])  # 设置表头信息
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应伸缩模式
        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑
        # tableWidget.resizeColumnsToContents()       # 根据内容自适应列宽
        # tableWidget.resizeRowsToContents()          # 根据内容自适应行高
        # tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置单元格选择方式为行模式
        # tableWidget.verticalHeader().setVisible(False)  # 隐藏第一列的表头
        # tableWidget.horizontalHeader().setVisible(False)  # 隐藏第一行的表头

        # 添加表格数据
        for num, i in enumerate(data):
            for col_num, col in enumerate(i):
                tableWidget.setItem(num, col_num, QTableWidgetItem(col))  # 向表格中添加数据
        tableWidget.setAlternatingRowColors(True)       # 表格颜色交替显示
        conLayout.addWidget(tableWidget)
        self.setLayout(conLayout)
        item = tableWidget.findItems('刘1明',Qt.MatchExactly)
        item = item[0]
        row = item.row()
        item.setForeground(QBrush(QColor(255,0,0)))
        print(row,'item:',item)
        tableWidget.verticalScrollBar().setSliderPosition(row)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableDome()
    example.show()
    sys.exit(app.exec())

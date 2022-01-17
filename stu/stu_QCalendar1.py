import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore

class calendarDemo(QWidget):
    def __init__(self):
        super(calendarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pyside6日历使用实例')
        mainLayout = QVBoxLayout()
        self.lb1 = QLabel("当前日期：")
        self.calendar = QCalendarWidget()       # 创建日历实例
        self.calendar.setMaximumDate(QDate(3000,1,1))
        self.calendar.setMinimumDate(QDate(1987,1,1))
        self.calendar.setGridVisible(True)
        self.calendar.move(20,20)
        self.calendar.clicked[QtCore.QDate].connect(self.showDate)
        date = self.calendar.selectedDate()
        self.lb1.setText(date.toString('yyyy-MM-dd dddd'))
        self.lb1.move(20,300)
        self.setGeometry(100,100,400,350)
        mainLayout.addWidget(self.lb1)
        mainLayout.addWidget(self.calendar)
        self.setLayout(mainLayout)

    def showDate(self,date):
        self.lb1.setText(date.toString('yyyy-MM-dd dddd'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = calendarDemo()
    radio_win.show()
    sys.exit(app.exec())
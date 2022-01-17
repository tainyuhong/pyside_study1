import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class listViewDemo(QWidget):
    def __init__(self):
        super(listViewDemo, self).__init__()
        self.setWindowTitle('Pyside6  ListView列表使用实例')
        self.resize(300,270)
        listv1 = QListView()
        slm = QStringListModel()
        self.qlist = ['item1','item2','item3','item4']
        slm.setStringList(self.qlist)
        listv1.setModel(slm)
        listv1.clicked.connect(self.clicked)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(listv1)
        self.setLayout(mainLayout)

    def clicked(self,qModeIndex):
        QMessageBox.information(self,'ListWidget','你选择了：'+self.qlist[qModeIndex.row()])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    radio_win = listViewDemo()
    radio_win.show()
    sys.exit(app.exec())
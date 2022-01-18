import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel

def initializeModel(model):
    model.setTable('people')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0,Qt.Horizontal,'id')
    model.setHeaderData(1,Qt.Horizontal,'name')
    model.setHeaderData(2,Qt.Horizontal,'address')

def createView(title,model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow():
    ret = model.insertRows(model.rowCount(),1)
    print('insertRows:{}'.format(ret))

def findrow(i):
    delrow = i.row()
    print('del row:{}'.format(delrow))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb.db')
    model = QSqlTableModel()
    delrow = -1
    initializeModel(model)
    view1 = createView('Table MOdel(view1)',model)
    view1.clicked.connect(findrow)

    dlg = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view1)
    addBtn = QPushButton('添加一行')
    addBtn.clicked.connect(addrow)
    layout.addWidget(addBtn)

    delBtn = QPushButton('删除一行')
    delBtn.clicked.connect(lambda :model.removeRow(view1.currentIndex().row()))
    layout.addWidget(delBtn)
    dlg.setLayout(layout)
    dlg.setWindowTitle('数据库连接实例')
    dlg.resize(430,450)
    dlg.show()
    sys.exit(app.exec())
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import QSqlDatabase,QSqlQuery

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb.db')
    dbConn = db.open()  # 打开数据库
    print(dbConn)
    if not dbConn:
        QMessageBox.Critical(None,('无法打开数据库'),('无法建立到数据库的连接'),QMessageBox.Cancel)
        return False
    query = QSqlQuery()
    query.exec('create table people (id int primary key,name char(20),address char(30) )')
    query.exec("insert into people values(1,'张三','湖南湘潭') ")
    query.exec("insert into people values(2,'张四','湖南湘潭') ")
    query.exec("insert into people values(3,'王五','湖南湘潭') ")
    query.exec("insert into people values(4,'杨六','湖南湘潭') ")
    query.exec("insert into people values(5,'毛毛','湖南株洲') ")
    query.exec("insert into people values(6,'吴柚','湖南长沙') ")
    db.close()
    return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    createDB()
    sys.exit(app.exec())
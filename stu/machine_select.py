# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machine_select.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_select_windows(object):
    def setupUi(self, select_windows):
        if not select_windows.objectName():
            select_windows.setObjectName(u"select_windows")
        select_windows.resize(835, 675)
        icon = QIcon()
        icon.addFile(u"img/11.ico", QSize(), QIcon.Normal, QIcon.Off)
        select_windows.setWindowIcon(icon)
        self.centralwidget = QWidget(select_windows)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 791, 631))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.select_table = QTableWidget(self.frame)
        self.select_table.setObjectName(u"select_table")
        self.select_table.setGeometry(QRect(10, 180, 770, 451))
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(320, 20, 161, 41))
        font = QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 70, 771, 92))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        self.room = QLineEdit(self.groupBox)
        self.room.setObjectName(u"room")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.room.sizePolicy().hasHeightForWidth())
        self.room.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.room, 0, 1, 2, 1)

        self.cabinet = QLineEdit(self.groupBox)
        self.cabinet.setObjectName(u"cabinet")
        sizePolicy1.setHeightForWidth(self.cabinet.sizePolicy().hasHeightForWidth())
        self.cabinet.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.cabinet, 1, 3, 1, 1)

        self.select_btn = QPushButton(self.groupBox)
        self.select_btn.setObjectName(u"select_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.select_btn.sizePolicy().hasHeightForWidth())
        self.select_btn.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.select_btn, 1, 4, 1, 1)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        sizePolicy1.setHeightForWidth(self.mg_ip.sizePolicy().hasHeightForWidth())
        self.mg_ip.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.mg_ip, 3, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)

        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        sizePolicy1.setHeightForWidth(self.machine_name.sizePolicy().hasHeightForWidth())
        self.machine_name.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.machine_name, 3, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 2, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 2, 2, 1)

        select_windows.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(select_windows)
        self.statusbar.setObjectName(u"statusbar")
        select_windows.setStatusBar(self.statusbar)

        self.retranslateUi(select_windows)

        QMetaObject.connectSlotsByName(select_windows)
    # setupUi

    def retranslateUi(self, select_windows):
        select_windows.setWindowTitle(QCoreApplication.translate("select_windows", u"\u8bbe\u5907\u67e5\u8be2", None))
        self.title.setText(QCoreApplication.translate("select_windows", u"\u8bbe\u5907\u67e5\u8be2", None))
        self.label.setText(QCoreApplication.translate("select_windows", u"\u673a   \u623f", None))
        self.select_btn.setText(QCoreApplication.translate("select_windows", u"\u67e5    \u8be2", None))
        self.label_3.setText(QCoreApplication.translate("select_windows", u"\u8bbe\u5907\u540d\u79f0", None))
        self.label_4.setText(QCoreApplication.translate("select_windows", u"\u7ba1\u7406IP", None))
        self.label_2.setText(QCoreApplication.translate("select_windows", u"\u673a      \u67dc", None))
    # retranslateUi


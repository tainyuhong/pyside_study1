# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MachineSelect.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MachineSelect(object):
    def setupUi(self, MachineSelect):
        if not MachineSelect.objectName():
            MachineSelect.setObjectName(u"MachineSelect")
        MachineSelect.resize(834, 755)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MachineSelect.sizePolicy().hasHeightForWidth())
        MachineSelect.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"C:/Users/zl/.designer/backup/img/11.ico", QSize(), QIcon.Normal, QIcon.Off)
        MachineSelect.setWindowIcon(icon)
        self.vbox = QGroupBox(MachineSelect)
        self.vbox.setObjectName(u"vbox")
        self.vbox.setGeometry(QRect(0, 0, 826, 697))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vbox.sizePolicy().hasHeightForWidth())
        self.vbox.setSizePolicy(sizePolicy1)
        self.vbox.setBaseSize(QSize(0, 0))
        self.vbox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.vbox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.vbox)
        self.title.setObjectName(u"title")
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.groupBox = QGroupBox(self.vbox)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cabinet = QLineEdit(self.groupBox)
        self.cabinet.setObjectName(u"cabinet")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cabinet.sizePolicy().hasHeightForWidth())
        self.cabinet.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.cabinet, 1, 3, 1, 1)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        sizePolicy3.setHeightForWidth(self.mg_ip.sizePolicy().hasHeightForWidth())
        self.mg_ip.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.mg_ip, 3, 1, 1, 1)

        self.room = QLineEdit(self.groupBox)
        self.room.setObjectName(u"room")
        sizePolicy3.setHeightForWidth(self.room.sizePolicy().hasHeightForWidth())
        self.room.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.room, 0, 1, 2, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 2, 1)

        self.select_btn = QPushButton(self.groupBox)
        self.select_btn.setObjectName(u"select_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.select_btn.sizePolicy().hasHeightForWidth())
        self.select_btn.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.select_btn, 1, 4, 1, 1)

        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        sizePolicy3.setHeightForWidth(self.machine_name.sizePolicy().hasHeightForWidth())
        self.machine_name.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.machine_name, 3, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 2, 2, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(800, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.select_table = QTableWidget(self.vbox)
        if (self.select_table.columnCount() < 12):
            self.select_table.setColumnCount(12)
        if (self.select_table.rowCount() < 15):
            self.select_table.setRowCount(15)
        self.select_table.setObjectName(u"select_table")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.select_table.sizePolicy().hasHeightForWidth())
        self.select_table.setSizePolicy(sizePolicy6)
        self.select_table.setMinimumSize(QSize(806, 500))
        self.select_table.setDragEnabled(False)
        self.select_table.setAlternatingRowColors(True)
        self.select_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.select_table.setGridStyle(Qt.SolidLine)
        self.select_table.setRowCount(15)
        self.select_table.setColumnCount(12)
        self.select_table.horizontalHeader().setVisible(True)
        self.select_table.horizontalHeader().setCascadingSectionResizes(False)
        self.select_table.horizontalHeader().setHighlightSections(True)
        self.select_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.select_table.verticalHeader().setVisible(False)
        self.select_table.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.select_table)

        self.layoutWidget = QWidget(MachineSelect)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 710, 811, 31))
        self.page_layout = QHBoxLayout(self.layoutWidget)
        self.page_layout.setSpacing(20)
        self.page_layout.setObjectName(u"page_layout")
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.layoutWidget)
        self.home_btn.setObjectName(u"home_btn")

        self.page_layout.addWidget(self.home_btn)

        self.pre_btn = QPushButton(self.layoutWidget)
        self.pre_btn.setObjectName(u"pre_btn")

        self.page_layout.addWidget(self.pre_btn)

        self.next_btn = QPushButton(self.layoutWidget)
        self.next_btn.setObjectName(u"next_btn")

        self.page_layout.addWidget(self.next_btn)

        self.last_btn = QPushButton(self.layoutWidget)
        self.last_btn.setObjectName(u"last_btn")

        self.page_layout.addWidget(self.last_btn)

        self.go_page_lb = QLabel(self.layoutWidget)
        self.go_page_lb.setObjectName(u"go_page_lb")

        self.page_layout.addWidget(self.go_page_lb)

        self.page_input_le = QLineEdit(self.layoutWidget)
        self.page_input_le.setObjectName(u"page_input_le")

        self.page_layout.addWidget(self.page_input_le)

        self.page_lb = QLabel(self.layoutWidget)
        self.page_lb.setObjectName(u"page_lb")

        self.page_layout.addWidget(self.page_lb)

        self.go_btn = QPushButton(self.layoutWidget)
        self.go_btn.setObjectName(u"go_btn")

        self.page_layout.addWidget(self.go_btn)

        self.total_page_lb = QLabel(self.layoutWidget)
        self.total_page_lb.setObjectName(u"total_page_lb")

        self.page_layout.addWidget(self.total_page_lb)

        self.current_page_lb = QLabel(self.layoutWidget)
        self.current_page_lb.setObjectName(u"current_page_lb")

        self.page_layout.addWidget(self.current_page_lb)

        self.page_layout.setStretch(0, 2)
        self.page_layout.setStretch(1, 2)
        self.page_layout.setStretch(2, 2)
        self.page_layout.setStretch(3, 2)
        self.page_layout.setStretch(4, 1)
        self.page_layout.setStretch(5, 1)
        self.page_layout.setStretch(6, 1)
        self.page_layout.setStretch(7, 1)
        self.page_layout.setStretch(8, 3)
        self.page_layout.setStretch(9, 3)

        self.retranslateUi(MachineSelect)

        QMetaObject.connectSlotsByName(MachineSelect)
    # setupUi

    def retranslateUi(self, MachineSelect):
        MachineSelect.setWindowTitle(QCoreApplication.translate("MachineSelect", u"\u8bbe\u5907\u67e5\u8be2\u7a97\u53e3", None))
        self.title.setText(QCoreApplication.translate("MachineSelect", u"\u8bbe\u5907\u67e5\u8be2", None))
        self.label.setText(QCoreApplication.translate("MachineSelect", u"\u673a   \u623f", None))
        self.label_4.setText(QCoreApplication.translate("MachineSelect", u"\u7ba1\u7406IP", None))
        self.select_btn.setText(QCoreApplication.translate("MachineSelect", u"\u67e5    \u8be2", None))
        self.label_2.setText(QCoreApplication.translate("MachineSelect", u"\u673a      \u67dc", None))
        self.label_3.setText(QCoreApplication.translate("MachineSelect", u"\u8bbe\u5907\u540d\u79f0", None))
        self.home_btn.setText(QCoreApplication.translate("MachineSelect", u"\u9996\u9875", None))
        self.pre_btn.setText(QCoreApplication.translate("MachineSelect", u"\u4e0a\u4e00\u9875", None))
        self.next_btn.setText(QCoreApplication.translate("MachineSelect", u"\u4e0b\u4e00\u9875", None))
        self.last_btn.setText(QCoreApplication.translate("MachineSelect", u"\u6700\u540e\u4e00\u9875", None))
        self.go_page_lb.setText(QCoreApplication.translate("MachineSelect", u"\u8df3\u8f6c\u5230", None))
        self.page_lb.setText(QCoreApplication.translate("MachineSelect", u"\u9875", None))
        self.go_btn.setText(QCoreApplication.translate("MachineSelect", u"\u8f6c\u5230", None))
        self.total_page_lb.setText(QCoreApplication.translate("MachineSelect", u"\u603b\u9875\u6570", None))
        self.current_page_lb.setText(QCoreApplication.translate("MachineSelect", u"\u5f53\u524d\u9875", None))
    # retranslateUi


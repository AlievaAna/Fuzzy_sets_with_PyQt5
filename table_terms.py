# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_terms.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table_terms(object):
    def setupUi(self, Table_terms):
        Table_terms.setObjectName("Table_terms")
        Table_terms.resize(296, 302)
        Table_terms.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.button_clear = QtWidgets.QPushButton(Table_terms)
        self.button_clear.setGeometry(QtCore.QRect(50, 220, 191, 23))
        self.button_clear.setObjectName("button_clear")
        self.button_save = QtWidgets.QPushButton(Table_terms)
        self.button_save.setGeometry(QtCore.QRect(50, 250, 191, 23))
        self.button_save.setObjectName("button_save")
        self.tableWidget = QtWidgets.QTableWidget(Table_terms)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Table_terms)
        QtCore.QMetaObject.connectSlotsByName(Table_terms)

    def retranslateUi(self, Table_terms):
        _translate = QtCore.QCoreApplication.translate
        Table_terms.setWindowTitle(_translate("Table_terms", "Таблица значений термов"))
        self.button_clear.setText(_translate("Table_terms", "Отменить изменения"))
        self.button_save.setText(_translate("Table_terms", "Сохранить изменения"))

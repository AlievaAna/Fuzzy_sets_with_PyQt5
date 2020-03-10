# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_matrix.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table_matrix(object):
    def setupUi(self, Table_matrix):
        Table_matrix.setObjectName("Table_matrix")
        Table_matrix.resize(681, 324)
        self.tableWidget = QtWidgets.QTableWidget(Table_matrix)
        self.tableWidget.setGeometry(QtCore.QRect(15, 11, 651, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.button_clear = QtWidgets.QPushButton(Table_matrix)
        self.button_clear.setGeometry(QtCore.QRect(240, 260, 191, 23))
        self.button_clear.setObjectName("button_clear")
        self.button_save = QtWidgets.QPushButton(Table_matrix)
        self.button_save.setGeometry(QtCore.QRect(240, 290, 191, 23))
        self.button_save.setObjectName("button_save")

        self.retranslateUi(Table_matrix)
        QtCore.QMetaObject.connectSlotsByName(Table_matrix)

    def retranslateUi(self, Table_matrix):
        _translate = QtCore.QCoreApplication.translate
        Table_matrix.setWindowTitle(_translate("Table_matrix", "Матрица исходных данных"))
        self.button_clear.setText(_translate("Table_matrix", "Очистить таблицу"))
        self.button_save.setText(_translate("Table_matrix", "Сохранить изменения"))

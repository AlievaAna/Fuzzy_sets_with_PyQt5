# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_table.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_table(object):
    def setupUi(self, Change_table):
        Change_table.setObjectName("Change_table")
        Change_table.resize(653, 358)
        self.tableWidget = QtWidgets.QTableWidget(Change_table)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 431, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.button_save = QtWidgets.QPushButton(Change_table)
        self.button_save.setGeometry(QtCore.QRect(460, 100, 181, 31))
        self.button_save.setObjectName("button_save")
        self.button_cancel = QtWidgets.QPushButton(Change_table)
        self.button_cancel.setGeometry(QtCore.QRect(460, 140, 181, 31))
        self.button_cancel.setObjectName("button_cancel")

        self.retranslateUi(Change_table)
        QtCore.QMetaObject.connectSlotsByName(Change_table)

    def retranslateUi(self, Change_table):
        _translate = QtCore.QCoreApplication.translate
        Change_table.setWindowTitle(_translate("Change_table", "Редактор матрицы исходных данных"))
        self.button_save.setText(_translate("Change_table", "Сохранить изменения"))
        self.button_cancel.setText(_translate("Change_table", "Отменить изменения"))

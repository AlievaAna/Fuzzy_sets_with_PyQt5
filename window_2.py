# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_2(object):
    def setupUi(self, window_2):
        window_2.setObjectName("window_2")
        window_2.resize(785, 361)
        self.centralwidget = QtWidgets.QWidget(window_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.value_experts = QtWidgets.QLineEdit(self.centralwidget)
        self.value_experts.setGeometry(QtCore.QRect(170, 20, 31, 20))
        self.value_experts.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.value_experts.setReadOnly(True)
        self.value_experts.setObjectName("value_experts")
        self.value_terms = QtWidgets.QLineEdit(self.centralwidget)
        self.value_terms.setGeometry(QtCore.QRect(170, 50, 31, 20))
        self.value_terms.setReadOnly(True)
        self.value_terms.setObjectName("value_terms")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.button_change_matrix = QtWidgets.QPushButton(self.centralwidget)
        self.button_change_matrix.setGeometry(QtCore.QRect(210, 300, 191, 23))
        self.button_change_matrix.setObjectName("button_change_matrix")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 391, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(420, 10, 351, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.button_back.setObjectName("button_back")
        window_2.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(window_2)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 785, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        window_2.setMenuBar(self.menuBar)
        self.action_save = QtWidgets.QAction(window_2)
        self.action_save.setObjectName("action_save")
        self.action_load = QtWidgets.QAction(window_2)
        self.action_load.setObjectName("action_load")
        self.action = QtWidgets.QAction(window_2)
        self.action.setObjectName("action")
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_load)
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(window_2)
        QtCore.QMetaObject.connectSlotsByName(window_2)

    def retranslateUi(self, window_2):
        _translate = QtCore.QCoreApplication.translate
        window_2.setWindowTitle(_translate("window_2", "Построение функции принадлежности"))
        self.label_2.setText(_translate("window_2", "Количество экспертов:"))
        self.label_3.setText(_translate("window_2", "Количество термов:"))
        self.label_4.setText(_translate("window_2", "Матрица данных:"))
        self.button_change_matrix.setText(_translate("window_2", "Редактировать матрицу данных"))
        self.button_back.setText(_translate("window_2", "Назад"))
        self.menu.setTitle(_translate("window_2", "Меню действий"))
        self.action_save.setText(_translate("window_2", "Сохранить данные в файл"))
        self.action_load.setText(_translate("window_2", "Загрузить данные из файла"))
        self.action.setText(_translate("window_2", "Выйти из приложения"))
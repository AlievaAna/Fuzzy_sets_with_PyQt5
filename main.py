from PyQt5 import QtWidgets, QtCore
from main_window import Ui_MainWindow
from window_2 import Ui_window_2
from table_terms import Ui_Table_terms
from table_matrix import Ui_Table_matrix
from change_table import Ui_Change_table
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.ticker as ticker
import matplotlib
import sys
import info
matplotlib.use("Qt5Agg")


class Main_Window(QtWidgets.QMainWindow):
    """Главное окно с выбором метода"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_terms.clicked.connect(self.open_table_terms)
        self.ui.button_matrix.clicked.connect(self.open_table_matrix)
        self.ui.button_next.clicked.connect(self.open_next_window)
        self.ui.combo_box_method.currentIndexChanged.connect(lambda: self.change_method(self.ui.combo_box_method.currentIndex()))

    def change_method(self, index):
        if index == 0:
            self.ui.spin_box_experts.setEnabled(True)
            self.ui.spin_box_terms.setEnabled(True)
            self.ui.spin_box_elements.setEnabled(True)
            self.ui.button_terms.setEnabled(True)
            self.ui.button_matrix.setEnabled(False)
            self.ui.button_next.setEnabled(False)
        elif index == 1:
            self.ui.spin_box_experts.setEnabled(False)
            self.ui.spin_box_terms.setEnabled(False)
            self.ui.spin_box_elements.setEnabled(True)
            self.ui.button_terms.setEnabled(False)
            self.ui.button_matrix.setEnabled(True)
            self.ui.button_next.setEnabled(False)
        elif index == 2:
            self.ui.spin_box_experts.setEnabled(False)
            self.ui.spin_box_terms.setEnabled(False)
            self.ui.spin_box_elements.setEnabled(False)
            self.ui.button_terms.setEnabled(False)
            self.ui.button_matrix.setEnabled(False)
            self.ui.button_next.setEnabled(False)


    def open_table_terms(self):
        """По кнопке "Ввод значений термов"
        открывается окно с таблицей термов"""
        self.table_terms = Window_terms(self)
        self.table_terms.show()
        self.hide()

    def open_table_matrix(self):
        """По кнопке "Ввод матрицы исходных данных"
        открывается окно с матрицей"""
        self.table_matrix = Window_matrix(self)
        self.table_matrix.show()
        self.hide()


    def open_next_window(self):
        """По кнопке "Построить функцию принадлежности"
        открывается окно с отрисовкой"""
        self.window_2 = Window_2(self)
        self.window_2.show()
        self.hide()


class Window_terms(QtWidgets.QWidget):
    """Окно с таблицей термов"""
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.value_terms = int(self.parent.ui.spin_box_terms.value())
        self.ui = Ui_Table_terms()
        self.ui.setupUi(self)
        self.build()

        self.ui.button_clear.clicked.connect(self.clear)
        self.ui.button_save.clicked.connect(self.save)

    # задание базовых параметров таблицы
    def build(self):
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(self.value_terms)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Term", "Value"])

        for i in range(self.value_terms):
            item = QtWidgets.QTableWidgetItem(f"term {i + 1}")
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(i, 0, item)
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(f"term {i + 1}"))

    # очистка таблицы
    def clear(self):
        self.ui.tableWidget.clear()
        self.build()

    # сохранение таблицы
    def save(self):
        info.TERMS_NAMES.clear()
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()

        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.ui.tableWidget.item(row, col).text())
                except AttributeError:
                    tmp.append(f"term {row}")
            info.TERMS_NAMES.append(tmp)

        self.hide()
        self.parent.ui.button_matrix.setEnabled(True)
        self.parent.show()


class Window_matrix(QtWidgets.QWidget):
    """Окно с матрицей исходных данных"""
    def __init__(self, parent=None):
        super().__init__()
        self.params = [parent.ui.combo_box_method.currentIndex(),
                       parent.ui.spin_box_experts.value(),
                       len(info.TERMS_NAMES),
                       parent.ui.spin_box_elements.value()]
        self.parent = parent
        self.ui = Ui_Table_matrix()
        self.ui.setupUi(self)

        if self.params[0] == 0:
            self.build_0()
        elif self.params[0] == 1:
            self.build_1()

        self.ui.button_clear.clicked.connect(lambda: self.clear(self.params[0]))
        self.ui.button_save.clicked.connect(lambda: self.save(self.params[0]))

    # задание базовых параметров таблицы
    def build_0(self):
        """Матрица экспертных мнений"""
        self.ui.tableWidget.setColumnCount(2 + self.params[3])
        self.ui.tableWidget.setRowCount(self.params[1] * self.params[2])

        # задание названий столбцов
        header_labels = ["Expert", "Term"]
        for i in range(self.params[3]):
            header_labels.append(f"Element_{i + 1}")
        self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)

        # задание экспертов и значений термов
        count = 0
        for i in range(self.params[1]):
            for j in range(self.params[2]):
                item_expert = QtWidgets.QTableWidgetItem(f"expert {i + 1}")
                item_term = QtWidgets.QTableWidgetItem(info.TERMS_NAMES[j][1])
                item_expert.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item_term.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(j + count, 0, item_expert)
                self.ui.tableWidget.setItem(j + count, 1, item_term)
            count += self.params[2]

    def build_1(self):
        """Матрица парных сравнений"""
        self.ui.tableWidget.setColumnCount(self.params[3])
        self.ui.tableWidget.setRowCount(self.params[3])

        # задание названий столбцов
        header_labels = []
        for i in range(self.params[3]):
            header_labels.append(f"Element_{i + 1}")
        self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.ui.tableWidget.setVerticalHeaderLabels(header_labels)

        # инизиализация матрицы
        for i in range(self.params[3]):
            for j in range(self.params[3]):
                if i == j:
                    item = QtWidgets.QTableWidgetItem("1")
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(i, j, item)
                elif i < j:
                    item = QtWidgets.QTableWidgetItem("")
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(i, j, item)

    # очистка таблицы
    def clear(self, index):
        self.ui.tableWidget.clear()
        if index == 0:
            self.build_0()
        elif index == 1:
            self.build_1()

    # сохранение таблицы
    def save(self, index):
        info.MATRIX.clear()
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        if index == 0:
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        tmp.append(self.ui.tableWidget.item(row, col).text())
                    except AttributeError:
                        tmp.append("0")
                info.MATRIX.append(tmp)
        elif index == 1:
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        if row < col:
                            item = self.ui.tableWidget.item(col, row).text()
                            item = round(1 / int(item), 3)
                            tmp.append(str(item))
                        else:
                            item = self.ui.tableWidget.item(row, col).text()
                            tmp.append(item)
                    except Exception:
                        tmp.append("1")
                info.MATRIX.append(tmp)

        self.hide()
        self.parent.ui.button_next.setEnabled(True)
        self.parent.show()


class Window_2(QtWidgets.QMainWindow):
    """Окно с отрисовкой"""
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = Ui_window_2()
        self.ui.setupUi(self)
        self.ui.button_change_matrix.clicked.connect(self.open_table)
        self.ui.button_back.clicked.connect(self.back)
        self.ui.action_save.triggered.connect(self.save_file)
        self.ui.action_load.triggered.connect(self.load_file)
        self.ui.action.triggered.connect(self.quit)
        self.parent_index = self.parent.ui.combo_box_method.currentIndex()
        if self.parent_index == 0:
            self.ui.value_experts.setText(str(len(info.MATRIX) // len(info.TERMS_NAMES)))
            self.ui.value_terms.setText(str(len(info.TERMS_NAMES)))
            self.build_0()
        elif self.parent_index == 1:
            self.ui.label_2.setEnabled(False)
            self.ui.label_3.setEnabled(False)
            self.ui.value_terms.setEnabled(False)
            self.ui.value_experts.setEnabled(False)
            self.build_1()

    def quit(self):
        QtWidgets.QApplication.quit()

    def save_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
        file = open(file_name, 'w')
        data = []
        for i in range(len(info.MATRIX)):
            data.append('|'.join(info.MATRIX[i]))
        file.write('\n'.join(data))
        file.close()

    def load_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
        file = open(file_name, 'r')
        data = file.readlines()

        info.MATRIX.clear()
        info.TERMS_NAMES.clear()

        if self.parent_index == 0:
            for i in data:
                info.MATRIX.extend([i.strip('\n').split('|')])
            elem_0 = info.MATRIX[0][0]
            for i in range(len(info.MATRIX)):
                if info.MATRIX[i][0] == elem_0:
                    info.TERMS_NAMES.append([f"term {i + 1}", info.MATRIX[i][1]])
            self.build_0()
        elif self.parent_index == 1:
            for i in data:
                info.MATRIX.extend([i.strip('\n').split('|')])
            self.build_1()

    def back(self):
        self.parent.ui.combo_box_method.setCurrentIndex(2)
        self.parent.show()
        self.hide()

    def open_table(self):
        self.change_table = Window_change_table(self)
        self.change_table.show()
        self.hide()

    # задание базовых параметров таблицы
    def build_0(self):
        """Матрица экспертных мнений"""
        self.ui.tableWidget.setColumnCount(len(info.MATRIX[0]))
        self.ui.tableWidget.setRowCount(len(info.MATRIX))

        # задание названий столбцов
        header_labels = ["Expert", "Term"]
        for i in range(len(info.MATRIX[0]) - 2):
            header_labels.append(f"Element_{i + 1}")
        self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)

        # заполнение таблицы
        for i in range(len(info.MATRIX)):
            for j in range(len(info.MATRIX[0])):
                item = QtWidgets.QTableWidgetItem(info.MATRIX[i][j])
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(i, j, item)

        self.draw()

    # отрисовка графика
    def draw(self):
        if self.parent_index == 0:
            self.myFig = CustomFigCanvas()
            self.ui.gridLayout.addWidget(self.myFig, *(0, 1))
        elif self.parent_index == 1:
            self.myFig = CustomFigCanvas_2()
            self.ui.gridLayout.addWidget(self.myFig, *(0, 1))

    # задание базовых параметров таблицы
    def build_1(self):
        """Матрица попарных сравнений"""
        self.ui.tableWidget.setColumnCount(len(info.MATRIX[0]))
        self.ui.tableWidget.setRowCount(len(info.MATRIX))

        # задание названий столбцов
        header_labels = []
        for i in range(len(info.MATRIX[0])):
            header_labels.append(f"Element_{i + 1}")
        self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.ui.tableWidget.setVerticalHeaderLabels(header_labels)

        # заполнение таблицы
        for i in range(len(info.MATRIX)):
            for j in range(len(info.MATRIX[0])):
                item = QtWidgets.QTableWidgetItem(info.MATRIX[i][j])
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(i, j, item)

        self.draw()


class Window_change_table(QtWidgets.QWidget):
    """Окно с матрицей исходных данных"""
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Change_table()
        self.ui.setupUi(self)
        if self.parent.parent_index == 0:
            self.build_0()
        elif self.parent.parent_index == 1:
            self.build_1()

        self.ui.button_save.clicked.connect(self.save)
        self.ui.button_cancel.clicked.connect(self.cancel)

    # задание базовых параметров таблицы
    def build_0(self):
        """Матрица экспертных мнений"""
        self.ui.tableWidget.setColumnCount(len(info.MATRIX[0]))
        self.ui.tableWidget.setRowCount(len(info.MATRIX))

        # задание названий столбцов
        header_labels = ["Expert", "Term"]
        for i in range(len(info.MATRIX[0]) - 2):
            header_labels.append(f"Element_{i + 1}")
        self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)

        # заполнение таблицы
        for i in range(len(info.MATRIX)):
            for j in range(len(info.MATRIX[0])):
                item = QtWidgets.QTableWidgetItem(info.MATRIX[i][j])
                if j < 2:
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(i, j, item)

    # задание базовых параметров таблицы
    def build_1(self):
        """Матрица парных сравнений"""
        self.ui.tableWidget.setColumnCount(len(info.MATRIX[0]))
        self.ui.tableWidget.setRowCount(len(info.MATRIX))

        # задание названий столбцов
        header_labels = []
        for i in range(len(info.MATRIX[0])):
            header_labels.append(f"Element_{i + 1}")
        self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.ui.tableWidget.setVerticalHeaderLabels(header_labels)

        # заполнение таблицы
        for i in range(len(info.MATRIX)):
            for j in range(len(info.MATRIX[0])):
                item = QtWidgets.QTableWidgetItem(info.MATRIX[i][j])
                if i <= j:
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(i, j, item)

        self.ui.tableWidget.setColumnCount(len(info.MATRIX[0]))
        self.ui.tableWidget.setRowCount(len(info.MATRIX))

    def save(self):
        info.MATRIX.clear()
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        if self.parent.parent_index == 0:
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        tmp.append(self.ui.tableWidget.item(row, col).text())
                    except AttributeError:
                        tmp.append('0')
                info.MATRIX.append(tmp)
        elif self.parent.parent_index == 1:
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        if row < col:
                            item = self.ui.tableWidget.item(col, row).text()
                            item = round(1 / int(item), 3)
                            tmp.append(str(item))
                        else:
                            item = self.ui.tableWidget.item(row, col).text()
                            tmp.append(item)
                    except Exception:
                        tmp.append("1")
                info.MATRIX.append(tmp)

        self.hide()
        if self.parent.parent_index == 0:
            self.parent.build_0()
        elif self.parent.parent_index == 1:
            self.parent.build_1()
        self.parent.show()

    def cancel(self):
        self.hide()
        self.parent.show()


class CustomFigCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot()

        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))

        amount_of_elements = len(info.MATRIX[0]) - 2

        x = [int(i) for i in range(1, amount_of_elements + 1)]
        y = self.count_y(amount_of_elements)

        for i in range(len(y)):
            self.ax.plot(x, y[i], label=info.TERMS_NAMES[i][1], marker='o')

        self.fig.suptitle('Функция принадлежности', fontsize=8)
        self.ax.legend(fontsize=8)
        self.ax.grid(True)

        FigureCanvas.__init__(self, self.fig)

    def count_y(self, amount_of_elements):
        rez = []
        for i in range(len(info.TERMS_NAMES)):
            rez.append([])

        amount_of_experts = len(info.MATRIX) // len(info.TERMS_NAMES)

        for i in range(amount_of_elements):
            for j in range(len(info.TERMS_NAMES)):
                summa = 0
                count = 0
                for k in range(amount_of_experts):
                    summa += int(info.MATRIX[count + j][2 + i])
                    count += len(info.TERMS_NAMES)
                rez[j].append(summa / amount_of_experts)

        return rez


class CustomFigCanvas_2(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot()

        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))

        amount_of_elements = len(info.MATRIX[0])

        x = [int(i) for i in range(1, amount_of_elements + 1)]
        y = self.count_y()

        self.ax.plot(x, y[0], label="субнормальное", marker="o")
        self.ax.plot(x, y[1], label="нормальное", marker="o")

        self.fig.suptitle('Функция принадлежности', fontsize=8)
        self.ax.legend(fontsize=8)
        self.ax.grid(True)

        FigureCanvas.__init__(self, self.fig)

    def count_y(self):
        rez_1 = []

        for i in range(len(info.MATRIX)):
            summa = 0
            for j in range(len(info.MATRIX)):
                summa += float(info.MATRIX[j][i])
            summa = 1 / summa
            rez_1.append(summa)
        rez_2 = []
        for i in rez_1:
            rez_2.append(i / max(rez_1))


        return [rez_1, rez_2]


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_Window()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
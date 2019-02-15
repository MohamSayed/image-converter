from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,\
    QTableWidgetItem, QHeaderView, QAbstractItemView


class ImageTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(QTableWidget, self).__init__(parent)
        self.setColumnCount(3)
        self.setHorizontalHeaderItem(0, QTableWidgetItem("Path"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Extension"))
        self.setHorizontalHeaderItem(2, QTableWidgetItem("Status"))
        #self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resizeColumnsToContents()

        self.setDragEnabled(False)

    def mouseDoubleClickEvent(self, event):
        pass

    def resizeEvent(self, event):
        """ Resize all sections to content and user interactive """

        super(QTableWidget, self).resizeEvent(event)
        header = self.horizontalHeader()
        for column in range(header.count()):
            header.setSectionResizeMode(column, QHeaderView.ResizeToContents)
            width = header.sectionSize(column)
            header.setSectionResizeMode(column, QHeaderView.Interactive)
            header.resizeSection(column, width)

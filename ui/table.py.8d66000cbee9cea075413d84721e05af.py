from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class CustomTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(QTableWidget, self).__init__(parent)
        self.setColumnCount(3)
        self.setHorizontalHeaderItem(0,QTableWidgetItem("Path"))
        self.setHorizontalHeader(1,QTableWidgetItem("Extension"))



    def mouseDoubleClickEvent(self, event):
        print("CLICK")
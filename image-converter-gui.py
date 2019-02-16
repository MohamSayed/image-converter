import sys
import os
import PIL.Image as Image
sys.path.append("ui/")
sys.path.append("core/")

import batch
import single
import table
import about
import convert

import utils

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool, QObject, QRunnable, pyqtSignal


images = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # images table
        self.tableWidget = table.ImageTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)

        self.path_count = 0
        self.extension_count = 0
        self.status_count = 0
        self.rowCount = 0
        self.worker = None

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")

        # select one image(file)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_3.addWidget(self.pushButton_save)

        # cancel converting
        # self.pushButton_cancel_converting = QtWidgets.QPushButton(self.centralwidget)
        # self.horizontalLayout_3.addWidget(self.pushButton_cancel_converting)

        # select folder & subfolder checkbox
        self.horizontalLayout_folder_subfolder = QtWidgets.QHBoxLayout()
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxLabel = QtWidgets.QLabel(self.centralwidget)
        self.checkBoxLabel.setText("sub folder")
        self.horizontalLayout_folder_subfolder.addWidget(self.pushButton_2)
        self.horizontalLayout_folder_subfolder.addWidget(self.checkBoxLabel)
        self.horizontalLayout_folder_subfolder.addWidget(self.checkBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_folder_subfolder)

        # progressbar
        self.progressbar = QtWidgets.QProgressBar(self.centralwidget)
        self.verticalLayout.addWidget(self.progressbar)
        self.progressbar.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionOpen_image = QtWidgets.QAction(MainWindow)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.actionOpen_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_folder.setObjectName("actionOpen_folder")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionClearList = QtWidgets.QAction(MainWindow)

        self.menuFile.addAction(self.actionOpen_image)
        self.menuFile.addAction(self.actionOpen_folder)

        self.menuFile.addAction(self.actionClearList)

        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # threading part
        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(5)

        self.connects()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image-converter"))
        self.pushButton_2.setText(_translate("MainWindow", "select folder"))
        self.pushButton.setText(_translate("MainWindow", "select image"))
        self.pushButton_save.setText(_translate("MainWindow","Convert && Save".encode(encoding="utf-8")))
        self.pushButton_save.setDisabled(True)

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionClearList.setText(_translate("MainWindow", "Clear list"))

        self.comboBox.addItems(batch.extensions)
        #self.pushButton_cancel_converting.setText(_translate("MainWindow", "Cancel"))

    def connects(self):
        self.pushButton.clicked.connect(self.browse_single_image)
        self.actionAbout.triggered.connect(about.show_dialog)
        self.actionExit.triggered.connect(sys.exit)
        self.pushButton_save.clicked.connect(self.convert)
        self.pushButton_2.clicked.connect(self.browse_directory)
        self.actionClearList.triggered.connect(self.clearTableItems)
        self.actionOpen_folder.triggered.connect(self.browse_directory)
        self.actionOpen_image.triggered.connect(self.browse_single_image)
        #self.pushButton_cancel_converting.clicked.connect(self.cancel_converting)

    # @clear @table @clear.table
    def clearTableItems(self):
        self.progressbar.setValue(0)
        self.path_count = 0
        self.extension_count = 0
        self.status_count = 0
        self.rowCount = 0
        images.clear()
        self.tableWidget.setRowCount(0)

    def browse_single_image(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget,
                                                         'Open file', 'C:\\', "Image files (*.jpg *.gif *.tiff *.*png *.bmp *.ico *.pnm)")
        if(len(filename[0]) > 0): # if user selected a file
            self.rowCount += 1
            self.tableWidget.setRowCount(self.rowCount)
            self.addItemToTable(filename[0], column="path")
            self.addItemToTable(filename[0].split(".")[-1], column="extension")

            images.append(filename[0])
            self.pushButton_save.setEnabled(True)
            self.comboBox.setCurrentText(filename[0].split(".")[-1])
            print(filename[0])

    def addItemToTable(self, value, column=''):
        if(column == "path"):
            self.tableWidget.setItem(
                self.path_count, 0, QtWidgets.QTableWidgetItem(value))
            self.path_count += 1

        if(column == "extension"):
            self.tableWidget.setItem(
                self.extension_count, 1, QtWidgets.QTableWidgetItem(value))
            self.extension_count += 1

        if(column == "status"):
            self.tableWidget.setItem(
                self.status_count, 2, QtWidgets.QTableWidgetItem(value))
            self.status_count += 1

    def cancel_converting(self):
        self.pool.cancel(self.worker)

    def convert(self):
        output_dirname = QtWidgets.QFileDialog.getExistingDirectory(
            self.centralwidget)       
        self.progressbar.setValue(0)

        # warning: hardcoded
        _progress = 1
        self.progressbar.setMaximum(len(images))
        self.progressbar.setMinimum(0)
        if output_dirname and images:
            for image in set(images):
                _progress += 1
                self.progressbar.setValue(_progress)
                image_name = ''
                if image.count("/") > 0 and not image.count("\\") > 0:
                    image_name = image.split(r".")[0].split("/")[-1]

                else:
                    image_name = image.split(r".")[0].split("\\")[-1]

                final_outpath = output_dirname + os.sep + image_name

                single.single_convert(
                    image, final_outpath, extension=self.comboBox.currentText())


    # directory
    def browse_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self.centralwidget)
        
        if(len(directory) > 0):
            self.pushButton_save.setEnabled(True)
            # @checkbox @subfolder
            if self.checkBox.isChecked():
                
                _images = utils.System.files_tree_list(directory,
                                                    extensions=batch.extensions)
                if _images.__len__() > 0:
                    images.extend(_images)
                    for image in _images:
                        
                        self.rowCount += 1
                        self.tableWidget.setRowCount(self.rowCount)
                        print(image)
                        self.addItemToTable(image, column="path")
                        self.addItemToTable(image.split(".")[-1], column="extension")
            else:        
                _images = utils.System.files_list(directory,
                                                    extensions=batch.extensions)
                if _images.__len__() > 0:
                    images.extend(_images)
                    for image in _images:
                        
                        self.rowCount += 1
                        self.tableWidget.setRowCount(self.rowCount)
                        print(image)
                        self.addItemToTable(image, column="path")
                        self.addItemToTable(image.split(".")[-1], column="extension")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

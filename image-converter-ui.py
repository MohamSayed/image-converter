# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image-converter-mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import about

import single
import batch

import sys
import os

images = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 443)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        # select image
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
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

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

        self.menuFile.addAction(self.actionOpen_image)
        self.menuFile.addAction(self.actionOpen_folder)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.connects()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image-converter"))
        self.pushButton_2.setText(_translate("MainWindow", "select folder"))
        self.pushButton.setText(_translate("MainWindow", "select image"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_save.setDisabled(True)

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

        self.comboBox.addItems(batch.extensions)

    def connects(self):
        self.pushButton.clicked.connect(self.browse_single_image)
        self.actionAbout.triggered.connect(about.show_dialog)
        self.actionExit.triggered.connect(sys.exit)
        self.pushButton_save.clicked.connect(self.convert_and_save)

    def browse_single_image(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget,
                                                         'Open file', 'C:\\', "Image files (*.jpg *.gif *.tiff *.*png *.bmp *.ico *.pnm)")
        self.listWidget.addItem(filename[0])
        if(filename):
            images.append(filename[0])
            self.pushButton_save.setEnabled(True)
            print(filename[0])
            
        
    def browse_directory():
        pass
    def convert_and_save(self):
        output_dirname = QtWidgets.QFileDialog.getExistingDirectory(
            self.centralwidget)

        # warning: hardcoded
        if(output_dirname and images):
            print("extension: " + self.comboBox.currentText())
            break_detection = images[0].split("/")[-1].split(r".")[0] if images[0].count(
                "/") > 0 else images[0].split("\\")[-1].split(r".")[0]
            final_outpath = output_dirname + os.sep + break_detection

            single.single_convert(
                images[0], final_outpath, extension=self.comboBox.currentText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

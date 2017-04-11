# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mediahomewindow.ui'
#
# Created: Mon Apr 10 20:32:26 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MediaHomeWindow(object):
    def setupUi(self, MediaHomeWindow):
        MediaHomeWindow.setObjectName("MediaHomeWindow")
        MediaHomeWindow.resize(728, 704)
        self.centralWidget = QtWidgets.QWidget(MediaHomeWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(550, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 290, 271, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addMediaButton = QtWidgets.QPushButton(self.centralWidget)
        self.addMediaButton.setGeometry(QtCore.QRect(10, 20, 161, 27))
        self.addMediaButton.setObjectName("addMediaButton")
        self.setDesinationButton = QtWidgets.QPushButton(self.centralWidget)
        self.setDesinationButton.setGeometry(QtCore.QRect(10, 60, 161, 27))
        self.setDesinationButton.setObjectName("setDesinationButton")
        self.radioScene = QtWidgets.QRadioButton(self.centralWidget)
        self.radioScene.setGeometry(QtCore.QRect(20, 100, 141, 22))
        self.radioScene.setChecked(True)
        self.radioScene.setObjectName("radioScene")
        self.radioGrid = QtWidgets.QRadioButton(self.centralWidget)
        self.radioGrid.setGeometry(QtCore.QRect(20, 120, 117, 22))
        self.radioGrid.setObjectName("radioGrid")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 150, 256, 225))
        self.graphicsView.setObjectName("graphicsView")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 390, 256, 225))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 254, 209))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 461, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutScroll = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutScroll.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutScroll.setObjectName("gridLayoutScroll")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        MediaHomeWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MediaHomeWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 728, 22))
        self.menuBar.setObjectName("menuBar")
        MediaHomeWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MediaHomeWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MediaHomeWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MediaHomeWindow)
        self.statusBar.setObjectName("statusBar")
        MediaHomeWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MediaHomeWindow)
        QtCore.QMetaObject.connectSlotsByName(MediaHomeWindow)

    def retranslateUi(self, MediaHomeWindow):
        _translate = QtCore.QCoreApplication.translate
        MediaHomeWindow.setWindowTitle(_translate("MediaHomeWindow", "MediaHomeWindow"))
        self.addMediaButton.setText(_translate("MediaHomeWindow", "Import Media"))
        self.setDesinationButton.setText(_translate("MediaHomeWindow", "Export Media"))
        self.radioScene.setText(_translate("MediaHomeWindow", "Graphics Scene"))
        self.radioGrid.setText(_translate("MediaHomeWindow", "Grid Layout"))


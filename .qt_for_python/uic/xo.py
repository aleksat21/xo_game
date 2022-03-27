# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aleksa/Desktop/projekti/xo_game/xo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1202, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.08, y1:0.063, x2:0.99, y2:0.903, stop:0 rgba(114, 159, 207, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xo_object = QtWidgets.QFrame(self.centralwidget)
        self.xo_object.setEnabled(True)
        self.xo_object.setGeometry(QtCore.QRect(420, 200, 450, 450))
        self.xo_object.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.xo_object.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.xo_object.setObjectName("xo_object")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.xo_object)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bt1 = QtWidgets.QPushButton(self.xo_object)
        self.bt1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt1.sizePolicy().hasHeightForWidth())
        self.bt1.setSizePolicy(sizePolicy)
        self.bt1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt1.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt1.setText("")
        self.bt1.setObjectName("bt1")
        self.gridLayout_2.addWidget(self.bt1, 0, 1, 1, 1)
        self.bt5 = QtWidgets.QPushButton(self.xo_object)
        self.bt5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt5.sizePolicy().hasHeightForWidth())
        self.bt5.setSizePolicy(sizePolicy)
        self.bt5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt5.setText("")
        self.bt5.setObjectName("bt5")
        self.gridLayout_2.addWidget(self.bt5, 1, 2, 1, 1)
        self.bt6 = QtWidgets.QPushButton(self.xo_object)
        self.bt6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt6.sizePolicy().hasHeightForWidth())
        self.bt6.setSizePolicy(sizePolicy)
        self.bt6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt6.setText("")
        self.bt6.setObjectName("bt6")
        self.gridLayout_2.addWidget(self.bt6, 2, 0, 1, 1)
        self.bt2 = QtWidgets.QPushButton(self.xo_object)
        self.bt2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt2.sizePolicy().hasHeightForWidth())
        self.bt2.setSizePolicy(sizePolicy)
        self.bt2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt2.setText("")
        self.bt2.setObjectName("bt2")
        self.gridLayout_2.addWidget(self.bt2, 0, 2, 1, 1)
        self.bt4 = QtWidgets.QPushButton(self.xo_object)
        self.bt4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt4.sizePolicy().hasHeightForWidth())
        self.bt4.setSizePolicy(sizePolicy)
        self.bt4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt4.setText("")
        self.bt4.setObjectName("bt4")
        self.gridLayout_2.addWidget(self.bt4, 1, 1, 1, 1)
        self.bt8 = QtWidgets.QPushButton(self.xo_object)
        self.bt8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt8.sizePolicy().hasHeightForWidth())
        self.bt8.setSizePolicy(sizePolicy)
        self.bt8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt8.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt8.setText("")
        self.bt8.setObjectName("bt8")
        self.gridLayout_2.addWidget(self.bt8, 2, 2, 1, 1)
        self.bt0 = QtWidgets.QPushButton(self.xo_object)
        self.bt0.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt0.sizePolicy().hasHeightForWidth())
        self.bt0.setSizePolicy(sizePolicy)
        self.bt0.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bt0.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt0.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt0.setText("")
        self.bt0.setObjectName("bt0")
        self.gridLayout_2.addWidget(self.bt0, 0, 0, 1, 1)
        self.bt7 = QtWidgets.QPushButton(self.xo_object)
        self.bt7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt7.sizePolicy().hasHeightForWidth())
        self.bt7.setSizePolicy(sizePolicy)
        self.bt7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt7.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt7.setText("")
        self.bt7.setObjectName("bt7")
        self.gridLayout_2.addWidget(self.bt7, 2, 1, 1, 1)
        self.bt3 = QtWidgets.QPushButton(self.xo_object)
        self.bt3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt3.sizePolicy().hasHeightForWidth())
        self.bt3.setSizePolicy(sizePolicy)
        self.bt3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 20px;\n"
"    font: 30pt \"Times New Roman\";\n"
"    color:rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(156, 159, 152);\n"
"    border-style: inset;\n"
"}")
        self.bt3.setText("")
        self.bt3.setObjectName("bt3")
        self.gridLayout_2.addWidget(self.bt3, 1, 0, 1, 1)
        self.bt0.raise_()
        self.bt1.raise_()
        self.bt2.raise_()
        self.bt3.raise_()
        self.bt4.raise_()
        self.bt5.raise_()
        self.bt8.raise_()
        self.bt7.raise_()
        self.bt6.raise_()
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setEnabled(True)
        self.horizontalFrame.setGeometry(QtCore.QRect(340, 20, 581, 121))
        self.horizontalFrame.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 20px")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btStart = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btStart.sizePolicy().hasHeightForWidth())
        self.btStart.setSizePolicy(sizePolicy)
        self.btStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btStart.setAutoFillBackground(False)
        self.btStart.setStyleSheet("QPushButton#btStart{\n"
"    background-color: rgb(138, 226, 52);\n"
"    border-radius: 30px;\n"
"    padding: 5px;\n"
"    font: 40pt \"Times New Roman\";\n"
"}\n"
"QPushButton#btStart:pressed{\n"
"     background-color: rgb(118, 200, 32);\n"
"    border-style: inset;\n"
"}")
        self.btStart.setObjectName("btStart")
        self.horizontalLayout.addWidget(self.btStart)
        self.btRestart = QtWidgets.QPushButton(self.centralwidget)
        self.btRestart.setGeometry(QtCore.QRect(970, 590, 186, 61))
        self.btRestart.setStyleSheet("QPushButton#btRestart{\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    alternate-background-color: rgb(52, 101, 164);\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#btRestart:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.btRestart.setAutoDefault(False)
        self.btRestart.setDefault(False)
        self.btRestart.setFlat(False)
        self.btRestart.setObjectName("btRestart")
        self.tbUserManual = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbUserManual.setGeometry(QtCore.QRect(10, 470, 321, 241))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setItalic(True)
        self.tbUserManual.setFont(font)
        self.tbUserManual.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbUserManual.setStyleSheet("QTextBrowser {\n"
"    background-color: rgb(238, 238, 236) ;\n"
"    border-style: outset;\n"
"    border-width: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.tbUserManual.setObjectName("tbUserManual")
        self.lbUserManual = QtWidgets.QLabel(self.centralwidget)
        self.lbUserManual.setGeometry(QtCore.QRect(10, 410, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbUserManual.setFont(font)
        self.lbUserManual.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: rgb(238, 238, 236);\n"
"    border-style: outset;\n"
"    border-width: 5px;\n"
"    border-color: rgb(164, 0, 0)\n"
"}")
        self.lbUserManual.setAlignment(QtCore.Qt.AlignCenter)
        self.lbUserManual.setObjectName("lbUserManual")
        self.horizontalFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame1.setGeometry(QtCore.QRect(0, 20, 331, 121))
        self.horizontalFrame1.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 20px;\n"
"")
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbPlayer = QtWidgets.QLabel(self.horizontalFrame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbPlayer.sizePolicy().hasHeightForWidth())
        self.lbPlayer.setSizePolicy(sizePolicy)
        self.lbPlayer.setStyleSheet("color: white;\n"
"background-color: rgb(239, 41, 41);\n"
"font: 36pt \"Times New Roman\";\n"
"border-radius: 20px;\n"
"")
        self.lbPlayer.setTextFormat(QtCore.Qt.PlainText)
        self.lbPlayer.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPlayer.setObjectName("lbPlayer")
        self.horizontalLayout_2.addWidget(self.lbPlayer)
        self.lbX = QtWidgets.QLabel(self.horizontalFrame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbX.sizePolicy().hasHeightForWidth())
        self.lbX.setSizePolicy(sizePolicy)
        self.lbX.setStyleSheet("color: white;\n"
"background-color: rgb(136, 138, 133);\n"
"font: 36pt \"Times New Roman\";\n"
"border-radius: 20px;")
        self.lbX.setTextFormat(QtCore.Qt.PlainText)
        self.lbX.setAlignment(QtCore.Qt.AlignCenter)
        self.lbX.setObjectName("lbX")
        self.horizontalLayout_2.addWidget(self.lbX)
        self.horizontalFrame2 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame2.setGeometry(QtCore.QRect(930, 20, 271, 121))
        self.horizontalFrame2.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 20px")
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbPlayer_3 = QtWidgets.QLabel(self.horizontalFrame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbPlayer_3.sizePolicy().hasHeightForWidth())
        self.lbPlayer_3.setSizePolicy(sizePolicy)
        self.lbPlayer_3.setStyleSheet("color: white;\n"
"background-color: rgb(239, 41, 41);\n"
"font: 36pt \"Times New Roman\";\n"
"border-radius: 20px;\n"
"")
        self.lbPlayer_3.setTextFormat(QtCore.Qt.PlainText)
        self.lbPlayer_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPlayer_3.setObjectName("lbPlayer_3")
        self.horizontalLayout_3.addWidget(self.lbPlayer_3)
        self.lbX_2 = QtWidgets.QLabel(self.horizontalFrame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbX_2.sizePolicy().hasHeightForWidth())
        self.lbX_2.setSizePolicy(sizePolicy)
        self.lbX_2.setStyleSheet("color: white;\n"
"background-color: rgb(136, 138, 133);\n"
"font: 36pt \"Times New Roman\";\n"
"border-radius: 20px;")
        self.lbX_2.setTextFormat(QtCore.Qt.PlainText)
        self.lbX_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbX_2.setObjectName("lbX_2")
        self.horizontalLayout_3.addWidget(self.lbX_2)
        self.lnHU = QtWidgets.QFrame(self.centralwidget)
        self.lnHU.setEnabled(True)
        self.lnHU.setGeometry(QtCore.QRect(406, 274, 481, 10))
        self.lnHU.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.lnHU.setFrameShape(QtWidgets.QFrame.HLine)
        self.lnHU.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnHU.setObjectName("lnHU")
        self.lnHC = QtWidgets.QFrame(self.centralwidget)
        self.lnHC.setEnabled(True)
        self.lnHC.setGeometry(QtCore.QRect(400, 419, 481, 10))
        self.lnHC.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.lnHC.setFrameShape(QtWidgets.QFrame.HLine)
        self.lnHC.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnHC.setObjectName("lnHC")
        self.lnHB = QtWidgets.QFrame(self.centralwidget)
        self.lnHB.setEnabled(True)
        self.lnHB.setGeometry(QtCore.QRect(400, 566, 481, 10))
        self.lnHB.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.lnHB.setFrameShape(QtWidgets.QFrame.HLine)
        self.lnHB.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnHB.setObjectName("lnHB")
        self.lnVL = QtWidgets.QFrame(self.centralwidget)
        self.lnVL.setEnabled(True)
        self.lnVL.setGeometry(QtCore.QRect(494, 189, 10, 471))
        self.lnVL.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.lnVL.setFrameShape(QtWidgets.QFrame.VLine)
        self.lnVL.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnVL.setObjectName("lnVL")
        self.lnVC = QtWidgets.QFrame(self.centralwidget)
        self.lnVC.setEnabled(True)
        self.lnVC.setGeometry(QtCore.QRect(642, 189, 10, 471))
        self.lnVC.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.lnVC.setFrameShape(QtWidgets.QFrame.VLine)
        self.lnVC.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnVC.setObjectName("lnVC")
        self.lnVR = QtWidgets.QFrame(self.centralwidget)
        self.lnVR.setEnabled(True)
        self.lnVR.setGeometry(QtCore.QRect(788, 189, 10, 471))
        self.lnVR.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.lnVR.setFrameShape(QtWidgets.QFrame.VLine)
        self.lnVR.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnVR.setObjectName("lnVR")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XO Game"))
        self.btStart.setText(_translate("MainWindow", "START"))
        self.btRestart.setText(_translate("MainWindow", "RESTART"))
        self.tbUserManual.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:20pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lbUserManual.setText(_translate("MainWindow", "User manual"))
        self.lbPlayer.setText(_translate("MainWindow", "PLAYER"))
        self.lbX.setText(_translate("MainWindow", "X"))
        self.lbPlayer_3.setText(_translate("MainWindow", "AI"))
        self.lbX_2.setText(_translate("MainWindow", "O"))

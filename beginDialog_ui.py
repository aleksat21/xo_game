# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(507, 412)
        Dialog.setStyleSheet("padding: 20px;\n"
"background-color:qlineargradient(spread:pad, x1:0.08, y1:0.063, x2:0.99, y2:0.903, stop:0 rgba(114, 159, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:inset;\n"
"border-width: 2px;\n"
"border-color: rgb(46, 52, 54)")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 505, 416))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vbBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vbBox.setContentsMargins(0, 0, 0, 5)
        self.vbBox.setObjectName("vbBox")
        self.hbTop_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.hbTop_2.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.hbTop_2.setObjectName("hbTop_2")
        self.hbTop = QtWidgets.QHBoxLayout(self.hbTop_2)
        self.hbTop.setContentsMargins(10, -1, 10, -1)
        self.hbTop.setObjectName("hbTop")
        self.rbPVP = QtWidgets.QRadioButton(self.hbTop_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbPVP.sizePolicy().hasHeightForWidth())
        self.rbPVP.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.rbPVP.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.rbPVP.setFont(font)
        self.rbPVP.setStyleSheet("QRadioButton{\n"
"    background-color: rgb(239, 239, 239);\n"
"      border-radius: 5px;\n"
"    padding: 10px;\n"
"}")
        self.rbPVP.setObjectName("rbPVP")
        self.hbTop.addWidget(self.rbPVP)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.hbTop.addItem(spacerItem)
        self.rbSinglePlayer = QtWidgets.QRadioButton(self.hbTop_2)
        self.rbSinglePlayer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbSinglePlayer.sizePolicy().hasHeightForWidth())
        self.rbSinglePlayer.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.rbSinglePlayer.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.rbSinglePlayer.setFont(font)
        self.rbSinglePlayer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rbSinglePlayer.setStyleSheet("QRadioButton{\n"
"    background-color: rgb(239, 239, 239);\n"
"      border-radius: 5px;\n"
"    padding: 10px;\n"
"}")
        self.rbSinglePlayer.setObjectName("rbSinglePlayer")
        self.hbTop.addWidget(self.rbSinglePlayer)
        self.hbTop.setStretch(0, 2)
        self.vbBox.addWidget(self.hbTop_2)
        self.hbCenterTop = QtWidgets.QHBoxLayout()
        self.hbCenterTop.setContentsMargins(5, -1, 5, -1)
        self.hbCenterTop.setObjectName("hbCenterTop")
        self.lbPrvi = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbPrvi.setFont(font)
        self.lbPrvi.setStyleSheet("border-style: inset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 3px;")
        self.lbPrvi.setObjectName("lbPrvi")
        self.hbCenterTop.addWidget(self.lbPrvi)
        self.lnPrvi = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lnPrvi.setFont(font)
        self.lnPrvi.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 10px;\n"
"border-style: inset;\n"
"border-width: 3px;\n"
"border-color: rgb(0, 0, 0);")
        self.lnPrvi.setObjectName("lnPrvi")
        self.hbCenterTop.addWidget(self.lnPrvi)
        self.vbBox.addLayout(self.hbCenterTop)
        self.hbCenterBottom = QtWidgets.QHBoxLayout()
        self.hbCenterBottom.setContentsMargins(5, -1, 5, -1)
        self.hbCenterBottom.setObjectName("hbCenterBottom")
        self.lbDrugi = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbDrugi.setFont(font)
        self.lbDrugi.setStyleSheet("border-style: inset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 3px;")
        self.lbDrugi.setObjectName("lbDrugi")
        self.hbCenterBottom.addWidget(self.lbDrugi)
        self.lnDrugi = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lnDrugi.setFont(font)
        self.lnDrugi.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 10px;\n"
"border-style: inset;\n"
"border-width: 3px;\n"
"border-color: rgb(0, 0, 0);")
        self.lnDrugi.setObjectName("lnDrugi")
        self.hbCenterBottom.addWidget(self.lnDrugi)
        self.vbBox.addLayout(self.hbCenterBottom)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbBox.addItem(spacerItem1)
        self.hbBottom = QtWidgets.QHBoxLayout()
        self.hbBottom.setContentsMargins(10, -1, 10, 15)
        self.hbBottom.setObjectName("hbBottom")
        self.btStart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btStart.setFont(font)
        self.btStart.setStyleSheet("QPushButton#btStart{\n"
"    background-color: rgb(138, 226, 52);\n"
"    border-radius: 30px;\n"
"    padding: 5px;\n"
"    font: 35pt \"Times New Roman\";\n"
"}\n"
"QPushButton#btStart:pressed{\n"
"     background-color: rgb(118, 200, 32);\n"
"    border-style: inset;\n"
"}")
        self.btStart.setObjectName("btStart")
        self.hbBottom.addWidget(self.btStart)
        self.vbBox.addLayout(self.hbBottom)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.rbPVP.setText(_translate("Dialog", "PVP"))
        self.rbSinglePlayer.setText(_translate("Dialog", "Singleplayer"))
        self.lbPrvi.setText(_translate("Dialog", "Player 1:"))
        self.lbDrugi.setText(_translate("Dialog", "Player 2:"))
        self.btStart.setText(_translate("Dialog", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

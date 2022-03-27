from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QKeySequence

import os
import sys
import xo_ui
import xo_class


class XO(xo_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(XO, self).__init__()
        self.setupUi(self)

        self.buttons = [self.bt0, self.bt1, self.bt2, self.bt3, self.bt4, self.bt5, self.bt6, self.bt7, self.bt8]

        self.btRestart.pressed.connect(lambda: self.btRestartAction())
        self.btStart.pressed.connect(lambda: self.btStartAction())

        # TODO add seperate config function
        self.game = None
        self.started = False
        self.lbPlayer.setMargin(10)

        self.bt0.pressed.connect(lambda: self.bt0Action())
        self.bt1.pressed.connect(lambda: self.bt1Action())
        self.bt2.pressed.connect(lambda: self.bt2Action())
        self.bt3.pressed.connect(lambda: self.bt3Action())
        self.bt4.pressed.connect(lambda: self.bt4Action())
        self.bt5.pressed.connect(lambda: self.bt5Action())
        self.bt6.pressed.connect(lambda: self.bt6Action())
        self.bt7.pressed.connect(lambda: self.bt7Action())
        self.bt8.pressed.connect(lambda: self.bt8Action())

        # TODO ovo treba da ide ispod u else granu akcija kod dugmica
        self.tbUserManual.setText("Morate da kliknete na START dugme prvo!")
    
    # TODO dodati LCD display koji broji rezultat
    # TODO dodati da se iscrtava linija kada neko pobedi

    def clearButtons(self):
        for button in self.buttons:
            button.setText("")
            button.setEnabled(True)
    
    def btRestartAction(self):
        self.clearButtons()
        self.game = xo_class.Game(tbUserManual=self.tbUserManual, buttons=self.buttons)

    def btStartAction(self):
        self.game = xo_class.Game(tbUserManual=self.tbUserManual, buttons=self.buttons)
        self.started = True

        self.bt1.setStyleSheet("""QPushButton{
	background-color: rgb(186, 189, 182);
	border-radius: 20px;
	font: 30pt "Times New Roman";
	color:rgb(164, 0, 0);
}
QPushButton:pressed {
    background-color: rgb(156, 159, 152);
    border-style: inset;
} """)

    def bt0Action(self):
        if self.started:
            self.game.updateTableStatePlayer(0, self.bt0)   
    def bt1Action(self):
        if self.started:
            self.game.updateTableStatePlayer(1, self.bt1)
    def bt2Action(self):
        if self.started:
            self.game.updateTableStatePlayer(2, self.bt2)
    def bt3Action(self):
        if self.started:
            self.game.updateTableStatePlayer(3, self.bt3)
    def bt4Action(self):
        if self.started:
            self.game.updateTableStatePlayer(4, self.bt4)
    def bt5Action(self):
        if self.started:    
            self.game.updateTableStatePlayer(5, self.bt5)
    def bt6Action(self):
        if self.started:            
            self.game.updateTableStatePlayer(6, self.bt6)
    def bt7Action(self):
        if self.started:    
            self.game.updateTableStatePlayer(7, self.bt7)
    def bt8Action(self):
        if self.started:
            self.game.updateTableStatePlayer(8, self.bt8)
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    xo = XO()
    xo.show()
    sys.exit(app.exec_())

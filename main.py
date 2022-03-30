from ast import Import
from re import S
from statistics import mode
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QShortcut, QMessageBox
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

import os, sys, copy
import xo_ui, beginDialog_ui ,xo_class


class BeginDialog(beginDialog_ui.Ui_Dialog, QtWidgets.QMainWindow):
    # TODO mozda napraviti konstruktor koji pamti koja su imena bila kada se klikne na change mode
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        self.hideAllInput()
        
        self.btStart.pressed.connect(lambda: self.begin())
        self.rbPVP.pressed.connect(lambda: self.showPVP())
        self.rbSinglePlayer.pressed.connect(lambda: self.showSinglePlayer())

    def clearAllInput(self):
        self.lnPrvi.clear()
        self.lnDrugi.clear()

    def hideAllInput(self):
        self.lnPrvi.hide()
        self.lbPrvi.hide()

        self.lnDrugi.hide()
        self.lbDrugi.hide()
    def showAllInput(self):
        self.lnPrvi.show()
        self.lbPrvi.show()
        
        self.lnDrugi.show()
        self.lbDrugi.show()

    def showSinglePlayer(self):
        self.hideAllInput()
        self.clearAllInput()

        self.lnPrvi.show()
        self.lbPrvi.show()

    def showPVP(self):
        self.hideAllInput()
        self.clearAllInput()

        self.showAllInput()
        

    def begin(self):
        if self.rbSinglePlayer.isChecked() and len(self.lnPrvi.text()) != 0:
            self.close()
            xo = XO(mode = 1, player1 = self.lnPrvi.text())
            xo.show()
        if self.rbPVP.isChecked() and len(self.lnPrvi.text()) != 0 and len(self.lnDrugi.text()) != 0:
            self.close()
            xo = XO(mode = 2, player1=self.lnPrvi.text(), player2=self.lnDrugi.text())
            xo.show()


class XO(xo_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    # TODO staviti da se menjaju boje u zavisnosti ko je na redu
    # TODO mozda staviti naizmenicno da se smenjuju kada je mode=2, odnosno ko je X a ko je O
    def __init__(self, mode, player1 = "Player 1" , player2 = "AI"):
        super(XO, self).__init__()
        self.setupUi(self)

        # mod 1 - vs AI 2 - pvp
        self.mode = mode

        # imena
        self.lbPlayer1.setText(player1 + " (X) ")
        self.lbPlayer2.setText(player2 + " (O) ")

        # podesiti fiksnu duzinu
        self.setFixedSize(1200, 800)


        # mapiranje dugmica koji se prosledjuju xo_class.Game konstruktoru
        self.buttons = {"bt0" : self.bt0, "bt1" : self.bt1, "bt2" : self.bt2, "bt3" : self.bt3, "bt4" : self.bt4, "bt5" : self.bt5, "bt6" : self.bt6, "bt7" : self.bt7, "bt8" :self.bt8}


        # linije za crtanje kada neko pobedi koje se prosledju xo_class.Game konstruktoru
        self.configDiagonals()
        self.lines = {"HU" : self.lnHU, "HC" : self.lnHC, "HB" : self.lnHB, "VL" : self.lnVL, "VC" : self.lnVC, "VR" : self.lnVR, "DTL" : self.lnDiagTopLeft, "DTR" : self.lnDiagTopRIght}

        # TODO add seperate config function ako se bude nakupilo naredbi

        # u startu se ne crtaju linije za pobedu
        self.hideLines()

        # AKCIJE
        self.btRestart.pressed.connect(lambda: self.btRestartAction())
        self.btChangeMode.pressed.connect(lambda: self.btChangeModeAction())

        # TODO needs more testing
        # for rbr , (btName, btObj) in enumerate(self.buttons.items()):
            # btObj.pressed.connect(lambda: self.btAction(rbr, btName))
            
        self.bt0.pressed.connect(lambda: self.bt0Action())
        self.bt1.pressed.connect(lambda: self.bt1Action())
        self.bt2.pressed.connect(lambda: self.bt2Action())
        self.bt3.pressed.connect(lambda: self.bt3Action())
        self.bt4.pressed.connect(lambda: self.bt4Action())
        self.bt5.pressed.connect(lambda: self.bt5Action())
        self.bt6.pressed.connect(lambda: self.bt6Action())
        self.bt7.pressed.connect(lambda: self.bt7Action())
        self.bt8.pressed.connect(lambda: self.bt8Action())

        self.game = xo_class.Game(buttons=self.buttons, lines=self.lines, graphicsView=self.gwCentralView, mode = self.mode)
    
        # TODO dodati LCD display koji broji rezultat

    def configDiagonals(self):

        scene = QtWidgets.QGraphicsScene()

        self.lnDiagTopLeft.setParent(None)
        self.lnDiagTopRIght.setParent(None)

        lineTopLeft = scene.addWidget(self.lnDiagTopLeft)
        lineTopLeft.setPos(self.gwCentralView.x() + 270, self.gwCentralView.y()/2 - 10)
        lineTopLeft.setRotation(45)
        
        lineTopRight  = scene.addWidget(self.lnDiagTopRIght)
        lineTopRight.setPos(self.gwCentralView.x() / 2, self.gwCentralView.y()/2)
        lineTopRight.setRotation(-45)

        self.gwCentralView.setScene(scene)

        self.lnDiagTopLeft.hide()
        self.lnDiagTopRIght.hide()

        self.gwCentralView.lower()
        
    def clearButtons(self):
        for name, button in self.buttons.items():
            button.setText("")
            button.setEnabled(True)

    def hideLines(self):
        for name , line in self.lines.items():
            line.hide()
        self.gwCentralView.lower()


    def btRestartAction(self):
        self.clearButtons()
        self.hideLines()
        self.game = xo_class.Game(buttons=self.buttons, lines=self.lines, graphicsView=self.gwCentralView, mode=self.mode)

    def btChangeModeAction(self):
        self.close()
        beginDialog = BeginDialog()
        beginDialog.show()

    # TODO needs more testing
    def btAction(self, rbr, name):
        self.game.updateTableStatePlayer(rbr, self.buttons[name])   

    def bt0Action(self):
            self.game.updateTableStatePlayer(0, self.buttons["bt0"])   
    def bt1Action(self):
            self.game.updateTableStatePlayer(1, self.buttons["bt1"])
    def bt2Action(self):
            self.game.updateTableStatePlayer(2, self.buttons["bt2"])
    def bt3Action(self):
            self.game.updateTableStatePlayer(3, self.buttons["bt3"])
    def bt4Action(self):
            self.game.updateTableStatePlayer(4, self.buttons["bt4"])
    def bt5Action(self):
            self.game.updateTableStatePlayer(5, self.buttons["bt5"])
    def bt6Action(self):
            self.game.updateTableStatePlayer(6, self.buttons["bt6"])
    def bt7Action(self):
            self.game.updateTableStatePlayer(7, self.buttons["bt7"])
    def bt8Action(self):
            self.game.updateTableStatePlayer(8, self.buttons["bt8"])

def main():            
    app = QtWidgets.QApplication(sys.argv)

    beginDialog = BeginDialog()
    beginDialog.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    
    

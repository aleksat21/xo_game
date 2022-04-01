from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QKeySequence


from typing import List
import copy
from main import XO

class Game:
    results = {"resP1" : 0 , "resP2" : 0 , "resTie" : 0}
    resP1 = 0
    resP2 = 0
    resTie = 0

    def clearResult():
        Game.results["resP1"] = 0
        Game.results["resP2"] = 0
        Game.results["resTie"] = 0


    def __init__(self, buttons:dict = None, lines:dict = None, graphicsView:QtWidgets.QGraphicsView = None, mode = None, label_players:dict = None, lcds:dict = None):
        self.table_state = [['.', '.','.'], 
                            ['.', '.','.'], 
                            ['.', '.','.']]


        # TODO podesiti da moze i racunar da bude X , to bi moralo u kontruktoru da se namesta i u Min, Max
        # 1 je igrac, 2 je racunar za sada
        self.player_turn = 1

        # labele cije se boje menjaju u zavisnosti od poteza igraca
        self.label_players = label_players

        # rezultat
        self.lcds = lcds
        
        # mode 1 - vs AI ,  2 - vs player
        self.mode = mode

        self.buttons = buttons

        self.finished = False
        self.lines = lines

        self.graphicsView = graphicsView
    
    def find_in_matrix(self, el):
        x_coord = (el - 1) // 3
        y_coord = (el - 1) % 3
        return (x_coord , y_coord)

    def evaluate(self, table_state):
        if table_state[0][0] != '.':
            if (table_state[0][0] == table_state[0][1] and table_state[0][1] == table_state[0][2]):
                
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["HU"].show()
                
                if table_state[0][0] == 'X':
                    return -1
                else:
                    return 1 
            elif (table_state[0][0] == table_state[1][0] and table_state[1][0] == table_state[2][0]):
                
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["VL"].show()

                if table_state[0][0] == 'X':
                    return -1
                else:
                    return 1 
        if table_state[1][1] != '.':
            if (table_state[1][1] == table_state[0][1] and table_state[1][1] == table_state[2][1]):
                
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["VC"].show()
                
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
            elif (table_state[1][1] == table_state[1][0] and table_state[1][0] == table_state[1][2]):
                
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["HC"].show()
                
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
            elif (table_state[1][1] == table_state[0][2] and table_state[0][2] == table_state[2][0]):
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["DTL"].show()
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
            elif(table_state[1][1] == table_state[0][0] and table_state[0][0] == table_state[2][2]):   
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["DTR"].show()
                
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
        if table_state[2][2] != '.':
            if (table_state[2][2] == table_state[2][1] and table_state[2][1] == table_state[2][0]):
                
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["HB"].show()
                
                if table_state[2][2] == 'X':
                    return -1
                else:
                    return 1
            elif (table_state[2][2] == table_state[1][2] and table_state[1][2] == table_state[0][2]):
                
                if self.finished:
                    self.graphicsView.raise_()
                    self.lines["VR"].show()
                
                if table_state[2][2] == 'X':
                    return -1
                else:
                    return 1
        
        for array in table_state:
            for el in array:
                if el == '.':
                    return None
        return 0


    def getNextSteps(table_state, sign):
        next_states = []
        next_steps = []

        for i in range(3):
            for j in range(3):
                if table_state[i][j] == '.':
                    tmp = copy.deepcopy(table_state)
                    tmp[i][j] = sign
                    next_states.append(tmp)
                    next_steps.append((i, j))
        return zip(next_states, next_steps)
    
    def testWinner(self):
        pobednik = self.evaluate(self.table_state)
        if pobednik != None:
            self.finished = True
            pobednik = self.evaluate(self.table_state)
            if pobednik == -1:
                Game.results["resP1"] += 1
                self.lcds["lcdP1"].display(Game.results["resP1"])
            elif pobednik == 1:
                Game.results["resP2"] += 1
                self.lcds["lcdP2"].display(Game.results["resP2"])
            elif pobednik == 0:
                Game.results["resTie"] += 1
                self.lcds["lcdTie"].display(Game.results["resTie"])
        return pobednik
    
    def colorGreenFirstPlayer(self):
        self.label_players["lbP1"].setStyleSheet("""color: white;
                background-color: rgb(138, 226, 52);
                font: 36pt "Times New Roman";
                border-radius: 20px;
                """)
        self.label_players["lbP2"].setStyleSheet("""color: white;
                background-color: rgb(239, 41, 41);
                font: 36pt "Times New Roman";
                border-radius: 20px;""")
    def colorGreenSecondPlayer(self):
        self.label_players["lbP2"].setStyleSheet("""color: white;
                background-color: rgb(138, 226, 52);
                font: 36pt "Times New Roman";
                border-radius: 20px;
                """)
        self.label_players["lbP1"].setStyleSheet("""color: white;
                background-color: rgb(239, 41, 41);
                font: 36pt "Times New Roman";
                border-radius: 20px;""")

    
    def updateTableStatePlayer(self, rbr: int, clickedButton: QtWidgets.QPushButton):
        # vs AI
        if self.mode == 1:
            if self.player_turn == 1:
                (x , y) = self.find_in_matrix(rbr + 1)
                self.table_state[x][y] = 'X'
    
                # TODO , ocistiti malo ovaj deo koda ako moze krace da se menja samo boja , probati sa .setFont(QColor)
                clickedButton.setStyleSheet("""QPushButton{
                                            background-color: rgb(186, 189, 182);
                                            border-radius: 20px;
                                            font: 30pt "Times New Roman";
                                            color: rgb(204, 0, 0);
                                        }
                                        QPushButton:pressed {
                                            background-color: rgb(156, 159, 152);
                                            border-style: inset;
                                        } """)
                clickedButton.setText("X")
                clickedButton.setEnabled(False)
                    
                if self.testWinner() == None:
                    self.player_turn = 2
                    self.updateTableStateAI()
        # singleplayer
        if self.mode == 2:
            if self.player_turn == 1:
                self.colorGreenSecondPlayer()
                (x , y) = self.find_in_matrix(rbr + 1)
                self.table_state[x][y] = 'X'
   
                # TODO , ocistiti malo ovaj deo koda ako moze krace da se menja samo boja , probati sa .setFont(QColor)
                clickedButton.setStyleSheet("""QPushButton{
                                           background-color: rgb(186, 189, 182);
                                           border-radius: 20px;
                                           font: 30pt "Times New Roman";
                                           color: rgb(204, 0, 0);
                                       }
                                       QPushButton:pressed {
                                           background-color: rgb(156, 159, 152);
                                           border-style: inset;
                                       } """)
                clickedButton.setText("X")
                clickedButton.setEnabled(False)

                if self.testWinner() == None:
                    self.player_turn = 2
            elif self.player_turn == 2:
                self.colorGreenFirstPlayer()
                (x , y) = self.find_in_matrix(rbr + 1)
                self.table_state[x][y] = 'O'
   
                # TODO , ocistiti malo ovaj deo koda ako moze krace da se menja samo boja , probati sa .setFont(QColor)
                clickedButton.setStyleSheet("""QPushButton{
                                     background-color: rgb(186, 189, 182);
                                     border-radius: 20px;
                                     font: 30pt "Times New Roman";
                                     color:rgb(0, 0, 0);
                                 }
                                 QPushButton:pressed {
                                     background-color: rgb(156, 159, 152);
                                     border-style: inset;
                                 } """)
                clickedButton.setText("O")
                clickedButton.setEnabled(False)

                if self.testWinner() == None:
                    self.player_turn = 1                            
                
    def updateTableStateAI(self):
        if self.player_turn == 2:
            # TODO alpha-beta optimizacija
            # TODO osigurati se kada igra AI da se disabluju dugmici pa kasnije da se aktiviraju ponovo samo oni koji su pre poteza bili aktivni
            (best_table_state , x, y) = self.Max(self.table_state)

            self.table_state[x][y] = 'O'
            rbr = x * 3 + y

            self.buttons[f"bt{rbr}"].setStyleSheet("""QPushButton{
                                    background-color: rgb(186, 189, 182);
                                    border-radius: 20px;
                                    font: 30pt "Times New Roman";
                                    color:rgb(0, 0, 0);
                                }
                                QPushButton:pressed {
                                    background-color: rgb(156, 159, 152);
                                    border-style: inset;
                                } """)
            self.buttons[f"bt{rbr}"].setText("O")
            self.buttons[f"bt{rbr}"].setEnabled(False)

            
            if self.testWinner() == None:
                self.player_turn = 1

    def Max(self, table_state):
        current_evaluation = self.evaluate(table_state)

        if current_evaluation != None:
            return (current_evaluation, None, None)
        
        a = float('-inf')

        best_x = None
        best_y = None

        for next_state, coords in Game.getNextSteps(table_state, 'O'):
            max_of_min, x, y = self.Min(next_state)

            if max_of_min > a:
                a = max_of_min
                best_x = coords[0] #x
                best_y = coords[1] #y

        return a , best_x, best_y         

    def Min(self, table_state):
        current_evaluation = self.evaluate(table_state)

        if current_evaluation != None:
            return (current_evaluation, None, None)
        
        a = float('inf')

        best_x = None
        best_y = None

        for next_state, coords in Game.getNextSteps(table_state, 'X'):
            min_of_max, x, y = self.Max(next_state)

            if min_of_max < a:
                a = min_of_max
                best_x = coords[0] #x
                best_y = coords[1] #y

        return a, best_x, best_y
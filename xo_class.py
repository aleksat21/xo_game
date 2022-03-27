from pickle import NONE
from select import select
from typing import List
from unittest import case
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QKeySequence

from typing import List

import copy

class Game:
    def __init__(self, tbUserManual: QtWidgets.QTextBrowser, buttons:dict = None, lines:dict = None):
        self.table_state = [['.', '.','.'], 
                            ['.', '.','.'], 
                            ['.', '.','.']]


        # TODO podesiti da moze i racunar da bude X , to bi moralo u kontruktoru da se namesta i u Min, Max
        # 1 je igrac, 2 je racunar za sada
        self.player_turn = 1


        self.buttons = buttons

        self.finished = False
        self.lines = lines

        self.tbUserManual = tbUserManual
        self.tbUserManual.setText(Game.get_uputstvo())

    def get_uputstvo():
        uputstvo = "Korisnicko uputstvo: \n 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9\n"
        return uputstvo
    
    def find_in_matrix(self, el):
        x_coord = (el - 1) // 3
        y_coord = (el - 1) % 3
        return (x_coord , y_coord)

    def evaluate(self, table_state):
        if table_state[0][0] != '.':
            if (table_state[0][0] == table_state[0][1] and table_state[0][1] == table_state[0][2]):
                
                if self.finished:
                    self.lines["HU"].show()
                
                if table_state[0][0] == 'X':
                    return -1
                else:
                    return 1 
            elif (table_state[0][0] == table_state[1][0] and table_state[1][0] == table_state[2][0]):
                
                if self.finished:
                    self.lines["VL"].show()

                if table_state[0][0] == 'X':
                    return -1
                else:
                    return 1 
        if table_state[1][1] != '.':
            if (table_state[1][1] == table_state[0][1] and table_state[1][1] == table_state[2][1]):
                
                if self.finished:
                    self.lines["VC"].show()
                
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
            elif (table_state[1][1] == table_state[1][0] and table_state[1][0] == table_state[1][2]):
                
                if self.finished:
                    self.lines["HC"].show()
                
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
            elif (table_state[1][1] == table_state[0][2] and table_state[0][2] == table_state[2][0]):
                # TODO dijagonala
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
            elif(table_state[1][1] == table_state[0][0] and table_state[0][0] == table_state[2][2]):   
                # TODO dijagonala
                if table_state[1][1] == 'X':
                    return -1
                else:
                    return 1
        if table_state[2][2] != '.':
            if (table_state[2][2] == table_state[2][1] and table_state[2][1] == table_state[2][0]):
                
                if self.finished:
                    self.lines["HB"].show()
                
                if table_state[2][2] == 'X':
                    return -1
                else:
                    return 1
            elif (table_state[2][2] == table_state[1][2] and table_state[1][2] == table_state[0][2]):
                
                if self.finished:
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

        restart = "Pritisnite restart da biste poceli ponovo partiju.."
        if pobednik != None:
            self.finished = True
            pobednik = self.evaluate(self.table_state)
            if pobednik == -1:
                self.tbUserManual.setText("Pobedio je igrac!\n\n" + restart)
            elif pobednik == 1:
                self.tbUserManual.setText('Pobedio je racunar!\n\n' + restart)
            elif pobednik == 0:
                self.tbUserManual.setText('Nereseno je!\n' + restart)

        return pobednik
    
    def updateTableStatePlayer(self, rbr: int, clickedButton: QtWidgets.QPushButton):
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
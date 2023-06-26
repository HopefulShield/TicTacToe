import sys
import numpy as np

""" 
AI player 
check if can win 
check if can lose 
check next best position 
check columns, check rows, check diagonals 
"""

""" 
main function with arg dictating that if arg0 = a, the ai player enabled {
initialize the 3x3 matrix arr to be empty 
"""
players = ["X", "O"]


class Board: 
    #board = np.full((3, 3), '_')
    def __init__(self): 
        self.player = 0 
        self.board = np.full((3, 3), "_")
        
    def print(self): 
        print("print Game")
        print("Player ", players[self.player % 2], "'s move")
        for i in range(3): 
            print(self.board[i])
            
    def unfilledCK(self):  
        #print("check if any unfilled spots: ", np.any(self.board == "_")) 
        return np.any(self.board == "_") 
        
    def winCK(self): 
        rplayer = self.rowCK() 
        cplayer = self.colCK() 
        dplayer = self.diaCK() 
        return rplayer or cplayer or dplayer        
        
    def rowCK(self):  
        for i in range(3): 
            #print(self.board[i, :])  
            if np.all(self.board[i, :] == "X"): 
                return "X"
            elif np.all(self.board[i, :] == "O"): 
                return "O"
        return None
    
    def colCK(self):  
        for i in range(3): 
            #print(self.board[:, i]) 
            if np.all(self.board[:, i] == "X"): 
                return "X"
            elif np.all(self.board[:, i] == "O"): 
                return "O" 
        return None
        
    def diaCK(self):  
        tltobr = self.board.diagonal()
        trtobl = np.fliplr(self.board).diagonal() 
        
        if (np.all(tltobr == "X") or np.all(trtobl == "X")): 
            return "X"
        elif (np.all(tltobr == "O") or np.all(trtobl == "O")): 
            return "O" 
        return None 
        
    def insertMove(self, row, col): 
        self.board[row][col] = players[self.player % 2]
        self.player += 1  
    
    def spotMT(self, row, col):  
        isempty = self.board[row][col] == "_" 
        return isempty 
            
    def getInput(self, string): 
        inputString = "Enter a Number between 0 and 2 for " + string + " selection: "
        while True:
            try:
                data=int(input(inputString))
                print("You entered: ", data) 
            except ValueError:
                print("Invalid input: Needs to be integer value") 
            else: 
                if ((data < 3) and (data >= 0)): 
                    return data 
                else: 
                    print("Invalid Input: Needs to be between 0 and 2")
                
    def getRowCol(self): 
        row = self.getInput("Row") 
        col = self.getInput("Col") 
        return row, col 
    
    def Game(self): 
        result = None 
        while self.unfilledCK(): #unfilled (true) = do not break out, filled = (false) = break out
            self.print() 
            while True: 
                row, col = self.getRowCol() 
                if self.spotMT(row, col): break 
                else: print("Invalid Input: Needs to be on an empty spot") 
            self.insertMove(row, col) 
            result = self.winCK() 
            if not (result == None): 
                break
        #self.print()
        print("Final Board")
        for i in range(3): 
            print(self.board[i])
        print("Winner of game is player: ", result)
        #print("Game is Tied")


if __name__ == "__main__":   
    testBoard = Board() 
    testBoard.Game() 
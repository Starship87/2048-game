#2048 game
import random
import time

score = 0
highscore = 0

board =[]

def newgame():
    global board
    #fill board
    board = []
    row = []
    for i in range(4):
        row.append(0)
    for j in range(4):
        board.append(row.copy())

def showboard():
    for i in range(4):
        row = ""
        for j in range (4):
            row = row + str(board[i][j]) + " "
        print(row)

def newnumber():
    newnum = 0
    newrow = random.randint(0,3)
    newcol = random.randint(0,3)
    while board[newrow][newcol] != 0:
        newrow = random.randint(0,3)
        newcol = random.randint(0,3)
    rand = random.randint(1, 100)
    if rand < 80:
        newnum = 2
    else:
        newnum = 4
        
newgame()
showboard()
            


     
    

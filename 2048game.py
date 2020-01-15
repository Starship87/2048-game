#2048 game
import random

score = 0
highscore = 0

board = []

def newgame():
    global board
    #fill board
    board = []
    row = []
    for i in range(4):
        row.append(0)
    for j in range(4):
        board.append(row.copy())
    newnumber()
    newnumber()

def showboard():
    for i in range(4):
        row = ""
        for j in range(4):
            row = row + str(board[i][j]) + " "
        print(row)

def newnumber():
    newnum = 0
    newrow = random.randint(0,3)
    newcol = random.randint(0,3)
    while board[newrow][newcol] != 0:
        newrow = random.randint(0,3)
        newcol = random.randint(0,3)
    rand = random.randint(1,100)
    if rand < 80:
        newnum = 2
    else:
        newnum = 4
    board[newrow][newcol] = newnum

def move():
    print("Select your direction (<, >, v, ^)")
    mymove = input()
    if mymove == "<":
        rotate(2)
        swiperight()
        rotate(2)
    elif mymove == ">":
        swiperight()
    elif mymove == "v":
        rotate(3)
        swiperight()
        rotate(1)
    elif mymove == "^":
        rotate(1)
        swiperight()
        rotate(3)
    else:
        print("Invalid selection")
        move()
    newnumber()
    showboard()
    move()

def swiperight():
    #a function to add the numbers and move them right
    global board
    for row in board:
        #if row[0] == row[1] and row[2] == row[3]:
        for i in range (3):
            n1 = row[i]
            n2 = row[i+1]
            if n1 == n2 or n2 == 0:
                row[i] = 0
                row[i+1] = n1 + n2
        for i in range (2):
                n1 = row[i]
                n2 = row[i+1]
                if n1 == n2 or n2 == 0:
                    row[i] = 0
                    row[i+1] = n1 + n2
        
def rotate(number_turns):
    global board
    # a function to rotate the board some number of quarter turns clockwise
    for j in range(number_turns):
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        for i in range (3, -1, -1):
            temp1.append(board[i][0])
            temp2.append(board[i][1])
            temp3.append(board[i][2])
            temp4.append(board[i][3])
        board = []
        board.append(temp1)
        board.append(temp2)
        board.append(temp3)
        board.append(temp4)
        def checkwin():
            win = False
            for row in board:
                for item in row:
                    if item == 2048:
                        win = True
    return win
newgame()
showboard()
move()

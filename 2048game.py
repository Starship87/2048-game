#2048 game
import random
from  tkinter import *

root = Tk()

score = 0
highscore = 0

board = []
squares = []
colors={
    0: "lime",
    2: "purple",
    4: "aqua",
    8: "BlanchedAlmond",
    16:"Crimson",
    32:"blue",
    64:"cyan",
    128:"yellow",
    256:"coral",
    512:"green",
    1024:"pink",
    2048:"violet",
    }

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

def makeboard():
    global squares
    #set up tkinter controls
    #title
    title = Label(root, text="Awesome 2048 Game",font="Arial 17 bold")
    title.grid(row=0, column=0, columnspan=4)
    #instructions
    instruc = Label(root, text="use the arrow keys to move",font="arial 12")
    instruc.grid(row=1, column=0, columnspan=4)
    #restart or new game
    restart = Button(root, text="New Game", font="Arial 14 bold")
    restart.grid(row=6, column=0, columnspan=2)
    #quit
    quitbtn = Button(root, text="Quit", font="Arial 14 bold")
    quitbtn.grid(row=6, column=2, columnspan=2)
    #all the squares
    for r in range(4):
        temprow = []
        for c in range(4):
            templabel = Label(root, height=2, width=4, relief="ridge", font="Arial 16 bold")
            temprow.append(templabel)
        squares.append(temprow)
        
    for r in range(4):
        for c in range(4):
            sq = squares[r][c]
            sq.grid(row=r+2, column=c)

def showboard():
    for i in range(4):
        row = ""
        for j in range(4):
            row = row + str(board[i][j]) + " "
        print(row)

def displayboard():
    global squares
    for r in range(4):
        for c in range(4):
            mycolor = colors[board[r][c]]
            squares[r][c].config(text=board[r][c],bg=mycolor)
        

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

def moveleft(e):
    rotate(2)
    swiperight()
    rotate(2)
    displayboard()
def moveright(e):
    swiperight()
    displayboard()
def moveup(e):
    rotate(1)
    swiperight()
    rotate(3)
    displayboard()
def movedown(e):
    rotate(3)
    swiperight()
    rotate(1)
    displayboard()

def bindkeys():
    global root
    root.bind("<down>", movedown)
    root.bind("<up>", moveup)
    root.bind("<right>", moveright)
    root.bind("<left>", moveleft)
    

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
makeboard()
newgame()
displayboard()
bindkeys()
root.mainloop()

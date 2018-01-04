#Pedro Gallino
#12/17/17
#finalProject.py - snake game

from ggame import *
from random import randint

#Constants
COLUMNS = 7
ROWS = 7
GREEN = Color(0x00ff00,1)
BLUE = Color(0x0000ff,1)
BLACK = Color(0x000000,1)
WHITE = Color(0xFFFFFF,1)

#Loads the Snake Board with beggining Snake and Food location
def loadSnakeBoard():
    data['board'] = []
    for i in range(COLUMNS):
        data['board'].append([0]*ROWS)
    data['board'][0][0] = 1
    data['board'][4][4] = -1

#Deletes the whole board and then checks if it should Sprite the you lose screen, If not then it draws the board
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    if data['gameOver'] == True:
        gameOverText = TextAsset('You LOSE', fill=BLACK, style='bold 40pt Times')
        Sprite(gameOverText,(500,300))
    else:
        drawSnakeBoard()

#Makes a loop and for each cell in the board and calls a fucntion that draws a square for each
def drawSnakeBoard():
    for c in range(COLUMNS):
        for r in range(ROWS):
            drawSnakeCell(r,c)

#Sprites a square for each cell and then checks to see if it needs to make a snake or a food in a squaew
def drawSnakeCell(rows,columns):
    square = RectangleAsset(50,50,LineStyle(2,BLACK),WHITE)
    data['Snake'] = EllipseAsset(20,20,LineStyle(2,GREEN),GREEN)
    data['food'] = EllipseAsset(20,20,LineStyle(2,BLUE),BLUE)
    
    Sprite(square,(rows*50,columns*50))
    
    if data['board'][columns][rows] >= 1:
        data['SnakeLocation'] = Sprite(data['Snake'],(rows*50+25,columns*50+25))
    elif data['board'][columns][rows] == -1:
        Sprite(data['food'],(rows*50+25,columns*50+25))

#If the game is not over: checks to see if the snake ran off the board, checks to see if the the snake ran into itself
#Checks to see if the snake ran into a fruit and checks if it did nothing, then it moves the snake accordinly
def moveSnake(r,c):
    if data['gameOver'] == False:
        findSnakeHead()
        
        #checks to see if the snake ran off the board, if it did then it makes the game be over
        if (data['SnakeHeadRow']*50 + r*50 ) < 0 or (data['SnakeHeadColumn']*50+ c*50) < 0 or (data['SnakeHeadRow']*50 + r*50) > 800 or (data['SnakeHeadColumn']*50 + c*50) > 500:
            data['gameOver'] = True
        
        #checks to see if the the snake ran into itself, if it did then it makes the game be over
        elif data['board'][data['SnakeHeadColumn']+c][data['SnakeHeadRow']+r] > 0:
            data['gameOver'] = True
            
        #Checks to see if the snake ran into a fruit, if it did it moves the snake accordingly and doesn't remove the tail
        if data['board'][data['SnakeHeadColumn']+c][data['SnakeHeadRow']+r] == -1:
            data['board'][data['SnakeHeadColumn']+c][data['SnakeHeadRow']+r] = data['head']+1
            data['SnakeLocation'] = Sprite(data['Snake'],(data['SnakeHeadRow']*50+r*50,data['SnakeHeadColumn']*50+c*50))
            redrawAll()
            placeFood()
        
        #If nothing before it happens it moves the snake accordingly and also removes the tail
        else:
            data['board'][data['SnakeHeadColumn']+c][data['SnakeHeadRow']+r] = data['head']+1
            data['SnakeLocation'] = Sprite(data['Snake'],(data['SnakeHeadRow']*50+r*50,data['SnakeHeadColumn']*50+c*50))
            redrawAll()
            removeTail()
    
#removes the tail of the snake by subtracting one to every snake of the board
def removeTail():
    for k in range(COLUMNS):
        for i in range(ROWS):
            if data['board'][k][i] >= 1:
                data['board'][k][i] -= 1

#Find the size and location of the head of the snake
def findSnakeHead():
    data['head'] = 0
    data['SnakeHeadRow'] = 0
    data['SnakeHeadColumn'] = 0
    
    
    for k in data['board']:
        for i in k:    
            if i > data['head']:
                data['head'] = i
    
    SnakeHeadRow = 0
    SnakeHeadColumn = 0
    for j in range(0,COLUMNS):
        SnakeHeadRow = 0
        for p in range(0,ROWS):
            if data['board'][SnakeHeadColumn][SnakeHeadRow] == data['head']:
                data['SnakeHeadRow'] = SnakeHeadRow
                data['SnakeHeadColumn'] = SnakeHeadColumn
                break    
            SnakeHeadRow += 1
        SnakeHeadColumn += 1
   
#Places a food in a random unoccupied sport in the board    
def placeFood():
    data['RandomRow'] = randint(0,ROWS)-1
    data['RandomColumn'] = randint(0,COLUMNS)-1
    if data['board'][data['RandomColumn']][data['RandomRow']] == 0:
        data['board'][data['RandomColumn']][data['RandomRow']] = -1
        Sprite(data['food'],(data['RandomRow']*50+25,data['RandomColumn']*50+25))
    else:
        placeFood()

#If the right arrow is pressed the snake moves right, and it changes the variable to keep it moving right
def keyPress1(event):
    moveSnake(1,0)
    data['movingDirection'] = 'right'
    redrawAll()

#If the left arrow is pressed the snake moves left, and it changes the variable to keep it moving left
def keyPress2(event):
    moveSnake(-1,0)
    data['movingDirection'] = 'left'
    redrawAll()

#If the up arrow is pressed the snake moves up, and it changes the variable to keep it moving up
def keyPress3(event):
    moveSnake(0,-1)
    data['movingDirection'] = 'up'
    redrawAll()

#If the up arrow is pressed the snake moves up, and it changes the variable to keep it moving up
def keyPress4(event):
    moveSnake(0,1)
    data['movingDirection'] = 'down'
    redrawAll()
    
#Checks to see which direction the snake is moving and it keeps it moving in the same direction
def step():
    if data['movingDirection'] == 'right':
        moveSnake(1,0)
    elif data['movingDirection'] == 'left':
        moveSnake(-1,0)
    elif data['movingDirection'] == 'up':
        moveSnake(0,-1)
    elif data['movingDirection'] == 'down':
        moveSnake(0,1)
        

if __name__ == '__main__':
    
    data = {}
    data['gameOver'] = False
    data['movingDirection'] = 'down'
    loadSnakeBoard()
    redrawAll()
    
    App().listenKeyEvent("keydown","right arrow", keyPress1)
    App().listenKeyEvent("keydown","left arrow", keyPress2)
    App().listenKeyEvent("keydown","up arrow", keyPress3)
    App().listenKeyEvent("keydown","down arrow", keyPress4)
    App().run(step)
    

























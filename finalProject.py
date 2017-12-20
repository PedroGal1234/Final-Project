#Pedro Gallino
#12/17/17
#finalProject.py - snake game

from ggame import *
from random import randint

COLUMNS = 10
ROWS = 16
GREEN = Color(0x00ff00,1)
BLUE = Color(0x0000ff,1)
BLACK = Color(0x000000,1)
WHITE = Color(0xFFFFFF,1)

def loadSnakeBoard():
    data['board'] = []
    for i in range(COLUMNS):
        data['board'].append([0]*ROWS)
    data['board'][1][1] = 1
    data['board'][7][14] = -1

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    drawSnakeBoard()
    if data['gameOver'] == True:
        gameOverText = TextAsset('You LOSE', fill=BLACK, style='bold 40pt Times')
        Sprite(gameOverText,(500,300))

def drawSnakeBoard():
    for c in range(COLUMNS):
        for r in range(ROWS):
            drawSnakeCell(r,c)

def drawSnakeCell(rows,columns):
    square = RectangleAsset(50,50,LineStyle(2,BLACK),WHITE)
    data['Snake'] = EllipseAsset(20,20,LineStyle(2,GREEN),GREEN)
    data['food'] = EllipseAsset(20,20,LineStyle(2,BLUE),BLUE)
    
    Sprite(square,(rows*50,columns*50))
    
    if data['board'][columns][rows] == 1:
        Sprite(data['Snake'],(rows*50,columns*50))
    elif data['board'][columns][rows] == -1:
        Sprite(data['food'],(columns*50,rows*50))
    
def placeFood():
    row = randint(0,ROWS)-1
    column = randint(0,COLUMNS)-1
    if data['board'][column][row] == 0:
        data['board'][column][row] = -1
        Sprite(data['food'],(row,column))
    else:
        placeFood()
    

if __name__ == '__main__':
    
    data = {}
    data['gameOver'] = False
    
    loadSnakeBoard()
    drawSnakeBoard()
    
    App().run()
























#Pedro Gallino
#12/17/17
#finalProject.py - snake game

from ggame import *
from random import randint

COLUMNS = 7
ROWS = 7
GREEN = Color(0x00ff00,1)
BLUE = Color(0x0000ff,1)
BLACK = Color(0x000000,1)
WHITE = Color(0xFFFFFF,1)

def loadSnakeBoard():
    data['board'] = []
    for i in range(COLUMNS):
        data['board'].append([0]*ROWS)
    data['board'][0][0] = 1
    data['board'][4][4] = -1

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    if data['gameOver'] == True:
        gameOverText = TextAsset('You LOSE', fill=BLACK, style='bold 40pt Times')
        Sprite(gameOverText,(500,300))
    else:
        drawSnakeBoard()

def drawSnakeBoard():
    for c in range(COLUMNS):
        for r in range(ROWS):
            drawSnakeCell(r,c)

def drawSnakeCell(rows,columns):
    square = RectangleAsset(50,50,LineStyle(2,BLACK),WHITE)
    data['Snake'] = EllipseAsset(20,20,LineStyle(2,GREEN),GREEN)
    data['food'] = EllipseAsset(20,20,LineStyle(2,BLUE),BLUE)
    
    Sprite(square,(rows*50,columns*50))
    
    if data['board'][columns][rows] >= 1:
        data['SnakeLocation'] = Sprite(data['Snake'],(rows*50+25,columns*50+25))
    elif data['board'][columns][rows] == -1:
        Sprite(data['food'],(rows*50+25,columns*50+25))


def moveSnake(r,c):
    if (data['SnakeLocation'].x + r*50 ) < 0 or (data['SnakeLocation'].y + c*50) < 0 or (data['SnakeLocation'].x + r*50) > 800 or (data['SnakeLocation'].y + c*50) > 500:
        data['gameOver'] = True
    """
    elif data['board'][data['SnakeLocation'].x/50 + r][data['SnakeLocation'].y/50 + c] > 0:
        data['gameOver'] = True
    """
    if data['board'][data['SnakeLocation'].y/50+c][data['SnakeLocation'].x/50+r] == -1:
        findSnakeHead()
        data['board'][data['SnakeLocation'].y/50+c][data['SnakeLocation'].x/50+r] = data['head']+1
        data['SnakeLocation'] = Sprite(data['Snake'],(data['SnakeLocation'].x+r*50,data['SnakeLocation'].y+c*50))
        redrawAll()
        placeFood()

    
    else:
        findSnakeHead()
        print('(',data['SnakeHeadRow'],',',data['SnakeHeadColumn'],')')
        data['board'][data['SnakeLocation'].y/50+c][data['SnakeLocation'].x/50+r] = data['head']+1
        data['SnakeLocation'] = Sprite(data['Snake'],(data['SnakeLocation'].x+r*50,data['SnakeLocation'].y+c*50))
        redrawAll()
        removeTail()


def removeTail():
    for k in range(COLUMNS):
        for i in range(ROWS):
            if data['board'][k][i] >= 1:
                data['board'][k][i] -= 1

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
       
def placeFood():
    row = randint(0,ROWS)-1
    column = randint(0,COLUMNS)-1
    if data['board'][column][row] == 0:
        data['board'][column][row] = -1
        Sprite(data['food'],(row*50+25,column*50+25))
    else:
        placeFood()

def keyPress1(event):
    moveSnake(1,0)
    redrawAll()

def keyPress2(event):
    moveSnake(-1,0)
    redrawAll()

def keyPress3(event):
    moveSnake(0,-1)
    redrawAll()

def keyPress4(event):
    moveSnake(0,1)
    redrawAll()

if __name__ == '__main__':
    
    data = {}
    data['gameOver'] = False
    
    loadSnakeBoard()
    redrawAll()
    
    App().listenKeyEvent("keydown","right arrow", keyPress1)
    App().listenKeyEvent("keydown","left arrow", keyPress2)
    App().listenKeyEvent("keydown","up arrow", keyPress3)
    App().listenKeyEvent("keydown","down arrow", keyPress4)
    App().run()
    

























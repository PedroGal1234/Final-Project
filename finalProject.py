#Pedro Gallino
#12/17/17
#finalProject.py - snake game

from ggame import *

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
    data['board'][0][0] = 1
    data['board'][1][1] = -1

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    drawSnakeBoard()
    if data['gameOver'] == True:
        gameOverText = TextAsset('You LOSE', fill=BLACK, style='bold 40pt Times')
        Sprite(gameOverText,(500,300))

def drawSnakeBoard():
  drawSnakeCell(ROWS,COLUMNS)

def drawSnakeCell(rows,columns):
    square = RectangleAsset(50,50,LineStyle(2.5,BLACK),WHITE)
    for i in range(COLUMNS):
        for k in range(ROWS):
            Sprite(square,(data['X-cell'],data['Y-cell']))
            data['X-cell'] += 50
        data['Y-cell'] += 50
        data['X-cell'] = 0
    
    


if __name__ == '__main__':
    
    data = {}
    data['gameOver'] = False
    data['X-cell'] = 0
    data['Y-cell'] = 0
    
    loadSnakeBoard()
    drawSnakeCell(ROWS,COLUMNS)
    
    App().run()
























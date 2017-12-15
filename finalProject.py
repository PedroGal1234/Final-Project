#Pedro Gallino
#12/17/17
#finalProject.py - snake game

from ggame import *

COLUMNS = 8
ROWS = 8
GREEN = Color(0x00ff00,1)
BLUE = Color(0x0000ff,1)
BLACK = Color(0x000000,1)
WHITE = Color(0xFFFFFF,1)

def loadSnakeBoard():
    board = []
    for i in range(COLUMNS):
        board.append([0]*ROWS)
    board[0][0] = 1
    board[1][1] = -1
    data['board'] = board

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    drawSnakeBoard()
    if data['gameOver'] == True:
        gameOverText = TextAsset('You LOSE', fill=BLACK, style='bold 40pt Times')
        Sprite(gameOverText,(500,300))

def drawSnakeBoard():
    for cell in data['board']:
        drawSnakeCell(ROWS,COLUMNS)

def drawSnakeCell(rows,columns):
    square = RectangleAsset(100,100,LineStyle(10,BLACK),WHITE)
    Sprite(square,(175,100))
    


if __name__ == '__main__':
    
    data = {}
    data['gameOver'] = False
    
    loadSnakeBoard()
    drawSnakeCell(ROWS,COLUMNS)
























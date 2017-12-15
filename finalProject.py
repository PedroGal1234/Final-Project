#Pedro Gallino
#12/17/17
#finalProject.py - snake game

from ggame import *

COLUMNS = 8
ROWS = 8
GREEN = Color(0x00ff00,1)
BLUE = Color(0x000ff,1)
BLACK = Color(0x00000,1)

def loadSnakeBoard():
    board = []
    for i in range(COLUMNS):
        board.append([0]*ROWS)
    board[0][0] = 1
    board[1][1] = -1
    data['board'] = board

def redrawAll:
    for item in App().spritelist[:]:
        item.destroy()

    drawSnakeBoard()
    if data['gameOver'] = True
        gameOverText = TextAsset('You LOSE', fill=BLACK, style='bold 40pt Times')
        Sprite(gameOverText,(500,500))

if __name__ == '__main__':
    
    data = {}
    data['gameOver'] = False
    
    loadSnakeBoard()
    























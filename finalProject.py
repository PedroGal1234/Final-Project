#Pedro Gallino
#12/17/17
#finalProject.py - snake game

from ggame import *

COLUMNS = 8
ROWS = 8

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


if __name__ == '__main__':
    data = {}
    loadSnakeBoard()
    print(data['board'])
    

























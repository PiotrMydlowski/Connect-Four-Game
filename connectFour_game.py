#Connect Four Game by P Mydlowski via tutorial

import pygame
import numpy as np
import sys

ROWS = 6
COLUMNS = 7
SQUARESIZE = 100
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

pygame.init()

width = COLUMNS * SQUARESIZE
height = (ROWS + 1)*SQUARESIZE
size = (width, height)
radius = int(SQUARESIZE/2 -5)
myFont = pygame.font.SysFont("monospace",75)

def createBoard():
    board = np.zeros((ROWS,COLUMNS))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValid(board, col):
    if ((col < 0) or (col > COLUMNS-1)):
        return False

    return board[ROWS -1][col] == 0

def getNextRow(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board, 0))

def winningMove(board, piece):
    #horizontal
    for c in range(COLUMNS-3):
        for r in range (ROWS):
            if board[r][c] == piece and board[r][c+1] == piece:
                if board[r][c+2] == piece and board[r][c+3] == piece:
                    return True
    #vertical
    for c in range(COLUMNS):
        for r in range (ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece:
                if board[r+2][c] == piece and board[r+3][c] == piece:
                    return True
    #backslash
    for c in range(COLUMNS-3):
        for r in range (ROWS-3):
            if board[r][c+3] == piece and board[r+1][c+2] == piece:
                if board[r+2][c+1] == piece and board[r+3][c] == piece:
                    return True

    #slash
    for c in range(COLUMNS-3):
        for r in range (ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece:
                if board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True
            
    return False

def drawBoard(board):

    board = np.flip(board, 0)
    
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if(board[r][c] == 1):
                pygame.draw.circle(screen, RED, (int((c+0.5)*SQUARESIZE), int((r+1.5)*SQUARESIZE)), radius)
            elif(board[r][c] == 2):
                pygame.draw.circle(screen, YELLOW, (int((c+0.5)*SQUARESIZE), int((r+1.5)*SQUARESIZE)), radius)
            else:
                pygame.draw.circle(screen, BLACK, (int((c+0.5)*SQUARESIZE), int((r+1.5)*SQUARESIZE)), radius)
    pygame.display.update()

board = createBoard()
gameOver = False
turn = 0
screen = pygame.display.set_mode(size)
drawBoard(board)

while not gameOver:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEMOTION:
            posx = int(event.pos[0]//SQUARESIZE)
            if turn%2 == 0:
                color = RED
            else:
                color = YELLOW
                
            pygame.draw.rect(screen, BLACK,(0,0,width,SQUARESIZE))
            pygame.draw.circle(screen, color, (int((posx+0.5)*SQUARESIZE), int(0.5*SQUARESIZE)), radius)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #ASK player 1
            if turn%2 == 0:
                selection = int(event.pos[0]//SQUARESIZE)
                if isValid(board, selection):
                    row = getNextRow(board, selection)
                    dropPiece(board, row, selection, 1)
                    turn += 1
                    if winningMove(board, 1):
                        print("Player 1 wins.")
                        label = myFont.render("PLAYER 1 WINS!",1,BLUE)
                        screen.blit(label, (40,10))
                        gameOver = True

            #ASK player 2
            else:
                selection = int(event.pos[0]//SQUARESIZE)
                if isValid(board, selection):
                    row = getNextRow(board, selection)
                    dropPiece(board, row, selection, 2)
                    turn += 1
                    if winningMove(board, 2):
                        print("Player 2 wins.")
                        label = myFont.render("PLAYER 2 WINS!",1,BLUE)
                        screen.blit(label, (40,10))
                        gameOver = True
            
    drawBoard(board)

##Console version   
##    #Ask player 1
##    if turn%2 == 0:
##        try:
##            selection = int(input("Player 1 moves. Type in a number 0-6: "))
##            if isValid(board, selection):
##                row = getNextRow(board, selection)
##                dropPiece(board, row, selection, 1)
##                if winningMove(board, 1):
##                    print("Player 1 wins.")
##                    gameOver = True
##                
##            else:
##                print("Choose a correct value.")
##                continue
##                
##        except:
##            print("Choose a correct value.")
##            continue
##        printBoard(board)
##    #Ask player 2
##    else:
##        try:
##            selection = int(input("Player 2 moves. Type in a number 0-6: "))
##            if isValid(board, selection):
##                row = getNextRow(board, selection)
##                dropPiece(board, row, selection, 2)
##                if winningMove(board, 2):
##                    print("Player 2 wins.")
##                    gameOver = True
##                
##            else:
##                print("Choose a correct value.")
##                continue
##        except:
##            print("Choose a correct value.")
##            continue
##        printBoard(board)
##
##    turn += 1
##
##input("Press any key to quit.")

pygame.time.wait(3000)
quit()

import random

# Update the board with a new move
def makeMove(board, letter, move):
    pass

# Given a board and a player's letter, check if that player has won
def isWinner(board, letter):
    pass

# Check if the move is valid (the space is empty)
def isSpaceFree(board, move):
    pass

# Check if the board is full
def isBoardFull(board):
    pass

# Get the player's move from input
def getPlayerMove(board):
    pass

def main():
    print ('Welcome to Tic Tac Toe')
    turn = who_goes_first()

    player_letter = input_player_letter()
    #Here assign computer_letter to be 'O' if player_letter is 'X' or vice versa


    # Initialize an empty board list here to pass to draw_board
    #board =
    draw_board(board)

main()

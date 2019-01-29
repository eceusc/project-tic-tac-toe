import random

def draw_board(board):
    # This function prints out the board that it was passed and should not return anything
    #HINT: the parameter board should hold a list that holds the position of 'X's and 'O's
    return

def input_player_letter():
    #Ask the player if they want to be 'X' or 'O'
    #Return the chosen letter
    #Hint: Use a loop to keep prompting the player for a letter if the input is not valid

    return

def who_goes_first():
    #Randomly choose who goes first
    #Return the string 'computer' or 'player'
    #HINT: look up the documentation for the 'random' library

    return

def main():

    print ('Welcome to Tic Tac Toe')
    turn = who_goes_first()

    player_letter = input_player_letter()
    #Here assign computer_letter to be 'O' if player_letter is 'X' or vice versa



    # Initialize your board list here to pass to draw_board
    #board =
    draw_board(board)

main()

# --------------Session 2---------------%

# initialize your board list as global list here to pass to draw the board
Board = [' '] * 10


def is_winner(board, letter):
    '''We want this function to see if the letter has won the game.
    This function will be called after every move so the game can detect the new move
    Given the board array and letter, return True if the player has won or False if the player
    has not won

    Hint: Detect all possibilities on how to win tic tac toe'''


def is_space_free(board, position):
    '''Return True if the space is free, false if it isn't'''


def player_move(board):
    '''Should ask the player where they want to go according to this position chart
                    _7_|_8_|_9_
                    _4_|_5_|_6_
                     1 | 2 | 3
                     (similar to the dialpad)
    Also check if the space is free. If not, prompt the player again
    Returns the integer that represents the position of the player move'''

def make_move(board, letter, position):
    '''Input the letter onto the board at the specified position'''


def is_board_full(board):
    '''We need to check is the board is full to declare a tie

    Hint: you can call other functions in this function'''


def play_again():
    '''Ask the player if they want to play again
    Return True is yes, False if no'''


# --------------Session 1---------------%
import random


def draw_board(board):
    # This function prints out the board that it was passed and should not return anything
    # HINT: pass a list to this function that holds the position of 'X's and 'O's
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('\n')


def input_player_letter():
    # Ask the player if they want to be 'X' or 'O'
    # Return the chosen letter
    # Hint: Use a loop to keep prompting the player for a letter if the input is not valid
    letter = ''
    while (letter not in ['X', 'O']):
        letter = input('Do you want to be X or O?\n').upper()
    return letter


def who_goes_first():
    # Randomly choose who goes first
    # Return the string 'computer' or 'player'
    # HINT: look up the documentation for the 'random' library
    if random.randint(0, 1) == 0:
        # print('You are going first!')
        return 'player'
    else:
        # print('You are going second!')
        return 'computer'


def main():
    print('Welcome to Tic Tac Toe')  # print beginning message

    # now we will use all of our helper functions to create the workflow of the game
    while True:
        # Reset the board, run the setup functions

        # indicate who will go first
        turn = who_goes_first()
        print('The ' + turn + ' will go first')

        # Ask the player for their letter
        player_letter = input_player_letter()
        if player_letter == 'X':
            computer_letter = 'O'
        else:
            computer_letter = 'X'
        game_on = True

        while (game_on):

            # check if player of computer is the starter, then make their move and check for win or tie

            # have a case for if player goes or if computer will go which will
            # 1. draw the board
            # 2. get the move from respective player
            # 3. make the move onto the board
            # 4. check if player/computer won
            # 5. check if its is a tie

            # when the game ends (game_on = False), ask if the player will want to play again
            # break if they do not want to play again




main()
# Description: Tic tac toe
# Requirements:
# 1.) 2 players should be able to play the game (both sitting at the same computer)
# 2.) The board should be printed out every time a player makes a move
# 3.) You should be able to accept input of the player position and then place a symbol on the board
# Author: John Royce Punay
# Date Created: March 4, 2018 3:57 PM

from random import randint

def main():
    print("                                               ")
    print("=========WELCOME TO TIC-TAC-TOE GAME===========")
    print("Please hit any 'button' to start the game!!!!")
    print("===============================================")
    print("                                               ")

    game_start()


def game_start():

    while True:
        board = [' '] * 10
        player1, player2 = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        play_game = input('Are you ready to play? Enter Yes or No.')
        
        if play_game.lower() == 'yes' or play_game.lower() == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1, position)
                if win_check(board, player1):
                    display_board(board)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'
                    
            else:
                 # Player2's turn.
            
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2, position)

                if win_check(board, player2):
                    display_board(board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break

def display_board(board):
    print("======================================================")
    print("|                 |                 |                |")
    print(
        f"|       {board[7]}         |         {board[8]}       |         {board[9]}      |"
    )
    print("|_________________|_________________|________________|")
    print("|                 |                 |                |")
    print(
        f"|       {board[4]}         |         {board[5]}       |         {board[6]}      |"
    )
    print("|_________________|_________________|________________|")
    print("|                 |                 |                |")
    print(
        f"|       {board[1]}         |         {board[2]}       |         {board[3]}      |"
    )
    print("|                 |                 |                |")
    print("======================================================")

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark) # diagonal
           ) 
def choose_first():
    random_number = randint(0,1)
    if random_number == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def clear_output():
    print("\n" * 100)

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# ** Run the main function here **
main()

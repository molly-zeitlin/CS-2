#Author: Molly Zeitlin
#Description: runs a complete game of battleship (user has 10 chances to find 4 randomly placed ships)
#Date: 4/6/2026
#Completed Functions: display_board, choose_ships, get_coordinates, ...
#Log: 1.0 MZ
#Bugs: 
#Bonuses: 

import random

def display_board(board):
    '''Print the board in a user-friendly format.
    Args:
        board: 2 dimensional array
    Returns:
        print: the board in a user-friendly format
    '''
    print("Here is the board:")
    for row in board:                                                                                           #create for loop to isolate each row
        for cell in row:                                                                                        #create another for loop to isolate each cell within each row
            print(cell, end=' ')                                                                                #display cell
        print()

def choose_ships(secret_board):
    '''Randomly choose 4 points on the secret board as the ships.
    Args:
        secret_board: 2 dimensional array
    Returns:
        secret_board: 2 dimensional array with ships chosen
    '''
    for i in range(4):
        row = random.randint(0, 4)
        column = random.randint(0, 4)
        if secret_board[row][column] == "| x |":
            secret_board[row][column] = "| S |"
        else:
            continue
    return secret_board

def get_coordinates(board):
    '''Ask user for coodinate point for their next move.
    Args:
        board: 2 dimensional array
    Returns:
        row: row where user wants to go for next move
        column: column where user wants to go for next mvove
        print: prompts user to enter numbers for coordinate points
    '''
    while True:
        try:
            row = int(input("What row would you like to shoot at? ")) - 1
        except ValueError:
            print("INVALID RESPONSE\nPlease enter valid numbers")
            continue
        try:
            column = int(input("What column would you like to shoot at? ")) - 1
        except ValueError:
            print("INVALID RESPONSE\nPlease enter valid numbers")
            continue
        try:
            if board[row][column] == "| x |":
                return row,column
        except ValueError:
            print("INVALID RESPONSE\nPlease enter valid numbers within range")
        
def player_move(board, secret_board, row,column):
    '''
    Shoots at user's desired point, and determines whether player "hit" or "missed" a ship.
    Args:
        board: 2 dimensional array
        secret_board: 2 dimensional array with ships chosen
        row: value of the row user wants to shoot at
        column: value of the column user wants to shoot at
    Returns:
        board: 2 dimensional array (altered with "hits" or "misses")
        print:
            inform user whether they "missed" or "hit" a ship
    '''
    if secret_board[row][column] == "| s |":
        board[row][column] = "| H |"
    else:
        board[row][column] = "| M |"

#def check_win(board, secret_board):

def main():
    board= [                                                            #build 2-dimensional board
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |']
        ]
    secret_board= [                                                     #build 2-dimensional secret board 
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |']
        ]
    print("Welcome to Battleship!")
    display_board(board)
    secret_board = choose_ships(secret_board)
    display_board(secret_board)#delete this!
    turns = 0
    while turns<10: 
        row,column = get_coordinates(board)
        player_move(board, secret_board, row,column)
        display_board(board)     
        #check_win(board)
        turns-=1

main()

#ask user for coordinates
    #check coordinates are valid
#try to shoot at valid point
    #if taken, ask for coordinates again
    #if empty, check if user has hit a ship (H) or missed (M)
###continue until either:
    #user has hit (H) all 4 ships
    #or user has completed 10 turns (without getting all ships) - and lost
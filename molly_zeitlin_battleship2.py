#Author: Molly Zeitlin
#Description: runs a complete game of battleship (each user has 10 chances to find 4 randomly placed ships)
#Date: 4/15/2026
#Completed Functions: display_board, choose_ships, get_coordinates, player_move, check_win, clear_screen
#Log: 2.0 MZ
#Bonuses: clears the terminal between each player's turn

import random
import time
import os

def display_board(board, player):
    '''
    Description: Print the board in a user-friendly format.
    Args:
        board: 2 dimensional array
    Returns: void
    '''
    print(f"Here is {player}'s board:")
    for row in board:    #create for loop to isolate each row
        for cell in row:   #create another for loop to isolate each cell within each row
            print(cell, end=' ')   #display each cell
        print()

def choose_ships(secret_board):
    '''
    Description: Randomly choose 4 points on the secret board as the ships.
    Args:
        secret_board: 2 dimensional array
    Returns:
        secret_board: 2 dimensional array with ships chosen
    '''
    i = 0
    #a loop to randomly place ships across the hidden board 4 times (4 ships in total on a board)
    while i < 4:
        row = random.randint(0, 4)
        column = random.randint(0, 4)
        if secret_board[row][column] == "| x |":
            secret_board[row][column] = "| s |"
            i+=1
        else:
            i+=1
            continue
    return secret_board

def get_coordinates(board, player):
    '''
    Description: Ask user for coodinate point for their next move.
    Args:
        board: 2 dimensional array
    Returns:
        row: row where user wants to go for next move
        column: column where user wants to go for next mvove
    '''
    #asks the user which row and which column they want to shoot at on their turn, and checks that the specified coordinate point is valid
    while True:
        try:
            row = int(input(f"{player}, what row would you like to shoot at? ")) - 1
        except ValueError:
            print("INVALID RESPONSE\nPlease enter valid numbers")
            continue
        try:
            column = int(input(f"{player}, what column would you like to shoot at? ")) - 1
        except ValueError:
            print(f"INVALID RESPONSE\n{player}, please enter valid numbers")
            continue
        try:
            if board[row][column] == "| x |":
                return row,column
            else:
                print(f"INVALID RESPONSE\n{player}, you already went there...\nPlease try again")
                continue
        except IndexError:
            print(f"INVALID RESPONSE\n{player}, please enter valid numbers within range")
            continue
        
def player_move(board, secret_board, row,column, player):
    '''
    Description: Shoots at user's desired point, and determines whether player "hit" or "missed" a ship.
    Args:
        board: 2 dimensional array
        secret_board: 2 dimensional array with ships chosen
        row: value of the row user wants to shoot at
        column: value of the column user wants to shoot at
    Returns:
        board: 2 dimensional array (altered with "hits" or "misses")
    '''
    #checks whether the user has hit a ship or missed, and changes the point on their board to reflect that result
    if secret_board[row][column] == "| s |":
        board[row][column] = "| H |"
        print(f"{player}, you hit a ship!!")
    else:
        board[row][column] = "| M |"
        print(f"{player}, you missed...")

def check_win(board):
    '''
    Description: Find all "| H |"s in board and determine user has won if 4 "| H |" found
    Args:
        board: 2 dimensional array (has user's "hits" and "misses")
    Returns:
        True: if user has won the game, (found all 4 ships) function returns True
    '''
    ship = 0                                            #counts the number of ships found on the user's board                                             
    for r in range (5):
        for c in range (5):
            if board[r][c] == ("| H |"):
                ship+=1
    if ship == 4:
        return True

def clear_screen(seconds):
    '''
    Description: Clears the terminal to clean up user's area
    Args:
        seconds: the amount of time the computer waits(in seconds) before clearing the screen
    Returns: void
    '''
    time.sleep(seconds)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    #build the boards (2 dimensional arrays)
    
    board1=[                                #this is player 1's shooting board (that they see with their hits and misses)                           
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |']
        ]
    secret_board1=[                         #this is player 1's secret board (hidden but their ships are placed and stored in proper location on this board)                         
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |']
        ]
    board2= [                               #this is player 2's shooting board (that they see with their hits and misses)                              
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |']
        ]
    secret_board2= [                        #this is player 2's secret board (hidden but their ships are placed and stored in proper location on this board)                            
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |'],
        ['| x |', '| x |', '| x |', '| x |', '| x |']
        ]
    print("Welcome to Battleship!\nEach player has 10 turns to find the other player's 4 hidden ships\nGOOD LUCK...")
    secret_board1= choose_ships(secret_board1)                              #places player 1's ships onto their hidden board
    secret_board2 = choose_ships(secret_board2)                             #places player 2' ships onto their hidden board
    player1 = input("Who would like to go first? (Enter name) ")
    player2 = input("Who is going second? (Enter name) ")
    turns = 0                                                               #variable is used to track how many times each player has shot at the board
    #loops of game play (each player goes 10 times unless someone wins)
    while turns<10: 
        display_board(board1,player1)
        row1,column1 = get_coordinates(board1,player1)
        player_move(board1,secret_board1,row1,column1, player1)
        display_board(board1,player1)     
        if check_win(board1):
            print(f"{player1} has WON!!")
            quit()
        clear_screen(3)
        display_board(board2,player2)
        row2,column2 = get_coordinates(board2, player2)
        player_move(board2, secret_board2, row2,column2, player2)
        display_board(board2, player2)
        if check_win(board2):
            print(f"{player2} has WON!!")
            quit()
        turns+=1
        time.sleep(1)
        if turns == 9:
            print(f"You each have 1 turn remaining")
        elif turns == 10:
            print("No turns remaining...\nGAME OVER")
        else:
            print(f"You each have {10-turns} turns remaining")
        clear_screen(2)
    print("YOU BOTH LOST...")

main()
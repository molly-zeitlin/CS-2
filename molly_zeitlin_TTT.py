# Author: Molly Zeitlin
# Date: 2/19/2026
#Description: runs one complete game of Tic Tac Toe
#List of completed functions: display_board, get_move, check_winner, play_game
#Log: 1.0 MZ

import random

def display_board(board):
    '''Print the board in a user-friendly format.
    Args:
        board: 2 dimensional array
    Returns:
        print: the board in a user-friendly format
    '''
    for row in board:                                                                                           #create for loop to isolate each row
        for cell in row:                                                                                        #create another for loop to isolate each cell within each row
            print(cell, end=' ')                                                                                #display cell
        print()

def get_move(board, player, xo):
    '''Get valid row and column for computer or player move.
    Args:
        board: 2 dimensional array
        player(str): either user or comp
        xo: either x or o depending on who's move
    Returns:
        the altered board
        print: message that the user's input was incorrect
    '''
    while True:
        if player == "comp":                                                                                    #if it is computer's turn
            move = random.randint(1, 9)                                                                         #set variable move to random number between 1 and 9 (inclusive)
        else:                                                                                                   #if is NOT computer's turn
            try:                                                                                                #try
                move = int(input(f"Player {xo}, enter number where you would like to go for your next move: ")) #set variable move to user response cornverted to an integer
            except ValueError:                                                                                  #except if error occurs becuase user did not respond with an integer
                print("INVALID RESPONSE\nplease enter valid number")                                            #display message
                continue                                                                                        #restart while loop

        #if variable is set to 1-9, check if that spot is avaible and set that spot to x or o (based on which player's turn it is) and end loop. if spot is unavailable, then check if it is the user's turn and display message
        if move == 1:                                                                                           
            if board[0][0] == "| 1 |":                                                                          
                board[0][0] = (f"| {xo} |")                                                                    
                break                                                                                   
            elif player == "user":                                                                         
                print("That space is already taken: please enter valid space")                       
        elif move == 2:
            if board[0][1] == "| 2 |":
                board[0][1] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        elif move == 3:
            if board[0][2] == "| 3 |":
                board[0][2] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        elif move == 4:
            if board[1][0] == "| 4 |":
                board[1][0] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        elif move == 5:
            if board[1][1] == "| 5 |":
                board[1][1] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        elif move == 6:
            if board[1][2] == "| 6 |":
                board[1][2] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        elif move == 7:
            if board[2][0] == "| 7 |":
                board[2][0] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        elif move == 8:
            if board[2][1] == "| 8 |":
                board[2][1] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        elif move == 9:
            if board[2][2] == "| 9 |":
                board[2][2] = (f"| {xo} |")
                break
            elif player == "user":
                print("That space is already taken: please enter valid space")
        else:
            print("INVALID RESPONSE")
    return board

def check_winner(board):
    '''Determine who winner is (if there is one).
    Args:
        board: 2 dimensional array
    Returns:
        print: if there is a winner, displays who won
    '''
    #if three spots on board in a row are the same (either x or o), then display message saying that player has won and end game
    if "| x |" == board[0][0] == board[0][1] == board[0][2] or "| x |" == board[0][0] == board[1][0] == board[2][0] or "| x |" == board[0][0] == board[1][1] == board[2][2] or "| x |" == board[0][2] == board[1][1] == board[2][0] or "| x |" == board[0][1] == board[1][1] == board[2][1] or "| x |" == board[0][2] == board[1][2] == board[2][2] or "| x |" == board[1][2] == board[1][1] == board[1][0] or "| x |" == board[2][0] == board[2][1] == board[2][2]:
        print("Player x has won the game!\nGAME OVER!")
        quit()
    elif "| o |" == board[0][0] == board[0][1] == board[0][2] or "| o |" == board[0][0] == board[1][0] == board[2][0] or "| o |" == board[0][0] == board[1][1] == board[2][2] or "| o |" == board[0][2] == board[1][1] == board[2][0] or "| o |" == board[0][1] == board[1][1] == board[2][1] or "| o |" == board[0][2] == board[1][2] == board[2][2] or "| o |" == board[1][2] == board[1][1] == board[1][0] or "| o |" == board[2][0] == board[2][1] == board[2][2]:
        print("Player o has won the game!\nGAME OVER!")
        quit()

def play_game():
    '''Run one complete game of Tic-Tac-Toe.'''
    turns = 0
    while True:
        board= [                                                            #build 2-dimensional board
        ['| 1 |', '| 2 |', '| 3 |'],
        ['| 4 |', '| 5 |', '| 6 |'],
        ['| 7 |', '| 8 |', '| 9 |']
        ]
        display_board(board)
        print("Welcome to Tic-Tac-Toe!")
        #ask user questions until game play begins
        uc1 = input("Would you like to play against the computer or in 2 player mode? (Write C or 2): ") #set variable (user choice 1) to user's response 
        if uc1 == "C" or uc1 == "c":
            while True:
                user = input("Who would you like to be? (Enter X or O): ").lower()
                if user == "x":
                    computer = "o"
                    break
                elif user == "o":
                    computer = "x"
                    break
                else:
                    print("INVALID RESPONSE")
            while True:
                uc3 = input("Would you like to go first? (Enter y or n): ").lower()
                if uc3 == "y":
                    #active game until draw or someone wins
                    while turns < 9:
                        board = get_move(board, "user", user)
                        display_board(board)
                        check_winner(board)
                        turns +=1
                        if turns == 9:
                            break
                        print("Computer's turn:")
                        board = get_move(board, "comp", computer)
                        display_board(board)
                        check_winner(board)
                        turns +=1
                    print("GAME OVER!\nNo one wins...\nTIE GAME!")
                    break
                elif uc3 == "n":
                    #active game until draw or someone wins
                    while turns < 9:
                        print("Computer's turn:")
                        board = get_move(board, "comp", computer)    
                        display_board(board)
                        check_winner(board)
                        turns +=1
                        if turns == 9:
                            break
                        board = get_move(board, "user", user)
                        display_board(board)
                        check_winner(board)
                        turns +=1
                    print("GAME OVER!\nNo one wins...\nTIE GAME!")
                    break
                else:
                    print("INVALID RESPONSE")
            break
        elif uc1 == "2":
            while True:
                uc2 = input("Who would like to go first? (Enter X or O): ").lower()
                if uc2 == "x":
                    #active game until draw or someone wins
                    while turns < 9:
                        board = get_move(board, "user", "x")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                        if turns == 9:
                            break
                        board = get_move(board, "user", "o")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                    print("GAME OVER!\nNo one wins...\nTIE GAME!")
                    break
                elif uc2 == "o":
                    #active game until draw or someone wins
                    while turns < 9:
                        board = get_move(board, "user", "o")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                        if turns == 9:
                            break
                        board = get_move(board, "user", "x")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                    print("GAME OVER!\nNo one wins...\nTIE GAME!")
                    break
                else:
                    print("INVALID RESPONSE")
            break
        else:
            print("INVALID REPONSE")

play_game()
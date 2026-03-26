# Tic-Tac-Toe
# Molly Zeitlin | 2/19/2026

import random

def display_board(board):
    """Print the board in a user-friendly format."""
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def get_move(board, player, xo):
    '''Get valid row and column for computer or player move.'''
    while True:
        if player == "comp":                                                                                    #if it is computer's turn
            move = random.randint(1, 9)                                                                         #set variable move to random number between 1 and 9 (inclusive)
        else:                                                                                                   #if is NOT computer's turn
            try:                                                                                                #try
                move = int(input(f"Player {xo}, enter number where you would like to go for your next move: ")) #set variable move to user response cornverted to an integer
            except ValueError:                                                                                  #except if error occurs becuase user did not respond with an integer
                print("INVALID RESPONSE\nplease enter valid number")                                            #display message
                continue                                                                                        #restart while loop

        if move == 1:                                                                                           #if variable move is set to 1
            if board[0][0] == "| 1 |":                                                                          #if 1 spot is available
                board[0][0] = (f"| {xo} |")                                                                     #set 1 spot to x or o (based on which player's turn it is)
                break                                                                                           #end loop
            elif player == "user":                                                                              #if 1 spot is unavaible and it is a user's turn
                print("That space is already taken: please enter valid space")                                  #display message
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
    """Determine who winner is (if there is one)."""
    if "| x |" == board[0][0] == board[0][1] == board[0][2] or "| x |" == board[0][0] == board[1][0] == board[2][0] or "| x |" == board[0][0] == board[1][1] == board[2][2] or "| x |" == board[0][2] == board[1][1] == board[2][0] or "| x |" == board[0][1] == board[1][1] == board[2][1] or "| x |" == board[0][2] == board[1][2] == board[2][2] or "| x |" == board[1][2] == board[1][1] == board[1][0] or "| x |" == board[2][0] == board[2][1] == board[2][2]:
        print("Player x has won the game!\nGAME OVER!")
        quit()
    elif "| o |" == board[0][0] == board[0][1] == board[0][2] or "| o |" == board[0][0] == board[1][0] == board[2][0] or "| o |" == board[0][0] == board[1][1] == board[2][2] or "| o |" == board[0][2] == board[1][1] == board[2][0] or "| o |" == board[0][1] == board[1][1] == board[2][1] or "| o |" == board[0][2] == board[1][2] == board[2][2] or "| o |" == board[1][2] == board[1][1] == board[1][0] or "| o |" == board[2][0] == board[2][1] == board[2][2]:
        print("Player o has won the game!\nGAME OVER!")
        quit()

def play_game():
    """Run one complete game of Tic-Tac-Toe."""
    turns = 0
    while True:
        board= [                                                            #build 2-dimensional board
        ['| 1 |', '| 2 |', '| 3 |'],
        ['| 4 |', '| 5 |', '| 6 |'],
        ['| 7 |', '| 8 |', '| 9 |']
        ]
        display_board(board)
        print("Welcome to Tic-Tac-Toe!")
        uc1 = input("Would you like to play against the computer or in 2 player mode? (Write C or 2): ")
        if uc1 == "C" or uc1 == "c":
            while True:
                uc2 = input("Who would you like to be? (Enter X or O): ")
                if uc2 == "X" or uc2 == "x":
                    user = "x"
                    computer = "o"
                    break
                elif uc2 == "O" or uc2 == "o":
                    user = "o"
                    computer = "x"
                    break
                else:
                    print("INVALID RESPONSE")
            while True:
                uc3 = input("Would you like to go first? (Enter y or n): ")
                if uc3 == "y" or uc3 == "Y":
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
                elif uc3 == "n" or uc3 == "N":
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
                uc2 = input("Who would like to go first? (Enter X or O): ")
                if uc2 == "x" or uc2 == "X":
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
                elif uc2 == "O" or uc2 == "o":
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
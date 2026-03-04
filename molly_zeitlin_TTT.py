# Tic-Tac-Toe
# Molly Zeitlin | 2/19/2026

#import random

def display_board(board):
    """Print the board in a user-friendly format."""
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def get_player_move(board, player):
    """Ask the player for a valid row and column."""
    # TODO: implement this
    while True:
        move = input(f"Player {player}, enter number where you would like to go for your next move: ")
        if move == "1":
            if board[0][0] == "| 1 |":
                board[0][0] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "2":
            if board[0][1] == "| 2 |":
                board[0][1] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "3":
            if board[0][2] == "| 3 |":
                board[0][2] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "4":
            if board[1][0] == "| 4 |":
                board[1][0] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "5":
            if board[1][1] == "| 5 |":
                board[1][1] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "6":
            if board[1][2] == "| 6 |":
                board[1][2] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "7":
            if board[2][0] == "| 7 |":
                board[2][0] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "8":
            if board[2][1] == "| 8 |":
                board[2][1] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        elif move == "9":
            if board[2][2] == "| 9 |":
                board[2][2] = (f"| {player} |")
                break
            else:
                print("That space is already taken: please enter valid space")
        else:
            print("INVALID RESPONSE")
    return board

'''
def get_comp_move(board, ___):
    """Return random computer move."""
    # TODO: implement this
    '''

def check_winner(board):
    """Return 'X', 'O', or None."""
    # TODO: implement this
    if "| X |" == board[0][0] == board[0][1] == board[0][2] or "| X |" == board[0][0] == board[1][0] == board[2][0] or "| X |" == board[0][0] == board[1][1] == board[2][2] or "| X |" == board[0][2] == board[1][1] == board[2][0] or "| X |" == board[0][1] == board[1][1] == board[2][1] or "| X |" == board[0][2] == board[1][2] == board[2][2] or "| X |" == board[1][2] == board[1][1] == board[1][0] or "| X |" == board[2][0] == board[2][1] == board[2][2]:
        print("Player X has won the game!\nGAME OVER!")
        quit()
    elif "| O |" == board[0][0] == board[0][1] == board[0][2] or "| O |" == board[0][0] == board[1][0] == board[2][0] or "| O |" == board[0][0] == board[1][1] == board[2][2] or "| O |" == board[0][2] == board[1][1] == board[2][0] or "| O |" == board[0][1] == board[1][1] == board[2][1] or "| O |" == board[0][2] == board[1][2] == board[2][2] or "| O |" == board[1][2] == board[1][1] == board[1][0] or "| O |" == board[2][0] == board[2][1] == board[2][2]:
        print("Player O has won the game!\nGAME OVER!")
        quit()

def play_game():
    """Run one complete game of Tic-Tac-Toe."""
    turns = 0
    while True:
        board= [
        ['| 1 |', '| 2 |', '| 3 |'],
        ['| 4 |', '| 5 |', '| 6 |'],
        ['| 7 |', '| 8 |', '| 9 |']
        ]
        display_board(board)
        print("Welcome to Tic-Tac-Toe!")
        uc1 = input("Would you like to play against the computer or in 2 player mode? (Write C or 2): ")
        if uc1 == "C" or uc1 == "c":
            print("c!!!")
            '''
            while True:
                uc2 = input("Who would you like to be? (Enter X or O): ")
                if uc2 != "x" or uc2 != "X" or uc2 != "o" or uc2 != "O":
                    print("INVALID RESPONSE")
                elif uc2 == "x":
                    computer = "o"
                    break
                else:
                    computer = "x"
                    break
            while True:
                uc3 = input("Would you like to go first? (Enter y or n: )")
                if uc3 == "y" or uc3 == "Y":
                    get_player_move(board, uc2)
                    break
                elif uc3 == "n" or uc3 == "N":
                    get_comp_move(board, computer)    
                    break
                else:
                    print("INVALID RESPONSE")
            '''
            break
        elif uc1 == "2":
            print("2!!")
            while True:
                uc2 = input("Who would like to go first? (Enter X or O): ")
                if uc2 == "x" or uc2 == "X":
                    while turns < 9:
                        board = get_player_move(board, "X")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                        board = get_player_move(board, "O")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                    break
                elif uc2 == "O" or uc2 == "o":
                    while turns < 9:
                        board = get_player_move(board, "O")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                        board = get_player_move(board, "X")
                        display_board(board)
                        check_winner(board)
                        turns +=1
                    break
                else:
                    print("INVALID RESPONSE")
                break
        else:
            print("INVALID REPONSE")
    print("GAME OVER!\nNo one wins...\nTIE GAME!")

play_game()


'''
TTT Algo:
1. Create board "E" of borders!
2. Players? or robot?!
3. Random choice of going first!
4. Random choice who is 'x'!
5. Infinite loop!
6. Print board!
7. Ask user(?) location on board!
8. Choose indicies, check if valid location, check if free, check if draw; check win;!
9. If win or draw; break loop!
10. Set next player to go!
'''
#NEXT STEP: WORK ON PLAYER VS. COMPUTER!
"""Battleship!
   Basic version
   Python 3
"""
#Vanity Title
print("""           .
            _\____
           |_===__`.        ==/
           \/  '---"\ _ _ _ _/
     ______/_______/_|_|_|_|_|
   _|---------------------==.`
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          BATTLESHIP 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
 Guess where my ship is!
 You have 4 tries.
""")
#Make a 5x5 board
board = []

for i in range(0, 5):
    board.append(['O'] * 5)

def print_board(board_in):
    for row in board_in:
        print(" ".join(row))

#Generate random indices
from random import randint

def random_row(board_in):
    return randint(0, len(board_in) -1)

def random_col(board_in):
    return randint(0, len(board_in) -1)

#Store random ship location
ship_row = random_row(board)
ship_col = random_col(board)

#Repeat 4 times
for turn in range(4):
    print("Turn", turn + 1)
    
#Prompt player to guess
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

#Test the hidden random location
#print("%s, %s" % (ship_row, ship_col))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        board[ship_row][ship_col] = "∎"
        break
    else:
        if guess_row not in range(5) or \
        guess_col not in range (5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print("Game over.")
            board[ship_row][ship_col] = "∎"
        print_board(board)


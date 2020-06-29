"""Rock-Paper-Scissors!
   Coding Excercise (Python 3 debugged using Thonny)
   https://www.codecademy.com/courses/learn-python/projects/rock-paper-scissors-pytho
   Python 2
   https://gist.github.com/bec8d0bfd603790be40ea6e472bc9400
"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message = {
    "tie": "Yawn it\'s a tie!",
    "won": "Yay you won!",
    "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
    print("User\'s choice is %s" % user_choice)
    print("Computer\'s choice is %s" % computer_choice)
    if user_choice == computer_choice:
        print(message["tie"])
    elif user_choice == options[0] and computer_choice == options[2] \
        or user_choice == options[1] and computer_choice == options[0] \
        or user_choice == options[2] and computer_choice == options[1]:
        print(message['won'])
    else:
        print(message["lost"])
        
def play_RPS():
    user_choice = input("Enter Rock, Paper, or Scissors: ").upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)
    return print("End of the session.")

play_RPS()

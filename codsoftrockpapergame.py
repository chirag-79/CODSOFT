# @codsoft #codsoft intrneship 
"""ROCK PAPER AND SCISSOR GAME"""
print("Welcome to the Rock paper and scissors game made by Chirag miglani")
import random

while True:
    user_choice = int(input("Enter your choice for playing:Type 0 for rock, Type 1 for paper, Type 2 for scissors: "))
    if user_choice not in [0, 1, 2]:
        print("The number you have entered is not appropriate! Please enter 0, 1, or 2.")
        continue
    # now its computer turn to play and choose among rock paper and scissor
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose: Rock")
    elif computer_choice == 1:
        print("Computer chose: Paper")
    elif computer_choice == 2:
        print("Computer chose: Scissors")
    if computer_choice == user_choice:
        print("the match you have played is a draw match")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("Congrats brother !! You have  won the game!")
    else:
        print("Oops! Computer wins this round,so sorry ")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")

#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md


#Requirements 
#1) Processing User inputs 

user_choice = input("Please choose one of: 'rock', 'paper', 'scissors': ")

print("User Chose:", user_choice)

#2) Validating user inputs

#3) Simulating computer selection 

import random

options = ("rock", "paper", "scissors")
computer_choice = random.choice(options)

print("Computer Chose:", computer_choice)

#4) determining the winner 
# using an if statement to choose the winner
# got some help with this during class time

if user_choice == computer_choice:
    print("Both players played", user_choice, "It is a tie :/")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You won :) ")
    else:
        print("Scissors cuts paper. You lost :(")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You won :)")
    else:
        print("Rock crushes scissors. You lost :(")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You won :)")
    else:
        print("Paper covers rock. You lost :(")

#5) displaying results 

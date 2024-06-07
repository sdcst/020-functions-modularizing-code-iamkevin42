"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random

def title():
    print("Welcome to my number guessing game, I'm thinking of a number from 1 to 1000 can you guess it?")
title()




def game():
    secretnumber=random.randint(1,1000)
    while True:
        guess= int(input('Enter your guess\n'))
        if guess == secretnumber:
            print(f"{secretnumber} was the right number!")
            exit()
        elif guess < secretnumber:
            print("Too low! Try guessing a higher number.")
        elif guess > secretnumber:
            print("Too high! Try guessing a lower number.")
game()









# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:15:29 2020

@author: Anna
"""

# Write a programme which:
    # a) Stores a random number (1-10) in a variable
    # b) Asks a user for their name and stores this in a variable
    # c) Ask the user to guess the number between 1-10
    # d) Tells the user whether they have guessed correctly
  
   
import random

# a) Store a random number (1-10) in variable named random_number.
random_number = random.randint(1, 10) 
# b) Ask user for name and store in variable named user_name. User types in name in shell and presses enter to continue the run of the code
user_name = input("What is your name?\n") 
# c) Ask for a number and will be put in variable called user_guess. Use casting to integer so computer knows response is integer, not a string.
user_guess = int(input("What number am I thinking of? Enter your guess between 1 and 10.\n"))
if user_guess == random_number:
    print("Congratulations", user_name, "you have guessed correctly!")
else:
    print("Incorrect", user_name + "! The number I was thinking of was", str(random_number) + ".")
        

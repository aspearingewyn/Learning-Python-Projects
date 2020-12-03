# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:31:11 2020

@author: Anna
"""

import random

if __name__ == "__main__":

    random_number = random.randint(1, 10)
    user_name = input("What is your name?\n")
    user_guess = (input("What number am I thinking of? Enter your guess between 1 and 10.\n"))

    if user_guess == "one":
        user_guess = 1
    elif user_guess == "two":
        user_guess = 2
    elif user_guess == "three":
        user_guess = 3
    elif user_guess == "four":
        user_guess = 4
    elif user_guess == "five":
        user_guess = 5
    elif user_guess == "six":
        user_guess = 6
    elif user_guess == "seven":
        user_guess = 7
    elif user_guess == "eight":
        user_guess = 8
    elif user_guess == "nine":
        user_guess = 9
    elif user_guess == "ten":
        user_guess = 10

    if user_guess == random_number:
        print("Congratulations", user_name, "you have guessed correctly!")
    else:
        print("Incorrect", user_name + "! The number I was thinking of was", str(random_number) + ".")

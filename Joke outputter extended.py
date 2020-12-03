# Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number.
# You should use a minimum of 3 jokes.

# Ask user for favourite number between 1 and 100.
User_Number = int(input("What is your favourite number between 1 and 100?\n"))

# If number is <25, print joke 1. Pycharm showed this simplified way of writing the same expression.


if 1 <= User_Number <= 25:
    print("What do you call a dinosaur with no eyes?")
    giveup = input("Type 'Tell me' for answer:\n")
    if giveup == "Tell me" or "tell me":
        print("Doyouthinkysaurus")
elif 25 < User_Number <= 50:
    print("What do you call a sleeping dinosaur?")
    giveup = input("Type 'Tell me' for answer:\n")
    if giveup == "Tell me" or "tell me":
        print("A dino-snore")
elif 50 < User_Number <= 75:
    print("What do you get when dinosaurs crash their cars?")
    giveup = input("Type 'Tell me' for answer:\n")
    if giveup == "Tell me" or "tell me":
        print("Tyrannosaurus wrecks")
else:
    print("What's the most polite dinosaur?")
    giveup = input("Type 'Tell me' for answer:\n")
    if giveup == "Tell me" or "tell me":
        print("A please-iosaur")

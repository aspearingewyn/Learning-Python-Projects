# Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number.
# You should use a minimum of 3 jokes.
# Use if, elif and else

# Ask user for favourite number between 1 and 100.
User_Number = int(input("What is your favourite number between 1 and 100?\n"))

# If number is <25, print joke 1. Remember to name the variable both times.
if User_Number >= 1 and User_Number <= 25:
    print("What do you call a dinosaur with no eyes?\n"
          "Doyouthinkysaurus")

# If number is between 25 and 50, print joke 2
elif User_Number > 25 and User_Number <= 50:
    print("What do you call a sleeping dinosaur?\n"
          "A dino-snore")

# If number is between 50 and 75, print joke 3
elif User_Number > 50 and User_Number <= 75:
    print("What do you get when dinosaurs crash their cars?\n"
          "Tyrannosaurus wrecks")

# If number is between 75 and 100, print joke 4
else:
    print("What's the most polite dinosaur?\n"
          "A please-iosaur")

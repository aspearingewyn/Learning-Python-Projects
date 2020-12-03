# Write a program that allows user to enter their favourite starter, main course, dessert and drink.
# Concatenate these and output a message which says “Your favourite meal is ………with a glass of….”

print("Hello! Let's find out your dream menu!")

# Ask for favourite starter
starter = input("What is your favourite starter?\n")

# Ask for favourite main
main = input("What is your favourite main course?\n")

# Ask for favourite dessert
dessert = input("What is your favourite dessert?\n")

# Ask for favourite drink
drink = input("What is your desired drink to accompany this meal?\n")

# Cocatenate and print outcome
print("Your dream menu is: a starter of", starter, "\n"
        "followed by a main course of", main, "\n"
        "with", dessert, "to finish\n"
        "accompanied by a nice glass of", drink)


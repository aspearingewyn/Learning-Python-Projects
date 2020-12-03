# Write a program which will ask for two numbers from a user.
# Then offer a menu to the user giving them a choice of operator:
# e.g. Enter “a” if you want to add
# “b” if you want to subtract
# Include +,-, /, *, **(to the power of) and square.
# Once the user has selected which operator they wish to use, perform the calculation.

print("Hello! I am here to help you perform a calculation with two numbers of your choice.")
# Ask for number 1
number1 = int(input("What is the first number in your calculation?\n"))

# Ask what operator they want to use.
print("What mathematical operator would you like to use?\n"
      "Type 'a' for addition, +\n"
      "Type 'b' for subtraction, -\n"
      "Type 'c' for multiplication, x\n"
      "Type 'd' for division, /\n"
      "Type 'e' for the power of, ^")
operator = input("Type one of the letters 'a' through to 'e' below:\n")

# Ask for number 2
number2 = int(input("What is the second number in your calculation?\n"))

# Print calculation
if operator == "a":
    print("The answer to", number1, "+", number2, "is", number1 + number2)

elif operator == "b":
    print("The answer to", number1, "-", number2, "is", number1 - number2)

elif operator == "c":
    print("The answer to", number1, "x", number2, "is", number1 * number2)

elif operator == "d":
    print("The answer to", number1, "/", number2, "is", number1 / number2)

else:
    print("The answer to", number1, "to the power of", number2, "is", number1 ** number2)



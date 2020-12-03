# A motorbike costs £2000 and loses 10% of its value every year.
# Using a loop, print the value of the bike every following year until it falls below £1000

value = 2000
year = 1
# Use a while loop which is conditional on the value being greater than £1000
while value >= 1000:
    value = value * 0.9
    print("The value of the motorbike after year", year, "is = £" + str(value))
    year = year + 1

"""
Multiplication table by for loop
"""
print(__doc__)
UserInput = int(input("Enter a int num = "))
for Multiplier in range(1, 11):
    print(UserInput, "x", Multiplier, " = ", Multiplier*UserInput)
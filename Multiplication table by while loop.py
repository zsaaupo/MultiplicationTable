"""
Multiplication table by while loop
"""
print(__doc__)

UserInput = int(input("Enter a int num = "))
Multiplier = 1
while Multiplier <= 10:
    print(UserInput, " x ", Multiplier, " = ",Multiplier*UserInput)
    Multiplier = Multiplier + 1
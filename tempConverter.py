import re

print("Option 1 -> Convert Celsius to Fahrenheit")
print("Option 2 -> Convert Fahrenheit to Celsius")
print("Type your option below(1/2)")
option = int(input("Option No: "))

if option == 1 :
    cValue = float(input("Value in Celsius: "))
    fValue = (cValue * 9 / 5) + 32
    print("Value in Fahrenheit: " + str(fValue))
elif option == 2 :
    fValue = float(input("Value in Fahrenheit: "))
    cValue = (fValue - 32) * 5 / 9
    print("Value in Celsius: " + str(cValue))
else :
    print("*Invalid Option*")
    print("Try 1 or 2")
    
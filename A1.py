def checkIfSame(number1, number2):
    if ((number1^number2) !=0):
        print("Numbers are not equal")
    else:
        print("Both the numbers are equal")

number1=int(input("Enter First number to compare : "))
number2=int(input("Enter Second number to compare : "))

checkIfSame(number1, number2)
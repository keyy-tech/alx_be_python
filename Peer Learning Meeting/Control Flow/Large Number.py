# Ask the user to enter 3 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("The largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is " + str(num2))
else:
    print(f"The largest number is {num3}")
# Taking two numbers and an operator as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Prompt the user for the operator
operator = input("Choose the operator (+,-,*./): ")

if num1 == 0 or num2 == 0:
    print("Cannot divide by zero.")
    exit()

# Using a match-case to perform the operation based on the operator
match operator:
    case "+":
        result = num1 + num2
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result is: {result}")
    case "/":
        # Using if-else to handle the division by zero
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    case _:
        print("Invalid operator. Please try again.")

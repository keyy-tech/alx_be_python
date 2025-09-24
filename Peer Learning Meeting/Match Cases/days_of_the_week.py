# Ask the user to entera number between 1 and 7
day_of_the_week = int(input("Enter a number between 1 and 7: "))

# Use match cases to print the day
match day_of_the_week:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day of the week. Please try again.")
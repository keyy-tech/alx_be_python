grade = int(input("Enter your exam score (0-100): "))


if grade >100 or grade < 0:
    print("Invalid score. Please try again.")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
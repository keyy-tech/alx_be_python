# Ask the user for a task description
task = input("Enter your task: ")

# Ask for the task's priority
priority = input("Priority (high/medium/low): ")

# Ask if is time bound
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        reminder = f"Reminder: '{task}' - This is a high priority task,"
    case "medium":
        reminder = f"Reminder: '{task}' - This is a medium priority task,"
    case "low":
        reminder = f"Reminder: '{task}' - This is a low priority task,"
    case _:
        reminder = f"Reminder: '{task}' - Priority not set."

if time_bound == "yes":
    reminder += " It requires immediate attention."
else:
    reminder += " It can be addressed later."


print(reminder)


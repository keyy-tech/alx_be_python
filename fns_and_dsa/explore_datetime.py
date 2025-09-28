from datetime import datetime,timedelta


def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current date and time:", display_current_datetime())

future_date = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date(future_date):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=future_date)
    return future_date.strftime("%Y-%m-%d")

print("Future date:", calculate_future_date(future_date))
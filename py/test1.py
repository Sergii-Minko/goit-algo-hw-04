from datetime import datetime  # Importing the datetime module

# Define an empty string variable for user input
string = ""

# Function to calculate the number of days from a given date to today


def get_days_from_today(date):
    try:
        # Convert the input date string to a datetime object
        date_object = datetime.strptime(date, "%Y-%m-%d")
    except:
        # If conversion fails (due to invalid format), return False
        return False

    # Get today's date
    today = datetime.today()

    # Calculate the difference in days between the input date and today
    return (today - date_object).days


# Prompt the user to input a date in YYYY-MM-DD format
string = input("Enter Date in YYYY-MM-DD format: ")

if string:
    # If the user provides input
    who_many_days = get_days_from_today(string)
    if not who_many_days:
        # If the input date is invalid, print an error message
        print("Invalid Date")
    else:
        # If the input date is valid, print the number of days from today
        print("Days from today: ", who_many_days)
else:
    # If the user doesn't provide any input, print a message
    print("Empty Input")

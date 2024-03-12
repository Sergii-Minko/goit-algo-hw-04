from datetime import datetime  # Importing datetime module to work with dates
from datetime import (
    timedelta,
)  # Importing timedelta module to work with time differences

users = [
    {"name": "John Doe", "birthday": "1985.03.15"},
    {"name": "Jane Smith", "birthday": "1990.03.10"},
    {"name": "Alice Johnson", "birthday": "1988.09.22"},
    {"name": "Bob Brown", "birthday": "1995.07.05"},
    {"name": "Boby Brown", "birthday": "1995.01.05"},
    {"name": "Anna Green", "birthday": "1994.03.09"},
    {"name": "Kate Black", "birthday": "1994.03.12"},
]


# Function to calculate the number of days until the upcoming birthday
def find_amount_of_days_before_birthday(birthday_date, today):
    # Replace the year of the birthday with the current year
    birthday_date = birthday_date.replace(year=today.year).date()

    if birthday_date >= today:
        # If the birthday is later or equal to today, calculate the difference in days
        amount_of_days = (birthday_date - today).days
        return amount_of_days
    elif birthday_date < today:
        # If the birthday has passed this year, calculate the difference until next year's birthday
        birthday_date = birthday_date.replace(year=(today.year + 1))
        amount_of_days = (birthday_date - today).days
        return amount_of_days


# Function to get upcoming birthdays within a week
def get_upcoming_birthdays(users):
    # Create an empty list to store upcoming birthdays
    upcoming_birthdays = []
    today = datetime.today().date()  # Get the current date

    for user in users:
        # Convert the birthday string to a date object
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d")
        # Calculate the number of days until the upcoming birthday
        days_until_birthday = find_amount_of_days_before_birthday(birthday_date, today)
        # Check if the birthday falls within the upcoming week
        if (days_until_birthday >= 0) and (days_until_birthday < 7):
            # Calculate the date to send congratulations
            congratulation_date = today + timedelta(days=days_until_birthday)
            # Adjust the date if it falls on a weekend
            if congratulation_date.isoweekday() == 6:  # If Saturday
                congratulation_date = congratulation_date + timedelta(days=2)
            elif congratulation_date.isoweekday() == 7:  # If Sunday
                congratulation_date = congratulation_date + timedelta(days=1)
            # Create a new user dictionary with name and congratulation date
            new_user = {}
            new_user["name"] = user["name"]
            new_user["congratulation_date"] = congratulation_date.strftime("%Y.%m.%d")
            # Add the user to the list of upcoming birthdays
            upcoming_birthdays.append(new_user)
    return upcoming_birthdays


# Call the function to get upcoming birthdays
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

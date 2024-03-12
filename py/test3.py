import re  # Import the regular expression module

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "501112211",
]
sanitized_numbers = []


# Function to normalize phone numbers to a standardized UA phone format
def normalize_phone(phone_number):
    phone_number = re.sub(r"\D+", "", phone_number)  # Remove all non-digit characters
    if len(phone_number) == 9:
        phone_number = "+380" + phone_number  # Add country code if it's missing
    elif len(phone_number) == 10:
        if phone_number[0] == "0":
            phone_number = "+38" + phone_number  # Add country code if it's missing
        else:
            phone_number = "+380" + phone_number[1:]  # Adjust the format
    elif len(phone_number) == 11:
        if phone_number[0] == "8":
            phone_number = "+3" + phone_number  # Add country code if it's missing
        else:
            phone_number = "+38" + phone_number[1:]  # Adjust the format
    elif len(phone_number) == 12:
        if phone_number[0] == "3":
            phone_number = "+" + phone_number  # Add '+' if missing
        else:
            phone_number = "+3" + phone_number[1:]  # Adjust the format
    return phone_number


# Iterate over the raw numbers and normalize them

for number in raw_numbers:
    if len(number) >= 9:  # Check if the string is long enough to be a phone number
        sanitized_numbers.append(normalize_phone(number))

        print(normalize_phone(number))  # Print the normalized phone number
    else:
        print(
            f"Неправильний формат номер телефона {number}"
        )  # If not long enough, print an error message


print("Нормалізовані номери телефонів для SMS-розсилки: ", sanitized_numbers)

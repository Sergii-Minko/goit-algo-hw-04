import random  # Import the random module to generate random numbers

min_value = 0
max_value = 0
quantity = 0


# Function to generate a list of unique random numbers within a given range
def numbers_ticket(min, max, quantity):
    numbers = []
    for i in range(quantity):
        number = random.randint(
            min, max
        )  # Generate a random number within the specified range
        while number in numbers:  # Check if the number is already in the list
            number = random.randint(min, max)  # If yes, generate a new random number
        numbers.append(number)  # Add the unique number to the list
    return sorted(numbers)  # Sort the list and return it


# Function to check and adjust the format of the input string
def check_format(string):
    global min_value, max_value, quantity
    # Check if the input is not empty and contains two commas (indicating three values)
    if (string != "") & (string.count(",") == 2):
        try:
            # Convert the input string into a list of integers
            numbers = [int(x) for x in string.split(",")]
            min_value = numbers[0]  # Extract the minimum value from the list
            max_value = numbers[1]  # Extract the maximum value from the list
            quantity = numbers[2]  # Extract the quantity from the list
        except:
            print(
                "Неправильний формат даних"
            )  # Print an error message if conversion fails
            return False

    else:
        print(
            "Неправильний формат даних"
        )  # Print an error message if input format is incorrect
        return False
    if (min_value < 1) or max_value > 1000:
        print(
            "Неправильний формат даних min має бути більшим за 0, max має бути меншим за 1000"
        )
        return False

    # Ensure the minimum value is less than or equal to the maximum value
    if min_value > max_value:
        # min_value, max_value = max_value, min_value
        print("Неправильний формат даних min має бути меншим за max")
        return False

    # If the range is smaller than the requested quantity of numbers, adjust the quantity
    if max_value - min_value + 1 < quantity:
        print("Неправильний формат даних quantity має бути меншим за (max - min) + 1")
        # quantity = (max_value - min_value) // 2
        # print("Нова кількість чисел: ", quantity)
        return False

    # Print the obtained data for the lottery ticket
    print("Отримані данні для лотерейного білету:")
    print(f"Мінімальне число: {min_value}")
    print(f"Максимальне число: {max_value}")
    print(f"Кількість чисел: {quantity}")

    return True


def get_numbers_ticket(min=0, max=0, quantity_value=0):
    global min_value, max_value, quantity
    # Set default values for the range and quantity if not provided
    if min == 0 and max == 0 and quantity_value == 0:
        # Prompt the user to input the range and quantity of numbers for the lottery ticket
        string = input("Введіть Ваш діапазон чисел min, max, quantity: ")
    else:
        string = str(min) + "," + str(max) + "," + str(quantity_value)

    # Loop until the input format is correct
    if not check_format(string):
        lottery_numbers = []
        return lottery_numbers
    else:
        # Generate lottery numbers based on the provided range and quantity
        lottery_numbers = numbers_ticket(min_value, max_value, quantity)
        # Print the generated lottery numbers
        return lottery_numbers


win_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", win_numbers)

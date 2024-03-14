from pathlib import Path

"""
    Функція для обчислення загальної суми та середньої заробітної плати з даних у файлі.

    Args:
        path (str): Шлях до файлу з даними про заробітну плату.

    Returns:
        tuple: Кортеж, що містить загальну суму та середню заробітну плату.
               Якщо файл не знайдено або відбулася помилка, повертається (0, 0).
"""


def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            array = file.readlines()
            if len(array) == 0:
                return 0, 0
            total = sum([float(i.split(",")[1].strip()) for i in array])
            return total, total / len(array)
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0


def main():
    path = input("Enter file path: ")
    if not path:
        path = "./py/name.txt"

    total, average = total_salary(path)

    print(
        f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}"
    )


if __name__ == "__main__":
    main()

from joke import get_random_joke
from colorama import Fore, Back, Style
import math
from log import log_info, log_warning, log_error


def main():
    name = input("Будь ласка, введіть ваше ім'я: ")
    print(f"Привіт, {name}!")

    while True:
        user_response = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()
        if user_response == "так":
            print(get_random_joke())
        elif user_response == "ні":
            print(f"До побачення, {name}!")
            break


if __name__ == "__main__":
    # main()

    print(Fore.RED + "Це червоний текст")
    print(Back.GREEN + "Це текст на зеленому фоні")
    print(Style.RESET_ALL)
    print("Це звичайний текст після скидання стилю")


def calculate_square_root(numbers: list) -> None:
    for number in numbers:
        try:
            if number < 0:
                # Логування попередження для від'ємних чисел
                log_warning(f"Знайдено від'ємне число: {number}. Пропускаємо.")
                continue

            root = math.sqrt(number)
            log_info(f"Квадратний корінь з {number} - {root:.2f}")

        except Exception as e:
            # Логування помилки у випадку інших винятків
            log_error(f"Помилка при обчисленні кореня для {number}: {e}")


if __name__ == "__main__":
    # Припустимо, у нас є список чисел
    numbers = [16, -4, 9, 25, 0, 4, "16"]
    calculate_square_root(numbers)

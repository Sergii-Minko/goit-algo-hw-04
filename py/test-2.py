from pathlib import Path

"""
    Функція для зчитування інформації про котів з файлу та повернення списку словників.

    Args:
        path (str): Шлях до файлу з даними про котів.

    Returns:
        list: Список словників з інформацією про котів. Кожен словник містить поля 'id', 'name' та 'age'.
              Якщо файл не знайдено або відбулася помилка, повертається порожній список.
    """


def get_cats_info(path):
    cat_list = []
    cat_dict = {}
    try:
        with open(path, "r", encoding="utf-8") as file:
            cat_data = file.readlines()
            if len(cat_data) == 0:
                return cat_list
            for i in range(len(cat_data)):
                cat_id, cat_name, cat_age = cat_data[i].split(",")
                cat_dict = {"id": cat_id, "name": cat_name, "age": int(cat_age)}
                cat_list.append(cat_dict)
            return cat_list

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return cat_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return cat_list


def main():
    path = input("Enter file path: ")
    if not path:
        path = "./py/cats.txt"

    print(get_cats_info(path))


if __name__ == "__main__":
    main()

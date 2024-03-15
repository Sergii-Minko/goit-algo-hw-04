# Розбиває введене користувачем рядок на команду та аргументи.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Додає новий контакт до словника контактів.
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    if args[0] in contacts:
        return "Contact already exists. Use 'change' command instead."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Змінює номер телефону існуючого контакту.
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    if args[0] not in contacts:
        return "Contact not found. Use 'add' command instead."
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


# Виводить телефонний номер для вказаного імені контакту.
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


# Виводить усі контакти.
def show_all(contacts):
    if len(contacts) == 0:
        return "No contacts."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(
                "Available commands:\nadd <name> <phone>\nchange <name> <phone>\nshow <name>\nall\nexit\n"
            )
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

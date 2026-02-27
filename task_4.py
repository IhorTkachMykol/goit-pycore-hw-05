def input_error(func):
    """
    Декоратор для обробки помилок користувача.
    Обробляє KeyError, ValueError, IndexError.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Give me name and phone please."

        except IndexError:
            return "Enter the argument for the command."

        except KeyError:
            return "Contact not found."

    return inner


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args   # може кинути ValueError або IndexError
    contacts[name] = phone
    return f"Contact added for {name}."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone
    return f"Contact updated for {name}."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "Contacts list:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
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

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

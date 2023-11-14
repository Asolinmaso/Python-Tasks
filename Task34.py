import json

def load_birthdays(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_birthdays(filename, birthdays):
    with open(filename, "w") as file:
        json.dump(birthdays, file, indent=4)

def add_birthday(birthdays):
    name = input("Enter the name of the scientist: ")
    birthday = input("Enter their birthday (MM/DD/YYYY): ")
    birthdays[name] = birthday

def main():
    filename = 'birthdays.json'
    birthdays = load_birthdays(filename)

    add_birthday(birthdays)
    save_birthdays(filename, birthdays)

    for name, birthday in birthdays.items():
        print(f"{name}: {birthday}")

if __name__ == "__main__":
    main()

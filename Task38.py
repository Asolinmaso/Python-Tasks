from datetime import datetime

def calculate_year_of_100th_birthday(current_year, age):
    return current_year + (100 - age)

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    current_year = datetime.now().year

    year_of_100th_birthday = calculate_year_of_100th_birthday(current_year, age)

    message = f"Hello {name}, you will turn 100 years old in the year {year_of_100th_birthday}."
    print(message)

if __name__ == "__main__":
    main()

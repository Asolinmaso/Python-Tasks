import random

def generate_number():
    return random.randint(1000, 9999)

def cows_and_bulls(number, guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == number[i]:
            cows += 1
        elif guess[i] in number:
            bulls += 1
    return cows, bulls

def main():
    number = str(generate_number())
    print("Random Generated Number",number)
    guesses = 0

    while True:
        user_guess = input("Enter a 4-digit number: ")
        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        guesses += 1
        cows, bulls = cows_and_bulls(number, user_guess)
        print(f"{cows} cows, {bulls} bulls")

        if cows == 4:
            print(f"Congratulations! You guessed the number {number} in {guesses} guesses.")
            break

if __name__ == "__main__":
    main()



import random

def modified_guessing_game():
    number = random.randint(1, 9)
    number_of_guesses = 0

    while True:
        try:
            guess = input("Guess a number between 1 and 9: ")
            if guess.lower() == 'exit':
                break

            guess = int(guess)
            if guess < 1 or guess > 9:
                print("Please enter a number within the range 1 to 9.")
                continue

            number_of_guesses += 1
            if guess == number:
                break
        except ValueError:
            print("That's not a valid number. Please try again.")

    print(f"You needed {number_of_guesses} guesses to guess the number {number}")

modified_guessing_game()

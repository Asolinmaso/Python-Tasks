import random

def guess_the_number():
    random_number = random.randint(1, 9)
    guesses = 0

    while True:
        user_guess = input("Guess a number between 1 and 9 or type 'exit' to stop playing): ")
        if user_guess.lower() == 'exit':
            break

        user_guess = int(user_guess)
        guesses += 1

        if user_guess < random_number:
            print("Too low!")
        elif user_guess > random_number:
            print("Too high!")
        else:
            print("Exactly right!")
            break

    print(f"Total guesses: {guesses}")

guess_the_number()

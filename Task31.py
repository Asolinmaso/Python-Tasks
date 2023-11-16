import random

def display_word(word, guesses):

    return " ".join([letter if letter in guesses else '_' for letter in word])

def hangman(words):
    word = random.choice(words).upper()
    guessed_letters = set()
    correct_guesses = set()

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while set(word) != correct_guesses:
        guess = input("Guess your letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            correct_guesses.add(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            print("Incorrect!")

        print(display_word(word, guessed_letters))

    print("Congratulations, you guessed the word!")

words_to_guess = ["EVAPORATE", "CLARITY", "SYNCHRONIZE", "MYSTICAL", "JUBILANT"]

hangman(words_to_guess)

import random

def load_random_word():
    words = ['python', 'hangman', 'programming', 'code', 'algorithm']
    return random.choice(words)

def display_hangman(tries):
    stages = ["""
                   --------
                   |      |
                   |      
                   |    
                   |      
                   -""",
              """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   -""",
              """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   -""",
              """
                   --------
                   |      |
                   |      O
                   |     /|
                   |      
                   -""",
              """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      
                   -""",
              """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |     / 
                   -""",
              """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |     / \\
                   -"""
              ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word) 
    guessed = False
    guessed_letters = set()
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(6-tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.add(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.add(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")

        print(display_hangman(6-tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def main():
    word = load_random_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = load_random_word()
        play(word)

if __name__ == "__main__":
    main()

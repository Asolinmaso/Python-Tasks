import random

def pick_random_word(filename):
   
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]

    return random.choice(words)

# Path to the SOWPODS file
sowpods_file = 'sowpods.txt'

# Get a random word from the file
random_word = pick_random_word(sowpods_file)
print(f"Random word: {random_word}")

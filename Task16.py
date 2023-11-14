import random
import string

def generate_password(length, strength='strong'):
    if strength == 'weak':
        words = ["apple", "orange", "banana", "grape", "cherry"]
        password = random.choice(words)
        if length > len(password):
            password += ''.join(random.choice(string.ascii_lowercase) for _ in range(length - len(password)))
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    password_strength = input("Enter password strength (weak/strong): ").lower()
    password_length = int(input("Enter password length: "))
    
    password = generate_password(password_length, password_strength)
    print("Generated password:", password)

# Running the main method
if __name__ == "__main__":
    main()

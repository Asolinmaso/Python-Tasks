def get_integer(help_text="Enter a number: "):
    return int(input(help_text))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

user_input = get_integer("Please enter a number to check if it's prime: ")
print("The number is prime." if is_prime(user_input) else "The number is not prime.")
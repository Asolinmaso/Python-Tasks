def is_palindrome(string):
    return string == string[::-1]

user_string = input("Enter a string to check if it's a palindrome: ")
print(f"{user_string} is a palindrome" if is_palindrome(user_string) else f"{user_string} is not palindrome")

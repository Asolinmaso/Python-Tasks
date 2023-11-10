def even_or_odd(num):
    if num % 4 == 0:
        return f"{num} is a multiple of 4."
    elif num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

def check_divisibility(num, check):
    if num % check == 0:
        return f"{num} divides evenly by {check}."
    else:
        return f"{num} does not divide evenly by {check}."

num = int(input("Enter a number: "))
print(even_or_odd(num))

num = int(input("Enter another number to check: "))
check = int(input("Enter a number to divide by: "))
print(check_divisibility(num, check))
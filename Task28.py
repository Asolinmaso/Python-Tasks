def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("The largest number among 3, 7, and 5 is:", find_max_of_three(3, 7, 5))
print("The largest number among 15, 10, and 12 is:", find_max_of_three(15, 10, 12))
print("The largest number among 8, 8, and 8 is:", find_max_of_three(8, 8, 8))

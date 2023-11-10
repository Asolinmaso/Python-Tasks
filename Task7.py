a = [1, 2, 3, 4, 9, 16, 36, 28, 14, 11, 80]
b = [x for x in a if x % 2 == 0]
b.sort()
print(b)
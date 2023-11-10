num = int(input("Enter a number: "))
print([i for i in range(1, num + 1) if num % i == 0])
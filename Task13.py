def generate_fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    sequence = [1, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

number_of_terms = int(input("How many Fibonacci numbers would you like to generate? "))
print("Fibonacci sequence:", generate_fibonacci(number_of_terms))

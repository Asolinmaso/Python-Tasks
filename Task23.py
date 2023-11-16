def read_numbers_from_file(filename):

    with open(filename, 'r') as file:
        return {int(line.strip()) for line in file}

def find_overlapping_numbers(file1, file2):

    numbers1 = read_numbers_from_file(file1)
    numbers2 = read_numbers_from_file(file2)

    return numbers1.intersection(numbers2)

primes_file = 'primes.txt'
happy_numbers_file = 'happy_numbers.txt'

overlapping_numbers = find_overlapping_numbers(primes_file, happy_numbers_file)

print("Overlapping numbers:", overlapping_numbers)

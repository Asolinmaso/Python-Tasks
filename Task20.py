def binary_search(ordered_list, number):
    low = 0
    high = len(ordered_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = ordered_list[mid]

        if guess == number:
            return True
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1

    return False

ordered_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

number_to_find = 9
print("Binary Search:", binary_search(ordered_list, number_to_find)) 

number_to_find = 8
print("Binary Search:", binary_search(ordered_list, number_to_find)) 

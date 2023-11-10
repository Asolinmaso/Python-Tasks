def remove_duplicates_with_loop(lst):
    new_list = []
    for element in lst:
        if element not in new_list:
            new_list.append(element)
    return new_list

def remove_duplicates_with_set(lst):
    return list(set(lst))

a = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7]
print("List after removing duplicates (loop):", remove_duplicates_with_loop(a))
print("List after removing duplicates (set):", remove_duplicates_with_set(a))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = list(set(a) & set(b))
print("Common elements (using sets):", common_elements)

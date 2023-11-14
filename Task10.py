import random

random_list1 = random.sample(range(1, 100), 10)
random_list2 = random.sample(range(1, 100), 12)
common_values_random = list(set([x for x in random_list1 if x in random_list2]))
print(random_list1,"are random_list1")
print(random_list2,"are random_list2")
print(common_values_random,"are common_values_random")
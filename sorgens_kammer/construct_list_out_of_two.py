""" Take two lists in, return a list of items that exist in the first, but not in the second """
import time


def create_list(list_1, list_2):
    result_list = []
    for item in list_1:
        if item not in list_2:
            result_list.append(item)
    return result_list


def create_list_optimized(list_1, list_2):
    return list(set(list_1) - set(list_2))

l1 = range(1000)
l2 = range(1, 1001, 2)

start = time.time()
print create_list(l1, l2)
finish = time.time() - start
print finish

start = time.time()
print create_list_optimized(l1, l2)
finish = time.time() - start
print finish

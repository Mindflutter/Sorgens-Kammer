"""Merge two sorted lists in linear time."""


def merge_lists(list_1, list_2):
    result = []
    pointer_a = 0
    pointer_b = 0

    while pointer_a < len(list_1) and pointer_b < len(list_2):
        if list_1[pointer_a] >= list_2[pointer_b]:
            result.append(list_2[pointer_b])
            pointer_b += 1
        else:
            result.append(list_1[pointer_a])
            pointer_a += 1

    while pointer_a < len(list_1):
        result.append(list_1[pointer_a])
        pointer_a += 1

    while pointer_b < len(list_2):
        result.append(list_2[pointer_b])
        pointer_b += 1
    print(result)


a = [0, 1, 3, 3, 5, 7]
b = [2, 4, 6]
merge_lists(a, b)

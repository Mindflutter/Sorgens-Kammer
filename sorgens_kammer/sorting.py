def quicksort(the_list, count=0):
    count += 1
    if len(the_list) < 2:
        return the_list, count
    else:
        # pivot_index = randint(0, len(the_list) - 1)
        pivot_index = 0
        pivot = the_list.pop(pivot_index)
        less, count = quicksort([x for x in the_list if x < pivot], count)
        greater, count = quicksort([x for x in the_list if x >= pivot], count)
        return less + [pivot] + greater, count


l1 = [1, 5, 5, 2, 6, -1, 3, 8, 10, -3, 8, 3]

print(quicksort(l1))

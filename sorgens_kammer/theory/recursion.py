def rec_sum(the_list):
    if len(the_list) == 1:
        return the_list[0]
    else:
        return the_list.pop() + rec_sum(the_list)


test_l = [1, 2, 3, 4, 5]
print(rec_sum(test_l[:]))
print(test_l)


def rec_count_elems(the_list):
    if len(the_list) == 1:
        return 1
    else:
        the_list.pop()
        return 1 + rec_count_elems(the_list)


print(rec_count_elems(test_l[:]))

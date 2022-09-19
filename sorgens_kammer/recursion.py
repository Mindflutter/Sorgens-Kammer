def rec_sum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l.pop() + rec_sum(l)


test_l = [1, 2, 3, 4, 5]
print(rec_sum(test_l[:]))
print(test_l)


def rec_count_elems(l):
    if len(l) == 1:
        return 1
    else:
        l.pop()
        return 1 + rec_count_elems(l)


print(rec_count_elems(test_l[:]))

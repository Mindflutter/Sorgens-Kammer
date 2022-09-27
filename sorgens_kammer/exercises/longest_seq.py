def longest_seq(seq: list) -> int:
    """ Longest sequence of 1"s in a binary vector """
    seq_cur = seq_max = 0
    for item in seq:
        if item == 0:
            seq_cur = 0
        if item == 1:
            seq_cur += 1
            seq_max = max(seq_cur, seq_max)
    return seq_max


# 2
seq1 = [0, 1, 1, 0, 1]
# 3
seq2 = [0, 1, 1, 0, 1, 1, 1]
# 3
seq3 = [0, 1, 1, 0, 1, 1, 1, 0, 1]
print(longest_seq(seq1))
print(longest_seq(seq2))
print(longest_seq(seq3))

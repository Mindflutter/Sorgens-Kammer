from itertools import product
from typing import List

letter_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def letter_combinations(digits: str) -> List[str]:
    """ Return all possible letter combinations from phone buttons input
    Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/ """

    # handling one special case
    if digits == "":
        return []
    letter_sequence = [letter_map[digit] for digit in digits]

    # using Cartesian product: all ordered combinations
    return ["".join(comb) for comb in product(*letter_sequence)]

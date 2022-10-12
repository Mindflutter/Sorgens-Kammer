from itertools import combinations
from typing import List

# short yet non-optimal solution
"""
# def sorter(self, t: tuple[int]):
#     if sum(t) == 0:
#         return tuple(sorted(t))
#
#
# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     unique_combinations = set(filter(None, map(self.sorter, combinations(nums, 3))))
#     return [list(triplet) for triplet in unique_combinations]
"""


def three_sum(nums: List[int]) -> List[List[int]]:
    """ Get unique combinations of integer triplets that sum up to zero from a given integer list
        Reference: https://leetcode.com/problems/3sum/
    """
    negatives = []
    positives = []
    zeros = []

    # divide input list into sublists
    for num in nums:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            zeros.append(num)

    # introduce sets for faster lookup
    unique_negatives = set(negatives)
    unique_positives = set(positives)
    unique_triplets = set()
    result = []

    # gather all triplets in the form of [-number, 0, number]
    if zeros:
        for negative in unique_negatives:
            triplet = [negative, 0, - negative]
            if -1 * negative in unique_positives:
                result.append(triplet)

    # add all-zero triplet if applicable
    if len(zeros) >= 3:
        result.append([0, 0, 0])

    # gather pairs of negative numbers and check if they sum up to a positive - that's a triplet
    negative_pairs = set(combinations(negatives, 2))
    for negative_pair in negative_pairs:
        pair_sum_pos = - (negative_pair[0] + negative_pair[1])
        if pair_sum_pos in unique_positives:
            triplet = [negative_pair[0], negative_pair[1], pair_sum_pos]
            triplet.sort()
            if tuple(triplet) not in unique_triplets:
                result.append(triplet)
                unique_triplets.add(tuple(triplet))

    # same as the previous step for pairs of positive numbers
    positive_pairs = set(combinations(positives, 2))
    for positive_pair in positive_pairs:
        pair_sum_neg = - (positive_pair[0] + positive_pair[1])
        if pair_sum_neg in unique_negatives:
            triplet = [positive_pair[0], positive_pair[1], pair_sum_neg]
            triplet.sort()
            if tuple(triplet) not in unique_triplets:
                result.append(triplet)
                unique_triplets.add(tuple(triplet))

    return result

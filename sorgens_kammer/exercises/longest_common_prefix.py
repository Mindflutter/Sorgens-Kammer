from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """ Find the longest common prefix in a list of strings
    Reference: https://leetcode.com/problems/longest-common-prefix/ """
    shortest_str = min(strs, key=len)

    i = 0  # empty str case
    for i, _ in enumerate(shortest_str, start=1):
        if not all(map(lambda x: x.startswith(shortest_str[:i]), strs)):
            return shortest_str[:i - 1]
    return shortest_str


print(longest_common_prefix(["a"]))

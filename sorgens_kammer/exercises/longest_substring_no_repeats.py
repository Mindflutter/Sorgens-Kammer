from collections import deque


def length_of_longest_substring(s: str) -> int:
    """ Get length of the longest substring without repeating characters
    Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/"""
    memory = deque()
    max_length = 0
    for char in s:
        if char in memory:
            while True:
                if memory.popleft() == char:
                    memory.append(char)
                    break
        else:
            memory.append(char)
            max_length = max(max_length, len(memory))
    return max_length


print(length_of_longest_substring("pwwkew"))

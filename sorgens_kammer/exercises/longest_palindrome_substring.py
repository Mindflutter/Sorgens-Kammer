import timeit


# FIXME: non-optimal solution
def longest_palindrome(s: str) -> str:
    """ Find the longest palindrome substring in a given string
    Reference: https://leetcode.com/problems/longest-palindromic-substring/ """
    longest = s[0]
    s_length = len(s)
    longest_length = 1

    for start_index in range(0, s_length):
        for end_index in range(2, s_length + 1):
            straight = s[start_index:end_index]
            if len(straight) > longest_length:
                reverse = straight[::-1]
                if straight == reverse:
                    longest = straight
                    longest_length = len(longest)

    return longest


test_string = "aaa"
t = timeit.Timer(stmt="longest_palindrome_substring.longest_palindrome(longest_palindrome_substring.test_string)",
                 setup="import longest_palindrome_substring")
print(t.timeit(10))

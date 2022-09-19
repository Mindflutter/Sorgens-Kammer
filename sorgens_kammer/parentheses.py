def check_parentheses(s):
    parentheses = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for char in s:
        # if opening parenthesis
        if char in parentheses:
            stack.append(char)
        # closing parenthesis must be the last opened
        elif not stack or parentheses[stack.pop()] != char:
            return False
    return not stack


# true
s1 = "()[]{}"
# false
s2 = "(]"
# false
s3 = "([)]"
# true
s4 = "{[]}"
print(check_parentheses(s1))
print(check_parentheses(s2))
print(check_parentheses(s3))
print(check_parentheses(s4))


def generate(cur, opened, closed, n):
    if len(cur) == 2 * n:
        print(cur)
        return
    if opened < n:
        generate(cur + '(', opened + 1, closed, n)
    if closed < opened:
        generate(cur + ')', opened, closed + 1, n)


generate('', 0, 0, 5)

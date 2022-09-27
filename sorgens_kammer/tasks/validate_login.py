""" Check if login matches the following rules:
    1. It is maximum 20 characters long
    2. Contains latin characters, digits or special characters ".", "-"
    3. Starts with latin character
    4. Ends with latin character or a digit
"""
import re
import time


def validate_1(login):
    login = login.lower()
    valid_pattern = re.compile("^([a-z]{1}|[a-z]{1}[a-z0-9\.-]{0,18}[a-z0-9]{1})$")
    result = valid_pattern.match(login)
    return result is not None


def validate_2(login):
    login = login.lower()
    latin_chars = "abcdefghijklmnpqrstuvwxyz"
    digits = "1234567890"
    special_chars = ".-"
    if len(login) <= 20 and login[0] in latin_chars and login[-1] in latin_chars + digits \
            and set(login) == set(login).intersection(latin_chars + digits + special_chars):
        return True
    else:
        return False


test_login = "a4234.sd-fsdv2"

start = time.time()
print(validate_1(test_login))
finish_1 = time.time() - start
print(round(finish_1, 6))

start = time.time()
print(validate_2(test_login))
finish_2 = time.time() - start
print(round(finish_2, 5))

print(finish_1 > finish_2)

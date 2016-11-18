#!/usr/bin/python

"""
A script that takes in a log file and outputs 10 most occurring substrings
according to a specified regular expression, in this case access IP addresses.
"""

import argparse
import re

from collections import Counter
from pprint import pprint


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', default='access.log')
    args = parser.parse_args()

    input_file = args.input_file
    regex = re.compile('Accessed: \d+\.\d+\.\d+\.\d+')
    occurrences = []

    with open(input_file) as access_log:
        for line in access_log:
            match = regex.search(line)
            if match:
                occurrences.append(match.group())

    result = Counter(occurrences).most_common(10)
    pprint(result)


if __name__ == '__main__':
    main()

# Problem 11: Text Wrap
# Link: https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap


def wrap(string, max_width):
    # textwrap.fill breaks a long string into lines of max_width
    return textwrap.fill(string, max_width)


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

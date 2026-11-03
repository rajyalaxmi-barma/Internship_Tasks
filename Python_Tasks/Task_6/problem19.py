# Problem 19: Company Logo
# Link: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
# count how many times each letter appears
counts = {}
for ch in s:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1

# find the top 3 letters
for i in range(3):
best = None

    # sorted() gives the letters in alphabetical order,
    # so when two letters have the same count, the earlier letter wins
    for ch in sorted(counts):
        if best is None or counts[ch] > counts[best]:
            best = ch

    print(best, counts[best])

    # remove it so we can find the next best letter
    del counts[best]

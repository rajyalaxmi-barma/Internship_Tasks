# Problem13: Sherlock and the Valid String
# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
     # count of each character
    char_count = {}
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    # how many characters have each frequency
    freq_count = {}
    for ch in char_count:
        f = char_count[ch]
        if f in freq_count:
            freq_count[f] += 1
        else:
            freq_count[f] = 1

    if len(freq_count) == 1:
        return "YES"
    elif len(freq_count) == 2:
        freqs = sorted(freq_count)
        low = freqs[0]
        high = freqs[1]
        if low == 1 and freq_count[low] == 1:
            return "YES"
        elif high - low == 1 and freq_count[high] == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

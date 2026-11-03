# Problem17: Separate the Numbers
# Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.

def separateNumbers(s):
    answer = "NO"

    if s[0] != "0":
        for length in range(1, len(s) // 2 + 1):
            first = int(s[:length])
            built = str(first)
            num = first

            while len(built) < len(s):
                num += 1
                built += str(num)

            if built == s:
                answer = "YES " + str(first)
                break

    print(answer)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

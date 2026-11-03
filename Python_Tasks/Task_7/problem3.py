# Problem3: Mars Exploration
# Link: https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def marsExploration(s):
    sos = "SOS"
    changed = 0

    for i in range(len(s)):
        if s[i] != sos[i % 3]:
            changed += 1

    return changed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

# Problem9: Beautiful Binary String
# Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    steps = 0
    i = 0

    while i <= len(b) - 3:
        if b[i:i + 3] == "010":
            steps += 1
            i += 3
        else:
            i += 1

    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

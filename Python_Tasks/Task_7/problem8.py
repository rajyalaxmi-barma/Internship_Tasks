# Problem8: Gemstones
# Link: https://www.hackerrank.com/challenges/gem-stones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    common = set(arr[0])

    for i in range(1, len(arr)):
        rock = set(arr[i])
        common = common.intersection(rock)

    return len(common)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

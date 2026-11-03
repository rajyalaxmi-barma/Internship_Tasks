# Problem19: Weighted Uniform Strings
# Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()
    current = 0

    for i in range(len(s)):
        value = ord(s[i]) - ord("a") + 1
        if i > 0 and s[i] == s[i - 1]:
            current += value
        else:
            current = value
        weights.add(current)

    result = []
    for x in queries:
        if x in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

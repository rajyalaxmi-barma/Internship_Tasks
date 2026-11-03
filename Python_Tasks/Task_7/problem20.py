# Problem20: Super Reduced String
# Link: https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def superReducedString(s):
    result = []

    for ch in s:
        if len(result) > 0 and result[-1] == ch:
            result.pop()
        else:
            result.append(ch)

    if len(result) == 0:
        return "Empty String"
    else:
        return "".join(result)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

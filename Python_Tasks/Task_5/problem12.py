#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(" ")

    new_words = []
    for word in words:
        if word == "":
            new_words.append(word)
        else:
            # make only the first letter capital, keep the rest as it is
            first_letter = word[0].upper()
            rest = word[1:]
            new_words.append(first_letter + rest)

    return " ".join(new_words)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

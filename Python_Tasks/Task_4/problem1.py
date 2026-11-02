# Problem 1: Python If-Else
# HackerRank Link: https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input().strip())

# odd numbers are always Weird
if n % 2 == 1:
    print("Weird")
# even numbers from here on
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")

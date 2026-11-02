# Problem 13: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

result = []

# numbers that are in a but not in b
for x in a:
    if x not in b:
        result.append(x)

# numbers that are in b but not in a
for x in b:
    if x not in a:
        result.append(x)

result.sort()
for x in result:
    print(x)

# Problem 7: Symmetric Difference
# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

# read the first set
m = int(input())
set_a = set()
for item in input().split():
    set_a.add(int(item))

# read the second set
n = int(input())
set_b = set()
for item in input().split():
    set_b.add(int(item))

# numbers that are in a or b, but not in both
result = []
for x in set_a:
    if x not in set_b:
        result.append(x)
for x in set_b:
    if x not in set_a:
        result.append(x)

# print in ascending order, one per line
result.sort()
for x in result:
    print(x)

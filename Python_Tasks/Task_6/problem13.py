# Problem 13: Set .union() Operation
# Link: https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english = set()
for item in input().split():
    english.add(int(item))

b = int(input())
french = set()
for item in input().split():
    french.add(int(item))

# union = students subscribed to at least one newspaper
both = english.union(french)
print(len(both))

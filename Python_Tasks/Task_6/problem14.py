# Problem 14: Set .intersection() Operation
# Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
english = set()
for item in input().split():
    english.add(int(item))

b = int(input())
french = set()
for item in input().split():
    french.add(int(item))

# intersection = students subscribed to both newspapers
both = english.intersection(french)
print(len(both))

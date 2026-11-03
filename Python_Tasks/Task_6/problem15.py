# Problem 15: Set .difference() Operation
# Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english = set()
for item in input().split():
    english.add(int(item))

b = int(input())
french = set()
for item in input().split():
    french.add(int(item))

# difference = students subscribed to English only
only_english = english.difference(french)
print(len(only_english))

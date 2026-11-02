# Problem 8: Set .add()
# Link: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())

countries = set()

for i in range(n):
    name = input()
    # a set ignores duplicates automatically
    countries.add(name)

# number of distinct country names
print(len(countries))

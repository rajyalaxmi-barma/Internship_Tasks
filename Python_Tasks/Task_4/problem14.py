# Problem 14: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())

countries = set()
for i in range(n):
    name = input()
    countries.add(name)     # a set ignores duplicates

print(len(countries))

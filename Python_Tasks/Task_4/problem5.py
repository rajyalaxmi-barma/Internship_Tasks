# Problem 5: Print Function
# HackerRank Link: https://www.hackerrank.com/challenges/python-print/problem

n = int(input())

result = ""
for i in range(1, n + 1):
    result = result + str(i)   # join the numbers as text
print(result)

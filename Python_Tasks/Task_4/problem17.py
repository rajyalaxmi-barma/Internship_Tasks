# Problem 17: Finding the Percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())

student_marks = {}
for i in range(n):
    parts = input().split()
    name = parts[0]
    marks = parts[1:]           # the rest are the marks (text)
    student_marks[name] = marks

query_name = input()

total = 0
count = 0
for mark in student_marks[query_name]:
    total = total + float(mark)
    count = count + 1

average = total / count
print("%.2f" % average)           # two digits after the decimal point

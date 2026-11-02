# Problem 14: Finding the Percentage
# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}

for i in range(n):
    line = input().split()
    name = line[0]

    # the remaining items are the marks
    marks = []
    for item in line[1:]:
        marks.append(float(item))

    student_marks[name] = marks

query_name = input()

marks = student_marks[query_name]
total = 0
for m in marks:
    total = total + m

average = total / len(marks)

# print with exactly 2 digits after the decimal point
print("%.2f" % average)

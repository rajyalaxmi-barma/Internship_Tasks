# Problem 13: Nested Lists
# Link: https://www.hackerrank.com/challenges/nested-list/problem

n=int(input())

names = []
grades = []
for i in range(n):
    name = input()
    score = float(input())
    names.append(name)
    grades.append(score)

# collect the different (unique) grades
unique_grades = []
for g in grades:
    if g not in unique_grades:
        unique_grades.append(g)

# sort grades from lowest to highest
unique_grades.sort()

# second lowest grade is at index 1
second_lowest = unique_grades[1]

# collect the names of students with that grade
result_names = []
for i in range(n):
    if grades[i] == second_lowest:
        result_names.append(names[i])

# print names in alphabetical order
result_names.sort()
for name in result_names:
    print(name)

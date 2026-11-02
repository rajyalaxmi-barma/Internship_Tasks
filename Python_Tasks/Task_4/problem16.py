# Problem 16: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())

names = []
scores = []
for i in range(n):
    name = input()
    score = float(input())
    names.append(name)
    scores.append(score)

# find the second lowest score
unique_scores = sorted(set(scores))
second_lowest = unique_scores[1]

# collect the students who have that score
result = []
for i in range(n):
    if scores[i] == second_lowest:
        result.append(names[i])

result.sort()       # alphabetical order
for name in result:
    print(name)

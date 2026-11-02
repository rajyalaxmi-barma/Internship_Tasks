# Problem 20: No Idea!
# HackerRank Link: https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))     # liked numbers
b = set(map(int, input().split()))     # disliked numbers

happiness = 0
for x in arr:
    if x in a:
        happiness = happiness + 1
    elif x in b:
        happiness = happiness - 1

print(happiness)

# Problem 6: Find the Runner-Up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))

# set removes duplicates, sorted puts them in increasing order
unique_scores = sorted(set(arr))

# the last item is the highest, the one before it is the runner-up
print(unique_scores[len(unique_scores) - 2])

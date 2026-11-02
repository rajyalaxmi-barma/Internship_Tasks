# Problem 1: Find the Runner-Up Score!
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())

# read the scores as text, then convert each one to a number
text_scores = input().split()
scores = []
for item in text_scores:
    scores.append(int(item))

# Step 1: find the highest score
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score

# Step 2: find the biggest score that is NOT the highest
runner_up = -100
for score in scores:
    if score != highest and score > runner_up:
        runner_up = score

print(runner_up)


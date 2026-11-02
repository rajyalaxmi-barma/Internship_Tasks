# Problem 17: No Idea!
# Link: https://www.hackerrank.com/challenges/no-idea/problem

n, m = input().split()

# the array can have repeated numbers, so we keep it as a list
arr = []
for item in input().split():
    arr.append(int(item))

# sets A (liked) and B (disliked) - sets make searching fast
set_a = set()
for item in input().split():
    set_a.add(int(item))

set_b = set()
for item in input().split():
    set_b.add(int(item))

happiness = 0
for number in arr:
    if number in set_a:
        happiness = happiness + 1
    elif number in set_b:
        happiness = happiness - 1

print(happiness)


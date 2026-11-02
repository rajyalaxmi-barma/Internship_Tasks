# Problem 19: collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

x = int(input())
sizes = list(map(int, input().split()))

# count how many shoes we have of each size
shoes = {}
for size in sizes:
    if size in shoes:
        shoes[size] = shoes[size] + 1
    else:
        shoes[size] = 1

n = int(input())
earned = 0

for i in range(n):
    size, price = map(int, input().split())
    # sell only if we still have that size
    if size in shoes and shoes[size] > 0:
        earned = earned + price
        shoes[size] = shoes[size] - 1

print(earned)

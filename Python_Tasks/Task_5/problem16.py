# Problem 16: Collections.Counter()
# Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())

# read shoe sizes and count how many shoes of each size we have
sizes_text = input().split()
sizes = []
for item in sizes_text:
    sizes.append(int(item))
shoe_count = Counter(sizes)

n = int(input())
earnings = 0

for i in range(n):
    size, price = input().split()
    size = int(size)
    price = int(price)

    # sell the shoe only if we still have that size
    if shoe_count[size] > 0:
        earnings = earnings + price
        shoe_count[size] = shoe_count[size] - 1

print(earnings)

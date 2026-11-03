# Problem 16: Check Subset
# Link: https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for case in range(t):
    n = int(input())
    set_a = set()
    for item in input().split():
        set_a.add(int(item))

    m = int(input())
    set_b = set()
    for item in input().split():
        set_b.add(int(item))

    # True if every element of A is also in B
    print(set_a.issubset(set_b))

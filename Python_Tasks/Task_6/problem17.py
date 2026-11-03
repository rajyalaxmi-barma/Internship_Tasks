# Problem 17: Check Strict Superset
# Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set()
for item in input().split():
    set_a.add(int(item))

n = int(input())
answer = True

for i in range(n):
    other = set()
    for item in input().split():
        other.add(int(item))

    # A must contain every element of the other set,
    # and A must also have at least one extra element
    if not (other.issubset(set_a) and len(set_a) > len(other)):
        answer = False

print(answer)

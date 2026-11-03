# Problem 18: Set Mutations
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())

set_a = set()
for item in input().split():
    set_a.add(int(item))

number_of_operations = int(input())

for i in range(number_of_operations):
    # first line: operation name and size of the other set
    operation = input().split()
    name = operation[0]

    # second line: the elements of the other set
    other = set()
    for item in input().split():
        other.add(int(item))

    if name == "update":
        set_a.update(other)
    elif name == "intersection_update":
        set_a.intersection_update(other)
    elif name == "difference_update":
        set_a.difference_update(other)
    elif name == "symmetric_difference_update":
        set_a.symmetric_difference_update(other)

# print the sum of the elements of the final set
total = 0
for x in set_a:
    total = total + x
print(total)

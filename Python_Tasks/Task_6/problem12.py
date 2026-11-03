# Problem 12: Set .discard(), .remove() & .pop()
# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split()

    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

# print the sum of the remaining elements
total = 0
for x in s:
    total = total + x
print(total)

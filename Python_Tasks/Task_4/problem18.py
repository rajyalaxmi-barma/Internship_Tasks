# Problem 18: Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

N = int(input())
lst = []

for i in range(N):
    parts = input().split()
    command = parts[0]

    if command == "insert":
        lst.insert(int(parts[1]), int(parts[2]))
    elif command == "print":
        print(lst)
    elif command == "remove":
        lst.remove(int(parts[1]))
    elif command == "append":
        lst.append(int(parts[1]))
    elif command == "sort":
        lst.sort()
    elif command == "pop":
        lst.pop()
    elif command == "reverse":
        lst.reverse()

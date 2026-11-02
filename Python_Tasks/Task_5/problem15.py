# Problem 15: Lists
# Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    my_list = []

for i in range(N):
    command = input().split()
    name = command[0]

    if name == "insert":
        position = int(command[1])
        value = int(command[2])
        my_list.insert(position, value)
    elif name == "print":
        print(my_list)
    elif name == "remove":
        value = int(command[1])
        my_list.remove(value)
    elif name == "append":
        value = int(command[1])
        my_list.append(value)
    elif name == "sort":
        my_list.sort()
    elif name == "pop":
        my_list.pop()
    elif name == "reverse":
        my_list.reverse()

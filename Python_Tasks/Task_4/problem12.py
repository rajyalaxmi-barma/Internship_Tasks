# Problem 12: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    distinct = set(array)       # keep each height only once

    total = 0
    for height in distinct:
        total = total + height

    avg = total / len(distinct)
    return round(avg, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Problem 15: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

counts = {}
for i in range(n):
    word = input().strip()
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

# number of distinct words
print(len(counts))

# counts in the order the words first appeared
numbers = []
for word in counts:
    numbers.append(str(counts[word]))
print(" ".join(numbers))

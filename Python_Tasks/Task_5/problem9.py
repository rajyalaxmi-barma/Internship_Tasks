# Problem 9: Word Order
# Link: https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

counts = {}      # word -> how many times it appeared
order = []       # words in the order they first appeared

for i in range(n):
    word = input().strip()
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
        order.append(word)

# first line: number of distinct words
print(len(order))

# second line: count of each word in order of first appearance
for word in order:
    print(counts[word], end=" ")
print()

# Problem 20: Piling Up!
# Link: https://www.hackerrank.com/challenges/piling-up/problem

t = int(input())

for case in range(t):
    n = int(input())

    blocks = []
    for item in input().split():
        blocks.append(int(item))

    left = 0                # index of the leftmost block
    right = n - 1           # index of the rightmost block
    previous = 2 ** 31    # the last block placed (start bigger than any block)
    possible = True

    while left <= right:
        # always take the bigger block from either end
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left = left + 1
        else:
            current = blocks[right]
            right = right - 1

        # a block can only go on top of a bigger (or equal) block
        if current > previous:
            possible = False
            break

        previous = current

    if possible:
        print("Yes")
    else:
        print("No")

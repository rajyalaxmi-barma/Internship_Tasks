# Problem 7: List Comprehensions
# Link: https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []

# try every combination of i, j, k
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            # keep it only if the sum is NOT equal to n
            if i + j + k != n:
                result.append([i, j, k])

print(result)

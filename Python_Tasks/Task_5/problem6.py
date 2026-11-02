# Problem 6: Introduction to Sets
# Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # a set keeps only unique values (removes duplicates)
    unique_heights = set(array)

    total = 0
    for height in unique_heights:
        total = total + height

    # average = sum / how many
    return total / len(unique_heights)


n = int(input())
text_values = input().split()
arr = []
for item in text_values:
    arr.append(int(item))

result = average(arr)
print(result)

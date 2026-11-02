# Problem 19: Merge the Tools!
# Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # go through the string in pieces of length k
    for i in range(0, len(string), k):
        piece = string[i:i + k]

        # keep each letter only the first time it appears
        result = ""
        for ch in piece:
            if ch not in result:
                result = result + ch

        print(result)


string, k = input(), int(input())
merge_the_tools(string, k)

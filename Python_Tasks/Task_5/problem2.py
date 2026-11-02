# Problem 2: String Split and Join
# Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # split() breaks the sentence into a list of words
    words = line.split(" ")
    # join() puts the words back together with "-" between them
    new_line = "-".join(words)
    return new_line


line = input()
result = split_and_join(line)
print(result)

# Problem 7: String Split and Join
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    words = line.split(" ")     # break the sentence into words
    return "-".join(words)      # put them back together with a hyphen


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Problem 10: Find a String
# HackerRank Link: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0
    sub_length = len(sub_string)

    # check every starting position (overlaps are counted too)
    for i in range(len(string) - sub_length + 1):
        part = string[i:i + sub_length]
        if part == sub_string:
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

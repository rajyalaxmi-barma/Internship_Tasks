# Problem 4: Find a String
# Link: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count=0
    sub_length = len(sub_string)

    for i in range(len(string) - sub_length + 1):
        # take a piece of the string with the same length as sub_string
        piece = string[i:i + sub_length]
        if piece == sub_string:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

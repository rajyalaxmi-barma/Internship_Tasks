# Problem 9: Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    before = string[:position]          # everything before the position
    after = string[position + 1:]       # everything after the position
    return before + character + after


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Problem 3: Mutations
# Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    # part of the string before the position
    before = string[:position]
    # part of the string after the position (skip the old character)
    after = string[position + 1:]
    # put the new character in the middle
    new_string = before + character + after
    return new_string


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

def mutate_string(string, position, character):
    before = string[:position]
    after = string[position + 1:]
    new_string = before + character + after
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

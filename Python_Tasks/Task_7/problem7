# Problem7: Alphabet Rangoli
# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3

    rows = []
    for i in range(size):
        # letters from size-1 down to i, then back up to size-1
        letters = alpha[size - 1:i:-1] + alpha[i:size]
        line = "-".join(letters)
        rows.append(line.center(width, "-"))

    # top half (narrow to wide)
    for i in range(size - 1, 0, -1):
        print(rows[i])

    # middle and bottom half (wide to narrow)
    for i in range(size):
        print(rows[i])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
